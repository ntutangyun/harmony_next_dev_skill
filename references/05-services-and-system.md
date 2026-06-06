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
2. Declare `backgroundModes` on the ability: e.g. `["audioPlayback", "audioRecording", "location", "bluetoothInteraction", "multiDeviceConnection", "wifiInteraction", "voip", "taskKeeping" /* device-dependent */]`.
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
