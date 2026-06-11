# 识别目标形状（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane-shape_

约束与限制

从5.0.0(12)开始，识别目标形状能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持平面语义及物体语义特性（ARENGINE_FEATURE_TYPE_SEMANTIC）。

引入AR Engine

开发者可参考管理AR会话章节的引入AR Engine。

创建AR会话

创建AR会话并配置为目标形状识别模式。

AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置语义识别模式为目标形状识别。
HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_TARGET);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);

创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。

AREngine_ARTrackableList *targetList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &targetList);

获取当前环境中的可跟踪对象

调用HMS_AREngine_ARSession_GetAllTrackables函数，检测当前环境中的所有可跟踪对象，并将结果存放在targetList中。

HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_TARGET, targetList);

获取可跟踪对象数量

调用HMS_AREngine_ARTrackableList_GetSize函数获取当前可跟踪对象数量，结果存放在targetSize中。

int32_t targetSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, targetList, &targetSize);

当targetSize等于0时，代表当前环境中无可跟踪对象。

当targetSize等于1时，代表当前环境中仅存在1个可跟踪对象。

当targetSize大于1时，代表当前环境中存在多个可跟踪对象。

遍历并识别物体形状

当环境中存在一个或多个可跟踪对象时，依次遍历targetList中所有可跟踪对象进行目标形状识别。

for (int i = 0; i < targetSize; ++i) {
    // 遍历可跟踪对象，进行形状识别。
}

对于第i个对象，创建并获取对象实例。

AREngine_ARTrackable *target = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, targetList, i, &target);

获取该实例跟踪状态，仅当跟踪状态为ARENGINE_TRACKING_STATE_TRACKING时，才可进行形状识别。

AREngine_ARTrackingState outTrackingState;
HMS_AREngine_ARTrackable_GetTrackingState(arSession, target, &outTrackingState);

if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
    continue;
}

获取该实例目标形状，识别结果存放在label中。

AREngine_ARTargetShapeLabel label = ARENGINE_TARGET_SHAPE_UNKNOWN;
HMS_AREngine_ARTarget_GetShapeType(arSession, reinterpret_cast<AREngine_ARTarget *>(target), &label);

其中，AREngine_ARTargetShapeLabel为枚举类型，描述了目标物体形状。

销毁可跟踪对象列表

HMS_AREngine_ARTrackableList_Destroy(targetList);

## Code blocks

### Code block 1

```
AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置语义识别模式为目标形状识别。
HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_TARGET);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### Code block 2

```
AREngine_ARTrackableList *targetList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &targetList);
```

### Code block 3

```
HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_TARGET, targetList);
```

### Code block 4

```
int32_t targetSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, targetList, &targetSize);
```

### Code block 5

```
for (int i = 0; i < targetSize; ++i) {
    // 遍历可跟踪对象，进行形状识别。
}
```

### Code block 6

```
AREngine_ARTrackable *target = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, targetList, i, &target);
```

### Code block 7

```
AREngine_ARTrackingState outTrackingState;
HMS_AREngine_ARTrackable_GetTrackingState(arSession, target, &outTrackingState);

if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
    continue;
}
```

### Code block 8

```
AREngine_ARTargetShapeLabel label = ARENGINE_TARGET_SHAPE_UNKNOWN;
HMS_AREngine_ARTarget_GetShapeType(arSession, reinterpret_cast<AREngine_ARTarget *>(target), &label);
```

### Code block 9

```
HMS_AREngine_ARTrackableList_Destroy(targetList);
```
