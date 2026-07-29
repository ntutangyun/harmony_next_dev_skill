# 阻断类客户端信息查询场景（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallauthclientsinfo-c_

从API版本26.0.0开始，新增阻断类客户端信息查询功能，支持应用获取设备上订阅了阻断类事件的所有客户端信息。其中，阻断类信息是指被系统拦截并阻止执行的安全审计事件记录。

场景介绍

应用调用HMS_SecurityAudit_AcquireAllAuthClientsInfo接口获取设备上订阅了阻断类事件的所有客户端信息，包括当前已被创建的客户端数量，以及每个客户端创建者的进程名、进程ID和用户ID。该接口常用于在应用创建阻断类客户端失败时，获取设备上已被创建的客户端信息。

约束和限制

当前能力仅支持PC/2in1设备。

当前支持查询全量安全审计阻断类客户端信息，最多存在16个客户端。

业务流程

流程说明：

应用调用查询阻断类客户端信息接口HMS_SecurityAudit_AcquireAllAuthClientsInfo获取全量安全审计阻断类客户端信息。

HMS_SecurityAudit_AcquireAllAuthClientsInfo接口同步返回阻断类客户端信息给应用，应用根据返回的阻断类客户端信息进行业务处理。

接口说明

接口如下表，更多接口及使用方法请参见API参考。

接口名	描述
int32_t HMS_SecurityAudit_AcquireAllAuthClientsInfo(char** outOwnedResult)	获取全量安全审计阻断类客户端信息。

开发步骤

说明

在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：企业类应用可用权限。

在CMakeLists.txt中导入安全审计共享库，并链接该库。

find_library(dsm-lib libsecurityaudit_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})

导入安全审计的头文件。

#include <cstdio>
#include "DeviceSecurityKit/security_audit.h"

应用调用HMS_SecurityAudit_AcquireAllAuthClientsInfo接口，获取全量安全审计阻断类客户端信息。

说明

应用在根据阻断类客户端信息进行业务处理后，需要释放查询接口出入参的内存。

char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllAuthClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo failed with error: %d\n", ret);
}
// ...
if (outOwnedResult != nullptr) {
    delete[] outOwnedResult;
    outOwnedResult = nullptr;
}

## Code blocks

### Code block 1

```
find_library(dsm-lib libsecurityaudit_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})
```

### Code block 2

```
#include <cstdio>
#include "DeviceSecurityKit/security_audit.h"
```

### Code block 3

```
char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllAuthClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllAuthClientsInfo failed with error: %d\n", ret);
}
// ...
if (outOwnedResult != nullptr) {
    delete[] outOwnedResult;
    outOwnedResult = nullptr;
}
```
