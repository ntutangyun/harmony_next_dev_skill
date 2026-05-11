# 预览(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview_

XComponent组件为预览流提供的SurfaceId，而XComponent的能力由UI提供，相关介绍可参考XComponent组件参考。

根据传入的SurfaceId，通过OH_CameraManager_GetSupportedCameraOutputCapability()方法获取当前设备支持的预览能力。通过OH_CameraManager_CreatePreviewOutput()方法创建预览输出流，其中，OH_CameraManager_CreatePreviewOutput()方法中的参数分别是cameraManager指针，previewProfiles数组中的第一项，步骤三中获取的surfaceId，以及返回的previewOutput指针。

Camera_ErrorCode NDKCamera::CreatePreviewOutput(void)
{
    if (previewProfile_ == nullptr) {
        OH_LOG_ERROR(LOG_APP, "Get previewProfiles failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    ret_ = OH_CameraManager_CreatePreviewOutput(cameraManager_, previewProfile_, previewSurfaceId_, &previewOutput_);
    OH_LOG_ERROR(LOG_APP, "create preview width: %{public}d, height: %{public}d, format: %{public}d",
        previewProfile_->size.width, previewProfile_->size.height, previewProfile_->format);
    if (previewSurfaceId_ == nullptr || previewOutput_ == nullptr || ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "CreatePreviewOutput failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    return ret_;
    PreviewOutputRegisterCallback();
}
camera_manager.cpp

使能。当session完成CommitConfig后通过调用OH_CaptureSession_Start()方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见Camera_ErrorCode。

Camera_ErrorCode NDKCamera::SessionStart(void)
{
    Camera_ErrorCode ret = OH_CaptureSession_Start(captureSession_);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Start success.");
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed. %d ", ret);
    }
    return ret;
}
camera_manager.cpp

通过OH_CaptureSession_Stop()方法停止预览流，接口调用失败会返回相应错误码，错误码类型参见Camera_ErrorCode。

Camera_ErrorCode NDKCamera::SessionStop(void)
{
    Camera_ErrorCode ret = OH_CaptureSession_Stop(captureSession_);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success.");
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
    }
    return ret;
}
camera_manager.cpp
状态监听

在相机应用开发过程中，可以随时监听预览输出流状态，包括预览流启动、预览流结束、预览流输出错误。

通过注册固定的frameStart回调函数获取监听预览启动结果，previewOutput创建成功时即可监听，预览第一次曝光时触发，有该事件返回结果则认为预览流已启动。

void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput)
{
    OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
}
camera_manager.cpp

通过注册固定的frameEnd回调函数获取监听预览结束结果，previewOutput创建成功时即可监听，预览完成最后一帧时触发，有该事件返回结果则认为预览流已结束。

void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount)
{
    OH_LOG_INFO(LOG_APP, "PreviewOutput frameCount = %{public}d", frameCount);
}
camera_manager.cpp

通过注册固定的error回调函数获取监听预览输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见Camera_ErrorCode。

void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode)
{
    OH_LOG_INFO(LOG_APP, "PreviewOutput errorCode = %{public}d", errorCode);
}
camera_manager.cpp
PreviewOutput_Callbacks *NDKCamera::GetPreviewOutputListener(void)
{
    static PreviewOutput_Callbacks previewOutputListener = {
        .onFrameStart = PreviewOutputOnFrameStart,
        .onFrameEnd = PreviewOutputOnFrameEnd,
        .onError = PreviewOutputOnError
    };
    return &previewOutputListener;
}


Camera_ErrorCode NDKCamera::PreviewOutputRegisterCallback(void)
{
    ret_ = OH_PreviewOutput_RegisterCallback(previewOutput_, GetPreviewOutputListener());
    if (ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
    }
    return ret_;
}
camera_manager.cpp
开发相机应用基础能力(C/C++)
预览流二次处理(C/C++)
