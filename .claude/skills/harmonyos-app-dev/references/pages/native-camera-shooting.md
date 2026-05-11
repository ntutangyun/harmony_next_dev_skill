# 拍照(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting_

--");
    } else {
        OH_LOG_ERROR(LOG_APP, "hasFlash fail-----");
    }


    // 查询闪光灯模式是否支持。
    bool isSupported = false;
    ret = OH_CaptureSession_IsFlashModeSupported(captureSession_, flashMode, &isSupported);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
    }
    if (isSupported) {
        OH_LOG_INFO(LOG_APP, "isFlashModeSupported success-----");
    } else {
        OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail-----");
    }


    // 设置闪光灯模式。
    ret = OH_CaptureSession_SetFlashMode(captureSession_, flashMode);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. %{public}d ", ret);
    }


    // 获取当前设备的闪光灯模式。
    ret = OH_CaptureSession_GetFlashMode(captureSession_, &flashMode);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode：%{public}d ", flashMode);
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. %d ", ret);
    }
    return ret;
}


// 对焦模式。
Camera_ErrorCode NDKCamera::IsFocusModeSupported(uint32_t mode)
{
    Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
    ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
    if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    return ret_;
}


Camera_ErrorCode NDKCamera::IsFocusMode(uint32_t mode)
{
    OH_LOG_INFO(LOG_APP, "IsFocusMode start.");
    Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
    ret_ = OH_CaptureSession_IsFocusModeSupported(captureSession_, focusMode, &isFocusModeSupported_);
    if (&isFocusModeSupported_ == nullptr || ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    ret_ = OH_CaptureSession_SetFocusMode(captureSession_, focusMode);
    if (ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "SetFocusMode failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    ret_ = OH_CaptureSession_GetFocusMode(captureSession_, &focusMode);
    if (&focusMode == nullptr || ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "GetFocusMode failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    OH_LOG_INFO(LOG_APP, "IsFocusMode end.");
    return ret_;
}


Camera_ErrorCode NDKCamera::setZoomRatioFn(uint32_t zoomRatio)
{
    float zoom = float(zoomRatio);
    // 获取支持的缩放范围。
    float minZoom;
    float maxZoom;
    Camera_ErrorCode ret = OH_CaptureSession_GetZoomRatioRange(captureSession_, &minZoom, &maxZoom);
    if (captureSession_ == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
    } else {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
            minZoom, maxZoom);
    }


    // 设置缩放比例。
    ret = OH_CaptureSession_SetZoomRatio(captureSession_, zoom);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. %{public}d ", ret);
    }


    // 获取当前设备的缩放比例。
    ret = OH_CaptureSession_GetZoomRatio(captureSession_, &zoom);
    if (ret == CAMERA_OK) {
        OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom：%{public}f ", zoom);
    } else {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. %{public}d ", ret);
    }
    return ret;
}
camera_manager.cpp

触发拍照。

通过OH_PhotoOutput_Capture_WithCaptureSetting()方法，执行拍照任务。

Camera_ErrorCode NDKCamera::TakePicture(int32_t degree)
{
    Camera_ErrorCode ret = CAMERA_OK;
    Camera_ImageRotation imageRotation;
    bool isMirSupported;
    OH_PhotoOutput_IsMirrorSupported(photoOutput_, &isMirSupported);
    OH_PhotoOutput_GetPhotoRotation(photoOutput_, degree, &imageRotation);


    Camera_PhotoCaptureSetting curPhotoSetting = {
        quality : QUALITY_LEVEL_HIGH,
        rotation : imageRotation,
        mirror : isMirSupported
    };
    ret = OH_PhotoOutput_Capture_WithCaptureSetting(photoOutput_, curPhotoSetting);
    OH_LOG_INFO(LOG_APP, "TakePicture get quality %{public}d, rotation %{public}d, mirror %{public}d",
        curPhotoSetting.quality, curPhotoSetting.rotation, curPhotoSetting.mirror);
    OH_LOG_INFO(LOG_APP, "TakePicture ret = %{public}d.", ret);
    return ret;
}
camera_manager.cpp
高性能拍照

从API version 21开始支持高性能拍照功能，即在进行单段式拍照时设置明确的画质优先策略。

单段式拍照的体验主要由出图速度和最终图片质量衡量。因此，为满足开发者在不同场景下的差异化需求，对这两项指标的侧重也不同。例如，街头抓拍要求快速捕捉瞬间，而风景或人像拍摄则更追求极致的画质。

注意

仅单段式拍照支持设置画质优先策略。若在分段式拍照中设置画质优先策略，该设置将无效。

画质优先策略

在使用单段式拍照时，支持设置速度优先和画质优先两种画质优先策略类型，并且分别对应着不同的Camera_PhotoQualityPrioritization枚举类型。

CAMERA_PHOTO_QUALITY_PRIORITIZATION_SPEED对应着速度优先，表示降低画质来提升拍照的速度。如果开发者在进行单段式拍照时没有设置明确的画质优先策略，单段式拍照就默认为速度优先状态。
CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY对应着画质优先，表示通过较长的耗时来得到画质更高的图片。
如何正确设置画质优先策略

为了正确的在单段式拍照中设置画质优先策略，高性能拍照功能提供了如下两个接口：

OH_PhotoOutput_IsPhotoQualityPrioritizationSupported：查询当前设备是否支持指定的画质优先策略。返回true表示支持，返回false表示不支持。在进行设置画质优先策略之前，必须先查询将要设置的画质优先策略在当前设备上是否可用。
OH_PhotoOutput_SetPhotoQualityPrioritization：画质优先策略设置接口，通过该接口设置对应的画质优先策略，实现高性能拍照。
开发步骤

高性能拍照相关接口需要在会话管理(C/C++)流程的使能步骤中进行调用。

具体调用时机如下：

在会话管理(C/C++)流程中的使能步骤中的OH_CaptureSession_CommitConfig()结束之后进行调用。

Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
  Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
{
  // 向会话中添加相机输入流。
  Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
    return ret;
  }


  // 向会话中添加预览输出流。
  ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
    return ret;
  }


  // 向会话中添加拍照输出流。
  ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
    return ret;
  }


  // 提交会话配置。
  ret = OH_CaptureSession_CommitConfig(captureSession);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
    return ret;
  }


  // 启动会话。
  ret = OH_CaptureSession_Start(captureSession);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
  }


  SetHighQualityPhotoQualityPrioritization(photoOutput);
  return ret;
}


void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
{
  Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
  bool isSupported = false;
  Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
  if (isSupported) {
    ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
    if (ret != 0) {
      OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
    }
  } else {
    OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
  }
}

在会话管理(C/C++)流程中的使能步骤中的OH_CaptureSession_CommitConfig()之前调用。

Camera_ErrorCode StartSession(Camera_CaptureSession* captureSession, Camera_Input* cameraInput,
  Camera_PreviewOutput* previewOutput, Camera_PhotoOutput* photoOutput)
{
  // 向会话中添加相机输入流。
  Camera_ErrorCode ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
    return ret;
  }


  // 向会话中添加预览输出流。
  ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
    return ret;
  }


  // 向会话中添加拍照输出流。
  ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
    return ret;
  }


  SetHighQualityPhotoQualityPrioritization(photoOutput);
  
  // 提交会话配置。
  ret = OH_CaptureSession_CommitConfig(captureSession);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
    return ret;
  }


  // 启动会话。
  ret = OH_CaptureSession_Start(captureSession);
  if (ret != CAMERA_OK) {
    OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
  }


  return ret;
}


void SetHighQualityPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput)
{
  Camera_PhotoQualityPrioritization quality = Camera_PhotoQualityPrioritization::CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY;
  bool isSupported = false;
  Camera_ErrorCode ret = OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(photoOutput, quality, isSupported);
  if (isSupported) {
    ret = OH_PhotoOutput_SetPhotoQualityPrioritization(photoOutput, quality);
    if (ret != 0) {
      OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_SetPhotoQualityPrioritization failed.");
    }
  } else {
    OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_IsPhotoQualityPrioritizationSupported not supported.");
  }
}
状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

通过注册固定的onFrameStart回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，拍照第一次曝光时触发。

// PhotoOutput Callback
void PhotoOutputOnFrameStart(Camera_PhotoOutput *photoOutput)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameStart");
}


void PhotoOutputOnFrameShutter(Camera_PhotoOutput *photoOutput, Camera_FrameShutterInfo *info)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutputOnFrameShutter");
}
camera_manager.cpp

通过注册固定的onFrameEnd回调函数获取监听拍照结束结果，photoOutput创建成功时即可监听。

void PhotoOutputOnFrameEnd(Camera_PhotoOutput *photoOutput, int32_t frameCount)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutput frameCount = %{public}d", frameCount);
}
camera_manager.cpp

通过注册固定的onError回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见Camera_ErrorCode。

void PhotoOutputOnError(Camera_PhotoOutput *photoOutput, Camera_ErrorCode errorCode)
{
    OH_LOG_INFO(LOG_APP, "PhotoOutput errorCode = %{public}d", errorCode);
}
camera_manager.cpp
PhotoOutput_Callbacks *NDKCamera::GetPhotoOutputListener(void)
{
    static PhotoOutput_Callbacks photoOutputListener = {
        .onFrameStart = PhotoOutputOnFrameStart,
        .onFrameShutter = PhotoOutputOnFrameShutter,
        .onFrameEnd = PhotoOutputOnFrameEnd,
        .onError = PhotoOutputOnError
    };
    return &photoOutputListener;
}


Camera_ErrorCode NDKCamera::PhotoOutputRegisterCallback(void)
{
    ret_ = OH_PhotoOutput_RegisterCallback(photoOutput_, GetPhotoOutputListener());
    if (ret_ != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_RegisterCallback failed.");
    }
    return ret_;
}
camera_manager.cpp
预览流二次处理(C/C++)
拍照实践(C/C++)
