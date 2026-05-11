# 游戏上划退出后，场景切换阶段存在振动，应该如何避免

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-2_

通过globalThis定义全局作用域的变量isCacheStatus，在onCreate生命周期函数中赋值false，isLaunchMirrorEnabled接口返回true时赋值true。

在函数startVibration前增加isCacheStatus校验，若当前处于缓存态，则不进行振动操作。

以团结工程为例，修改如下：

// TuanjiePlayerAbilityBase.ets
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
onCreate(): void {
  globalThis.isCacheStatus = false;
  // ......
}
onWindowStageWillDestroy(): void {
  if (launchAcceleration.isLaunchMirrorEnabled()) {
    globalThis.isCacheStatus = true;
    // ......
  }
}


// TuanjieVibrate.ets
static vibrate(vibrateMs: number) {
  if (globalThis.isCacheStatus) {
    console.info('globalThis.isCacheStatus true, vibration returned.');
    return;
  }
  // ......
}
通过加载内存镜像启动的游戏会全屏显示来电提醒，应该如何避免
快速启动的游戏存在三方SDK功能异常，应该如何排查
