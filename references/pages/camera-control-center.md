# 相机控制器(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-control-center_

function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
  let isSupported: boolean = videoSession.isControlCenterSupported();
  return isSupported;
}

通过getSupportedEffectTypes接口，查询当前设备及当前场景下，相机控制器支持的效果类型。

function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
  let effectTypes: Array<camera.ControlCenterEffectType> = [];
  effectTypes = videoSession.getSupportedEffectTypes();
  return effectTypes;
}

若设备及场景支持相机控制器，使用enableControlCenter接口可启用或关闭控制器。

function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
  let isSupported: boolean = videoSession.isControlCenterSupported();
  if (isSupported) {
    videoSession.enableControlCenter(enable);
  }
}

使能相机控制器后，可以在状态栏看到新增的视频效果图标。

点击视频效果图标，在弹出的二级页面中，用户可调节控制器支持的效果，如图所示为美颜和背景虚化。

状态监听

使用相机控制器的过程中，应用可以监听控制器效果的使能状态。

通过注册controlCenterEffectStatusChange的回调函数获取控制器中各效果的使能状态。

当控制器中某效果使能状态发生变化时，callback返回ControlCenterStatusInfo参数。

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';


function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(`Callback Error, errorCode: ${err.code}`);
    return;
  }
  console.info(`controlCenterEffectStatusChange: ${status}`);
}


function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.on('controlCenterEffectStatusChange', callback);
}
压力管控(ArkTS)
微距能力设置(ArkTS)
