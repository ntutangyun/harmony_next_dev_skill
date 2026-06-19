# 小游戏登录（必选）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-login_

小游戏接入基础游戏服务的小游戏登录API后，支持玩家使用华为账号快速进入游戏，且小游戏的华为账号实名认证、未成年人防沉迷功能由基础游戏服务实现。

前提条件

已完成开发准备。

业务流程

玩家启动小游戏。

小游戏调用init接口初始化Game Service Kit。初始化后，弹出华为隐私协议窗口，玩家确认同意后，可继续往下执行。

小游戏调用on接口注册小游戏防沉迷事件监听。

小游戏调用miniGameLogin接口。小游戏顶部弹出欢迎横幅，并向小游戏返回playerId、playerSign等信息。同时对玩家是否完成实名认证及是否成年进行校验。

若玩家未完成实名认证，miniGameLogin接口自动弹出实名认证窗口要求玩家进行实名认证。

若玩家账号实名认证为未成年人，miniGameLogin接口将自动检测未成年人的游戏时间。若玩家不在指定时间内登录小游戏，将强制玩家退出小游戏并返回1002000006错误码。

接口说明

具体API说明详见接口文档。

接口名	描述
init(context: common.UIAbilityContext, callback: AsyncCallback<void>): void	游戏初始化接口，使用默认的上下文信息，通过callback回调获取返回值。
on(type: 'miniGameAddictionPrevented', callback: Callback<string>): void	小游戏防沉迷事件监听接口，通过callback回调获取小游戏防沉迷事件结果。
off(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void	取消小游戏防沉迷事件监听接口。
miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>	小游戏登录接口，通过Promise对象获取返回值。

开发步骤

[h2]导入模块

导入Game Service Kit及公共模块。

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

[h2]初始化

调用init接口初始化Game Service Kit。

onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent('pages/index', (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  });
}

[h2]监听小游戏防沉迷事件

调用on接口注册小游戏防沉迷事件监听。

private miniGameAddictionPreventedCallback(result: string) {
  // 退出小游戏
}
// ...
// 调用on接口注册小游戏防沉迷事件监听
try {
  gamePlayer.on('miniGameAddictionPrevented', this.miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
}

[h2]小游戏登录

调用miniGameLogin接口登录小游戏。

let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.MiniGameLoginParam = {
  'gameAppId': '123xxx', // 小游戏appId
  'extraData': 'xxx' // 附加信息，要求JSON String格式
};
try {
  gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
    hilog.info(0x0000, 'testTag', `Succeeded in logging in`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
}

[h2]取消监听小游戏防沉迷事件

游戏退出时通过调用off接口取消监听状态。

// 取消miniGameAddictionPrevented事件的全部监听
try {
  gamePlayer.off('miniGameAddictionPrevented');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
```

### Code block 2

```
onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent('pages/index', (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  });
}
```

### Code block 3

```
private miniGameAddictionPreventedCallback(result: string) {
  // 退出小游戏
}
// ...
// 调用on接口注册小游戏防沉迷事件监听
try {
  gamePlayer.on('miniGameAddictionPrevented', this.miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
}
```

### Code block 4

```
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.MiniGameLoginParam = {
  'gameAppId': '123xxx', // 小游戏appId
  'extraData': 'xxx' // 附加信息，要求JSON String格式
};
try {
  gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
    hilog.info(0x0000, 'testTag', `Succeeded in logging in`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
}
```

### Code block 5

```
// 取消miniGameAddictionPrevented事件的全部监听
try {
  gamePlayer.off('miniGameAddictionPrevented');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
}
```
