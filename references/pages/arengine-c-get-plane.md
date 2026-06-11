# 检测环境中的平面（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-plane_

概要

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.0(12)开始，检测环境平面能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SLAM）。

引入AR Engine

开发者可参考管理AR会话章节的引入AR Engine。

创建ARSession

开发者可以参考管理AR会话创建ARSession。

创建平面对象列表

创建一个平面对象列表planeList，用于存放AR Engine运行过程中检测到的所有平面。

AREngine_ARTrackableList *planeList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &planeList);

设置可跟踪对象类型为ARENGINE_TRACKABLE_PLANE。

AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;

识别当前环境中的平面

调用HMS_AREngine_ARSession_GetAllTrackables函数，检测当前环境中的所有平面，并将结果存放在planeList中。

HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);

获取平面数量

调用HMS_AREngine_ARTrackableList_GetSize函数获取平面数量，结果存放在planeListSize中。

int32_t planeListSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize);

在应用环境中，可能存在0个、1个或多个平面。

当planeListSize等于0时，表示当前环境中不存在平面。

当planeListSize等于1时，表示当前环境中仅存在1个平面。

当planeListSize大于1时，表示当前环境中存在多个平面。

获取平面实例

当存在1个或多个平面时，可以依次遍历planeList获取所有平面对象。

for (int i = 0; i < planeListSize; ++i) {
    // 遍历所有平面对象，根据您的应用进行处理。
}

对于第i个平面，创建并获取可跟踪对象，并将其转化为平面对象AREngine_ARPlane。

AREngine_ARTrackable *arTrackable = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable);
AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane*>(arTrackable);

说明

AR Engine中，任何物体都被定义为可跟踪对象AREngine_ARTrackable。平面也是一种可跟踪对象，开发者可以通过类型转换reinterpret_cast将可跟踪对象AREngine_ARTrackable转化为平面对象AREngine_ARPlane。

销毁平面对象列表

HMS_AREngine_ARTrackableList_Destroy(planeList);

## Code blocks

### Code block 1

```
AREngine_ARTrackableList *planeList = nullptr;
HMS_AREngine_ARTrackableList_Create(arSession, &planeList);
```

### Code block 2

```
AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
```

### Code block 3

```
HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList);
```

### Code block 4

```
int32_t planeListSize = 0;
HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize);
```

### Code block 5

```
for (int i = 0; i < planeListSize; ++i) {
    // 遍历所有平面对象，根据您的应用进行处理。
}
```

### Code block 6

```
AREngine_ARTrackable *arTrackable = nullptr;
HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable);
AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane*>(arTrackable);
```

### Code block 7

```
HMS_AREngine_ARTrackableList_Destroy(planeList);
```
