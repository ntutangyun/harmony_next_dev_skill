# 实现游戏伴随

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-development_

从API版本26.0.0开始，新增游戏伴随服务。游戏伴随服务为游戏陪玩类的应用提供游戏应用状态感知、游戏应用截图等基础能力。

游戏应用状态感知：实时感知游戏的进程创建、切换前台、后台或者终止等状态变化并通知应用。

游戏应用截图：实时捕获游戏画面并以文件描述符方式传递给应用，用于实现游戏画面分享等功能。

约束与限制

从API版本26.0.0开始，仅支持Phone设备。

截图频率当前为1s截一张图。

业务流程

用户启动游戏陪玩类应用。

用户启动游戏。

游戏进程创建。

游戏陪伴类应用调用onGameApplicationStatus接口注册游戏应用状态监听，监听游戏前后台状态变化。

游戏陪伴类应用调用onGameSnapshot接口注册游戏应用截图监听，用于接收游戏画面截图。

游戏状态发生变化时（切换到前台、后台或终止时）。

游戏伴随服务通过onGameApplicationStatus回调通知已注册的游戏陪伴类应用。

游戏伴随服务通过onGameSnapshot回调向游戏陪伴类应用发送游戏截图数据（文件描述符方式）。

用户退出所有游戏，游戏伴随服务通过onGameApplicationStatus回调通知游戏陪伴类应用BUDDY_TERMINATED状态，表示游戏伴随服务已终止。

接口说明

具体API说明请详见游戏伴随服务接口文档。

接口名	描述
onGameApplicationStatus(callback: Callback<GameApplicationStatusInfo>): void	注册游戏应用状态变化的事件监听。
offGameApplicationStatus(callback?: Callback<GameApplicationStatusInfo>): void	取消游戏应用状态变化的事件监听。
onGameSnapshot(callback: Callback<number>): void	注册游戏应用截图的事件监听。
offGameSnapshot(callback?: Callback<number>): void	取消游戏应用截图的事件监听。

开发步骤

 import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
 import { hilog } from '@kit.PerformanceAnalysisKit';
 import { image } from '@kit.ImageKit';
 import { BusinessError } from '@kit.BasicServicesKit';

private statusCallback: (statusInfo: gameBuddyService.GameApplicationStatusInfo) => void = (statusInfo) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ` + statusInfo.status);
};
private snapshotCallback: (fd: number) => void = (fd) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};

try {
  gameBuddyService.onGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

try {
  gameBuddyService.onGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

try {
  gameBuddyService.offGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

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
private statusCallback: (statusInfo: gameBuddyService.GameApplicationStatusInfo) => void = (statusInfo) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ` + statusInfo.status);
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
  gameBuddyService.onGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 5

```
try {
  gameBuddyService.offGameApplicationStatus(this.statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService',
    `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

### Code block 6

```
try {
  gameBuddyService.offGameSnapshot(this.snapshotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
