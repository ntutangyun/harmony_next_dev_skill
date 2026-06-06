# 对焦(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-focus_

function isFocusModeSupported(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    // 以检查是否支持自动对焦模式为例。
    status = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFocusModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}

调用setFocusMode设置对焦模式。

若设置为自动对焦模式，支持调用setFocusPoint设置对焦点，根据对焦点执行一次自动对焦。

说明

需要在Session调用commitConfig完成配流之后调用。

function setFocusMode(photoSession: camera.PhotoSession): void {
  const focusPoint: camera.Point = {x: 1, y: 1};
  try {
    // 设置自动对焦模式。
    photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_AUTO);
    // 设置对焦点。
    photoSession.setFocusPoint(focusPoint);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusMode and setFocusPoint call failed. error code: ${err.code}`);
  }
}
状态监听

在相机应用开发过程中，可以随时监听相机聚焦的状态变化。

通过注册focusStateChange的回调函数获取监听结果，仅当自动对焦模式时，且相机对焦状态发生改变时触发该事件。

function onFocusStateChange(photoSession: camera.PhotoSession): void {
  photoSession.on('focusStateChange', (err: BusinessError, focusState: camera.FocusState) => {
    if (err !== undefined && err.code !== 0) {
      console.error(`focusStateChange error code: ${err.code}`);
      return;
    }
    console.info(`focusStateChange focusState: ${focusState}`);
    // 为保证对焦功能的用户体验，在自动对焦成功后，可将对焦模式设置为连续自动对焦，且相机对焦状态发生改变时触发该事件。
    if (focusState === camera.FocusState.FOCUS_STATE_FOCUSED) {
      photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
    }
  });
}
YUV拍照(ArkTS)
相机旋转
