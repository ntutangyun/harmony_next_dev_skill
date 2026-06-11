# 设置审批信息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-audit-info_

场景介绍

当文件外发需经过审批流程控制时，Enterprise Space Kit为应用提供设置审批信息的能力，审批信息包括审批ID、用户ID、用户名称、审批时间、审批评论和文件审批状态。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setAuditInfo(transactionNum: string, info: AuditInfo): number	设置审批信息并返回结果。

开发步骤

导入Enterprise Space Kit模块。

import { fileTransfer } from '@kit.EnterpriseSpaceKit';

调用setAuditInfo接口，设置审批信息。

const transactionNum: string = '1111111';
const info: fileTransfer.AuditInfo = {
  auditId: '123456',
  userId: '100',
  userName: 'test',
  time: Date.now(),
  comments: 'Waiting approval',
  status: '1'
};
try {
  const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
  console.info(`Succeeded in setting audit info, number:`, ret);
} catch (err) {
  console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { fileTransfer } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const transactionNum: string = '1111111';
const info: fileTransfer.AuditInfo = {
  auditId: '123456',
  userId: '100',
  userName: 'test',
  time: Date.now(),
  comments: 'Waiting approval',
  status: '1'
};
try {
  const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
  console.info(`Succeeded in setting audit info, number:`, ret);
} catch (err) {
  console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
}
```
