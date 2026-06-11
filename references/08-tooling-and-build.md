# DevEco Studio, hvigor, ohpm, signing, publishing

Source pages:
- ide-tools-overview, ide-software-install, ide-project, ide-code-edit
- ide-signing, ide-run-device, ide-debug-app
- ide-hvigor, ide-hvigor-commandline, ide-ohpm-cli, ide-publish-app

## DevEco Studio (IDE)

The official IDE built on IntelliJ. Install from https://developer.huawei.com/consumer/cn/deveco-studio/. Confirm version ≥ 6.1.0 Release for HarmonyOS 5+ NEXT projects.

Key panels:
- **Project Structure** (`File > Project Structure`): module dependencies, signing, build variants.
- **Build Profile** editor: GUI for `build-profile.json5`.
- **Previewer** (right toolbar): hot reload preview of a .ets file. Works for most pages.
- **Run / Debug** dropdown: pick target (device, simulator, emulator), then Run.
- **Profiler**: dropdown next to Run — for CPU, memory, network, frame drops.

Tip: the *Code Linter* feature is configurable via `codelinter.json5`. To run from CLI: `codelinter -p ./entry` (see command-line tools below).

For **C/C++** (NDK) code, DevEco has a built-in **Clang-Tidy** static checker (`pages/ide-clang-tidy.md`). Configure rules in the *Clang-Tidy Checks* panel, a project-root `.clang-tidy` file, or *Code > Inspect Code…* (Inspection-checks). Supports live (real-time) checking and manual checks; ticking *live update (show in "Current File")* enables all three rule sources.

## hvigor (build tool)

`hvigor` is the HarmonyOS build orchestrator. Each project has:
- `hvigorfile.ts` at the project root → orchestrates all modules.
- A `hvigorfile.ts` per module → declares the module-level build pipeline.
- `build-profile.json5` carries the configuration values that the script consumes.

### Common CLI tasks (via `hvigorw`)

```bash
# from project root
./hvigorw clean              # clean build outputs
./hvigorw assembleHap        # build HAP packages for default product
./hvigorw assembleHap --mode module -p product=default
./hvigorw assembleApp        # build the .app for AppGallery
./hvigorw --mode debug assembleHap
./hvigorw --list-tasks       # see all tasks
```

Args you'll commonly tweak:
- `-p <key>=<value>` — override build params (e.g. `product`, `buildMode`).
- `--mode module` — build only a single module.
- `--no-daemon` — for CI.
- `--debug` — full task logs (verbose).

The `hvigorw` script lives at the project root. On Windows there's also `hvigorw.bat`.

### Targets, products, build modes

`build-profile.json5` carries `app.products[]` and per-module `module.targets[]`. Products can override applyToProducts in modules, change bundleName per product (e.g. dev vs. prod), set sign profiles, etc.:

```json5
{
  "app": {
    "signingConfigs": [
      { "name": "default", "type": "HarmonyOS", "material": { /* keystore … */ } }
    ],
    "products": [
      { "name": "default", "signingConfig": "default", "compatibleSdkVersion": "5.0.0(12)" },
      { "name": "internal", "signingConfig": "default", "bundleName": "com.example.myapp.dev" }
    ]
  },
  "modules": [
    { "name": "entry", "srcPath": "./entry", "targets": [{ "name": "default", "applyToProducts": ["default", "internal"] }] }
  ]
}
```

`buildMode` can be `debug` or `release` and toggles signing, code obfuscation, log stripping.

### Build customization

Plugin points in `hvigorfile.ts`:

```typescript
import { appTasks } from '@ohos/hvigor-ohos-plugin';

export default {
  system: appTasks,
  plugins: [
    // custom plugin object: { pluginId, apply: (node) => { node.registerTask({...}) } }
  ]
};
```

Inject tasks at well-known lifecycle hooks (`@OhosBuildHook(beforeAssemble, afterAssemble, ...)` patterns). Use `obfuscation-rules.txt` for ProGuard-style rules in `release`.

## ohpm (package manager)

Manages third-party Open Harmony Package Manager packages (the HAR/HSP ecosystem). Installed alongside DevEco Studio; CLI is `ohpm`.

```bash
ohpm init                    # init a package
ohpm install @ohos/axios     # add a runtime dep
ohpm install --save-dev <pkg>
ohpm uninstall <pkg>
ohpm publish                 # publish (requires registry credentials)
ohpm config set registry https://ohpm.openharmony.cn/ohpm/
```

Configured per project via `oh-package.json5`:

```json5
{
  "name": "myapp",
  "version": "1.0.0",
  "description": "",
  "main": "",
  "dependencies": {
    "@ohos/axios": "^2.2.7"
  },
  "devDependencies": {}
}
```

Packages land in `oh_modules/` (analogous to `node_modules/`). Don't check it in.

## Signing & running on device

Two signing flows:

### Automatic (recommended for dev)

1. `File > Project Structure > Signing Configs`.
2. Click **Sign In** (uses your Huawei developer account) if not signed in.
3. Tick **Automatically generate signature**.

DevEco creates a debug signature material and updates `build-profile.json5`. No manual P12 / cer / sign profile file management.

### Manual

You'll need:
- `.p12` keystore
- `.csr` (cert signing request) → produce a `.cer` from AGC console
- `.p7b` profile from AGC (debug or release)

Configure under `signingConfigs[0].material` in `build-profile.json5`.

### Common pitfalls

- `signing` failed: account hasn't accepted developer terms, or device not registered to your account. Connect device once with same Huawei ID.
- Time skew between local clock and device blocks signing. Sync NTP.

### Running

- **Local device**: USB-connect a HarmonyOS device → green Run.
- **Emulator**: enable in `Device Manager` → DevEco downloads system image.
- **Simulator** (lightweight wearable): emulates wearable-class devices.

CLI deploy: `hdc app install entry/build/default/outputs/default/entry-default-signed.hap`. `hdc` is HarmonyOS's adb-equivalent.

## Debugging

Run/Debug from the toolbar. Breakpoints inside `.ets` files Just Work. Console output goes to the *Log* panel; system logs use `hilog`:

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
hilog.info(DOMAIN, 'tag', 'msg=%s', 'hi');
```

`hilog levels`: `debug`, `info`, `warn`, `error`, `fatal`. Filter in DevEco's Log panel by Domain ID (hex) and/or Tag.

## Publishing

For release: build `.app` via `./hvigorw assembleApp` after switching `buildMode` to `release` and signing with a release profile. Upload to AppGallery Connect (AGC) via web console.

Step summary:
1. Reserve the bundleName at AGC (`AppGallery Connect → My apps → Add app → HarmonyOS`).
2. Register a release signing certificate (CSR → submit → download `.cer` and `.p7b`).
3. Configure `signingConfigs.material` for the release product.
4. `./hvigorw assembleApp -p buildMode=release -p product=default`.
5. Upload the `.app` in AGC; submit for review.

## Useful command-line tools

- `hvigorw` — build (see above).
- `ohpm` — packages (see above).
- `hdc` — device interaction (`hdc list targets`, `hdc shell`, `hdc app install`, `hdc file send`).
- `codelinter` — lint code: `codelinter -p ./entry`.
- `hstack` — stack-trace symbolicator: `hstack -d <hap.unstripped.app.so> -i 0x12345`.
- `image-tool` — convert app icons.
- DevEco's Codegenie family (AI coding assist) — invoke via the IDE menus; not all features available offline.
