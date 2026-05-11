# 取消订阅公共事件（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription_

CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)	取消订阅公共事件。
开发步骤

引用头文件。

#include "hilog/log.h"
#include "BasicServicesKit/oh_commonevent.h"
common_event_unsubscribe.h

在CMake脚本中添加动态链接库。

target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libohcommonevent.so
)

取消订阅公共事件。

订阅者订阅公共事件并完成业务需求后，可以通过OH_CommonEvent_UnSubscribe主动取消订阅事件。

void Unsubscribe(CommonEvent_Subscriber *subscriber)
{
    // 通过传入订阅者来退订事件
    int32_t ret = OH_CommonEvent_UnSubscribe(subscriber);
    OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_UnSubscribe ret <%{public}d>.", ret);
}
common_event_unsubscribe.cpp
订阅公共事件（C/C++）
发布公共事件（C/C++）
