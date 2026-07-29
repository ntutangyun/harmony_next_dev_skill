# 接入手写笔跟手性加速

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-frame-boost-c_

从API版本26.0.0开始，新增手写笔跟手性加速接口，支持笔记类应用提升手写笔书写时延。

场景介绍

在应用使用书写绘制功能时，获取到界面的触摸事件的类型，通过调用手写笔跟手性加速的接口，可以提升手写笔书写时延。

接口说明

名称	描述
int32_t HMS_HandWrite_SetRefreshDelayOff(const char* xcomponentId, const bool enable)	提升手写笔书写时延。

开发步骤

手写笔跟手性加速接口需要在自定义渲染（XComponent）上注册触摸事件回调获得当前触屏输入的事件类型，请参考自定义渲染开发指南。

[h2]在CMake脚本中链接动态库

target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include) # 当编译过程中手写笔加速接口头文件缺失时尝试加入此命令
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos) # 当编译过程中手写笔加速API链接异常时尝试加入此命令
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhandwrite_ndk.z.so)

[h2]导入模块

#include <ace/xcomponent/native_interface_xcomponent.h>
#include <handwrite/native_handwrite_api.h>
#include <hilog/log.h>

[h2]示例代码

native_handwrite_api.hHMS_HandWrite_SetRefreshDelayOff()接口获取当前触屏输入的事件类型。

#include <ace/xcomponent/native_interface_xcomponent.h>
#include <handwrite/native_handwrite_api.h>
#include <hilog/log.h>

void DispatchTouchEvent(OH_NativeXComponent *xcomponent, void *window)
{
    char id[128] = {};
    uint64_t idBufferSize = sizeof(id);
    if (OH_NativeXComponent_GetXComponentId(xcomponent, id, &idBufferSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        TLOGE("failed to get xcomponent id");
        return;
    }
    std::string xcomponentId(id);
    OH_NativeXComponent_TouchEvent touchEvent;
    if (OH_NativeXComponent_GetTouchEvent(component, window, &touchEvent) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        TLOGE("failed to get touch event");
        return;
    }
    int32_t errcode = INT32_MIN;
    if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_DOWN) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), true);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "down error code is %{public}d", errcode);
    } else if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_UP || touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_CANCEL) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), false);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "up or cancel error code is %{public}d", errcode);
    }
}

## Code blocks

### Code block 1

```
target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include) # 当编译过程中手写笔加速接口头文件缺失时尝试加入此命令
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos) # 当编译过程中手写笔加速API链接异常时尝试加入此命令
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhandwrite_ndk.z.so)
```

### Code block 2

```
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <handwrite/native_handwrite_api.h>
#include <hilog/log.h>
```

### Code block 3

```
#include <ace/xcomponent/native_interface_xcomponent.h>
#include <handwrite/native_handwrite_api.h>
#include <hilog/log.h>

void DispatchTouchEvent(OH_NativeXComponent *xcomponent, void *window)
{
    char id[128] = {};
    uint64_t idBufferSize = sizeof(id);
    if (OH_NativeXComponent_GetXComponentId(xcomponent, id, &idBufferSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        TLOGE("failed to get xcomponent id");
        return;
    }
    std::string xcomponentId(id);
    OH_NativeXComponent_TouchEvent touchEvent;
    if (OH_NativeXComponent_GetTouchEvent(component, window, &touchEvent) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        TLOGE("failed to get touch event");
        return;
    }
    int32_t errcode = INT32_MIN;
    if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_DOWN) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), true);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "down error code is %{public}d", errcode);
    } else if (touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_UP || touchEvent.type == OH_NativeXComponent_TouchEventType::OH_NATIVEXCOMPONENT_CANCEL) {
        errcode = HMS_HandWrite_SetRefreshDelayOff(xcomponentId.c_str(), false);
        OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "PenKit", "up or cancel error code is %{public}d", errcode);
    }
}
```
