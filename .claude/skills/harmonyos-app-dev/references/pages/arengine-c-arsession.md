# 管理AR会话（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession_

管理AR会话支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考硬件要求判断设备是否支持。

引入AR Engine

引入头文件。

#include "ar/ar_engine_core.h"

编写CMakeLists.txt。

find_library(
    # Sets the name of the path variable.
    arengine-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    libarengine_ndk.z.so
)


target_link_libraries(entry PUBLIC
    ${arengine-lib}
)
创建AR会话

应用开始时，调用HMS_AREngine_ARSession_Create函数创建一个AR会话。

AREngine_ARSession *arSession = nullptr;
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
自定义配置AR会话

创建一个AREngine_ARConfig对象来配置当前AR会话。如缺省，则使用默认配置，具体配置可参考HMS_AREngine_ARConfig_Create。

// 创建一个拥有合理默认配置的配置对象。
AREngine_ARConfig *arConfig = nullptr;
HMS_AREngine_ARConfig_Create(arSession, &arConfig);


// 此处配置arConfig。


// 配置AREngine_ARSession会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);


// 释放指定的配置对象的内存空间。
HMS_AREngine_ARConfig_Destroy(arConfig);

具体可配置项，请参考AR Engine API参考。

销毁AR会话

应用结束时，调用HMS_AREngine_ARSession_Destroy函数销毁当前的AR会话。

HMS_AREngine_ARSession_Destroy(arSession);
管理AR会话（ArkTS）
运动跟踪
