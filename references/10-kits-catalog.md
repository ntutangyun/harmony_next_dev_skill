# HarmonyOS SDK Kits catalog (where to look for each capability)

This catalog maps a feature area to the Kit you import from, the typical entry-point module, and the canonical doc page. Each Kit is documented in detail at `https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/<slug>`.

When a user asks for a capability, identify the kit, then either:
1. Read the bundled overview page in `references/pages/<slug>.md` (if it's one we crawled), or
2. Fetch the canonical URL.

## Application framework

| Capability | Kit / import | Canonical slug |
|---|---|---|
| UIAbility, ExtensionAbility, Context, Want | `@kit.AbilityKit` | `ability-kit` |
| Accessibility | `@kit.AccessibilityKit` | `accessibility-kit` |
| State preferences, KV, RDB, distributed data | `@kit.ArkData` | `arkdata` |
| ArkTS runtime extensions | `@kit.ArkTS` | `arkts` |
| ArkUI components, animations, gestures | `@kit.ArkUI` | `arkui` |
| Embedded Web view | `@kit.ArkWeb` | `arkweb` |
| Background tasks | `@kit.BackgroundTasksKit` | `background-task-kit` |
| Content embed (cross-process UI fragments) | `@kit.ContentEmbedKit` | `content-embed-kit` |
| File system, Picker | `@kit.CoreFileKit` | `core-file-kit` |
| ArkTS cards (widgets) | `@kit.FormKit` | `form-kit` |
| Input method | `@kit.IMEKit` | `ime-kit` |
| Cross-process / cross-device IPC | `@kit.IPCKit` | `ipc-kit` |
| i18n / l10n | `@kit.LocalizationKit` | `localization-kit` |

## System

| Capability | Kit / import | Canonical slug |
|---|---|---|
| Crypto, keystore, biometrics | `@kit.UniversalKeystoreKit`, `@kit.UserAuthenticationKit` | `system-security` |
| Algorithm-level crypto (encrypt/decrypt, sign/verify, digest, MAC, KDF, key agreement) — guides consolidated per algorithm in the 2026-09 docs (one page covers all AES modes GCM/CCM/CBC/ECB/XTS/segmented; likewise SM4, RSA encrypt, RSA sign) | `@kit.CryptoArchitectureKit` (`cryptoFramework`) | `crypto-aes-sym-encrypt-decrypt`, `crypto-sm4-sym-encrypt-decrypt`, `crypto-rsa-asym-encrypt-decrypt`, `crypto-rsa-sign-sig-verify` (+ `-ndk` variants), `crypto-architecture-glossary` |
| Network: HTTP, WebSocket, connectionmgr, certs | `@kit.NetworkKit` | `system-network` |
| Bluetooth, Wi-Fi, NFC | `@kit.ConnectivityKit` | `system-network` |
| Telephony, SMS | `@kit.TelephonyKit` | `system-basicfun` |
| Sensors, vibrator, light | `@kit.SensorServiceKit` | `system-hardware` |
| Battery, performance, hilog | `@kit.BasicServicesKit`, `@kit.PerformanceAnalysisKit` | `system-basicfun`, `system-debug-optimize` |
| Kernel enhance (QoS task scheduling, 格物, Purgeable memory) | `@kit.KernelEnhanceKit` (NDK: `qos/qos.h`, `libqos.so`) | `kernel-enhance-kit`, `qos-guidelines` |
| Network acceleration / multi-network concurrency | `@kit.NetworkBoostKit` | `networkboost-introduction` |
| Enterprise threat protection (virus remediation, file isolation) | `@kit.EnterpriseThreatProtectionKit` | `enterprise-threat-protection-kit-guide`, `enterprisethreatprotection-introduction` |
| MDM (device management) | `@kit.MDMKit` | (visit MDMKit pages) |

## Media

| Capability | Kit / import | Canonical slug |
|---|---|---|
| Audio I/O, AVPlayer, AVRecorder, sound pool | `@kit.MediaKit`, `@kit.AudioKit` | `media-kit`, `audio-kit` |
| Audio focus & audio session (并发/打断管理: MIX/DUCK/PAUSE) | `@kit.AudioKit` | `audio-playback-concurrency-audio-session-overview`, `audio-session` |
| Spatial audio rendering (空间渲染, C/C++, API 23+) | `@kit.AudioKit` (OHAudioSuite) | `audio-suite-space-render` |
| Codecs | `@kit.AVCodecKit` | `avcodec-kit` |
| Playback session controls | `@kit.AVSessionKit` | `avsession-kit` |
| Camera (preview, capture, video) | `@kit.CameraKit` | `camera-kit` |
| DRM | `@kit.DrmKit` | `drm-kit` |
| Image decoding / encoding / processing | `@kit.ImageKit` | `image-kit` |
| MediaLibrary (Photos/Videos albums) | `@kit.MediaLibraryKit` | `medialibrary-kit` |
| Ringtones | `@kit.RingtoneKit` | `ringtone-kit-guide` |
| QR / barcode scan | `@kit.ScanKit` | `scan-kit-guide` |

## Graphics

| Capability | Kit / import | Slug |
|---|---|---|
| 2D vector / canvas / paint | `@kit.ArkGraphics2D` | `arkgraphics-2d` |
| 3D scene rendering | `@kit.ArkGraphics3D` | `arkgraphics-3d` |
| GPU/Vulkan helpers | `@kit.GraphicsAccelerateKit` | `graphics-accelerate-kit-guide` |
| XEngine | `@kit.XEngineKit` | `xengine-kit-guide` |
| AR sessions | `@kit.ARKit` (AR Engine) | `ar-engine-guide` |
| Spatial reconstruction | `@kit.SpatialReconKit` | `spatial-recon-kit-guide` |

## Application services (Huawei mobile services)

These typically require account configuration in AGC.

| Capability | Kit / import | Slug |
|---|---|---|
| HUAWEI ID sign-in, account info | `@kit.AccountKit` | `account-kit-guide` |
| Ads (banner, native, rewarded) | `@kit.AdsKit` | `ads-kit-guide` |
| App Linking deep links | `@kit.AppLinkingKit` | `app-linking-kit-guide` |
| AppGallery / store | `@kit.StoreKit` | `store-kit-guide` |
| Calendar | `@kit.CalendarKit` | `calendar-kit` |
| Call (voip / Telecom) | `@kit.CallKit` | `call-kit-guide` |
| Cloud functions / DB / storage | `@kit.CloudFoundationKit` | `cloud-foundation-kit-guide` |
| Contacts | `@kit.ContactsKit` | `contacts-kit` |
| Enterprise data isolation | `@kit.EnterpriseSpaceKit` | `enterprise-space-kit-guide` |
| File Manager service | `@kit.FileManagerServiceKit` | `file-manager-service-kit-guide` |
| Game controller | `@kit.GameControllerKit` | `game-controller-kit` |
| Game Service (leaderboards, achievements) | `@kit.GameServiceKit` | `game-service-kit-guide` |
| Health (fitness, heart rate, sleep); LiteWearable health apps | `@kit.HealthServiceKit` | `health-service-kit-guide`, `health-litewearable-app-dev` |
| In-app purchases | `@kit.IAPKit` | `iap-kit-guide` |
| Live View (lock-screen / always-on cards) | `@kit.LiveViewKit` | `live-view-kit-guide` |
| Location (GPS, geofence) | `@kit.LocationKit` | `location-kit` |
| Map (rendering, navigation, geocoding) | `@kit.MapKit` | `map-kit-guide` |
| Notification | `@kit.NotificationKit` | `notification-kit` |
| Payment (Huawei Pay) | `@kit.PaymentKit` | `payment-kit-guide` |
| PDF rendering | `@kit.PDFKit` | `pdf-kit-guide` |
| Preview (document/image picker preview) | `@kit.PreviewKit` | `preview-kit-guide` |
| Push notifications | `@kit.PushKit` | `push-kit-guide` |
| Reader (ebook / pdf) | `@kit.ReaderKit` | `reader-kit-guide` |
| Scenario Fusion (multi-device co-op) | `@kit.ScenarioFusionKit` | `scenario-fusion-kit-guide` |
| Screen-time guardrails | `@kit.ScreenTimeGuardKit` | `screen-time-guard-kit-guide` |
| Share Sheet (cross-app) | `@kit.ShareKit` | `share-kit-guide` |
| Wallet (passes, payment cards) | `@kit.WalletKit` | `wallet-kit-guide` |
| Weather | `@kit.WeatherServiceKit` | `weather-service-kit-guide` |

## AI

| Capability | Kit / import | Slug |
|---|---|---|
| Agent Framework Kit — launch a published agent via Function component (HMAF) | `@kit.AgentFrameworkKit` | `harmony-agent-framework-kit-guide`, `hmaf-introduction` |
| Device-side A2A agents — *expose* an agent via `AgentExtensionAbility` (API 24+) | `@kit.AbilityKit` (`AgentExtensionAbility`) | `agent-guideline`, `agent-overview`, `agent-development`, `agent-extension-configuration` — see `references/04-ability-and-lifecycle.md` |
| CANN heterogeneous compute | `@kit.CANNKit` | `cann-kit-guide` |
| CANN on-device LLM (大模型能力: quantization + model conversion) | `@kit.CANNKit` | `cannkit-llm-developer`, `cannkit-llm-model-quantization`, `cannkit-llm-model-conversion` |
| Speech (TTS, ASR core) | `@kit.CoreSpeechKit`, `@kit.SpeechKit` | `core-speech-kit-guide`, `speech-kit-guide` |
| Vision (face, text, body, gesture) core / scenario | `@kit.CoreVisionKit`, `@kit.VisionKit` | `core-vision-kit-guide`, `vision-kit-guide` |
| User intents framework (Siri-style intents) | `@kit.IntentsKit` | `intents-kit-guide` |
| Multimodal awareness (多模态融合感知): device stationary/motion state, operating hand / holding hand (动作感知), metadata binding (记忆链接) — subscribe/unsubscribe model, needs permissions + sensor support | `@kit.MultimodalAwarenessKit` (`stationary`, `motion`) | `multimodalawareness-kit-intro`, `stationary-guidelines`, `stationary-glossary` |
| MindSpore Lite inference | `@kit.MindSporeLiteKit` | `mindspore-lite-kit` |
| Natural Language understanding | `@kit.NaturalLanguageKit` | `natural-language-kit-guide` |
| Neural Network Runtime | `@kit.NeuralNetworkRuntimeKit` | `neural-network-runtime-kit` |

## NDK / native development

When ArkTS isn't enough (perf-critical compute, existing C/C++):
- Build with the **NDK** (gn / CMake project under `cpp/`).
- Bind to ArkTS via **NAPI** (`napi_api.h`). Auto-generated by DevEco for "Native C++" template.
- Embed an `XComponent` to render native OpenGL / Vulkan inside ArkUI.
- Page: `ndk-development-overview`, `create-with-ndk`, `build-with-ndk`, `coding`, `build-toolchain`, `debugging-profiling`, `hardware-compatibility`.
- **Build ArkUI from C/C++ (ArkUI-NDK)** — the native C-API now covers layout, lists/grids, Swiper, navigation, Text/form/media components, and event handling: `ndk-layout-container`, `ndk-common-attribute-layout`, `arkts-list-and-grid-ndk`, `ndk-swiper`, `ndk-navigation-query`, `ndk-use-text-component`, `ndk-build-form-components`, `arkts-build-media-ndk`, `ndk-add-component-events`, `ndk-add-event-response`, `ndk-bind-input-events`. See `references/03-arkui-ui.md`.
- C/C++ static analysis: DevEco's built-in **Clang-Tidy** (`ide-clang-tidy`, see `references/08-tooling-and-build.md`).

## Accessories, external displays & casting (what an app can and can't do)

Useful when someone designs **hardware that pairs with a HarmonyOS phone** (e.g. a screen+keyboard "laptop shell") or wants the phone to drive another screen. Key constraints, all from the guides:

- **Accessory Kit** (`@kit.AccessoryKit`, `accessoryAccessManager`; `accessorykit-introduction`, `accessory-dev-guides`, `accessory-kit-glossary`) — pairing picker, association wake-up (auto-launch the vendor app when the accessory connects), system-service attach, trust management; `showAccessPicker` / `queryAttachedService` / `registerConnectListener` / `connect` / `disconnect` / `detachService`; half-managed vs fully-managed pairing modes (half-managed: re-connect within 365 days needs no new confirmation). **Restricted**: open only to Huawei-ecosystem partner enterprise apps, needs ACL permission `ohos.permission.ALLOW_ACCESSORY_ACCESS` granted after partnership + test admission; China mainland only; Phone/Tablet/PC-2in1 hosts; the accessory must support Wi-Fi P2P + BLE.
- **System screen mirroring** is done by the OS, not by apps. The receiving device must support **Cast+** (Huawei) or **Miracast** (`avsession-extended-screen`).
- **Extended-screen casting** (`@kit.AVSessionKit`, `avsession-extended-screen`): *after* the system has started a wired/wireless cast (virtual extended screen ≥ 1080P), an app gets the displays via `session.getAllCastDisplays()` / `session.on('castDisplayChange', cb)` (`CastDisplayState.STATE_ON/OFF`), then launches **its own** second UIAbility there with `context.startAbility(want, { displayId })`. It must fill the screen, and the system rejects it unless the main-screen foreground UIAbility belongs to the same app. So this gives dual-screen for your own app only, not a desktop for the whole phone.
- **Virtual screens / multi-screen `Screen` APIs are system-app only** (some also need `ohos.permission.CAPTURE_SCREEN`); third-party apps can only query/listen to `display` properties (`displaymanager-overview`, `screenproperty-guideline`). Logical screen types: main, mirror, extended, 异源 (heterogeneous) (`display-terminology`).
- **Desktop-like windowing**: PC/2in1 windows are free-form by default; the docs list **电脑模式 (PC mode)** only for some Tablets, while some Phones offer **自由多窗** (free multi-window) (`freeform-window-overview`). The guides give no API for a phone "desktop mode" on an external screen.
- **Input peripherals**: `@kit.InputKit` `inputDevice.getDeviceList()` / `getKeyboardType()` / `on('change')` to detect a physical keyboard (`inputdevice-guidelines`); mouse pointer styles (`pointerstyle-guidelines`); ArkUI keyboard/mouse events (`arkts-interaction-development-guide-keyboard`, `-mouse`). **NearLink Kit** (星闪, `@kit.NearLinkKit`, `nearlink-introduction`) is a low-power, high-rate short-range link whose example uses include mice and styluses. USB/HID peripheral drivers go through the DDK guides (`usb-ddk-guidelines`, `hid-ddk-guidelines`).

## How to use this catalog

When the user says "I want X":
1. Look up X in the table.
2. Either read the bundled `references/pages/<slug>.md` (some are pre-crawled; most aren't), or **fetch the canonical URL** `https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/<slug>` if you have web access.
3. Always validate the API surface against the version the user is targeting (their `compileSdkVersion` / `compatibleSdkVersion`).

If neither approach works, point the user at the URL — they can read alongside you, and you can write code while they verify availability.
