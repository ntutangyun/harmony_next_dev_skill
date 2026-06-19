# Services, background tasks, notifications, permissions, IPC

Source pages:
- background-task-overview, transient-task, continuous-task
- notification-overview, notification-with-wantagent
- common-event-overview, request-permissions
- ipc-rpc-overview, ipc-rpc-development-guideline

## Background task model

HarmonyOS treats background work explicitly — there's no general-purpose "service runs forever" pattern. Pick the lightest one that fits:

| Type | Lifetime | Common use |
|---|---|---|
| **Transient task** (短时任务) | ≤ ~2 minutes per request, ≤ 10 min/day | Finish a short job after the app goes background (uploading the last chunk, fast network call) |
| **Continuous task** (长时任务) | While needed, while user-visible | Music playback, navigation, audio recording, large file IO, location, etc. — must match a declared *type* and show a notification |
| **Deferred task** (延迟任务 / WorkScheduler) | OS-scheduled later, can run in low-power window | Periodic sync, opportunistic upload |
| **Agent reminder** (后台代理提醒) | Alarms, calendar reminders | Time-based reminders |

### Transient task

```typescript
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

backgroundTaskManager.requestSuspendDelay('uploadAvatar', () => {
  // called shortly before the OS forces us to stop
});
// when done:
backgroundTaskManager.cancelSuspendDelay(requestId);
```

Quota check: `backgroundTaskManager.getRemainingDelayTime(requestId).then(ms => ...)`.

### Continuous task

1. Declare permission `ohos.permission.KEEP_BACKGROUND_RUNNING` in `module.json5`.
2. Declare `backgroundModes` on the ability — must be a REAL mode string from the official type table (表1 长时任务类型): `["dataTransfer", "audioPlayback", "audioRecording", "location", "bluetoothInteraction", "multiDeviceConnection", "voip", "taskKeeping", "avPlaybackAndRecord" /* API 22+ */, "specialScenarioProcessing" /* API 22+ */]`. There is **no** `wifiInteraction` (or generic "monitoring") mode — see the note below. `taskKeeping` (compute, e.g. antivirus) is API 21+ and on non-PC devices (phones/tablets) requires the ACL permission `ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM` (system/restricted — not available to retail apps).
3. Call `startBackgroundRunning` on the UIAbility and pass a `WantAgent` to a foreground notification:

```typescript
import { backgroundTaskManager, wantAgent } from '@kit.AbilityKit';

const agentInfo: wantAgent.WantAgentInfo = {
  wants: [{ bundleName: 'com.example.myapp', abilityName: 'EntryAbility' }],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
};

const agent = await wantAgent.getWantAgent(agentInfo);

await backgroundTaskManager.startBackgroundRunning(this.context,
  backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, agent);
// later
await backgroundTaskManager.stopBackgroundRunning(this.context);
```

Stopping a continuous task while it's needed (e.g. paused music) gets you killed quickly — only stop when the user has finished.

> **No background mode for idle monitoring (e.g. Wi-Fi events).** The official type table is exactly the modes listed above — there is NO `wifiInteraction` / `networkInteraction` / generic "keep-alive" mode. A continuous task must correspond to active, user-visible work, and the system verifies the declared activity is actually happening (e.g. `DATA_TRANSFER` needs real data transfer) — it cancels a task that just idles. So you **cannot** keep a backgrounded process alive merely to listen for Wi-Fi / common events. Dynamic `commonEventManager` subscriptions only deliver while the app is **foreground** (HarmonyOS freezes backgrounded processes; on return to foreground it replays up to ~30 s of missed events). For event-driven background wake-ups there is `StaticSubscriberExtensionAbility`, but **system** common events (Wi-Fi state, etc.) are gated and generally not statically subscribable by retail third-party apps. `WorkScheduler` deferred tasks are the retail background option, but the minimum interval is **2 h** (4 h / 24 h / 48 h for less-active app groups) — too slow for near-real-time reactions. Conclusion: on a retail phone, always-on / near-real-time background event listening needs **system privileges** (system app, or a Xiaoyi device-side agent via HMAF / `AgentExtensionAbility`).

## Notifications

Send a basic text/picture/progress notification:

```typescript
import { notificationManager } from '@kit.NotificationKit';

const req: notificationManager.NotificationRequest = {
  id: 1,
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'Hello',
      text: 'Click me',
      additionalText: ''
    }
  },
  // attach a WantAgent so tapping opens our ability
  wantAgent: agent     // from wantAgent.getWantAgent(...)
};

await notificationManager.publish(req);
```

Other content types: `NOTIFICATION_CONTENT_LONG_TEXT`, `_PICTURE`, `_MULTILINE`, `_CONVERSATION`, plus live-view notifications via Live View Kit.

Slots (categories) control sound/priority — declare via `notificationManager.addSlot({ type, ... })`. Enable in module config via `ohos.permission.NOTIFICATION_CONTROLLER` for cross-app.

To **subscribe to / observe** notifications from a long-running extension (e.g. a companion-device or relay app), use the **notification subscriber extension** (`通知订阅扩展能力`) — see `pages/notification-subscriber-extension.md` and `pages/notification-subscriber-extension-ability-development-steps.md`.

## Common events (broadcast)

Local pub/sub within the device. Use sparingly — prefer direct calls or `eventHub` where possible.

```typescript
import { commonEventManager } from '@kit.BasicServicesKit';

const subscriber = await commonEventManager.createSubscriber({ events: ['my.app.action'] });
commonEventManager.subscribe(subscriber, (err, data) => {
  if (!err) console.log(data.event, data.parameters);
});

// publish
commonEventManager.publish('my.app.action', { code: 0, data: 'payload', parameters: { x: 1 } });
```

System-defined events: `usual.event.BOOT_COMPLETED`, `usual.event.SCREEN_ON`, `usual.event.BATTERY_LOW`, etc. Listening to system events usually needs a matching permission.

For cross-process bidirectional comm, see IPC/RPC below.

## Permissions

### Static declaration (`module.json5`)

```json5
"requestPermissions": [
  {
    "name": "ohos.permission.LOCATION",
    "reason": "$string:reason_location",
    "usedScene": { "abilities": ["EntryAbility"], "when": "inuse" }
  },
  {
    "name": "ohos.permission.CAMERA",
    "reason": "$string:reason_camera",
    "usedScene": { "abilities": ["EntryAbility"], "when": "inuse" }
  }
]
```

`when` is `inuse` (granted only while ability foreground) or `always` (continuous). Reason must be a localized string resource.

### Runtime grant

```typescript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

const need: Permissions[] = ['ohos.permission.LOCATION'];
const mgr = abilityAccessCtrl.createAtManager();
const result = await mgr.requestPermissionsFromUser(this.context, need);

const granted = result.authResults.every((code) => code === 0);
if (!granted) {
  // explain and direct to settings
}
```

Some permissions require **systemap** signature (system apps only). For user-permission grants, distinguish:
- `user_grant` — always need runtime prompt.
- `system_grant` — granted at install if declared (e.g. INTERNET — always granted but must be declared).

Check current state with `mgr.checkAccessTokenSync(tokenId, permName)` → `GRANTED` / `DENIED`.

## IPC / RPC

For in-device cross-process calls and remote-device calls via DistributedSched. Stage model exposes this through `RemoteAbility` and `SequenceablePayload` types.

```typescript
import { rpc } from '@kit.IPCKit';

class MyStub extends rpc.RemoteObject {
  constructor(descriptor: string) { super(descriptor); }
  onRemoteRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, options: rpc.MessageOption): boolean {
    if (code === 1) {
      const arg = data.readString();
      reply.writeString(`echo:${arg}`);
      return true;
    }
    return false;
  }
}
```

Expose via a `ServiceExtensionAbility` and `onConnect`/`onDisconnect`. Client side calls `bindServiceExtensionAbility(want, connection)` and on `onAbilityConnectDone(remote)` wraps `new rpc.MessageOption()` + `data.writeString(...)` + `remote.sendMessageRequest(code, data, reply, options)`.

For type-safe wrappers, define an interface with `@kit.IPCKit` `Sendable` / `Sequenceable` data classes.

## Audio focus, screen lock, sensors

These domains have dedicated kits — see `references/10-kits-catalog.md` (Audio Kit, Sensor Service Kit, Notification Kit, etc.).
