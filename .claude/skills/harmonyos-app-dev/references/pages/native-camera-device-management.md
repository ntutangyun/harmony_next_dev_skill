# 相机管理 (C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-device-management_

Camera_ErrorCode CreateCameraManager(Camera_Manager** cameraManager)
{
    // 创建CameraManager对象。
    Camera_ErrorCode ret = OH_Camera_GetCameraManager(cameraManager);
    if (*cameraManager == nullptr || ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
    }
    return ret;
}
说明

如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。

通过OH_CameraManager_GetSupportedCameras()方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，无法进行后续操作。

Camera_ErrorCode GetSupportedCameras(Camera_Manager* cameraManager, Camera_Device** cameras, uint32_t &size)
{
    // 获取相机列表。
    Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameras(cameraManager, cameras, &size);
    if (cameras == nullptr || size == 0 || ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
    }
    // 在不使用cameras时，需要调用delete[]释放。
    for (uint32_t index = 0; index < size; index++) {
       OH_LOG_INFO(LOG_APP, "cameraId  =  %{public}s ", (*cameras)[index].cameraId);              // 获取相机ID。
       OH_LOG_INFO(LOG_APP, "cameraPosition  =  %{public}d ", (*cameras)[index].cameraPosition);  // 获取相机位置。
       OH_LOG_INFO(LOG_APP, "cameraType  =  %{public}d ", (*cameras)[index].cameraType);          // 获取相机类型。
       OH_LOG_INFO(LOG_APP, "connectionType  =  %{public}d ", (*cameras)[index].connectionType);  // 获取相机连接类型。
    }
    return ret;
}
状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过OH_CameraManager_RegisterCallback()注册cameraStatus事件，通过回调返回监听结果，callback返回Camera_StatusInfo参数，参数的具体内容可参考相机管理器回调接口实例Camera_StatusInfo。

void CameraStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
{
   OH_LOG_INFO(LOG_APP, "CameraStatusCallback is called");
}
CameraManager_Callbacks* GetCameraManagerListener()
{
   static CameraManager_Callbacks cameraManagerListener = {
      .onCameraStatus = CameraStatusCallback
   };
   return &cameraManagerListener;
}
Camera_ErrorCode RegisterCameraStatusCallback(Camera_Manager &cameraManager)
{
    Camera_ErrorCode ret = OH_CameraManager_RegisterCallback(&cameraManager, GetCameraManagerListener());
    if (ret != CAMERA_OK) {
       OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
    }
    return ret;
}
开发相机应用必选能力(C/C++)
设备输入(C/C++)
