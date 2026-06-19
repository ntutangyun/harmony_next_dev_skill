# 通知类客户端信息查询场景（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallclientsinfo-c_

从26.0.0开始，支持三方安全应用获取设备上全量的安全审计通知类客户端信息。

场景介绍

应用调用HMS_SecurityAudit_AcquireAllClientsInfo接口可以获取设备上订阅了安全审计通知类事件的所有客户端信息，用于查看当前已被创建的客户端数量以及每个客户端创建者的进程名、进程ID和用户ID。

约束和限制

当前能力仅支持2in1设备。

当前支持查询全量安全审计通知类客户端信息，最多存在16个客户端。

业务流程

流程说明：

应用调用查询通知类客户端信息接口HMS_SecurityAudit_AcquireAllClientsInfo获取全量安全审计通知类客户端信息。

HMS_SecurityAudit_AcquireAllClientsInfo接口同步返回通知类客户端信息给应用，应用根据返回的通知类客户端信息进行业务处理。

接口说明

接口如下表，更多接口及使用方法请参见API参考。

接口名	描述
int32_t HMS_SecurityAudit_AcquireAllClientsInfo(char** outOwnedResult)	获取全量安全审计通知类客户端信息。

开发步骤

说明

在开发准备过程中，需要申请权限：ohos.permission.QUERY_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：申请使用企业类应用可用权限。

在CMakeLists.txt中导入安全审计共享库，并链接该库。

find_library(dsm-lib libsecurityaudit_ndk.z.so)
target_link_libraries(entry PUBLIC libace_napi.z.so ${dsm-lib})

导入安全审计的头文件。

#include <DeviceSecurityKit/security_audit.h>
#include <cstdio>

调用HMS_SecurityAudit_AcquireAllClientsInfo接口，获取全量安全审计通知类客户端信息。

说明

应用在根据通知类客户端信息进行业务处理后，需要释放查询接口出入参的内存。

char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllClientsInfo failed with error: %d\n", ret);
}
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
#include <DeviceSecurityKit/security_audit.h>
#include <cstdio>
```

### Code block 3

```
char *outOwnedResult = nullptr;
int32_t ret = HMS_SecurityAudit_AcquireAllClientsInfo(&outOwnedResult);
if (ret == 0 && outOwnedResult != nullptr) {
    printf("HMS_SecurityAudit_AcquireAllClientsInfo outOwnedResult: %s\n", outOwnedResult);
} else {
     printf("HMS_SecurityAudit_AcquireAllClientsInfo failed with error: %d\n", ret);
}
if (outOwnedResult != nullptr) {
    delete[] outOwnedResult;
    outOwnedResult = nullptr;
}
```
