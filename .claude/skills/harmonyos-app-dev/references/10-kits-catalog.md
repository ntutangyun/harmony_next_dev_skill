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
| Network: HTTP, WebSocket, connectionmgr, certs | `@kit.NetworkKit` | `system-network` |
| Bluetooth, Wi-Fi, NFC | `@kit.ConnectivityKit` | `system-network` |
| Telephony, SMS | `@kit.TelephonyKit` | `system-basicfun` |
| Sensors, vibrator, light | `@kit.SensorServiceKit` | `system-hardware` |
| Battery, performance, hilog | `@kit.BasicServicesKit`, `@kit.PerformanceAnalysisKit` | `system-basicfun`, `system-debug-optimize` |
| MDM (device management) | `@kit.MDMKit` | (visit MDMKit pages) |

## Media

| Capability | Kit / import | Canonical slug |
|---|---|---|
| Audio I/O, AVPlayer, AVRecorder, sound pool | `@kit.MediaKit`, `@kit.AudioKit` | `media-kit`, `audio-kit` |
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
| AR sessions | `@kit.ARKit` (AR Engine) | `ar-engine-kit-guide` |
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
| Health (fitness, heart rate, sleep) | `@kit.HealthServiceKit` | `health-service-kit-guide` |
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
| Agent framework (LLM agents / tool use) | `@kit.AgentFrameworkKit` | `harmony-agent-framework-kit-guide` |
| CANN heterogeneous compute | `@kit.CANNKit` | `cann-kit-guide` |
| Speech (TTS, ASR core) | `@kit.CoreSpeechKit`, `@kit.SpeechKit` | `core-speech-kit-guide`, `speech-kit-guide` |
| Vision (face, text, body, gesture) core / scenario | `@kit.CoreVisionKit`, `@kit.VisionKit` | `core-vision-kit-guide`, `vision-kit-guide` |
| User intents framework (Siri-style intents) | `@kit.IntentsKit` | `intents-kit-guide` |
| MindSpore Lite inference | `@kit.MindSporeLiteKit` | `mindspore-lite-kit` |
| Natural Language understanding | `@kit.NaturalLanguageKit` | `natural-language-kit-guide` |
| Neural Network Runtime | `@kit.NeuralNetworkRuntimeKit` | `neural-network-runtime-kit` |

## NDK / native development

When ArkTS isn't enough (perf-critical compute, existing C/C++):
- Build with the **NDK** (gn / CMake project under `cpp/`).
- Bind to ArkTS via **NAPI** (`napi_api.h`). Auto-generated by DevEco for "Native C++" template.
- Embed an `XComponent` to render native OpenGL / Vulkan inside ArkUI.
- Page: `ndk-development-overview`, `create-with-ndk`, `build-with-ndk`, `coding`, `build-toolchain`, `debugging-profiling`, `hardware-compatibility`.

## How to use this catalog

When the user says "I want X":
1. Look up X in the table.
2. Either read the bundled `references/pages/<slug>.md` (some are pre-crawled; most aren't), or **fetch the canonical URL** `https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/<slug>` if you have web access.
3. Always validate the API surface against the version the user is targeting (their `compileSdkVersion` / `compatibleSdkVersion`).

If neither approach works, point the user at the URL — they can read alongside you, and you can write code while they verify availability.
