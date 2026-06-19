# 推荐使用OHAudio开发音频录制功能(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohaudio-for-recording_

OHAudio是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输入功能的场景。

当音频流处于工作状态（非released状态）时，会占用系统的音频流资源。由于系统对音频流数量有限制，所以当客户端暂时不使用音频流时，调用OH_AudioCapturer_Release()回收音频资源，做好资源利用，避免后续创建音频流失败。

OHAudio音频录制状态变化示意图：

使用入门

开发者要使用OHAudio提供的录制能力，需要添加对应的头文件。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取完整示例。

[h2]在 CMake 脚本中链接动态库

target_link_libraries(sample PUBLIC libohaudio.so)

[h2]添加头文件

开发者通过引入<native_audiostreambuilder.h>和<native_audiocapturer.h>头文件，使用音频录制相关API。

#include <ohaudio/native_audiocapturer.h>
#include <ohaudio/native_audiostreambuilder.h>

开发步骤

详细的API说明请参考OHAudio。

[h2]音频流构造器

OHAudio提供OH_AudioStreamBuilder接口，遵循构造器设计模式，用于构建音频流。开发者需要根据业务场景，指定对应的OH_AudioStream_Type。

OH_AudioStream_Type包含两种类型：

AUDIOSTREAM_TYPE_RENDERER

AUDIOSTREAM_TYPE_CAPTURER

使用OH_AudioStreamBuilder_Create创建构造器示例：

OH_AudioStreamBuilder* builder;
OH_AudioStreamBuilder_Create(&builder, streamType);

在音频业务结束之后，开发者应该执行OH_AudioStreamBuilder_Destroy接口来销毁构造器。

OH_AudioStreamBuilder_Destroy(builder);

开发者可以通过以下几个步骤来实现一个简单的录制功能。

[h2]实现音频录制

创建构造器。

OH_AudioStreamBuilder* builder;
OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_CAPTURER);

配置音频流参数。

创建音频录制构造器后，可以设置音频流所需要的参数，可以参考下面的案例。

// 设置音频采样率。
const int SAMPLING_RATE_48K = 48000;
OH_AudioStreamBuilder_SetSamplingRate(builder, SAMPLING_RATE_48K);
// 设置音频声道。
const int channelCount = 2;
OH_AudioStreamBuilder_SetChannelCount(builder, channelCount);
// 设置音频采样格式。
OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
// 设置音频流的编码类型。
OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW);
// 设置输入音频流的工作场景。
OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_MIC);

注意，音频录制的音频数据需要通过回调接口读入，开发者要实现回调接口，从API version 12开始支持使用OH_AudioStreamBuilder_SetCapturerReadDataCallback设置回调函数。回调函数的声明请查看OH_AudioCapturer_OnReadDataCallback。

设置音频回调函数。

多音频并发处理可参考文档处理音频焦点事件，仅接口语言差异。

void MyOnReadData_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    void* audioData,
    int32_t audioDataSize)
{
    // 从buffer中取出length长度的录音数据。
}

void MyOnInterruptEvent_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
}

void MyOnError_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioStream_Result error)
{
    // 根据error表示的音频异常信息，做出相应的处理。
}
// ...
    // 配置音频中断事件回调函数。
    OH_AudioCapturer_OnInterruptCallback OnInterruptCb = MyOnInterruptEvent_NewAPI;
    OH_AudioStreamBuilder_SetCapturerInterruptCallback(builder, OnInterruptCb, nullptr);

    // 配置音频异常回调函数。
    OH_AudioCapturer_OnErrorCallback OnErrorCb = MyOnError_NewAPI;
    OH_AudioStreamBuilder_SetCapturerErrorCallback(builder, OnErrorCb, nullptr);

    // 配置音频输入流的回调。
    OH_AudioCapturer_OnReadDataCallback OnReadDataCb = MyOnReadData_NewAPI;
    OH_AudioStreamBuilder_SetCapturerReadDataCallback(builder, OnReadDataCb, nullptr);

构造录制音频流。

OH_AudioCapturer* audioCapturer;
OH_AudioStreamBuilder_GenerateCapturer(builder, &audioCapturer);

使用音频流。

录制音频流中包含以下接口，用来实现对音频流的控制。

接口	说明
OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer)	开始录制。
OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer)	暂停录制。
OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer)	停止录制。
OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer)	释放缓存数据。
OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer)	释放录制实例。

注意

音频流控制接口执行会有耗时（例如OH_AudioCapturer_Stop接口单次执行普遍超过50ms），应避免在主线程中直接调用，以免造成界面显示卡顿。

释放构造器。

构造器不再使用时，需要释放相关资源。

OH_AudioStreamBuilder_Destroy(builder);

[h2]设置低时延模式

当设备支持低时延通路时，开发者可以使用低时延模式创建音频录制构造器，获得更低时延的音频体验。

开发流程与普通录制（实现音频录制）场景一致，仅需要在步骤1创建音频录制构造器时，调用OH_AudioStreamBuilder_SetLatencyMode()设置低时延模式。

注意

当音频录制场景OH_AudioStream_SourceType为AUDIOSTREAM_SOURCE_TYPE_VOICE_COMMUNICATION时，不支持主动设置低时延模式，系统会根据设备的能力，决策输入的音频通路。

部分场景（如通话来电）下系统能力受限会回落至普通音频通路模式，缓冲区大小也会发生变化，此时应同普通音频通路模式一样根据缓冲区大小将缓冲区中数据一次性全部取走，否则录制的数据会出现不连续，导致杂音。

OH_AudioStream_LatencyMode latencyMode = AUDIOSTREAM_LATENCY_MODE_FAST;
OH_AudioStreamBuilder_SetLatencyMode(builder, latencyMode);

[h2]设置静音打断模式

静音打断模式提供将打断策略从停止录音切换为静音录制的功能，可以实现录音全程不被系统基于焦点并发规则打断的效果，并且录音过程中也不影响其他应用启动录音。开发者在创建音频录制构造器时，调用OH_AudioStreamBuilder_SetCapturerWillMuteWhenInterrupted接口设置是否开启静音打断模式。默认不开启，此时由音频焦点策略管理并发音频流的执行顺序。开启后，被其他应用打断导致停止或暂停录制时会进入静音录制状态，在此状态下录制的音频没有声音。

[h2]回声消除功能

回声消除功能可在支持的设备上有效消除录音过程中的回声干扰，提升音频采集质量。开发者可通过指定特定的音频输入源类型OH_AudioStream_SourceType（AUDIOSTREAM_SOURCE_TYPE_VOICE_COMMUNICATION、AUDIOSTREAM_SOURCE_TYPE_LIVE）来启用该功能，系统将会自动对采集的音频信号进行回声消除处理。

在启用前，建议先调用OH_AudioStreamManager_IsAcousticEchoCancelerSupported接口（从API version 20开始支持）查询当前设备对音频输入源类型OH_AudioStream_SourceType是否支持回声消除功能，以确保功能的可用性。若支持，则可在创建音频录制构造器时通过OH_AudioStreamBuilder_SetCapturerInfo 设置相应的音频输入源类型，从而激活回声消除处理流程。

注意事项

从API version 12开始不再推荐使用OH_AudioCapturer_Callbacks的方式设置音频回调函数。若必须使用，需要注意在设置音频回调函数时，通过下面两种方式中的任意一种来设置音频回调函数，避免不可预期的行为。

方式1：请确保OH_AudioCapturer_Callbacks的每一个回调都被自定义的回调方法或空指针初始化。

int32_t MyOnReadData_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    void* buffer,
    int32_t length)
{
    // 从buffer中取出length长度的录音数据。
    return 0;
}
int32_t MyOnInterruptEvent_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
    return 0;
}
// ...
    // 配置回调函数，如果需要监听，则赋值。
    callbacks.OH_AudioCapturer_OnReadData = MyOnReadData_Legacy;
    callbacks.OH_AudioCapturer_OnInterruptEvent = MyOnInterruptEvent_Legacy;

    // （必选）如果不需要监听，使用空指针初始化。
    callbacks.OH_AudioCapturer_OnStreamEvent = nullptr;
    callbacks.OH_AudioCapturer_OnError = nullptr;

方式2：使用前，初始化并清零结构体。

int32_t MyOnReadData_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    void* buffer,
    int32_t length)
{
    // 从buffer中取出length长度的录音数据。
    return 0;
}
int32_t MyOnInterruptEvent_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
    return 0;
}
// ...
    // 使用前，初始化并清零结构体。
    OH_AudioCapturer_Callbacks callbacks = {0};
    // 配置需要的回调函数。
    callbacks.OH_AudioCapturer_OnReadData = MyOnReadData_Legacy;
    callbacks.OH_AudioCapturer_OnInterruptEvent = MyOnInterruptEvent_Legacy;

示例代码

音频低时延录制与播放

## Code blocks

### Code block 1

```
target_link_libraries(sample PUBLIC libohaudio.so)
```

### Code block 2

```
#include <ohaudio/native_audiocapturer.h>
#include <ohaudio/native_audiostreambuilder.h>
```

### Code block 3

```
OH_AudioStreamBuilder* builder;
OH_AudioStreamBuilder_Create(&builder, streamType);
```

### Code block 4

```
OH_AudioStreamBuilder_Destroy(builder);
```

### Code block 5

```
OH_AudioStreamBuilder* builder;
OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_CAPTURER);
```

### Code block 6

```
// 设置音频采样率。
const int SAMPLING_RATE_48K = 48000;
OH_AudioStreamBuilder_SetSamplingRate(builder, SAMPLING_RATE_48K);
// 设置音频声道。
const int channelCount = 2;
OH_AudioStreamBuilder_SetChannelCount(builder, channelCount);
// 设置音频采样格式。
OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
// 设置音频流的编码类型。
OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW);
// 设置输入音频流的工作场景。
OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_MIC);
```

### Code block 7

```
void MyOnReadData_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    void* audioData,
    int32_t audioDataSize)
{
    // 从buffer中取出length长度的录音数据。
}

void MyOnInterruptEvent_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
}

void MyOnError_NewAPI(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioStream_Result error)
{
    // 根据error表示的音频异常信息，做出相应的处理。
}
// ...
    // 配置音频中断事件回调函数。
    OH_AudioCapturer_OnInterruptCallback OnInterruptCb = MyOnInterruptEvent_NewAPI;
    OH_AudioStreamBuilder_SetCapturerInterruptCallback(builder, OnInterruptCb, nullptr);

    // 配置音频异常回调函数。
    OH_AudioCapturer_OnErrorCallback OnErrorCb = MyOnError_NewAPI;
    OH_AudioStreamBuilder_SetCapturerErrorCallback(builder, OnErrorCb, nullptr);

    // 配置音频输入流的回调。
    OH_AudioCapturer_OnReadDataCallback OnReadDataCb = MyOnReadData_NewAPI;
    OH_AudioStreamBuilder_SetCapturerReadDataCallback(builder, OnReadDataCb, nullptr);
```

### Code block 8

```
OH_AudioCapturer* audioCapturer;
OH_AudioStreamBuilder_GenerateCapturer(builder, &audioCapturer);
```

### Code block 9

```
OH_AudioStreamBuilder_Destroy(builder);
```

### Code block 10

```
OH_AudioStream_LatencyMode latencyMode = AUDIOSTREAM_LATENCY_MODE_FAST;
OH_AudioStreamBuilder_SetLatencyMode(builder, latencyMode);
```

### Code block 11

```
int32_t MyOnReadData_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    void* buffer,
    int32_t length)
{
    // 从buffer中取出length长度的录音数据。
    return 0;
}
int32_t MyOnInterruptEvent_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
    return 0;
}
// ...
    // 配置回调函数，如果需要监听，则赋值。
    callbacks.OH_AudioCapturer_OnReadData = MyOnReadData_Legacy;
    callbacks.OH_AudioCapturer_OnInterruptEvent = MyOnInterruptEvent_Legacy;

    // （必选）如果不需要监听，使用空指针初始化。
    callbacks.OH_AudioCapturer_OnStreamEvent = nullptr;
    callbacks.OH_AudioCapturer_OnError = nullptr;
```

### Code block 12

```
int32_t MyOnReadData_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    void* buffer,
    int32_t length)
{
    // 从buffer中取出length长度的录音数据。
    return 0;
}
int32_t MyOnInterruptEvent_Legacy(
    OH_AudioCapturer* capturer,
    void* userData,
    OH_AudioInterrupt_ForceType type,
    OH_AudioInterrupt_Hint hint)
{
    // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
    return 0;
}
// ...
    // 使用前，初始化并清零结构体。
    OH_AudioCapturer_Callbacks callbacks = {0};
    // 配置需要的回调函数。
    callbacks.OH_AudioCapturer_OnReadData = MyOnReadData_Legacy;
    callbacks.OH_AudioCapturer_OnInterruptEvent = MyOnInterruptEvent_Legacy;
```
