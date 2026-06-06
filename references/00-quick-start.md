# Quick start: build your first HarmonyOS NEXT app

Source pages:
- https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-overview
- https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-with-ets-stage

## Prerequisites

- **DevEco Studio** (6.1.0 Release or later recommended). Install from https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install.
- Huawei developer account (free) to enable automatic signing.
- A real HarmonyOS NEXT device, the bundled emulator, or simulator.

## Create an empty Stage-model app

1. `Create Project` → `Application` (or `Atomic Service` for an元服务) → template `Empty Ability` → `Next`.
2. Set `Compatible SDK` (the minimum API version). API 12 is a safe baseline; the latest at time of writing is API 23 (HarmonyOS 6.1.0). Other fields default.
3. `Finish`. The wizard generates project skeleton and resources.

## Generated layout (Stage model)

```
ProjectRoot/
├── AppScope/
│   ├── app.json5                 # App-wide config: bundleName, version, icon, label
│   └── resources/                # App-level resources
├── entry/                        # First module — compiled into entry.hap
│   ├── src/main/
│   │   ├── ets/
│   │   │   ├── entryability/EntryAbility.ets   # UIAbility entry point
│   │   │   ├── entrybackupability/             # Optional: backup extension
│   │   │   └── pages/Index.ets                 # First page
│   │   ├── resources/                          # Module-level resources
│   │   └── module.json5                        # Module config: abilities, pages, permissions
│   ├── build-profile.json5
│   ├── hvigorfile.ts             # Module-level hvigor build script
│   ├── obfuscation-rules.txt
│   └── oh-package.json5          # Module dependencies (ohpm)
├── build-profile.json5           # Project-level: signingConfigs, products
├── hvigorfile.ts                 # Project-level hvigor script
└── oh-package.json5              # Project-level: overrides, parameterFile
```

Don't rename `AppScope/` — it is referenced by tooling.

## A two-page hello-world

`entry/src/main/ets/pages/Index.ets`:

```typescript
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
      Button() {
        Text('Next').fontSize(30).fontWeight(FontWeight.Bold)
      }
      .type(ButtonType.Capsule)
      .margin({ top: 20 })
      .backgroundColor('#0D9FFB')
      .width('40%')
      .height('5%')
      .onClick(() => {
        let router = this.getUIContext().getRouter();
        router.pushUrl({ url: 'pages/Second' })
          .catch((err: BusinessError) => {
            console.error(`Jump failed: ${err.code} ${err.message}`);
          });
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

Create `entry/src/main/ets/pages/Second.ets`:

```typescript
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Second {
  @State message: string = 'Hi there';

  build() {
    Column() {
      Text(this.message).fontSize(50).fontWeight(FontWeight.Bold)
      Button() { Text('Back').fontSize(30) }
        .type(ButtonType.Capsule).margin({ top: 20 })
        .backgroundColor('#0D9FFB').width('40%').height('5%')
        .onClick(() => {
          try {
            this.getUIContext().getRouter().back();
          } catch (err) {
            const e = err as BusinessError;
            console.error(`Back failed: ${e.code} ${e.message}`);
          }
        })
    }.width('100%').height('100%')
  }
}
```

**Register both pages** in `entry/src/main/resources/base/profile/main_pages.json`:

```json
{
  "src": [
    "pages/Index",
    "pages/Second"
  ]
}
```

Tip: when adding a page via `Right click pages > New > Page > Empty Page`, the page is registered automatically. If you create it via `New > ArkTS File`, you must add it to `main_pages.json` yourself.

Better-than-router: for new code prefer the `Navigation` component (see `references/03-arkui-ui.md`).

## Run it

1. Connect device or start emulator.
2. `File > Project Structure > Project > Signing Configs` → tick **Automatically generate signature** (you'll be prompted to Sign In once).
3. Click the green Run button in the toolbar.

## Where to go next

- Project anatomy / config files: `references/01-app-structure.md`
- ArkTS state management, decorators: `references/02-arkts-language.md`
- Building real UIs with layouts, lists, navigation: `references/03-arkui-ui.md`
- Multi-page, multi-ability lifecycle: `references/04-ability-and-lifecycle.md`
