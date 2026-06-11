# Abilities, lifecycle, Want, Context, windows

Source pages:
- application-models, uiability-overview, uiability-lifecycle, uiability-launch-type
- uiability-usage, uiability-data-sync-with-ui, uiability-intra-device-interaction
- want-overview, explicit-implicit-want-mappings
- application-context-stage, extensionability-overview
- window-overview, application-window-stage
- launch-page, ability-startup-with-explicit-want, component-startup-rules

## Component types (Stage model)

- **UIAbility** — has UI. The primary user-facing unit. Examples: an app's main window, a separate "Settings" surface, a deep-link target. Each launched UIAbility appears as its own task in Recents (unless launchType says otherwise).
- **ExtensionAbility** — no UI. Specialised subclasses for system extension points:
  - `ServiceExtensionAbility` — long-running background service.
  - `BackupExtensionAbility` — backup & restore of app data.
  - `FormExtensionAbility` — provides ArkTS cards (widgets).
  - `InputMethodExtensionAbility`, `WorkSchedulerExtensionAbility`, `AccessibilityExtensionAbility`, etc.
- `AbilityStage` — module-level container. Optional. Created when the first ability of the module is launched. Override `onCreate()`/`onAcceptWant()` to influence specified-mode keys.

## UIAbility skeleton

```typescript
// entry/src/main/ets/entryability/EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'EntryAbility', 'onCreate');
    // one-time init
  }

  onWindowStageCreate(stage: window.WindowStage): void {
    stage.loadContent('pages/Index', (err) => {
      if (err.code) hilog.error(DOMAIN, 'EntryAbility', 'loadContent failed: %s', JSON.stringify(err));
    });
    stage.on('windowStageEvent', (event) => {
      // foreground, background, focused, unfocused
    });
  }

  onForeground(): void { /* visible & interactive */ }
  onBackground(): void { /* hidden */ }
  onWindowStageDestroy(): void { /* WindowStage going away */ }
  onDestroy(): void { /* instance destroyed */ }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // re-launch on an existing instance (singleton/specified)
  }

  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult {
    // persist state across cold-restart / cross-device migration
    return AbilityConstant.OnSaveResult.ALL_AGREE;
  }
}
```

### Lifecycle order

**Foreground launch**: `onCreate` → `onWindowStageCreate` → `onForeground`. Switching to another app: `onBackground`. Returning: `onNewWant` (only when started again) → `onForeground`.

**Background launch via `startAbilityByCall()`**: `onCreate` → `onBackground` (no `onWindowStageCreate`). Bringing it to front later: `onNewWant` → `onWindowStageCreate` → `onForeground`.

Keep lifecycle callbacks fast — they run on the UI thread. Offload heavy work to async tasks or workers.

### Listen to lifecycle from anywhere

Use `applicationContext.on('abilityLifecycle', observer)` for a global view:

```typescript
const ctx = this.context.getApplicationContext();
const id = ctx.on('abilityLifecycle', {
  onAbilityCreate(ability) { /*…*/ },
  onWindowStageCreate(ability, stage) {},
  onAbilityForeground(ability) {},
  onAbilityBackground(ability) {},
  onAbilityDestroy(ability) {},
});
// later: ctx.off('abilityLifecycle', id);
```

## Launch modes

Configured on the ability in `module.json5`:

| Mode | Behaviour |
|---|---|
| `singleton` (default) | One instance ever. Re-launch goes through `onNewWant`. One Recents task. |
| `multiton` (formerly `standard`) | A new instance every `startAbility`. Many Recents tasks. |
| `specified` | App decides by key. Override `AbilityStage.onAcceptWant(want)` to return a string key; system reuses if the key matches. |

```json5
{ "abilities": [{ "name": "EntryAbility", "launchType": "singleton" /* … */ }] }
```

## Want — intents, but explicit-first

`Want` is the message passed between abilities. Two ways to address:

1. **Explicit Want** — name the bundle and ability:
   ```typescript
   const want: Want = {
     bundleName: 'com.example.target',
     abilityName: 'EntryAbility',
     parameters: { foo: 'bar' }
   };
   this.context.startAbility(want);
   ```

2. **Implicit Want** — declare an `entities` + `actions` + (optional) `uri` + `type`, and the system finds matching abilities that declared a `skill` filter in `module.json5`:
   ```typescript
   const want: Want = {
     action: 'ohos.want.action.viewData',
     uri: 'https://example.com',
     entities: ['entity.system.browsable']
   };
   ```

The `skills` block of `module.json5` is how an ability advertises what implicit wants it accepts:

```json5
"skills": [{
  "entities": ["entity.system.home", "entity.system.browsable"],
  "actions":  ["ohos.want.action.viewData"],
  "uris":     [{ "scheme": "https", "host": "example.com" }]
}]
```

Always prefer explicit Want for in-app navigation. Implicit Want is for "open a link", "share to", "pick a contact"-style hand-offs to other apps.

## Context — your gateway to system services

Every component receives a `Context`. Hierarchy:

- `Context` (base — abstract)
- `AbilityContext` — for UIAbility (`this.context` inside UIAbility)
- `ExtensionContext` family — per extension type
- `ApplicationContext` — process-wide (`abilityContext.getApplicationContext()`)
- `UIAbilityContext` extends `AbilityContext` with `startAbility`, `startAbilityForResult`, etc.

What lives on Context:

```typescript
ctx.applicationInfo       // bundleName, version
ctx.resourceManager       // load strings/media/colors at runtime
ctx.filesDir              // app sandbox files
ctx.cacheDir              // cacheable
ctx.tempDir               // ephemeral
ctx.bundleCodeDir         // read-only hap dir
ctx.distributedFilesDir   // for distributed file sharing
ctx.area                  // EL1 / EL2 storage level
ctx.config                // current screen density/orientation/lang
ctx.eventHub              // local pub/sub channel within process
ctx.getApplicationContext().setColorMode(ConfigurationConstants.ColorMode.COLOR_MODE_DARK)
```

`eventHub` is the canonical way for a UIAbility and the UI tree to talk:

```typescript
// in UIAbility
this.context.eventHub.on('refresh', (data) => {});
// from any page
this.getUIContext().getHostContext()?.eventHub.emit('refresh', someData);
```

For cross-page state without prop drilling, prefer `AppStorage`/`LocalStorage` instead.

## Window stage

Each UIAbility owns a `WindowStage`. `loadContent('pages/Index')` swaps the loaded page (or initial mount). Other tricks:

```typescript
stage.getMainWindow().then((win) => {
  win.setWindowSystemBarProperties({ statusBarContentColor: '#FFFFFF' });
  win.setPreferredOrientation(window.Orientation.AUTO_ROTATION_PORTRAIT);
  win.setWindowKeepScreenOn(true);
});

// Sub windows
stage.createSubWindow('confirm-dialog').then((sub) => { sub.showWindow() });
```

## Starting components

```typescript
this.context.startAbility(want)                                          // start UIAbility, async
this.context.startAbilityForResult(want).then((result) => {})            // get a result back
this.context.startServiceExtensionAbility(want)                          // start a service extension
this.context.startAbilityWithAccount(want, accountId)                    // multi-user devices
this.context.requestModalUIExtension(want, options)                      // request UI extension modal
this.context.openLink('https://example.com', { appLinkingOnly: true })   // App Linking
this.context.terminateSelf()
```

For self-termination with a result use `terminateSelfWithResult(result)`.

### Inter-app redirection (应用间跳转) practices

For the "open another app" family of flows there's now a dedicated practice set (`pages/typical-scenarios-for-inter-app-jumping.md`, `pages/inter-application-redirection.md`):
- **Social sharing** redirection — `pages/social-sharing-redirection.md`.
- **Ad** redirection — `pages/ad-redirection.md`.
- **Special text recognition** redirection (jump from recognized phone/address/etc.) — `pages/special-text-recognition-redirection.md`.
- **Web ⇄ app** mutual launch — `pages/navigating-between-web-and-apps.md`.

These build on App Linking (`openLink`, see above), implicit Want, and Universal Link patterns. Prefer App Linking (HTTPS, verified domain) over scheme-only `uri` for cross-app entry points.

### App restart (应用重启)

`pages/app-restart.md` documents two active-restart paths plus failure-recovery restart:
- `ApplicationContext.restartApp()` (API 12+) — restart **without** keeping the app window (user briefly sees the launcher). Main thread only; app must be focused; no repeat within 3 s; does **not** fire abilities' `onDestroy`.
- `UIAbilityContext.restartApp()` (API 22+) — restart **keeping** the window for a seamless experience.

Use after a dynamic update or to fully re-initialize internal state.

## ExtensionAbility quick map

| Use case | Pick |
|---|---|
| Background service | `ServiceExtensionAbility` (system apps) or `Background Tasks Kit` (3P) |
| Backup user data | `BackupExtensionAbility` (auto-wired when `backup` is in templates) |
| ArkTS card / widget | `FormExtensionAbility` (see `references/07-cards-and-i18n.md`) |
| Action panel / share UI | `UIExtensionAbility` |
| Input method | `InputMethodExtensionAbility` |
| Device-side agent (端侧A2A) | `AgentExtensionAbility` (type `"agent"`, API 24+) — see below |
| Wallpaper, sticker, accessibility, work scheduler, etc. | Matching `*ExtensionAbility` |

Declare them under `module.json5 → extensionAbilities[]` with a `type` field that matches the kind.

## Device-side agents — 端侧A2A / HMAF (API 24+)

From API 24, HarmonyOS adds a **device-side A2A (Agent-to-Agent) framework**, the on-device extension of HMAF (Harmony Agent Framework). It lets an app expose an intelligent agent that *system apps* (the Agent client) can discover and talk to over a standardized A2A protocol — capability description, two-way data channel, optional auth, optional UI rendering — without pre-agreed tight coupling. Source: `pages/agent-guideline.md`, `pages/agent-overview.md`, `pages/agent-development.md`.

Core pieces:
- **AgentCard** describes the agent (name, description, skills, input/output MIME modes, provider, version). Configured by hand in `resources/base/profile/agent_config.json`; an `AgentExtensionAbility` references it via `metadata`. One `agent_config.json` per AgentExtensionAbility. Field reference (retitled page): `pages/agent-extension-configuration.md` ("AgentExtensionAbility配置文件说明").
- **AgentSkill** — a concrete function the agent can run; an agent needs ≥1 skill.

Service-side skeleton (`pages/agent-extension-ability.md`):

```typescript
import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';

export default class AgentExtAbility extends AgentExtensionAbility {
  private comProxy: common.AgentHostProxy | null = null;
  onCreate(want: Want) {}
  onConnect(want: Want, proxy: common.AgentHostProxy) { this.comProxy = proxy; }
  onDisconnect(want: Want, proxy: common.AgentHostProxy) { this.comProxy = null; }
  onData(proxy: common.AgentHostProxy, data: string) {
    proxy.sendData('reply message');           // respond to the client
  }
  onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
    proxy.authorize('auth success');           // optional mutual auth
  }
  onDestroy() {}
}
```

Register it in `module.json5 → extensionAbilities[]` with `"type": "agent"` and a `srcEntry` pointing at the file (plus `metadata` referencing `agent_config.json`). Results can optionally be rendered into the client app via `AgentUIExtensionAbility`. Note this is distinct from the higher-level **Agent Framework Kit** (`pages/hmaf-introduction.md`, Function component that *launches* an agent published on the Xiaoyi open platform) — see `references/10-kits-catalog.md`.

## Permissions runtime grant

```typescript
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

const permissions: Permissions[] = ['ohos.permission.ACCESS_BLUETOOTH'];

abilityAccessCtrl.createAtManager()
  .requestPermissionsFromUser(this.context, permissions)
  .then((result) => {
    if (result.authResults.every((s) => s === 0)) { /* granted */ }
  });
```

Declare each permission in `module.json5.requestPermissions[]` with `name`, user-facing `reason` (resource ref), and `usedScene { abilities, when: 'inuse' | 'always' }`.

See also `references/05-services-and-system.md` for system-permission catalog.
