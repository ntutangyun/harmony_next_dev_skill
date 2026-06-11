# 取消订阅公共事件（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-common-event-unsubscription_

场景介绍

订阅者在完成业务需求之后，需要取消订阅公共事件。

接口说明

详细的API说明请参考oh_commonevent.h。

接口名	描述
CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)	取消订阅公共事件。

开发步骤

引用头文件。

#include "hilog/log.h"
#include "BasicServicesKit/oh_commonevent.h"

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

## Code blocks

### Code block 1

```
#include "hilog/log.h"
#include "BasicServicesKit/oh_commonevent.h"
```

### Code block 2

```
target_link_libraries(entry PUBLIC
    libace_napi.z.so
    libhilog_ndk.z.so
    libohcommonevent.so
)
```

### Code block 3

```
void Unsubscribe(CommonEvent_Subscriber *subscriber)
{
    // 通过传入订阅者来退订事件
    int32_t ret = OH_CommonEvent_UnSubscribe(subscriber);
    OH_LOG_Print(LOG_APP, LOG_INFO, 1, "CES_TEST", "OH_CommonEvent_UnSubscribe ret <%{public}d>.", ret);
}
```
