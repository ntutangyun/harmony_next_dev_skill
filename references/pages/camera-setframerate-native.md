# 动态调整预览帧率(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-setframerate-native_

动态调整帧率是直播、视频等场景下控制预览效果的重要能力之一。应用可通过此能力，显式地控制流输出帧率，以适应不同帧率下的业务目标。

某些场景下降低帧率可在相机设备启用时降低功耗。

约束与限制

支持的帧率范围及帧率的设置依赖于硬件能力的实现，不同的硬件平台可能拥有不同的默认帧率。

开发流程

相机使用预览功能前，均需要创建相机会话。完成会话配置后，应用提交和开启会话，才可以开始调用相机相关功能。

流程图如下所示：

与普通的预览流程相比，动态调整预览帧率的注意点如图上标识：

调用OH_CameraManager_CreateCaptureSession创建会话（Session）时，需要指定模式为NORMAL_PHOTO或NORMAL_VIDEO。

仅当Session处于NORMAL_PHOTO或NORMAL_VIDEO模式时，支持调整预览流帧率。调整帧率的创建会话方式见创建Session会话并指定模式。

动态调整帧率的操作，可在启动预览前后任意时刻调用。

动态调整帧率在预览里属于可选操作，可以完成：

查询当前支持调整的帧率范围

设置当前帧率

获取当前生效的帧率设置

如何配置会话（Session）、释放资源，请参考会话管理 > 预览。

导入模块

导入NDK接口，导入方法如下。

// 导入NDK接口头文件
#include "hilog/log.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_input.h"
#include "ohcamera/capture_session.h"
#include "ohcamera/photo_output.h"
#include "ohcamera/preview_output.h"
#include "ohcamera/video_output.h"
#include "ohcamera/camera_manager.h"

在CMake脚本中链接相关动态库。

target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)

创建Session会话并指定模式

相机使用预览等功能前，均需创建相机会话，调用OH_CameraManager_CreateCaptureSession创建一个会话。

创建会话时调用OH_CaptureSession_SetSessionMode指定Camera_SceneMode为NORMAL_PHOTO或NORMAL_VIDEO，创建出的Session处于拍照或录像模式。

以创建Session会话并指定为NORMAL_PHOTO模式为例：

Camera_ErrorCode CreateCaptureSession(Camera_Manager *cameraManager, Camera_CaptureSession *captureSession) {
   Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
    }
    // 设置会话模式为拍照或录像模式，此处以拍照模式为例
    ret = OH_CaptureSession_SetSessionMode(captureSession, Camera_SceneMode::NORMAL_PHOTO);
    return ret;
}

动态调整帧率

调用OH_PreviewOutput_GetSupportedFrameRates，查询当前previewOutput支持的帧率范围。

说明

需要在Session调用OH_CaptureSession_CommitConfig完成配流之后调用。

Camera_ErrorCode PreviewOutputGetSupportedFrameRates(Camera_PreviewOutput* previewOutput,
    Camera_FrameRateRange** frameRateRange, uint32_t* size) {
    Camera_ErrorCode ret = OH_PreviewOutput_GetSupportedFrameRates(previewOutput, frameRateRange, size);

    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetSupportedFrameRates failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    for (uint32_t i = 0; i < *size; i++) {
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates min %{public}d", (*frameRateRange)[i].min);
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates max %{public}d", (*frameRateRange)[i].max);
    }
    return ret;
}

根据实际开发需求，调用OH_PreviewOutput_SetFrameRate接口对帧率进行动态调整。

说明

调用时机：

需要在Session调用OH_CaptureSession_CommitConfig完成配流之后调用。

可在Session调用OH_CaptureSession_Start启动预览前后任意时刻调用。

OH_PreviewOutput_SetFrameRate调用限制：

在调用OH_PreviewOutput_SetFrameRate接口设置非固定帧率后，不支持再次调用该接口重新设置动态帧率。

在调用OH_PreviewOutput_SetFrameRate接口设置固定帧率后，支持重新设置固定帧率，但必须保证新设置的帧率可以整除之前设置的帧率或者被之前设置的帧率整除。

Camera_ErrorCode PreviewOutputSetFrameRate(Camera_PreviewOutput* previewOutput,
    uint32_t minFps, uint32_t maxFps){
    Camera_ErrorCode ret = OH_PreviewOutput_SetFrameRate(previewOutput, minFps, maxFps);
    if (ret != CAMERA_OK) {
        return CAMERA_INVALID_ARGUMENT;
    }
    return ret;
}

（可选）通过OH_PreviewOutput_GetActiveFrameRate接口查询已设置过并生效的帧率。

仅通过OH_PreviewOutput_SetFrameRate接口显式设置过帧率才可查询当前生效帧率信息。

Camera_ErrorCode PreviewOutputGetActiveFrameRate(Camera_PreviewOutput* previewOutput,
    Camera_FrameRateRange* frameRateRange){
    Camera_ErrorCode ret = OH_PreviewOutput_GetActiveFrameRate(previewOutput, frameRateRange);
    if (ret != CAMERA_OK) {
        return CAMERA_INVALID_ARGUMENT;
    }
    OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ min %{public}d", (*frameRateRange).min);
    OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ max %{public}d", (*frameRateRange).max);
    return ret;
}

## Code blocks

### Code block 1

```
// 导入NDK接口头文件
#include "hilog/log.h"
#include "ohcamera/camera.h"
#include "ohcamera/camera_input.h"
#include "ohcamera/capture_session.h"
#include "ohcamera/photo_output.h"
#include "ohcamera/preview_output.h"
#include "ohcamera/video_output.h"
#include "ohcamera/camera_manager.h"
```

### Code block 2

```
target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
```

### Code block 3

```
Camera_ErrorCode CreateCaptureSession(Camera_Manager *cameraManager, Camera_CaptureSession *captureSession) {
   Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
    if (captureSession == nullptr || ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
    }
    // 设置会话模式为拍照或录像模式，此处以拍照模式为例
    ret = OH_CaptureSession_SetSessionMode(captureSession, Camera_SceneMode::NORMAL_PHOTO);
    return ret;
}
```

### Code block 4

```
Camera_ErrorCode PreviewOutputGetSupportedFrameRates(Camera_PreviewOutput* previewOutput,
    Camera_FrameRateRange** frameRateRange, uint32_t* size) {
    Camera_ErrorCode ret = OH_PreviewOutput_GetSupportedFrameRates(previewOutput, frameRateRange, size);

    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetSupportedFrameRates failed.");
        return CAMERA_INVALID_ARGUMENT;
    }
    for (uint32_t i = 0; i < *size; i++) {
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates min %{public}d", (*frameRateRange)[i].min);
        OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates max %{public}d", (*frameRateRange)[i].max);
    }
    return ret;
}
```

### Code block 5

```
Camera_ErrorCode PreviewOutputSetFrameRate(Camera_PreviewOutput* previewOutput,
    uint32_t minFps, uint32_t maxFps){
    Camera_ErrorCode ret = OH_PreviewOutput_SetFrameRate(previewOutput, minFps, maxFps);
    if (ret != CAMERA_OK) {
        return CAMERA_INVALID_ARGUMENT;
    }
    return ret;
}
```

### Code block 6

```
Camera_ErrorCode PreviewOutputGetActiveFrameRate(Camera_PreviewOutput* previewOutput,
    Camera_FrameRateRange* frameRateRange){
    Camera_ErrorCode ret = OH_PreviewOutput_GetActiveFrameRate(previewOutput, frameRateRange);
    if (ret != CAMERA_OK) {
        return CAMERA_INVALID_ARGUMENT;
    }
    OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ min %{public}d", (*frameRateRange).min);
    OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ max %{public}d", (*frameRateRange).max);
    return ret;
}
```
