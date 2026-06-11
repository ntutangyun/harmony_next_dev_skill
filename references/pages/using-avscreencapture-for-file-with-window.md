# 使用AVScreenCapture实现窗口级录屏(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avscreencapture-for-file-with-window_

从API version 10开始，开发者可通过AVScreenCapture模块的C API接口实现窗口/屏幕录制，采集麦克风和设备的音视频源数据。

本开发指导以指定窗口录制为例，介绍如何使用AVScreenCapture的C API实现精准窗口捕获。该方案聚焦特定窗口内容，避免全屏干扰，适用于教学演示、在线课程、会议记录及特定内容采集等场景。

方式一：录制某个指定窗口，需要设置指定窗口ID。该场景下，启动录屏后，会弹出共享内容选择对话框。详细的API声明请参考OH_CaptureMode中的OH_CAPTURE_SPECIFIED_WINDOW模式。

方式二（推荐）：使用系统Picker列表弹窗，选择期望录制的窗口。使用OH_AVScreenCapture_StrategyForPickerPopUp设置是否弹出屏幕捕获Picker。从API version 20开始，支持在PC/2in1设备上设置弹出屏幕捕获Picker；从API version 23开始，支持在Phone/Tablet设备上设置弹出屏幕捕获Picker。

申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

如果配置了采集麦克风音频数据，需向用户申请授权配置麦克风权限ohos.permission.MICROPHONE和申请长时任务(ArkTS)。

从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限ohos.permission.TIMEOUT_SCREENOFF_DISABLE_LOCK，实现在屏幕熄灭但不锁屏的场景下，继续保持录制的效果。配置方式请参见声明权限。

从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限ohos.permission.CUSTOM_SCREEN_RECORDING，实现在录制屏幕时不再弹出隐私警告弹窗。配置方式请参见受限开放权限。

开发步骤及注意事项

在CMake脚本中链接动态库

target_link_libraries(entry PUBLIC libnative_avscreen_capture.so)

添加头文件。

#include "napi/native_api.h"
#include <multimedia/player_framework/native_avscreen_capture.h>
#include <multimedia/player_framework/native_avscreen_capture_base.h>
#include <multimedia/player_framework/native_avbuffer.h>
#include <multimedia/player_framework/native_avscreen_capture_errors.h>
#include "hilog/log.h"
#include <unistd.h>
#include <fcntl.h>
#include <string>

调用OH_AVScreenCapture_Create方法创建AVScreenCapture实例capture。

g_avCapture = OH_AVScreenCapture_Create();

调用OH_AVScreenCapture_Init方法配置屏幕录制参数。

创建AVScreenCapture实例capture后，可以设置屏幕录制所需要的参数。

void SetConfig(OH_AVScreenCaptureConfig &config)
{
    OH_AudioCaptureInfo micCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH_MIC
    };

    OH_AudioCaptureInfo innerCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH_ALL_PLAYBACK
    };

    OH_AudioEncInfo audioEncInfo = {
        .audioBitrate = 48000,
        .audioCodecformat = OH_AAC_LC
    };

    OH_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 720,
        .videoFrameHeight = 1280,
        .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
    };

    OH_VideoEncInfo videoEncInfo = {
        .videoCodec = OH_H264,
        .videoBitrate = 2000000,
        .videoFrameRate = 30
    };

    OH_AudioInfo audioInfo = {
        .micCapInfo = micCapInfo,
        .innerCapInfo = innerCapInfo,
        .audioEncInfo = audioEncInfo
    };

    OH_VideoInfo videoInfo = {
        .videoCapInfo = videoCapInfo,
        .videoEncInfo = videoEncInfo
    };

    config = {
        .captureMode = OH_CAPTURE_HOME_SCREEN,
        .dataType = OH_ORIGINAL_STREAM, // 录屏数据类型，原始码流或文件
        .audioInfo = audioInfo,
        .videoInfo = videoInfo
    };
}

方式一：需传入期望录制的窗口ID进行录屏。

// 如果期望录制单个窗口，需传入单个窗口ID；如果期望同时录制多个窗口，需传入期望录制的窗口ID列表。
std::vector<int32_t> missionIds = {88}; // 指定录制的窗口ID。
config.videoInfo.videoCapInfo.missionIDs = missionIds.data();
config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(missionIds.size());
config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW; // 设置录屏模式为录制指定窗口。

// 设置为false，代表录屏启动后不弹出系统Picker，弹出隐私提示弹窗。
OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();
OH_AVScreenCapture_StrategyForPickerPopUp(strategy, false);
OH_AVScreenCapture_SetCaptureStrategy(capture, strategy);

方式二（推荐）：通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。

// 通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。
OH_AVScreenCapture_CaptureStrategy *strategy = OH_AVScreenCapture_CreateCaptureStrategy();
OH_AVScreenCapture_StrategyForPickerPopUp(strategy, true);
OH_AVScreenCapture_SetCaptureStrategy(g_avCapture, strategy);

调用OH_AVScreenCapture_StartScreenRecording方法开始进行窗口级录制。

result = OH_AVScreenCapture_StartScreenRecording(g_avCapture);

调用OH_AVScreenCapture_StopScreenRecording方法停止录制。

result = OH_AVScreenCapture_StopScreenRecording(g_avCapture);

调用OH_AVScreenCapture_Release方法销毁实例，释放资源。

OH_AVScreenCapture_Release(g_avCapture);
g_avCapture = nullptr;

## Code blocks

### Code block 1

```
target_link_libraries(entry PUBLIC libnative_avscreen_capture.so)
```

### Code block 2

```
#include "napi/native_api.h"
#include <multimedia/player_framework/native_avscreen_capture.h>
#include <multimedia/player_framework/native_avscreen_capture_base.h>
#include <multimedia/player_framework/native_avbuffer.h>
#include <multimedia/player_framework/native_avscreen_capture_errors.h>
#include "hilog/log.h"
#include <unistd.h>
#include <fcntl.h>
#include <string>
```

### Code block 3

```
g_avCapture = OH_AVScreenCapture_Create();
```

### Code block 4

```
void SetConfig(OH_AVScreenCaptureConfig &config)
{
    OH_AudioCaptureInfo micCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH_MIC
    };

    OH_AudioCaptureInfo innerCapInfo = {
        .audioSampleRate = 48000,
        .audioChannels = 2,
        .audioSource = OH_ALL_PLAYBACK
    };

    OH_AudioEncInfo audioEncInfo = {
        .audioBitrate = 48000,
        .audioCodecformat = OH_AAC_LC
    };

    OH_VideoCaptureInfo videoCapInfo = {
        .videoFrameWidth = 720,
        .videoFrameHeight = 1280,
        .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
    };

    OH_VideoEncInfo videoEncInfo = {
        .videoCodec = OH_H264,
        .videoBitrate = 2000000,
        .videoFrameRate = 30
    };

    OH_AudioInfo audioInfo = {
        .micCapInfo = micCapInfo,
        .innerCapInfo = innerCapInfo,
        .audioEncInfo = audioEncInfo
    };

    OH_VideoInfo videoInfo = {
        .videoCapInfo = videoCapInfo,
        .videoEncInfo = videoEncInfo
    };

    config = {
        .captureMode = OH_CAPTURE_HOME_SCREEN,
        .dataType = OH_ORIGINAL_STREAM, // 录屏数据类型，原始码流或文件
        .audioInfo = audioInfo,
        .videoInfo = videoInfo
    };
}
```

### Code block 5

```
// 如果期望录制单个窗口，需传入单个窗口ID；如果期望同时录制多个窗口，需传入期望录制的窗口ID列表。
std::vector<int32_t> missionIds = {88}; // 指定录制的窗口ID。
config.videoInfo.videoCapInfo.missionIDs = missionIds.data();
config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(missionIds.size());
config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW; // 设置录屏模式为录制指定窗口。

// 设置为false，代表录屏启动后不弹出系统Picker，弹出隐私提示弹窗。
OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();
OH_AVScreenCapture_StrategyForPickerPopUp(strategy, false);
OH_AVScreenCapture_SetCaptureStrategy(capture, strategy);
```

### Code block 6

```
// 通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。
OH_AVScreenCapture_CaptureStrategy *strategy = OH_AVScreenCapture_CreateCaptureStrategy();
OH_AVScreenCapture_StrategyForPickerPopUp(strategy, true);
OH_AVScreenCapture_SetCaptureStrategy(g_avCapture, strategy);
```

### Code block 7

```
result = OH_AVScreenCapture_StartScreenRecording(g_avCapture);
```

### Code block 8

```
result = OH_AVScreenCapture_StopScreenRecording(g_avCapture);
```

### Code block 9

```
OH_AVScreenCapture_Release(g_avCapture);
g_avCapture = nullptr;
```
