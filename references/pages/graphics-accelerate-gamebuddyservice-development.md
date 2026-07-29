# 实现游戏伴随

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-development_

从API版本26.0.0开始，新增游戏伴随服务。游戏伴随服务为游戏陪玩类的应用提供伴随悬浮窗、游戏状态感知、音频采集与传输、游戏截图、消息通知等基础能力。

伴随悬浮窗：在游戏运行时展示可自定义的悬浮窗，呈现应用标识和状态信息

游戏状态感知：实时感知游戏的进程创建、切换前台/后台、终止等状态变化并通知应用

音频采集与传输：采集游戏音频数据并传输给应用，实现游戏声音的伴随播放

游戏截图：实时捕获游戏画面并以文件描述符方式传递给应用，用于实现游戏画面分享等功能

消息通知：提供双向消息通道，应用可向游戏伴随服务发送状态消息

约束与限制

从API版本26.0.0开始，支持Phone设备。

截图频率当前为1s截一张图。

业务流程

用户启动游戏，游戏进程创建后，系统检测到游戏启动。

系统自动拉起游戏伴随服务，并初始化悬浮窗模块。

客户端应用（如游戏陪伴类应用）调用onGameApplicationStatus接口注册游戏状态监听，监听游戏前后台状态变化。

客户端应用（如游戏陪伴类应用）调用onQueryMessage接口注册查询消息监听，用于接收音频信息等数据。

客户端应用（如游戏陪伴类应用）调用onGameSnapshot接口注册截图监听，用于接收游戏画面截图。

客户端应用（如游戏陪伴类应用）调用setFloatWindowAvatar接口设置悬浮窗的头像和描述。

客户端应用（如游戏陪伴类应用）调用sendAppStateMessage接口向游戏伴随服务发送状态消息。

游戏状态发生变化时（切换到前台或后台），游戏伴随服务通过onGameApplicationStatus回调通知已注册的客户端应用。

游戏伴随服务通过onQueryMessage回调向客户端应用发送音频信息。

游戏伴随服务通过onGameSnapshot回调向客户端应用发送游戏截图数据（文件描述符方式）。

用户退出游戏，游戏进程终止，系统自动销毁游戏伴随服务。

游戏伴随服务通过onGameApplicationStatus回调通知客户端应用BUDDY_TERMINATED状态，表示游戏伴随服务已终止。

接口说明

具体API说明请详见游戏伴随服务接口文档。

接口名	描述
setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise<void>	设置悬浮窗的头像和头像描述。
sendAppStateMessage(message: AppStateMessage): Promise<void>	客户端应用发送状态消息给游戏伴随服务。
onGameApplicationStatus(callback: Callback<GameApplicationStatus>): void	注册游戏应用状态变化的事件监听。
offGameApplicationStatus(callback?: Callback<GameApplicationStatus>): void	取消游戏应用状态变化的事件监听。
onQueryMessage(callback: Callback<QueryMessage>): void	注册用户查询消息的事件监听。
offQueryMessage(callback?: Callback<QueryMessage>): void	取消用户查询消息的事件监听。
onGameSnapshot(callback: Callback<number>): void	注册游戏应用截图的事件监听。
offGameSnapshot(callback?: Callback<number>): void	取消游戏应用截图的事件监听。

开发步骤

导入模块。

 import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
 import { hilog } from '@kit.PerformanceAnalysisKit';
 import { image } from '@kit.ImageKit';
 import { BusinessError } from '@kit.BasicServicesKit';

注册回调函数

private statusCallback: (status: gameBuddyService.GameApplicationStatus) => void = (status) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ` + status);
};
private messageCallback: (message: gameBuddyService.QueryMessage) => void = (message) => {
  hilog.info(0x0000, 'gameBuddyService', `Query message received:`, JSON.stringify(message));
};
private snapshotCallback: (fd: number) => void = (fd) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};

调用onGameApplicationStatus接口，注册游戏状态监听。

try {
  gameBuddyService.onGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

调用onQueryMessage接口，注册用户查询消息监听。

try {
  gameBuddyService.onQueryMessage(this.messageCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

调用onGameSnapshot接口，注册游戏截图监听。

try {
  gameBuddyService.onGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

调用setFloatWindowAvatar接口，设置游戏伴随服务悬浮窗的头像和描述。

let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: { height: 100, width: 100 }
};
let pixelMap = image.createPixelMapSync(opts);
gameBuddyService.setFloatWindowAvatar(pixelMap, 'avatar description').then(() => {
  hilog.info(0x0000, 'gameBuddyService', `Set avatar success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService',
    `Set avatar failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});

调用sendAppStateMessage接口，向游戏伴随服务发送应用状态消息。

const appStateMessage: gameBuddyService.AppStateMessage = {
  type: gameBuddyService.MessageType.INFORMATION,
  message: message
};
gameBuddyService.sendAppStateMessage(appStateMessage).then(() => {
  hilog.info(0x0000, 'gameBuddyService', `send appState message success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService',
    `send appState message failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});

调用offGameApplicationStatus接口，取消游戏状态监听。

try {
  gameBuddyService.offGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

调用offQueryMessage接口，取消用户查询消息监听。

try {
  gameBuddyService.offQueryMessage(this.messageCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

调用offGameSnapshot接口，取消游戏截图监听。

try {
  gameBuddyService.offGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

## Code blocks

### Code block 1

```
 import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
 import { hilog } from '@kit.PerformanceAnalysisKit';
 import { image } from '@kit.ImageKit';
 import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
private statusCallback: (status: gameBuddyService.GameApplicationStatus) => void = (status) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ` + status);
};
private messageCallback: (message: gameBuddyService.QueryMessage) => void = (message) => {
  hilog.info(0x0000, 'gameBuddyService', `Query message received:`, JSON.stringify(message));
};
private snapshotCallback: (fd: number) => void = (fd) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};
```

### Code block 3

```
try {
  gameBuddyService.onGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 4

```
try {
  gameBuddyService.onQueryMessage(this.messageCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 5

```
try {
  gameBuddyService.onGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 6

```
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: { height: 100, width: 100 }
};
let pixelMap = image.createPixelMapSync(opts);
gameBuddyService.setFloatWindowAvatar(pixelMap, 'avatar description').then(() => {
  hilog.info(0x0000, 'gameBuddyService', `Set avatar success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService',
    `Set avatar failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});
```

### Code block 7

```
const appStateMessage: gameBuddyService.AppStateMessage = {
  type: gameBuddyService.MessageType.INFORMATION,
  message: message
};
gameBuddyService.sendAppStateMessage(appStateMessage).then(() => {
  hilog.info(0x0000, 'gameBuddyService', `send appState message success`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'gameBuddyService',
    `send appState message failed, errorCode: ${err.code}, errorMessage: ${err.message}`);
});
```

### Code block 8

```
try {
  gameBuddyService.offGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 9

```
try {
  gameBuddyService.offQueryMessage(this.messageCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 10

```
try {
  gameBuddyService.offGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
