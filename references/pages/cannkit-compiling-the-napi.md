# 配置项目NAPI

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-compiling-the-napi_

编译HAP时，NAPI层的so需要编译依赖NDK中的libneural_network_core.so和libhiai_foundation.so。

头文件引用

按需引用NNCore和CANN Kit的头文件。

#include "neural_network_runtime/neural_network_core.h"
#include "CANNKit/hiai_options.h"
编写CMakeLists.txt

CMakeLists.txt示例代码如下。

# the minimum version of CMake.
cmake_minimum_required(VERSION 3.4.1)
project(CANNDemo)


set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})


include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)


include_directories(${HMOS_SDK_NATIVE}/sysroot/usr/lib)
FIND_LIBRARY(cann-lib hiai_foundation)


add_library(entry SHARED Classification.cpp HIAIModelManager.cpp)


target_link_libraries(entry PUBLIC libace_napi.z.so
    libhilog_ndk.z.so
    librawfile.z.so
    ${cann-lib}
    libneural_network_core.so
    )
创建项目
集成模型
