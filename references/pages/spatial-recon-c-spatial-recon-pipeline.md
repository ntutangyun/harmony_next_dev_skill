# 重建三维场景（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-c-spatial-recon-pipeline_

概要

从6.1.0(23)开始，Spatial Recon Kit支持通过视觉输入对三维场景进行重建。使用本Kit进行重建，分为以下几个步骤。

开发者输入一系列图像和对应的信息（相机内参、位姿）。

使用已经输入的数据进行重建。

如有需要，可以将重建结果保存。

其中，数据帧可以重复输入。

输入数据帧

Spatial Recon Kit要求开发者输入一系列图像和对应的信息（相机内参、位姿）。本Kit支持以下两种输入形式：

使用AR Engine的数据结构。

依据HMS_SpatialRecon_DataFrame结构体的定义组装数据。

为了保证重建效果和鲁棒性，不论使用何种格式，当前仅支持输入宽度（width）为1080像素且高度（height）为1440像素的图像进行重建。如果输入其余尺寸的图像，结果是未定义的。

[h2]输入AR Engine的数据结构进行重建

直接使用AR Engine的数据帧时，需要确保推入数据帧之前，先更新一次AR引擎的计算结果。

// 包含AREngine头文件
#include "ar/ar_engine_core.h"

#ifndef CHECK
#define CHECK(condition)                                                                                               \
    do {                                                                                                               \
        auto ret = (condition);                                                                                        \
        if (ret) {                                                                                                     \
            LOGE("*** CHECK FAILED at %{public}s:%{public}d: %{public}s ",                                             \
                 __FILE__, __LINE__, #condition);                                                                      \
            abort();                                                                                                   \
        }                                                                                                              \
    } while (false);
#endif

// 需要首先配置好AR引擎

// 创建一个新的AREngine_ARSession会话
AREngine_ARSession *arSession = nullptr;

AREngine_ARFrame *arFrame = nullptr;

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession));
// 配置AREngine_ARSession
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(arSession, &arConfig));
// 设置预览画面尺寸
// 推荐使用 width = 1080, height = 1440图像
CHECK(HMS_AREngine_ARConfig_SetPreviewSize(arSession, arConfig, 1080, 1440));
// 设置画面更新模式。
CHECK(HMS_AREngine_ARConfig_SetUpdateMode(arSession, arConfig, ARENGINE_UPDATE_MODE_LATEST));
CHECK(HMS_AREngine_ARConfig_SetFocusMode(arSession, arConfig, ARENGINE_FOCUS_MODE_AUTO));
CHECK(HMS_AREngine_ARSession_Configure(arSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
// 创建一个新的AREngine_ARFrame对象
CHECK(HMS_AREngine_ARFrame_Create(arSession, &arFrame));

// 更新AR引擎计算结果
AREngine_ARStatus arRet = HMS_AREngine_ARSession_Update(arSession, arFrame);

// 推入数据帧
HMS_SpatialReconStatus ret = HMS_SpatialRecon_PushARFrame(spatialReconSession,
   arSession, arFrame);

[h2]根据Spatial Recon Kit 定义的数据结构进行重建

开发者也可以手动依据HMS_SpatialRecon_DataFrame结构体的定义进行自定义配置。

HMS_SpatialRecon_DataFrame inputFrame;

inputFrame.focalX = usrFocalX;
inputFrame.focalY = usrFocalY;
inputFrame.principalX = usrPrincipalX;
inputFrame.principalY = usrPrincipalY;
inputFrame.imageWidth = usrWidth;
inputFrame.imageHeight = usrHeight;

// ... 组装其他字段

// 仅支持RGB格式输入
inputFrame.format = SPATIAL_RECON_IMAGEDATA_FORMAT_RGB;
inputFrame.imageData = rgbData;

HMS_SpatialReconStatus ret= HMS_SpatialRecon_PushFrame(reconSession, &inputFrame);

调用HMS_SpatialRecon_PushFrame和HMS_SpatialRecon_PushARFrame时，需要保证输入数据是有效的。否则会返回SPATIAL_RECON_STATUS_FAILED。

调用HMS_SpatialRecon_PushFrame或HMS_SpatialRecon_PushARFrame时，系统会自动选取关键帧进行保存，用于后续重建。

使用Spatial Recon Kit能力进行重建

在获取了必要的输入以后，开发者可以调用HMS_SpatialRecon_StartSession函数进行重建。

开发者需要根据当前应用是否处于前台运行，在每一次调用HMS_SpatialRecon_StartSession函数之后，使用HMS_SpatialRecon_SetRunningMode设定对应的运行模式，让操作系统可以更好地分配计算资源。

此标志位如未正确设置，可能导致性能或者功耗劣化。

由于重建过程中对系统资源消耗较大，Spatial Recon Kit仅支持同一时刻只有一个session正在进行重建。如果同一时刻有多个session同时进行重建，会导致未定义行为。

auto noCaptureFinishedCB = [](HMS_SpatialReconStatus status) {
   // 在这里放callBack需要执行的任务，打印信息/调用其他回调
   return;
};

HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_StartSession(spatialReconSession,
   &info, noCaptureFinishedCB) // 如果writeInfo不为空，则重建完成会自动保存

// 更新RunningMode。如果应用当前处于前台，则设定为前台模式。否则设定为后台模式。
HMS_SpatialRecon_SetRunningMode(SPATIAL_RECON_RUNNING_FOREGROUND_MODE);

// 可以按需获取当前进度
float progress = 0.0f;
HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, NULL);

暂停与继续

Spatial Recon Kit支持重建过程中任意时刻要求暂停或继续。由于空间重建会消耗大量的系统资源，建议开发者在应用中提供开关，让用户能控制何时暂停、何时继续。

由于空间重建计算量较大，强烈建议开发者通过HMS的公共事件接口，订阅热公共事件COMMON_EVENT_THERMAL_LEVEL_CHANGED。当检测到设备温度过高时，自动暂停重建并提示用户，防止过热导致卡顿，影响用户体验。

Spatial Recon Kit提供了相关的接口，在调用HMS_SpatialRecon_StartSession启动重建以后，可以通过调用HMS_SpatialRecon_PauseSession接口暂停重建，通过调用HMS_SpatialRecon_ResumeSession接口继续重建。

// 暂停
HMS_SpatialRecon_PauseSession(spatialReconSession);

// 继续
HMS_SpatialRecon_ResumeSession(spatialReconSession);

保存重建结果

调用HMS_SpatialRecon_StartSession函数时，如果传入的writeInfo非空，重建结束以后会根据writeInfo配置的信息自动保存结果。如果传入的writeInfo为空，可以在重建结束以后手动保存结果。

HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置，开发者可以根据需要保存为PLY（点云）或运镜视频文件（MP4）。
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_SaveResultToFile(spatialReconSession,
&info, NULL); // 保存重建结果到文件

由于保存MP4的过程需要消耗系统的渲染、编解码资源，Spatial Recon Kit仅支持同一时刻只有一个session正在保存MP4。如果同一时刻有多个session同时进行保存MP4，会导致未定义行为。

注册支持额外数据输入的回调函数

从26.0.0开始，Spatial Recon Kit支持HMS_SpatialReconNGCallbackFunc回调函数，支持接收额外数据，供开发者使用。

typedef void (*HMS_SpatialReconNGCallbackFunc)(HMS_SpatialReconStatus, void*); // HMS_SpatialReconNGCallbackFunc 类型定义

从26.0.0开始，本kit提供HMS_SpatialRecon_RegisterNGCallbackFunc函数，供开发者注册新的HMS_SpatialReconNGCallbackFunc回调函数，用于通知开发者重建或保存的结果。关于回调函数生效的时机，有以下注意事项：

开发者应自行保证回调入口地址的正确性：若需要注册回调函数，必须传入有效的、类型匹配的函数指针。若需要取消回调函数，需要传入nullptr。

在调用HMS_SpatialRecon_StartSession函数提交重建任务之前，HMS_SpatialRecon_RegisterNGCallbackFunc函数只影响重建任务结束后的回调行为。开发者可以在调用HMS_SpatialRecon_StartSession函数之前任意注册、修改、取消回调。此时，开发者无法针对重建结束后保存模型的任务进行回调设置。

在调用HMS_SpatialRecon_StartSession函数提交重建任务之后，HMS_SpatialRecon_RegisterNGCallbackFunc函数只影响保存任务结束后的回调行为。开发者可以在调用HMS_SpatialRecon_StartSession函数之前任意注册、修改、取消回调。此时，即使重建仍未结束，开发者也无法影响重建结束后的回调行为。

HMS_SpatialReconStatus HMS_SpatialRecon_RegisterNGCallbackFunc(HMS_SpatialRecon_Session*
    spatialReconSession, HMS_SpatialReconNGCallbackFunc onSpatialReconFinished, void* data);

注册NGCallback时，Spatial Recon Kit 将保存data指针。在调用NGCallback回调函数时，作为入参传入给NGCallback回调函数。

请注意，除保存指针、作为入参传递以外，Spatial Recon Kit 不会做任何操作，也无法对回调函数中处理data指针的过程做任何保护。开发者需要自行保证data指针得到安全、正确的处理。

#include <map>
#include <hilog/log.h>
#ifndef LOGI
#define LOGI(...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "[SpatialReconKitSample][C]", __VA_ARGS__))
#endif

#ifndef LOGE
#define LOGE(...) ((void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, "[SpatialReconKitSample][C]", __VA_ARGS__))
#endif

// -----------------初始化--------------------
std::map<HMS_SpatialRecon_Session, HMS_SpatialReconStatus> sessionStatsMap = {};

auto it = sessionStatsMap.find(spatialReconSession);
if (it == sessionStatsMap.end()) {
    map[spatialReconSession] = SPATIAL_RECON_STATUS_STAGE_BUILDING;
}

auto callbackWithData = [](HMS_SpatialReconStatus status, void* data) {
    // 将状态码写入到data指针指向的位置中
    auto statusPtr = reinterpret_cast<HMS_SpatialReconStatus*>(data);
    *statusPtr = status;
    return;
};


// -------------------重建--------------------
// 先注册回调函数，再启动重建
auto& sessionStatus = sessionStatsMap[spatialReconSession];
HMS_SpatialReconStatus* statusPtr = &sessionStatus;

HMS_SpatialReconStage sessionStage = SPATIAL_RECON_STAGE_BUILDING;

// 检查stage处于INIT状态，则此时注册回调会在重建结束时调用
float progress = 0.f;
HMS_SpatialReconStatus ret = HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, &sessionStage);

if (sessionStage != SPATIAL_RECON_STAGE_INIT) {
    LOGE("Registering finish reconstruction callback when not at initialzied");
}

ret = HMS_SpatialRecon_RegisterNGCallbackFunc(spatialReconSession, callbackWithData,
    statusPtr);

ret = HMS_SpatialRecon_StartSession(spatialReconSession,
   nullptr, nullptr) // 注册了NGCallback以后，旧风格的callback将会被覆盖。因此，在这里无需注册旧风格callback

// ----------------保存--------------------
// 检查stage处于FINISHED状态，则此时注册回调会在保存结束时调用

HMS_SpatialReconStatus ret = HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, &sessionStage);

if (sessionStage != SPATIAL_RECON_STAGE_FINISHED) {
    LOGE("Registering finish saving callback when not at finished");
}


ret = HMS_SpatialRecon_RegisterNGCallbackFunc(spatialReconSession, callbackWithData,
    statusPtr);


HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置，开发者可以根据需要保存为PLY（点云）或运镜视频文件（MP4）。
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_SaveResultToFile(spatialReconSession,
    &info, NULL); // 已经注册了新的回调，则不必注册旧的回调

## Code blocks

### Code block 1

```
// 包含AREngine头文件
#include "ar/ar_engine_core.h"

#ifndef CHECK
#define CHECK(condition)                                                                                               \
    do {                                                                                                               \
        auto ret = (condition);                                                                                        \
        if (ret) {                                                                                                     \
            LOGE("*** CHECK FAILED at %{public}s:%{public}d: %{public}s ",                                             \
                 __FILE__, __LINE__, #condition);                                                                      \
            abort();                                                                                                   \
        }                                                                                                              \
    } while (false);
#endif

// 需要首先配置好AR引擎

// 创建一个新的AREngine_ARSession会话
AREngine_ARSession *arSession = nullptr;

AREngine_ARFrame *arFrame = nullptr;

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession));
// 配置AREngine_ARSession
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(arSession, &arConfig));
// 设置预览画面尺寸
// 推荐使用 width = 1080, height = 1440图像
CHECK(HMS_AREngine_ARConfig_SetPreviewSize(arSession, arConfig, 1080, 1440));
// 设置画面更新模式。
CHECK(HMS_AREngine_ARConfig_SetUpdateMode(arSession, arConfig, ARENGINE_UPDATE_MODE_LATEST));
CHECK(HMS_AREngine_ARConfig_SetFocusMode(arSession, arConfig, ARENGINE_FOCUS_MODE_AUTO));
CHECK(HMS_AREngine_ARSession_Configure(arSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
// 创建一个新的AREngine_ARFrame对象
CHECK(HMS_AREngine_ARFrame_Create(arSession, &arFrame));

// 更新AR引擎计算结果
AREngine_ARStatus arRet = HMS_AREngine_ARSession_Update(arSession, arFrame);

// 推入数据帧
HMS_SpatialReconStatus ret = HMS_SpatialRecon_PushARFrame(spatialReconSession,
   arSession, arFrame);
```

### Code block 2

```
HMS_SpatialRecon_DataFrame inputFrame;

inputFrame.focalX = usrFocalX;
inputFrame.focalY = usrFocalY;
inputFrame.principalX = usrPrincipalX;
inputFrame.principalY = usrPrincipalY;
inputFrame.imageWidth = usrWidth;
inputFrame.imageHeight = usrHeight;

// ... 组装其他字段

// 仅支持RGB格式输入
inputFrame.format = SPATIAL_RECON_IMAGEDATA_FORMAT_RGB;
inputFrame.imageData = rgbData;

HMS_SpatialReconStatus ret= HMS_SpatialRecon_PushFrame(reconSession, &inputFrame);
```

### Code block 3

```
auto noCaptureFinishedCB = [](HMS_SpatialReconStatus status) {
   // 在这里放callBack需要执行的任务，打印信息/调用其他回调
   return;
};

HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_StartSession(spatialReconSession,
   &info, noCaptureFinishedCB) // 如果writeInfo不为空，则重建完成会自动保存

// 更新RunningMode。如果应用当前处于前台，则设定为前台模式。否则设定为后台模式。
HMS_SpatialRecon_SetRunningMode(SPATIAL_RECON_RUNNING_FOREGROUND_MODE);

// 可以按需获取当前进度
float progress = 0.0f;
HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, NULL);
```

### Code block 4

```
// 暂停
HMS_SpatialRecon_PauseSession(spatialReconSession);

// 继续
HMS_SpatialRecon_ResumeSession(spatialReconSession);
```

### Code block 5

```
HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置，开发者可以根据需要保存为PLY（点云）或运镜视频文件（MP4）。
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_SaveResultToFile(spatialReconSession,
&info, NULL); // 保存重建结果到文件
```

### Code block 6

```
typedef void (*HMS_SpatialReconNGCallbackFunc)(HMS_SpatialReconStatus, void*); // HMS_SpatialReconNGCallbackFunc 类型定义
```

### Code block 7

```
HMS_SpatialReconStatus HMS_SpatialRecon_RegisterNGCallbackFunc(HMS_SpatialRecon_Session*
    spatialReconSession, HMS_SpatialReconNGCallbackFunc onSpatialReconFinished, void* data);
```

### Code block 8

```
#include <map>
#include <hilog/log.h>
#ifndef LOGI
#define LOGI(...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "[SpatialReconKitSample][C]", __VA_ARGS__))
#endif

#ifndef LOGE
#define LOGE(...) ((void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, "[SpatialReconKitSample][C]", __VA_ARGS__))
#endif

// -----------------初始化--------------------
std::map<HMS_SpatialRecon_Session, HMS_SpatialReconStatus> sessionStatsMap = {};

auto it = sessionStatsMap.find(spatialReconSession);
if (it == sessionStatsMap.end()) {
    map[spatialReconSession] = SPATIAL_RECON_STATUS_STAGE_BUILDING;
}

auto callbackWithData = [](HMS_SpatialReconStatus status, void* data) {
    // 将状态码写入到data指针指向的位置中
    auto statusPtr = reinterpret_cast<HMS_SpatialReconStatus*>(data);
    *statusPtr = status;
    return;
};


// -------------------重建--------------------
// 先注册回调函数，再启动重建
auto& sessionStatus = sessionStatsMap[spatialReconSession];
HMS_SpatialReconStatus* statusPtr = &sessionStatus;

HMS_SpatialReconStage sessionStage = SPATIAL_RECON_STAGE_BUILDING;

// 检查stage处于INIT状态，则此时注册回调会在重建结束时调用
float progress = 0.f;
HMS_SpatialReconStatus ret = HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, &sessionStage);

if (sessionStage != SPATIAL_RECON_STAGE_INIT) {
    LOGE("Registering finish reconstruction callback when not at initialzied");
}

ret = HMS_SpatialRecon_RegisterNGCallbackFunc(spatialReconSession, callbackWithData,
    statusPtr);

ret = HMS_SpatialRecon_StartSession(spatialReconSession,
   nullptr, nullptr) // 注册了NGCallback以后，旧风格的callback将会被覆盖。因此，在这里无需注册旧风格callback

// ----------------保存--------------------
// 检查stage处于FINISHED状态，则此时注册回调会在保存结束时调用

HMS_SpatialReconStatus ret = HMS_SpatialRecon_GetProgress(spatialReconSession, &progress, &sessionStage);

if (sessionStage != SPATIAL_RECON_STAGE_FINISHED) {
    LOGE("Registering finish saving callback when not at finished");
}


ret = HMS_SpatialRecon_RegisterNGCallbackFunc(spatialReconSession, callbackWithData,
    statusPtr);


HMS_SpatialRecon_ModelWriteInfo info;
// ... 组装对应的保存时需要的配置，开发者可以根据需要保存为PLY（点云）或运镜视频文件（MP4）。
info.modelFormat = SPATIAL_RECON_OUTPUT_FORMAT_MP4;

HMS_SpatialReconStatus ret = HMS_SpatialRecon_SaveResultToFile(spatialReconSession,
    &info, NULL); // 已经注册了新的回调，则不必注册旧的回调
```
