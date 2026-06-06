# 手电筒使用(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-torch-use_

function isTorchSupported(cameraManager: camera.CameraManager) : boolean {
  let torchSupport: boolean = false;
  try {
    torchSupport = cameraManager.isTorchSupported();
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to torch. errorCode = ' + err.code);
  }
  console.info('Returned with the torch support status:' + torchSupport);
  return torchSupport;
}

通过CameraManager中的isTorchModeSupported方法，检测是否支持指定的手电筒模式TorchMode。

function isTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : boolean {
  let isTorchModeSupport: boolean = false;
  try {
    isTorchModeSupport = cameraManager.isTorchModeSupported(torchMode);
  } catch (error) {
    let err = error as BusinessError;
    console.error('Failed to set the torch mode. errorCode = ' + err.code);
  }
  return isTorchModeSupport;
}

通过CameraManager中的setTorchMode方法，设置当前设备的手电筒模式。以及通过CameraManager中的getTorchMode方法，获取当前设备的手电筒模式。

说明

在使用getTorchMode方法前，需要先注册监听手电筒的状态变化，请参考状态监听。

function setTorchModeSupported(cameraManager: camera.CameraManager, torchMode: camera.TorchMode) : void {
  cameraManager.setTorchMode(torchMode);
  let isTorchMode = cameraManager.getTorchMode();
  console.info(`Returned with the torch mode supported mode: ${isTorchMode}`);
}
状态监听

在相机应用开发过程中，可以随时监听手电筒状态，包括手电筒打开、手电筒关闭、手电筒不可用、手电筒恢复可用。手电筒状态发生变化，可通过回调函数获取状态的变化。

注册torchStatusChange事件后，回调会返回监听结果，callback返回TorchStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例TorchStatusInfo。

function onTorchStatusChange(cameraManager: camera.CameraManager): void {
  cameraManager.on('torchStatusChange', (err: BusinessError, torchStatusInfo: camera.TorchStatusInfo) => {
    if (err !== undefined && err.code !== 0) {
      console.error(`Callback Error, errorCode: ${err.code}`);
      return;
    }
    console.info(`onTorchStatusChange, isTorchAvailable: ${torchStatusInfo.isTorchAvailable}, isTorchActive: ${torchStatusInfo.
      isTorchActive}, level: ${torchStatusInfo.torchLevel}`);
  });
}
元数据(ArkTS)
适配不同折叠状态的摄像头变更(ArkTS)
