# 实现游戏预启动加速

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-development_

业务流程

游戏启动加速服务根据用户的使用习惯，在系统资源充足时提前加载游戏。

UIAbility的onCreate生命周期回调中会通过want.parameters携带启动参数，若参数ohos.params.gamePrelaunch为true，则表示当前UIAbility是由游戏预启动运行的，开发者需记录该启动原因，为后续通知系统游戏启动完成做判断。

随即游戏进入UIAbility的onForeground生命周期，此时游戏引擎开始运行，游戏启动完成状态以及启动过程中的业务检测通常由引擎侧负责处理。因此，游戏可根据不同运行状态，主动通知游戏启动加速服务当前预启动流程的执行结果：当预启动正常完成时，触发完成通知；当检测到需要中断的情况（如资源更新等）时，触发终止通知。

终止预启动

开发者需调用terminateGamePrelaunch接口通知游戏启动加速服务退出当前的游戏预启动，游戏加速服务接收到消息后会同步通知程序框架服务。

系统程序框架接收到退出游戏预启动通知后，当前游戏的UIAbility将会进入onDestroy生命周期。

预启动完成

游戏会继续运行，引擎会开始自渲染并运行到登录页或大厅界面，若当次为游戏预启动，开发者需调用completeGamePrelaunch接口，通知游戏启动加速服务当前游戏已启动完成。

系统程序框架接收到游戏预启动完成通知后，当前游戏的UIAbility将会进入onBackground生命周期。

用户启动游戏。

游戏的UIAbility直接进入onForeground，将展示游戏预启动完成时的界面。

接口说明

具体API说明请详见接口文档。

接口名	描述
completeGamePrelaunch(context: common.UIAbilityContext): Promise<void>	通知系统当前游戏预启动已完成。
terminateGamePrelaunch(context: common.UIAbilityContext): Promise<void>	通知系统退出当前游戏预启动流程。

开发步骤

获取UIAbility启动原因。

开发者可在UIAbility的onCreate生命周期回调中通过want.parameters获取启动原因，当参数ohos.params.gamePrelaunch为true时，表示当前UIAbility是由游戏预启动运行的。

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

let isPrelaunchStart: boolean = false;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 判断是否是预启动运行，want中ohos.params.gamePrelaunch可能为undefined，赋值时需设置默认值false
    isPrelaunchStart = (want.parameters?.["ohos.params.gamePrelaunch"] as boolean) ?? false;
    console.info(`EntryAbility onCreate, isPrelaunchStart:${isPrelaunchStart}`);
    // ...
  }
}

通知启动加速服务当前游戏预启动完成。

async completeGamePrelaunch() {
  if (!isPrelaunchStart) {
    // 若当次非预启动运行，游戏启动完成后不进行任何处理
    return;
  }
  if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
    try {
      // 通知启动加速服务，当次预启动已完成
      await launchAcceleration.completeGamePrelaunch(this.context);
      console.info('completeGamePrelaunch success');
    } catch (err) {
      console.error(`completeGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}

通知启动加速服务取消当次游戏预启动。

async terminateGamePrelaunch() {
  if (!isPrelaunchStart) {
    // 若当次非预启动运行，游戏启动完成后不进行任何处理
    return;
  }
  if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
    try {
      // 通知启动加速服务，终止当前预启动
      await launchAcceleration.terminateGamePrelaunch(this.context);
      console.info('terminateGamePrelaunch success');
    } catch (err) {
      console.error(`terminateGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}

## Code blocks

### Code block 1

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

let isPrelaunchStart: boolean = false;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 判断是否是预启动运行，want中ohos.params.gamePrelaunch可能为undefined，赋值时需设置默认值false
    isPrelaunchStart = (want.parameters?.["ohos.params.gamePrelaunch"] as boolean) ?? false;
    console.info(`EntryAbility onCreate, isPrelaunchStart:${isPrelaunchStart}`);
    // ...
  }
}
```

### Code block 2

```
async completeGamePrelaunch() {
  if (!isPrelaunchStart) {
    // 若当次非预启动运行，游戏启动完成后不进行任何处理
    return;
  }
  if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
    try {
      // 通知启动加速服务，当次预启动已完成
      await launchAcceleration.completeGamePrelaunch(this.context);
      console.info('completeGamePrelaunch success');
    } catch (err) {
      console.error(`completeGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

### Code block 3

```
async terminateGamePrelaunch() {
  if (!isPrelaunchStart) {
    // 若当次非预启动运行，游戏启动完成后不进行任何处理
    return;
  }
  if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
    try {
      // 通知启动加速服务，终止当前预启动
      await launchAcceleration.terminateGamePrelaunch(this.context);
      console.info('terminateGamePrelaunch success');
    } catch (err) {
      console.error(`terminateGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
