# App structure, packaging, and configuration files

Source pages:
- application-package-overview, application-package-structure-stage, application-package-dev
- hap-package, har-package, in-app-hsp
- application-configuration-file-overview-stage, app-configuration-file, module-configuration-file
- resource-categories-and-access, application-models

## Stage model is the default — and the only forward-going model

HarmonyOS NEXT introduced two app models historically; only **Stage model** is current. Stage uses:
- `UIAbility` — component with UI (one per page-set / user interaction surface).
- `ExtensionAbility` — components without UI for specific scenarios (cards, services, input methods, backup, etc.).
- A single `ArkTS engine` per process is **shared** across components — state and objects can flow between abilities. (FA model gave each ability its own engine.)
- `app.json5` + `module.json5` describe app and modules. (FA used `config.json`.)

Stage Components are written as **classes**, not anonymous exports — they can be subclassed.

## Project layout

```
ProjectRoot/
├── AppScope/                       # App-wide — DO NOT rename
│   ├── app.json5                   # App-wide config
│   └── resources/                  # App-wide resources (icons, app_name)
├── <module>/                       # Each module compiles to one HAP/HAR/HSP
│   ├── src/main/
│   │   ├── ets/                    # ArkTS source (.ets files)
│   │   ├── resources/              # Module resources
│   │   └── module.json5            # Module config
│   ├── build-profile.json5         # Module build config
│   ├── hvigorfile.ts               # Module hvigor script
│   ├── obfuscation-rules.txt
│   └── oh-package.json5            # Module dependencies
├── build-profile.json5             # Project signing, products, targets
├── hvigorfile.ts                   # Project hvigor script
└── oh-package.json5                # Project-wide deps/overrides
```

At compile time, `AppScope/app.json5` and the module's `module.json5` get **merged** into the HAP's final `module.json`. AppScope resources also merge into module resources (AppScope wins on collisions).

## Module types & package outputs

| Module type | Compile output | Distribution | Notes |
|---|---|---|---|
| `entry` | `entry.hap` | Required; one per app | Main module — must contain at least one UIAbility with `entity.system.home` skill |
| `feature` | `*.hap` | Dynamic feature module | Independently distributable; on-demand install with `deliveryWithInstall:false` |
| `har` | `*.har` | Static library, bundled into HAP/HSP at compile time | No runtime presence — like a static lib |
| `shared` (HSP) | `*.hsp` | Dynamic shared package | Loaded at runtime, shared across HAPs of the same app |

A full app = the bundle of HAPs + HSPs → packaged as **`*.app`** (called **App Pack**) for AppGallery upload. `pack.info` is auto-generated alongside.

- **In-app HSP**: shared library only your own app uses — referenced via `dependencies` in `oh-package.json5`.
- **Cross-app shared HSP**: must be published, has its own bundleName/version.
- HAR is embedded; you can't ship updates without rebuilding HAP.

## app.json5 — key fields

`AppScope/app.json5` is the **only** file describing app-global metadata. Required minimum:

```json5
{
  "app": {
    "bundleName": "com.example.myapp",        // reverse-DNS, 7-128 bytes, unique
    "vendor": "example",
    "versionCode": 1000000,                   // integer; must increase per release
    "versionName": "1.0.0",
    "icon": "$media:layered_image",           // -> AppScope/resources/base/media/...
    "label": "$string:app_name",              // -> string resource for localization
    "minAPIVersion": 12,
    "targetAPIVersion": 12
  }
}
```

Optional/notable fields:
- `bundleType`: `app` (default) | `atomicService` (元服务) | `shared` | `appService` | `appPlugin`.
- `debug`: auto-toggled by DevEco; do not set by hand for releases.
- `multiAppMode`: `appClone` for cloned-app support; `maxCount` 2–5.
- `assetAccessGroups`: list of system app bundles whose assets your app may read (e.g. `com.ohos.photos`).
- `cloudFileSyncEnabled`, `cloudStructuredDataSyncEnabled`: opt-in cloud sync.
- `appEnvironments`: env vars exposed via `applicationContext.applicationInfo.appEnvironments`.

## module.json5 — key fields

`<module>/src/main/module.json5` describes the module:

```json5
{
  "module": {
    "name": "entry",                          // unique within app
    "type": "entry",                          // entry | feature | har | shared
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",            // entry UIAbility name
    "deviceTypes": ["phone", "tablet"],       // required: which device types this module supports
    "deliveryWithInstall": true,              // install with app (false = on-demand)
    "pages": "$profile:main_pages",           // -> resources/base/profile/main_pages.json
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:EntryAbility_label",
        "startWindow": "$profile:start_window",   // start window resource
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,                          // can other apps start it?
        "skills": [                                // implicit-want filters
          {
            "entities": ["entity.system.home"],
            "actions": ["ohos.want.action.home"]
          }
        ]
      }
    ],
    "extensionAbilities": [/* … */],
    "requestPermissions": [
      {
        "name": "ohos.permission.ACCESS_BLUETOOTH",
        "reason": "$string:reason",
        "usedScene": { "abilities": ["EntryAbility"], "when": "inuse" }
      }
    ],
    "routerMap": "$profile:router_map"            // for Navigation-driven routing
  }
}
```

- `type` must match the module's role. `entry` modules must declare the launcher `skill` shown above.
- `deviceTypes` values: `phone`, `tablet`, `2in1`, `tv`, `car`, `wearable`. Different modules can declare different sets.
- `installationFree` is **auto-set** when `bundleType: atomicService` — don't set manually.
- `isolationMode` (HAP only, on 2in1/tablet): `nonisolationFirst` / `isolationFirst` / `isolationOnly` / `nonisolationOnly` controls whether the module runs in its own process.

## Resources & references

Resources live under `<module>/src/main/resources/` (and `AppScope/resources/` for app-wide). Layout:

```
resources/
├── base/                                       # default resources
│   ├── element/string.json                     # string resources
│   ├── element/color.json
│   ├── element/float.json
│   ├── media/                                  # images, animations
│   ├── profile/                                # JSON descriptors (main_pages, router_map, start_window)
│   └── layout/                                 # (rarely used in ArkTS — XML legacy)
├── en_US/                                      # locale-specific overrides
├── zh_CN/
├── rawfile/                                    # raw assets shipped as-is, accessible by path
└── resfile/                                    # accessible via fd from app sandbox
```

Reference resources from code with `$r('app.media.icon')`, `$r('app.string.app_name')`, etc. From JSON, use `$<type>:<name>` like `$string:app_name`, `$media:layered_image`, `$profile:main_pages`.

Folder qualifiers (e.g. `phone-dark-ldpi/`) let you override per device type, dark/light mode, language, and screen density. Match order: most specific qualifiers win.

`rawfile/` resources are loaded by relative path via `resourceManager.getRawFileContent('subdir/file.bin')`. Use for fonts, large JSON, sample data.

## Where to read next

- Want it deeper? Visit each canonical page listed under "Source pages" above.
- For abilities + lifecycle: `references/04-ability-and-lifecycle.md`.
- For permissions and `requestPermissions` runtime grant flow: `references/05-services-and-system.md`.
