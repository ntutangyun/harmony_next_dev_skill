# Testing, performance, security, UX guidelines

Source pages:
- app-testing-overview, ut
- experience-suggestions-overview, performance-experience-suggestions
- security-privacy-experience-standards, experience-suggestions-ux

## Testing surface

HarmonyOS ships **hypium** as its unit + UI testing framework. It comes with DevEco Studio templates.

### Unit testing

Tests live in `entry/src/ohosTest/ets/test/`. A simple test:

```typescript
import { describe, it, expect, beforeEach } from '@ohos/hypium';

export default function calculatorTest() {
  describe('Calc', () => {
    let calc: { add(a: number, b: number): number };
    beforeEach(() => { calc = { add: (a, b) => a + b }; });
    it('adds', 0, () => {
      expect(calc.add(2, 3)).assertEqual(5);
    });
  });
}
```

A test list file (`List.test.ets`) aggregates suites for the runner to pick up:

```typescript
import calculatorTest from './Calculator.test';
export default function testsuite() {
  calculatorTest();
}
```

Run: in DevEco, right-click the `ohosTest` folder → Run. Or CLI: `./hvigorw test`.

### UI testing

UI tests use the same hypium runner plus `@ohos.UiTest` to drive the UI:

```typescript
import { Driver, ON, MatchPattern } from '@ohos.UiTest';

const driver = Driver.create();
await driver.assertComponentExist(ON.text('Hello World'));
await driver.findComponent(ON.text('Next', MatchPattern.EQUALS)).then((c) => c.click());
await driver.delayMs(500);
await driver.assertComponentExist(ON.text('Hi there'));
```

UI tests must run on a device/emulator (not just JVM). The runner deploys two HAPs: the app under test (`entry`) plus a test HAP (`ohosTest`).

### Specialised testing services

AppGallery's *Test Service* provides cloud-run tests: compatibility, stability (monkey), performance (start-up time, memory, frame), power. Submit a `.hap` via AGC console.

## Performance suggestions (must-knows)

### Cold start time

- Minimize work in `EntryAbility.onCreate` / `onWindowStageCreate`. Load and parse small data, defer the rest to `onWindowStageCreate → loadContent`'s callback or to `aboutToAppear` in the first page.
- Use the **AppStartup framework** (`app_startup_config.json5`) to declare initialization tasks with dependencies. The framework runs them in parallel where possible.
- Defer non-critical features behind feature flags.

### List perf

- For lists >50 items, switch to `LazyForEach`.
- Implement a proper `keyGenerator` — never let it be the index, otherwise items mis-recycle.
- Mark item components `@Reusable` and implement `aboutToReuse(params)`.
- Avoid setting `width('100%').height('100%')` on the inner-most child if parent already constrains; ArkUI's layout pass works harder than it needs to.

### State management

- Move expensive computations into `@Computed` (V2) or memoize in plain code; avoid recomputing in `build()`.
- Don't reassign large arrays/objects unless you have to — the framework will diff aggressively.
- Use `@Track` to limit which class fields trigger re-render.

### Frame drops & jank

- Long synchronous code on the UI thread blocks frame production. Move to TaskPool / Worker.
- Use the **Profiler → Lag and Frame Loss** template to spot main-thread offenders.
- Avoid synchronous file or DB IO on the UI thread.

### Memory & GC

- Release `HttpRequest` / `WebSocket` / `RdbStore` / file handles explicitly.
- Watch out for `setInterval` / `setTimeout` callbacks that keep references alive after navigation.
- Use the **Allocation / Snapshot** Profiler templates to chase leaks.

## Security & privacy

Code & data:
- **Never** put secrets (API keys, certs) in plaintext source. Use `Universal Keystore Kit` to store keys in secure storage.
- For network certs: pin via `network-security-config` JSON; never trust user CAs unless your threat model says so.
- Don't log PII or tokens with `hilog`. Use a redactor.
- Code obfuscation: enable in `obfuscation-rules.txt`; release builds auto-obfuscate when `buildMode: release`.

Permissions:
- Ask only what you need. The system grades sensitive perms (`user_grant`) and shows a sheet.
- For `LOCATION`, prefer `APPROXIMATE_LOCATION` over `LOCATION`. For continuous, declare `LOCATION_IN_BACKGROUND` and explain.
- For `INTERNET` (auto-granted but must be declared), keep your traffic on HTTPS; cleartext HTTP requires a `network-security-config` opt-in per domain.

Data handling:
- Pick the right `securityLevel` for KV / RDB stores: `S1` (default), `S2`, `S3`, `S4`. Higher = stronger encryption, lower performance.
- Use **Asset Kit** (`@kit.AssetStoreKit`) for short-token storage; `Universal Keystore Kit` for cryptographic operations. For ECC key interop, Crypto Architecture Kit now supports converting between compressed and uncompressed ECC public keys / points (`pages/crypto-convert-compressed-or-uncompressed-ecc-pubkey.md`, NDK variant `*-ndk`).
- For backup: declare allowed dirs in `BackupExtensionAbility` (`backupExtensionInfo` whitelist/blacklist).

Authentication:
- For login: **Account Kit** offers "Sign in with HUAWEI ID" (`getQuickLoginAnonymousPhone`, `oneStepLogin`).
- For biometrics: **User Authentication Kit** (`userAuth` API) — face / fingerprint.

## UX guidelines (highlights)

The official UX guide is dense; the things you usually act on:

- **Dark mode** — set `colorMode` in `module.json5` (`auto` / `dark` / `light`); test all screens in both.
- **Multi-device** — use ResponsivePattern (GridRow) or **Adaptive layout**; avoid hard-coded breakpoints.
- **System bars** — set `systemBarProperties` once at `onWindowStageCreate`; respect safe-area insets via `expandSafeArea([SafeAreaType.SYSTEM])` on the root.
- **Splash screen** — replace the auto-generated `start_window.png` and customize colors.
- **Localization** — keep all user-visible strings in resources, prefer `LengthMetrics` for spacing across density.
- **Accessibility** — every interactive element should have `accessibilityText` (or rely on inner Text). Test with TalkBack equivalent.
- **Haptics** — `@kit.SensorServiceKit` `vibrator.startVibration` for confirmation tactile feedback.
- **Atomic Services (元服务)** must fit ≤ 10 MB at install; use HSP for sharing common code.

## Where to dig deeper

For each topic above, the canonical pages on developer.huawei.com expand into much greater detail — visit the specific slug referenced in the source list at the top of each section.
