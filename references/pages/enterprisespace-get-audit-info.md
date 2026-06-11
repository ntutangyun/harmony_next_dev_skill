# 获取审批信息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-audit-info_

场景介绍

Enterprise Space Kit为应用提供获取审批信息的能力。文件外发需经过审批流程控制，通过调用审批状态同步接口实时获取审批结果，审批完成后允许文件外发至个人空间，若审批被拒绝或撤销则禁止外发。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getAuditInfo(transactionNum: string): AuditInfo	获取审批信息。

开发步骤

导入Enterprise Space Kit模块。

import { fileTransfer } from '@kit.EnterpriseSpaceKit';

调用getAuditInfo接口，获取审批信息，并且查看打印信息。

const transactionNum: string = '1111111';
try {
  const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
  console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
} catch (err) {
  console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { fileTransfer } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const transactionNum: string = '1111111';
try {
  const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
  console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
} catch (err) {
  console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
}
```
