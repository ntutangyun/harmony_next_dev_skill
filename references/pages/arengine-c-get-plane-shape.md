# 识别目标形状（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane-shape_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.0(12)开始，识别目标形状能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持平面语义及物体语义特性（ARENGINE_FEATURE_TYPE_SEMANTIC）。

引入AR Engine

开发者可参考管理AR会话章节的引入AR Engine。

创建AR会话

创建AR会话并配置为物体语义识别模式。

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
// 配置AREngine_ARSession。
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));

创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。

AREngine_ARTrackableList *planeList = nullptr;
// 创建可跟踪对象列表。
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &planeList));

获取当前环境中的可跟踪对象

调用HMS_AREngine_ARSession_GetAllTrackables函数，检测当前环境中的所有可跟踪对象，并将结果存放在targetList中。

CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList));

获取可跟踪对象数量

调用HMS_AREngine_ARTrackableList_GetSize函数获取当前可跟踪对象数量，结果存放在targetSize中。

int32_t planeListSize = 0;
// 获取列表中可跟踪对象的数量。
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize));

当targetSize等于0时，代表当前环境中无可跟踪对象。

当targetSize等于1时，代表当前环境中仅存在1个可跟踪对象。

当targetSize大于1时，代表当前环境中存在多个可跟踪对象。

遍历并识别物体形状

当环境中存在一个或多个可跟踪对象时，依次遍历targetList中所有可跟踪对象进行物体语义识别。

for (int i = 0; i < planeListSize; ++i) {
    // ...
}

对于第i个对象，创建并获取对象实例。

AREngine_ARTrackable *arTrackable = nullptr;
// 从可跟踪对象列表中获取指定索引的对象。
CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable));
AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);

获取该实例跟踪状态，仅当跟踪状态为ARENGINE_TRACKING_STATE_TRACKING时，才可进行形状识别。

AREngine_ARTrackingState outTrackingState;
CHECK(HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState));
// ...
if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
    continue;
}

获取该实例目标形状，识别结果存放在label中。

参考HMS_AREngine_ARTarget_GetShapeType。AREngine_ARTargetShapeLabel为枚举类型，描述了目标物体形状。

销毁可跟踪对象列表

HMS_AREngine_ARTrackableList_Destroy(planeList);

## Code blocks

### Code block 1

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
// 配置AREngine_ARSession。
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### Code block 2

```
AREngine_ARTrackableList *planeList = nullptr;
// 创建可跟踪对象列表。
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &planeList));
```

### Code block 3

```
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList));
```

### Code block 4

```
int32_t planeListSize = 0;
// 获取列表中可跟踪对象的数量。
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize));
```

### Code block 5

```
for (int i = 0; i < planeListSize; ++i) {
    // ...
}
```

### Code block 6

```
AREngine_ARTrackable *arTrackable = nullptr;
// 从可跟踪对象列表中获取指定索引的对象。
CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable));
AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
```

### Code block 7

```
AREngine_ARTrackingState outTrackingState;
CHECK(HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState));
// ...
if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
    continue;
}
```

### Code block 8

```
HMS_AREngine_ARTrackableList_Destroy(planeList);
```
