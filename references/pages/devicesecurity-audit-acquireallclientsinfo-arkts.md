# 通知类客户端信息查询场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquireallclientsinfo-arkts_

从26.0.0开始，支持三方安全应用获取设备上全量的安全审计通知类客户端信息。

场景介绍

应用调用acquireAllClientsInfo接口可以获取设备上订阅了安全审计通知类事件的所有客户端信息，用于查看当前已被创建的客户端数量以及每个客户端创建者的进程名、进程ID和用户ID。

约束和限制

当前能力仅支持2in1设备。

当前支持查询全量安全审计通知类客户端信息，最多存在16个客户端。

业务流程

流程说明：

应用调用查询通知类客户端信息接口acquireAllClientsInfo获取全量通知类客户端信息。

acquireAllClientsInfo接口同步返回通知类客户端信息给应用，应用根据返回的通知类客户端信息进行业务处理。

接口说明

接口如下表，更多接口及使用方法请参见API参考。

接口名	描述
acquireAllClientsInfo(): string	获取所有的安全审计通知类客户端信息。

开发步骤

说明

在开发准备过程中，需要申请权限：ohos.permission.QUERY_AUDIT_EVENT。只允许清单内的企业类应用申请该权限，申请方式请参考：申请使用企业类应用可用权限。

导入Device Security Kit模块及相关公共模块。

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

开发者调用查询通知类客户端信息接口acquireAllClientsInfo，获取所有的通知类客户端信息。

const TAG = "SecurityAuditJsTest";
try {
  hilog.info(0x0000, TAG, 'acquireAllClientsInfo begin.');
  const result = securityAudit.acquireAllClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllClientsInfo.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllClientsInfo failed: %{public}d %{public}s', e.code, e.message);
}

## Code blocks

### Code block 1

```
import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG = "SecurityAuditJsTest";
try {
  hilog.info(0x0000, TAG, 'acquireAllClientsInfo begin.');
  const result = securityAudit.acquireAllClientsInfo();
  hilog.info(0x0000, TAG, 'Succeeded in acquireAllClientsInfo.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireAllClientsInfo failed: %{public}d %{public}s', e.code, e.message);
}
```
