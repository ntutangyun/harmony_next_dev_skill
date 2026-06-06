# 手电筒使用(C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-torch-use_

Camera_ErrorCode ret = OH_CameraManager_IsTorchSupported(cameraManager, &isTorchSupported);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_IsTorchSupported failed.");
    }
    if (isTorchSupported) {
        OH_LOG_INFO(LOG_APP, "isTorchSupported success.");
    } else {
        OH_LOG_ERROR(LOG_APP, "isTorchSupported failed.");
    }
    return isTorchSupported;
}

通过OH_CameraManager_IsTorchSupportedByTorchMode()方法，检测当前设备是否支持指定的手电筒模式。

bool IsTorchSupportedByTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode)
{
    bool torchModeSupported = false;
    Camera_ErrorCode ret = OH_CameraManager_IsTorchSupportedByTorchMode(cameraManager, torchMode, &torchModeSupported);
    if (ret != CAMERA_OK) {
         OH_LOG_ERROR(LOG_APP, "OH_CameraManager_IsTorchSupported failed.");
    }
    if (torchModeSupported) {
         OH_LOG_INFO(LOG_APP, "isTorchModeSupported success.");
    } else {
         OH_LOG_ERROR(LOG_APP, "isTorchModeSupported failed. %{public}d ", ret);
    }
    return torchModeSupported;
}

通过OH_CameraManager_SetTorchMode()方法，设置当前设备的手电筒模式。

Camera_ErrorCode SetTorchMode(Camera_Manager* cameraManager, Camera_TorchMode torchMode)
{
    // 在torchMode支持的情况下进行设置手电筒模式。
    Camera_ErrorCode ret = OH_CameraManager_SetTorchMode(cameraManager, torchMode);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_SetTorchMode failed. %{public}d ", ret);
    } else {
        OH_LOG_INFO(LOG_APP, "OH_CameraManager_SetTorchMode success.");
    }
    return ret;
}
状态监听

在相机应用开发过程中，可以随时监听手电筒状态，包括手电筒打开、手电筒关闭、手电筒不可用、手电筒恢复可用。手电筒状态发生变化，可通过回调函数获取状态的变化。

注册torchStatus事件，回调会返回监听结果，callback返回Camera_TorchStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例Camera_TorchStatusInfo。

void TorchStatusCallback(Camera_Manager *cameraManager, Camera_TorchStatusInfo* torchStatus)
{
   OH_LOG_INFO(LOG_APP, "TorchStatusCallback is called.");
}
Camera_ErrorCode RegisterTorchStatusCallback(Camera_Manager *cameraManager)
{
    Camera_ErrorCode ret = OH_CameraManager_RegisterTorchStatusCallback(cameraManager, TorchStatusCallback);
    if (ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterTorchStatusCallback failed.");
    }
    return ret;
}
元数据(C/C++)
压力管控(C/C++)
