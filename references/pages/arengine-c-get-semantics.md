# 识别平面语义（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-semantics_

约束与限制

从5.0.0(12)开始，识别平面语义能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持平面语义及物体语义特性（ARENGINE_FEATURE_TYPE_SEMANTIC）。

引入AR Engine

开发者可参考管理AR会话章节的引入AR Engine。

创建AR会话

创建AR会话并配置为平面语义识别模式。

AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置语义识别模式为平面语义识别。
HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_PLANE);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);

检测环境中的平面

进行平面语义识别之前，需要先检测环境中的平面。开发者可以参考检测环境中的平面完成平面检测过程，并获取环境中的平面数量。当存在平面时，就可以继续下面的步骤。

初始化平面语义标签

创建并初始化平面语义标签label，用于描述平面的语义。

AREngine_ARSemanticPlaneLabel label = ARENGINE_PLANE_UNKNOWN;

平面语义标签定义为枚举类型，包括12种枚举值（1种未知类型+11种平面类型）。

typedef enum {
    /** Unknown type. */
    ARENGINE_PLANE_UNKNOWN = 0,
    /** Wall. */
    ARENGINE_PLANE_WALL = 1,
    /** Floor. */
    ARENGINE_PLANE_FLOOR = 2,
    /** Seat. */
    ARENGINE_PLANE_SEAT = 3,
    /** Table. */
    ARENGINE_PLANE_TABLE = 4,
    /** Ceiling. */
    ARENGINE_PLANE_CEILING = 5,
    /** Door. */
    ARENGINE_PLANE_DOOR = 6,
    /** Window. */
    ARENGINE_PLANE_WINDOW = 7,
    /** Bed. */
    ARENGINE_PLANE_BED = 8,
    /** Plane Space. */
    ARENGINE_PLANE_SPACE = 9,
    /** Cube Volume. */
    ARENGINE_CUBE_VOLUME = 10,
    /** Cube Space. */
    ARENGINE_CUBE_SPACE = 11,
} AREngine_ARSemanticPlaneLabel;

识别平面类型

调用HMS_AREngine_ARPlane_GetLabel函数，获取平面类型，结果存放在label中。平面的获取可以参考获取平面实例。

HMS_AREngine_ARPlane_GetLabel(arSession, arPlane, &label);

## Code blocks

### Code block 1

```
AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置语义识别模式为平面语义识别。
HMS_AREngine_ARConfig_SetSemanticMode(arSession, arConfig, ARENGINE_SEMANTIC_MODE_PLANE);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### Code block 2

```
AREngine_ARSemanticPlaneLabel label = ARENGINE_PLANE_UNKNOWN;
```

### Code block 3

```
typedef enum {
    /** Unknown type. */
    ARENGINE_PLANE_UNKNOWN = 0,
    /** Wall. */
    ARENGINE_PLANE_WALL = 1,
    /** Floor. */
    ARENGINE_PLANE_FLOOR = 2,
    /** Seat. */
    ARENGINE_PLANE_SEAT = 3,
    /** Table. */
    ARENGINE_PLANE_TABLE = 4,
    /** Ceiling. */
    ARENGINE_PLANE_CEILING = 5,
    /** Door. */
    ARENGINE_PLANE_DOOR = 6,
    /** Window. */
    ARENGINE_PLANE_WINDOW = 7,
    /** Bed. */
    ARENGINE_PLANE_BED = 8,
    /** Plane Space. */
    ARENGINE_PLANE_SPACE = 9,
    /** Cube Volume. */
    ARENGINE_CUBE_VOLUME = 10,
    /** Cube Space. */
    ARENGINE_CUBE_SPACE = 11,
} AREngine_ARSemanticPlaneLabel;
```

### Code block 4

```
HMS_AREngine_ARPlane_GetLabel(arSession, arPlane, &label);
```
