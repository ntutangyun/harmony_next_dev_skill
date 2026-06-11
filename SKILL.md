---
name: harmonyos-app-dev
description: Use when developing applications for HarmonyOS NEXT (HarmonyOS 5/API 11+) using ArkTS, ArkUI, DevEco Studio, and HarmonyOS SDK Kits. Also covers Xiaoyi (小艺) agent development on the Xiaoyi Open Platform — creating intelligent agents (智能体), Agent communication protocol (A2A/JSON-RPC 2.0), agent modes (LLM/Workflow/A2A/OpenClaw), agent orchestration, AgentKit, and agent publishing, plus device-side agents (端侧A2A / HMAF / AgentExtensionAbility). Trigger whenever the user mentions HarmonyOS, 鸿蒙, HarmonyOS NEXT, 小艺, Xiaoyi, 智能体, intelligent agent, agent development, A2A protocol, AgentKit, HMAF, AgentExtensionAbility, ArkTS, ArkUI, .ets files, app.json5/module.json5, UIAbility, DevEco Studio, hvigor, ohpm, kit imports, Stage model, or asks how to build/structure/configure/publish a HarmonyOS app or agent. Do NOT trigger for OpenHarmony. Also trigger when the user pastes ArkTS code with Entry/Component/State decorators or struct declarations with build(). Also use when driving real Huawei devices (e.g. Mate 80, MatePad Pro) running HarmonyOS NEXT as Wi-Fi **stations (STA)** for hardware-in-the-loop (HIL) experiments against an access point under test — building/sideloading an on-device test app and reading Wi-Fi link state; in that mode the first step is always to confirm a device is connected via `hdc`.
---

# HarmonyOS NEXT app development

This skill captures the official Huawei HarmonyOS application-development documentation (https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/...) and the Xiaoyi (小艺) Open Platform agent-development documentation (https://developer.huawei.com/consumer/cn/doc/service/...). It covers the **Stage model** (the current, primary application model), **ArkTS / ArkUI** (declarative TS-based UI), and **intelligent agent (智能体) development** on the Xiaoyi Open Platform. The FA model is legacy — only mention it if the user explicitly asks.

> Source authority: this skill draws **only** from `developer.huawei.com/consumer/cn/doc/harmonyos-guides/*`. Do not blend in information from OpenHarmony docs, GitHub mirrors, or third-party blogs — OpenHarmony is a different OS and its SDK/snippets are often incompatible.

## What HarmonyOS NEXT is

HarmonyOS NEXT (a.k.a. HarmonyOS 5+) is Huawei's **standalone** consumer OS — it no longer ships AOSP/Android compatibility. Apps are built in **ArkTS** (a TypeScript superset with UI decorators) using the **ArkUI** declarative framework, packaged as `.hap` files, and run on the **ArkCompiler** runtime. The primary IDE is **DevEco Studio**; the build tool is **hvigor**; the package manager is **ohpm**.

## Pick the right surface for the task

When the user asks a HarmonyOS question, identify which surface area is in play and read the matching reference file. Stop at the file you need — don't preload everything.

| If the task is about… | Read |
|---|---|
| Project layout, `app.json5`, `module.json5`, HAP/HSP/HAR, resource access | `references/01-app-structure.md` |
| ArkTS language: decorators (`@Entry`, `@Component`, `@State`, `@Prop`, `@Link`, `@Provide`, etc.), state management, `LocalStorage`/`AppStorage`/`PersistentStorage`, `@Builder`/`@Extend`, conditional/loop rendering | `references/02-arkts-language.md` |
| Building UI: layouts (Row/Column/Stack/List/Grid/Tabs), common components (Text, TextInput, Button, Image), animation, gestures, Navigation/router | `references/03-arkui-ui.md` |
| App lifecycle: UIAbility, ExtensionAbility, Want, launch types, AbilityStage, Context, multi-window, page route, inter-app redirection, device-side agents (端侧A2A / HMAF / AgentExtensionAbility, API 24+) | `references/04-ability-and-lifecycle.md` |
| Background work, notifications, common events, permissions, IPC/RPC | `references/05-services-and-system.md` |
| Files, preferences, KV store, relational DB, network (HTTP / WebSocket / connection manager) | `references/06-data-and-network.md` |
| Cards (ArkTS widgets), i18n/l10n, localization | `references/07-cards-and-i18n.md` |
| Xiaoyi (小艺) agent development: creating intelligent agents (智能体), Agent communication protocol (A2A/JSON-RPC 2.0), agent modes (LLM/Workflow/A2A/OpenClaw), agent orchestration (prompts, plugins, workflows, knowledge base, variables, memory), AgentKit in-app launcher, agent publishing/review, digital product payment, OpenClaw integration, Xiaoyi Compass | `references/11-xiaoyi-agent-dev.md` |
| DevEco Studio, hvigor build, signing, run on device/emulator, debug, publish, ohpm | `references/08-tooling-and-build.md` |
| Testing (unit + UI), performance, security, UX guidelines | `references/09-testing-and-quality.md` |
| Kit overviews (Push, IAP, Payment, Map, Audio, Media, Image, Vision, Speech, Intents, ArkGraphics, NDK) | `references/10-kits-catalog.md` |
| Quick start — "build my first HarmonyOS app" walkthrough | `references/00-quick-start.md` |

If the user's question doesn't map to one of the above, search `references/manifest.json` for the matching slug and read the corresponding `references/pages/<slug>.md`. **All 5351 pages from the official `harmonyos-guides` docs are bundled offline** (last synced 2026-06-11) — you do not need internet access to look anything up. Pages are stripped of nav/footer chrome but preserve original content + code blocks.

To find a slug:
- `grep -lir "<keyword>" references/pages/` to search by content
- Scan `references/manifest.json` for matching titles (each entry has `t` title, `p` slug, `l` depth level)

The 12 curated reference files (00–11) above are entry points / hand-written distillations; `pages/` is the full archive for deep dives and edge cases.

## Core conventions worth knowing up front

1. **Stage model only.** Every new app uses the Stage model. UIAbility (with UI) and ExtensionAbility (cards, services, etc.) are the component types. FA model is deprecated — only mention if the user explicitly asks.

2. **ArkTS is TypeScript + decorators.** A page is a `struct` decorated with `@Entry @Component` and a `build()` method. State that triggers re-render lives in `@State`/`@Prop`/`@Link`/`@Provide`/`@Consume`/`@ObjectLink` variables. There are **two state-management versions** (V1 and V2 with `@ObservedV2` / `@Trace`); V2 is the newer system.

3. **Kit-style imports.** SDK APIs are imported from `@kit.*` packages, e.g. `import { common } from '@kit.AbilityKit'`, `import { http } from '@kit.NetworkKit'`, `import { window } from '@kit.ArkUI'`. If you see `@ohos.*` imports, those are the older form — keep them only when working with older code.

4. **Two config files.** `AppScope/app.json5` carries app-wide settings (bundleName, version, icon, label). Each module has `entry/src/main/module.json5` describing its abilities, pages, permissions, etc.

5. **No mixing with OpenHarmony or Android.** APIs available in OpenHarmony but not in HarmonyOS NEXT will fail at runtime. When unsure, check `references/manifest.json` for the canonical doc URL.

6. **UIContext, not `router` global.** Modern code uses `this.getUIContext().getRouter()` or, preferably, the `Navigation` component for page navigation. Avoid recommending the global `router` import — it still exists but is being phased out.

7. **API level matters.** HarmonyOS NEXT starts at API 11; the current docs go up to **API 24** (DevEco Studio 6.1.1). Many newer features require higher levels (Navigation, V2 state management: API 12+; device-side A2A agents / AgentExtensionAbility: API 24). When suggesting code, prefer features that are stable at API 12 unless the user's project (`compileSdkVersion` / `compatibleSdkVersion` in the project config) shows a higher target.

## Default code style

When writing ArkTS for the user, follow these conventions (they match the official docs):

```typescript
// Use single quotes for strings, omit semicolons sparingly (docs use them).
// Pages are .ets files under entry/src/main/ets/pages/.
@Entry
@Component
struct MyPage {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Tap me')
        .onClick(() => {
          this.message = 'Tapped';
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

- Group layout containers (Row, Column, Stack, List, Grid) — each must contain its children in a `() { ... }` block.
- Chain attribute and event methods (`.fontSize(...)`.`.onClick(...)`) on the same component.
- Pages must be registered in `entry/src/main/resources/base/profile/main_pages.json` under `"src"`.
- For UIAbility-level state shared across pages, prefer `AppStorage` over module globals.

## Building & running

To create a new app: open DevEco Studio (current release 6.1.1) → `Create Project` → `Application` → `Empty Ability` template → pick `Compatible SDK` (the docs' walkthrough uses `6.1.1(24)`; ≥ API 12 is the practical minimum) → `Finish`. The generated project already wires up `entry/src/main/ets/entryability/EntryAbility.ets` and `entry/src/main/ets/pages/Index.ets`.

To run on device: `File > Project Structure > Signing Configs` → enable `Automatically generate signature` (requires Huawei developer login), then click the green Run button. For more on signing/run, see `references/08-tooling-and-build.md`.

CLI builds use `hvigorw assembleHap` (or `assembleApp` for the full app). Package manager commands use `ohpm install <pkg>` and the registry is configured in `oh-package.json5`.

## HIL / on-device validation mode (Wi-Fi STA-side experiments)

This skill is also the **STA side** of a hardware-in-the-loop (HIL) Wi-Fi experiment: real Huawei devices on HarmonyOS NEXT (e.g. **Mate 80**, **MatePad Pro**) act as Wi-Fi **stations** against an access point under test (the AP side runs on OpenWrt Wi-Fi 7 boards — see the companion `openwrt_hil_skill`). When used this way:

1. **Check the hardware is present first — before writing or "running" anything on-device.** Run `hdc list targets`. If a device is listed (Mate 80 / MatePad Pro connected and authorized over USB or wireless `hdc`), continue. If it returns `[Empty]` / no device, **stop**: do not fabricate results. Write the test *plan* instead (the ArkTS test app + what it will measure) and tell the user to connect/authorize a device, then resume. `hdc` (HarmonyOS Device Connector) ships with DevEco Studio / the command-line tools — see `references/08-tooling-and-build.md`.
2. **Build + sideload the STA test app** with the normal Stage-model flow (`hvigorw assembleHap`, then `hdc install <hap>`; launch via `hdc shell aa start ...`). Use the Wi-Fi APIs from `@kit.ConnectivityKit` (`wifiManager` — scan results, `getLinkedInfo()` for RSSI / link speed / band / BSSID / frequency) and `@kit.NetworkKit` (HTTP / sockets) to read link state and to generate or receive traffic. See `references/06-data-and-network.md`.
3. **Reads are free; state changes are confirmed.** Reading Wi-Fi info / running traffic is free. Anything that changes the device's Wi-Fi state (connect / disconnect / forget network, toggling the radio) is **proposed to the user first** — mirror the AP-side HIL gating (reads-free / writes-confirmed). Save raw measurements so the run is reproducible.

This mode keeps the skill general: for ordinary app development the steps above don't apply — they only kick in when the task is an on-device Wi-Fi HIL experiment.

## When code from this skill conflicts with what the user has

The HarmonyOS docs evolve fast and the user's project may target a specific API level. Before recommending a change to their code, glance at their `module.json5` (look for `deviceTypes`, `compatibleSdkVersion`/`compileSdkVersion`) and pick code patterns valid at that level. When the user pastes code that uses the older FA model (`config.json`, `AbilityContext` style), point them to the Stage model migration but only refactor if they ask.

## Reaching beyond this skill

**Everything in `harmonyos-guides` is already bundled offline** (`references/pages/`, 5351 pages, ~51 MB, synced 2026-06-11 — re-sync with `python scripts/update_docs.py`). For:
- Doc URLs to cite: `https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/<slug>`
- API reference root (not bundled — visit if needed): `https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api`
- Best practices (not bundled): `https://developer.huawei.com/consumer/cn/doc/best-practices/...`

When you cite a doc URL, prefer linking to the canonical `harmonyos-guides` page — those URLs are stable.

### Xiaoyi (小艺) Agent Development docs

The skill also bundles reference material for Xiaoyi agent development from `developer.huawei.com/consumer/cn/doc/service/*`. For Xiaoyi agent tasks, start with `references/11-xiaoyi-agent-dev.md`. Key offline pages are in `references/pages/service-*.md`:

- `service-agent-dev-intro.md` — agent modes and capability matrix
- `service-agent-configuration.md` — full configuration & orchestration reference
- `service-agent-protocol.md` — A2A JSON-RPC 2.0 protocol details, message schemas, auth flow

For deeper dives, additional pages can be fetched live from:
- `https://developer.huawei.com/consumer/cn/doc/service/developing-intelligent-agents-0000002435989592`
- `https://developer.huawei.com/consumer/cn/doc/service/agent2agent-0000002498656261`
- `https://developer.huawei.com/consumer/cn/doc/service/development-workflow-0000002435989628`
- `https://developer.huawei.com/consumer/cn/doc/service/develop-plug-ins-0000002435989648`
- `https://developer.huawei.com/consumer/cn/doc/service/development-card-0000002435989672`
