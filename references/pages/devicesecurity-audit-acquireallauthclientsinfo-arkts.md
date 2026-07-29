# 阻断类客户端信息查询场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallauthclientsinfo-arkts_

从API版本26.0.0开始，新增阻断类客户端信息查询功能，支持应用获取设备上订阅了阻断类事件的所有客户端信息。其中，阻断类信息是指被系统拦截并阻止执行的安全审计事件记录。

场景介绍

应用通过调用acquireAllAuthClientsInfo接口获取设备上订阅了阻断类事件的所有客户端信息，包括当前已被创建的客户端数量，以及每个客户端创建者的进程名、进程ID和用户ID。该接口常用于在应用创建阻断类客户端失败时，获取设备上已被创建的客户端信息。

约束和限制

当前能力仅支持PC/2in1设备。

当前支持查询全量安全审计阻断类客户端信息，最多存在16个客户端。

业务流程

流程说明：

应用调用查询阻断类客户端信息接口acquireAllAuthClientsInfo获取全量阻断类客户端信息。

acquireAllAuthClientsInfo接口同步返回阻断类客户端信息给应用，应用根据返回的阻断类客户端信息信息进行业务处理。

接口说明

接口如下表，更多接口及使用方法请参见API参考。

接口名	描述
acquireAllAuthClientsInfo(): string	获取所有的安全审计阻断类客户端信息。

开发步骤

说明

在开发准备过程中，需要申请权限：ohos.permission.kernel.AUTH_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：企业类应用可用权限。

导入Device Security Kit模块及相关公共模块。

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

应用调用查询阻断类客户端信息接口acquireAllAuthClientsInfo，获取所有的阻断类客户端信息。

const TAG = 'SecurityAuditJsTest';
try {
  hilog.info(0x0000, TAG, 'acquireAllAuthClientsInfo begin.');
  const result = securityAudit.acquireAllAuthClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllAuthClientsInfo.');
  // ...
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllAuthClientsInfo failed: %{public}d %{public}s', e.code, e.message);
  // ...
}

## Code blocks

### Code block 1

```
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG = 'SecurityAuditJsTest';
try {
  hilog.info(0x0000, TAG, 'acquireAllAuthClientsInfo begin.');
  const result = securityAudit.acquireAllAuthClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllAuthClientsInfo.');
  // ...
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllAuthClientsInfo failed: %{public}d %{public}s', e.code, e.message);
  // ...
}
```
