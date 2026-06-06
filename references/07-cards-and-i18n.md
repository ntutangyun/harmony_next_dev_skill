# ArkTS cards (widgets) and internationalization

Source pages:
- arkts-ui-widget, arkts-ui-widget-creation, arkts-ui-widget-lifecycle
- i18n-l10n, i18n, l10n

## ArkTS cards (服务卡片 / widgets)

An **ArkTS card** is a small UI surface your app provides — pinned to home screen, lockscreen, or app-launcher previews. Two flavors:

- **Dynamic widget** (default) — supports event bindings (`postCardAction`), can update via the FormExtensionAbility.
- **Static widget** — pure presentation, no interaction. Set via `form_config.json` → `isDynamic: false`.

### Packaging options

- **Shared package**: card UI + host app live in the same module. Easiest. Set in DevEco via *Right click entry → New → Service Widget → Dynamic Widget*.
- **Standalone widget package** (API 20+): card UI in a separate `library` module, app in `entry`. Cross-links via `module.json5.formWidgetModule` (in entry) and `formExtensionModule` (in library). Allows the widget to update independently.

### Files generated

When creating a widget, DevEco produces:
- `EntryFormAbility.ets` — the `FormExtensionAbility` lifecycle handler (provides cards).
- `widget/pages/WidgetCard.ets` — the card UI (a `@Component` struct).
- `resources/base/profile/form_config.json` — card metadata (sizes, refresh rate, initial dimensions).
- `module.json5` is updated under `extensionAbilities[]` with the FormExtensionAbility entry.

### FormExtensionAbility lifecycle

```typescript
import { formBindingData, formInfo, formProvider, FormExtensionAbility } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want): formBindingData.FormBindingData {
    // user just added the widget; return initial data
    return formBindingData.createFormBindingData({ title: 'Hello card' });
  }
  onCastToNormalForm(formId: string) {}                          // resizing
  onUpdateForm(formId: string) {                                 // refresh
    const fresh = formBindingData.createFormBindingData({ title: 'Updated' });
    formProvider.updateForm(formId, fresh);
  }
  onChangeFormVisibility(newStatus: { [key: string]: number }) {}
  onFormEvent(formId: string, message: string) {                 // postCardAction round trip
    // message is the JSON the card emitted
  }
  onRemoveForm(formId: string) {}
  onConfigurationUpdate(config) {}
}
```

### Card UI (WidgetCard.ets)

A card UI is just a `@Component` struct, **without `@Entry`** (it's hosted, not navigated). Use `postCardAction` to trigger updates / launch your app:

```typescript
@Entry @Component                   // some templates use @Entry; the runtime tolerates it for cards
struct WidgetCard {
  @LocalStorageProp('title') readonly title: string = 'Hello card';

  build() {
    Column() {
      Text(this.title).fontSize(18).fontWeight(FontWeight.Bold)
      Button('Open')
        .onClick(() => {
          // route to the host app
          postCardAction(this, {
            action: 'router',
            abilityName: 'EntryAbility',
            params: { from: 'card' }
          });
        })
    }
    .width('100%').height('100%').padding(12)
  }
}
```

`postCardAction` actions: `router` (start a UIAbility), `message` (call provider → `onFormEvent`), `call` (start a service extension), `quickaction` (predefined system action).

### form_config.json minimum

```json5
{
  "forms": [{
    "name": "widget",
    "isDefault": true,
    "isDynamic": true,
    "src": "./ets/widget/pages/WidgetCard.ets",
    "uiSyntax": "arkts",
    "window": { "designWidth": 720, "autoDesignWidth": true },
    "colorMode": "auto",
    "supportDimensions": ["2*2", "2*4", "4*4"],
    "defaultDimension": "2*4",
    "updateEnabled": true,
    "scheduledUpdateTime": "10:30",
    "updateDuration": 1                                     // 30-min units
  }]
}
```

Refresh rules: `updateDuration` is in 30-minute steps (1 = every 30 min). Cards on the lockscreen / when not visible may skip refreshes.

## Internationalization (i18n)

Source: `i18n-l10n`, `i18n`, `l10n`.

ArkTS exposes the **ICU**-based `@kit.LocalizationKit` for runtime locale, number/date formatting, message lookup.

### Translatable strings

Place defaults in `resources/base/element/string.json`:

```json
{
  "string": [
    { "name": "app_name", "value": "Hello HarmonyOS" }
  ]
}
```

Per-locale overrides in sibling folders: `resources/en_US/element/string.json`, `resources/zh_CN/...`, etc.

Reference from .ets via `$r('app.string.app_name')` or `this.context.resourceManager.getStringSync($r('app.string.app_name').id)`.

### Plurals & format args

```json
{
  "stringPlural": [{
    "name": "n_files",
    "value": [
      { "quantity": "one", "value": "%d file" },
      { "quantity": "other", "value": "%d files" }
    ]
  }]
}
```

```typescript
const count = 3;
const text = this.context.resourceManager.getPluralStringValueSync(
  $r('app.plural.n_files').id, count, count);
```

For inline format args use `getStringSync(id, ...args)`.

### Number / date / currency

```typescript
import { intl } from '@kit.LocalizationKit';

const nf = new intl.NumberFormat(['zh-CN'], { style: 'currency', currency: 'CNY' });
console.log(nf.format(1234.5));     // ¥1,234.50

const df = new intl.DateTimeFormat(['en-GB'], { dateStyle: 'long', timeStyle: 'short' });
console.log(df.format(new Date()));
```

### System locale

```typescript
import { i18n } from '@kit.LocalizationKit';

const locale = i18n.System.getSystemLocale();          // 'zh-Hans-CN'
const lang = i18n.System.getSystemLanguage();          // 'zh-Hans'
const region = i18n.System.getSystemRegion();          // 'CN'
const isRTL = i18n.isRTL(locale);
```

To **force** an app-wide locale (override system), set on the ApplicationContext:

```typescript
this.context.getApplicationContext().setLanguage('en-US');
this.context.getApplicationContext().setColorMode(ConfigurationConstants.ColorMode.COLOR_MODE_DARK);
```

After the change, the runtime restarts the ability so resource resolution picks up the new locale.

### Common gotchas

- Hard-coded strings won't translate — always go through `string.json`.
- Concatenating sentences from fragments breaks word order in some languages — prefer a single template with placeholders.
- RTL? Use `direction(Direction.Rtl)` on Row/Column or rely on `i18n.isRTL()`.
- For pluralisation in Chinese (one form), `other` works for all counts.
