# DevEco Studio, hvigor, ohpm, signing, publishing

Source pages:
- ide-tools-overview, ide-software-install, ide-project, ide-code-edit
- ide-signing (+ ide-signing-auto, ide-signing-manual), ide-run-device, ide-debug-app
- ide-deveco-cli-* (DevEco CLI), ide-deveco-code-* (DevEco Code), ide-hvigor-releasenote
- ide-hvigor, ide-hvigor-commandline, ide-ohpm-cli, ide-publish-app

## DevEco Studio (IDE)

The official IDE built on IntelliJ. Install from https://developer.huawei.com/consumer/cn/deveco-studio/. Current release is **DevEco Studio 26.0.0 Release** (bundles HarmonyOS SDK 26.0.0(26); version numbering jumped from 6.1.1 to 26.0.0). From 26.0.0 the Profiler / performance tools work with any device on API 20+ without having to match the IDE version to the device API level (`ide-app-analyzer-rules`).

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

### What's new in hvigor (DevEco Studio 26.0.0, per `ide-hvigor-releasenote`)

- Project `build-profile.json5` → `strictMode.apiCompatibilityCheck` (`warn` default / `error`): flag ArkTS APIs whose *since* version is above `compatibleSdkVersion`.
- `strictMode.disableStrictCheckPaths` (skip strict checks for listed third-party lib dirs); `packOptions.deduplicateSo` (drop duplicate `.so` across HAP/HSP when building the APP).
- `tscConfig.tsImportSoCheck`; module `nativeLib.enableSoDirCollection` (load `.so` from `libs/{ABI}/` subdirs).
- `hvigor-config.json5` → `properties["hvigor.daemon.idleTimeout"]` (daemon max idle time).
- Merge a bytecode HAR + all its deps into one standalone HAR (多HAR合并打包); per-target/product/buildMode dependency configuration via plugin.
- Plugin API: `getAllDependencyInfo`; `getOhpmDependencyInfoV2` / `getOhpmRemoteHspDependencyInfoV2` replace the non-V2 versions.

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

Automatic signing covers most debugging. **Manual signing is required** for cross-device debugging, cross-app interaction debugging, offline debugging, several developers sharing one key, or kits that need a certificate fingerprint configured (`ide-signing`).

### Automatic (recommended for dev) — `ide-signing-auto`

1. `File > Project Structure > Signing Configs`.
2. Click **Sign In** (uses your Huawei developer account) if not signed in.
3. Tick **Automatically generate signature**.

DevEco creates a debug signature material and updates `build-profile.json5`. No manual P12 / cer / sign profile file management. Two variants:
- **Linked to a registered AGC app** (DevEco 6.0.0 Beta5+; all regions from 6.1.1 Beta1): DevEco looks up the team's AGC app with the same bundle name, lets you enable open capabilities (Account/Location/Intents Kit on by default; others direct or by application — Push Kit can't be turned off once enabled) and request ACL permissions (a short-lived temporary profile is issued until the ACL request is approved). Pick the team in the *Team* dropdown.
- **Not linked** to an AGC app.
- From **26.0.0**, signing can start after registering the device in AGC; with several devices connected, all of them are written into the certificate.
- Local system time must match Beijing time (UTC+8) or signing fails.

### Manual — `ide-signing-manual`

Generate the key + CSR via **Build > Generate Key and CSR** (DevEco 6.1.0 Beta2+; key-store password ≥ 8 chars mixing ≥ 2 character classes; validity ≥ 25 years recommended). You'll need:
- `.p12` keystore
- `.csr` (cert signing request) → produce a `.cer` from AGC console
- `.p7b` profile from AGC (debug or release)

Configure under `signingConfigs[0].material` in `build-profile.json5`.

### Common pitfalls

- `signing` failed: account hasn't accepted developer terms, or device not registered to your account. Connect device once with same Huawei ID.
- Time skew between local clock and device blocks signing. Sync NTP.

### Running

- **Local device**: USB-connect a HarmonyOS device → green Run.
- **Emulator**: enable in `Device Manager` → DevEco downloads system image. Most Kit overview pages now carry a 模拟器支持情况 section; general differences are in `ide-emulator-specification`. ArkUI-specific gaps on the emulator (per `arkui-overview`): `Image.enableAnalyzer` / image AI analysis (`ImageAnalyzerController`), HDR (`drawableDescriptor.setHdrComposition`), `OH_ArkUI_TextDataDetectorConfig`, `EmbeddedComponent` (ArkTS + NDK `embedded_component.h`), `@ohos.pluginComponent`, `toolbar`, the `@Preview` decorator, `AbilityBase_Want`, `ArkUI_SelectedDragPreviewStyle`, `restoreId`.
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

## DevEco CLI — agent-facing command line (`ide-deveco-cli-*`)

**DevEco CLI** (1.2.0 July 2026, 1.3.0 Aug 2026) packages the HarmonyOS toolchain, knowledge base and curated Skills as a CLI designed to be driven by general AI coding agents (Cursor, OpenCode, …). Runs on Windows/macOS and, from 1.3.0, Linux (set `DEVECO_CLI_CLI_PATH`, e.g. `/opt/command-line-tools`). Needs DevEco Studio 6.0.0+ installed and Node.js (22+ recommended).

```bash
npm install -g @deveco/deveco-cli@stable   # drop @stable for the preview channel
devecocli --version && devecocli update
devecocli init --skill | --mcp [--project <path>] [--agent <name>]   # install the deveco-cli Skill or MCP server into your agent
devecocli auth login | status | team list | logout                    # 1.3.0+: some features need a Huawei ID
devecocli docs search 沉浸光感 [--catalog best-practices] [--format json]; devecocli docs read <documentId>
devecocli create --app-name MyApp [--project-path ./MyApp]
devecocli build [--product <p>] [--modules entry library@phone] [--build-mode release]; devecocli build clean
devecocli signature generate [--product <p>] [--team-id <id>] [--force]   # auto debug signing (1.3.0)
devecocli run [--module entry] [--device 127.0.0.1:5555] [--ability EntryAbility] [--uninstall] [--apply changes.txt | --hotreload-apply change.txt]
devecocli log [--level E] [--crash] [--bundle-name com.example.app] [--follow]
devecocli check lint [--fix] [--incremental] [--format json]; devecocli check compat …   # Code Linter rules / target-SDK API-change scan
devecocli emulator list|start|stop|create|delete|image …|shake|power|rotate|fold|battery|geolocation|sensor|scene
devecocli device list|view; devecocli ui layout|window list|screenshot|click|doubleclick|longclick|swipe|fling|drag|text
devecocli skills list|find|add|remove; devecocli serve mcp; devecocli serve lsp --arkts|--cpp
```

**DevEco Code** (`ide-deveco-code-*`, 0.1.1 July 2026, 0.2.0 Aug 2026) is Huawei's terminal AI coding agent for HarmonyOS, built on BitFun + open-source OpenCode (model/provider/MCP/Skill config, Agent & Goal modes) with the HarmonyOS Skills and DevEco toolchain integrated; 0.2.0 integrates the DevEco CLI atomic capabilities.
