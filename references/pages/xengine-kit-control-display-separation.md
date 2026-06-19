# 控显分离

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-control-display-separation_

从API版本26.0.0开始，新增控显分离特性。

XEngine Kit针对折叠屏设备推出“控显分离”创新方案。在设备展开态下，该方案通过将屏幕划分为两个对称的独立区域，深度还原复古掌机的交互逻辑：上半屏承载核心渲染画面，下半屏集中交互触控。

约束与限制

支持的设备类型：仅支持部分折叠屏设备。

可通过以下方式查询相关扩展特性是否支持：

目前仅支持基于Vulkan API开发的游戏，使用HMS_XEG_SetControlDisplaySeparationStatusListener接口进行查询，若函数返回结果为true，则表示当前硬件系统支持该特性，游戏侧可显式展示特性开关并允许启用该特性，若返回false，则表示不支持，游戏侧须隐藏该特性开关并禁止启用该特性。

接口说明

以下接口为使用控显分离特性需要使用的接口，关于这些接口的详细说明见接口文档。

接口名	描述
bool HMS_XEG_SetControlDisplaySeparationStatusListener(PFN_HMS_XEG_ControlDisplaySeparationStatusCallback callback)	设置控显分离特性全局唯一监听函数。
void HMS_XEG_RemoveControlDisplaySeparationStatusListener()	移除控显分离特性全局唯一监听函数。
bool HMS_XEG_SetControlDisplaySeparationActive(bool flag)	设置控显分离特性使能开关。

业务流程

环境配置：游戏应用需首先在module.json5配置文件中声明控显分离特性，以启用系统级的适配能力。

启动加载：用户启动游戏，触发应用初始化流程。

能力监测：应用调用HMS_XEG_SetControlDisplaySeparationStatusListener注册状态监听回调。根据接口本身的返回值确认当前硬件系统是否支持控显分离。若支持，XEngine Kit 将实时监测设备屏幕的物理形态，并通过注册的回调函数返回当前状态是否允许启用该特性（例如：折叠屏展开态允许，折叠态不允许），状态记录至status。

特性开关设置：在设备支持的前提下，游戏侧可以向用户提供功能开关，并将用户的开启状态记录至isFeatureOn。

特性场景识别：当设备状态允许且用户已开启功能时，游戏应用需识别当前业务场景（如对局中）是否需触发该特性，状态记录至isActive。

控显分离状态刷新：当status（设备态）、isFeatureOn（用户态）或isActive（场景态）中任意变量发生变化时，需即时刷新控显分离特性状态，并调用HMS_XEG_SetControlDisplaySeparationActive设置特性使能开关，详见开发步骤。

关键UI标识（可选）：系统默认将主画面布局在上半屏，其余UI布局在下半屏。若需将特定UI置于上半屏显示，需对其进行关键标记，详见开发步骤。

资讯副屏（可选）：游戏应用如果想在控显分离生效时候，在下半屏额外渲染其他内容，则直接在当前场景下，渲染即可。

当用户退出应用或不再使用该功能时，调用HMS_XEG_RemoveControlDisplaySeparationStatusListener注销监听，释放相关资源。

开发步骤

本章以在Vulkan应用程序中集成为例，说明XEngine集成操作过程。

[h2]配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

头文件引用

#include <algorithm>
#include <string>
#include <vector>
#include <xengine/xeg_control_display_separation.h>

编写CMakeLists.txt

CMakeLists.txt部分示例代码如下：

find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
)
target_link_libraries(nativerender PUBLIC
    # 其他库文件
    # ...
    ${xengine-lib})

[h2]集成XEngine控显分离特性（Vulkan）

使用Vulkan图形API搭建图像渲染管线，并集成控显分离代码需要在Native层实现，渲染结果通过XComponent组件显示到屏幕。

// 增加以下字段
// ...
"metadata": [
    {
        "name": "XEngineKit_ControlDisplaySeparation",
        "value": "true"
    },
],
// ...

// 当前硬件系统是否支持该特性
bool isSystemSupport = false;

// 设备状态，用于描述当前状态是否允许启用该特性（例如折叠屏展开态允许，折叠态不允许）
XEG_ControlDisplaySeparationStatus status = XEG_ControlDisplaySeparationStatus::UNAVAILABLE;

// 用户配置开关，用于描述用户或者游戏本身是否打开该特性
bool isFeatureOn = false;

// 特性使能开关，用于描述当前场景是否使能控显分离（例如：游戏大厅场景不使能，游戏对局内使能）
bool isActive = false;

// 状态回调函数
void ControlDisplaySeparationHandler(XEG_ControlDisplaySeparationStatus controlDisplaySeparationStatus) {
    status = controlDisplaySeparationStatus;
    UpdateControlDisplaySeparation(); // 刷新控显分离特性状态
}
// 注册控显分离状态监听，注册成功表示当前设备支持控显分离特性，否则不支持
bool isSystemSupport = HMS_XEG_SetControlDisplaySeparationStatusListener(ControlDisplaySeparationHandler);

特性开关设置：游戏应用可以在用户点击设置页面时，如果设备支持该特性，则可以提供特性开关选项。并将特性开关结果赋值给isFeatureOn。

特性场景识别：当设备状态允许且用户已开启功能时，游戏应用需识别当前业务场景（如对局中）是否需触发该特性，状态记录至isActive。

void UpdateControlDisplaySeparation() {
    if(isFeatureOn == true && status == XEG_ControlDisplaySeparationStatus::AVAILABLE && isActive == true){ // 需要开启控显分离
        if(HMS_XEG_SetControlDisplaySeparationActive(true)) { // 开启成功
            // 调用游戏引擎分辨率设置接口，将渲染分辨率的高度设为原来的一半
            // 关键UI标识（可选），标识后关键UI可以渲染到上半屏
            // 渲染额外的资讯副屏（可选）， 和其他UI在同一个render pass渲染即可
        } else { // 开启失败
            isActive = false;
        }
    } else { // 需要关闭控显分离
        if(HMS_XEG_SetControlDisplaySeparationActive(false)) {
            // 调用游戏引擎分辨率设置接口，将渲染分辨率的高度设为全屏高度
        } else {
            // 关闭失败，需要进一步定位原因。
        }
    }
}

关键UI标识（可选）：控显分离特性默认将主画面渲染至上半屏，其余UI渲染至下半屏。若需将血条、角色名等特定UI保留在上半屏，须在特性开启时对其进行标识。开发者可采用模板值标记方案，通过预先为目标UI设置统一的标签，并在特性生效时，将这些UI对应的模板值统一设置为200，系统底层即可识别并将其渲染至上半屏。

资讯副屏（可选）：在控显分离模式下，原本为避开中心画面而设计在屏幕两侧的UI布局，会导致下半屏中心区域出现大量空白。应用可利用该空间展示游戏计分板、实时战报等额外资讯内容以丰富交互体验。新增资讯内容的实现方式与常规UI一致，直接在当前场景下执行渲染即可。

if(exit) {
    HMS_XEG_RemoveControlDisplaySeparationStatusListener();
}

## Code blocks

### Code block 1

```
#include <algorithm>
#include <string>
#include <vector>
#include <xengine/xeg_control_display_separation.h>
```

### Code block 2

```
find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
)
target_link_libraries(nativerender PUBLIC
    # 其他库文件
    # ...
    ${xengine-lib})
```

### Code block 3

```
// 增加以下字段
// ...
"metadata": [
    {
        "name": "XEngineKit_ControlDisplaySeparation",
        "value": "true"
    },
],
// ...
```

### Code block 4

```
// 当前硬件系统是否支持该特性
bool isSystemSupport = false;

// 设备状态，用于描述当前状态是否允许启用该特性（例如折叠屏展开态允许，折叠态不允许）
XEG_ControlDisplaySeparationStatus status = XEG_ControlDisplaySeparationStatus::UNAVAILABLE;

// 用户配置开关，用于描述用户或者游戏本身是否打开该特性
bool isFeatureOn = false;

// 特性使能开关，用于描述当前场景是否使能控显分离（例如：游戏大厅场景不使能，游戏对局内使能）
bool isActive = false;
```

### Code block 5

```
// 状态回调函数
void ControlDisplaySeparationHandler(XEG_ControlDisplaySeparationStatus controlDisplaySeparationStatus) {
    status = controlDisplaySeparationStatus;
    UpdateControlDisplaySeparation(); // 刷新控显分离特性状态
}
// 注册控显分离状态监听，注册成功表示当前设备支持控显分离特性，否则不支持
bool isSystemSupport = HMS_XEG_SetControlDisplaySeparationStatusListener(ControlDisplaySeparationHandler);
```

### Code block 6

```
void UpdateControlDisplaySeparation() {
    if(isFeatureOn == true && status == XEG_ControlDisplaySeparationStatus::AVAILABLE && isActive == true){ // 需要开启控显分离
        if(HMS_XEG_SetControlDisplaySeparationActive(true)) { // 开启成功
            // 调用游戏引擎分辨率设置接口，将渲染分辨率的高度设为原来的一半
            // 关键UI标识（可选），标识后关键UI可以渲染到上半屏
            // 渲染额外的资讯副屏（可选）， 和其他UI在同一个render pass渲染即可
        } else { // 开启失败
            isActive = false;
        }
    } else { // 需要关闭控显分离
        if(HMS_XEG_SetControlDisplaySeparationActive(false)) {
            // 调用游戏引擎分辨率设置接口，将渲染分辨率的高度设为全屏高度
        } else {
            // 关闭失败，需要进一步定位原因。
        }
    }
}
```

### Code block 7

```
if(exit) {
    HMS_XEG_RemoveControlDisplaySeparationStatusListener();
}
```
