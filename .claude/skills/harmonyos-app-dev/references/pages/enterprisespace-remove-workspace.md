# 移除工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-remove-workspace_

removeWorkspace(localId: number): Promise<void>	移除工作空间。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用removeWorkspace接口，移除工作空间，并且查看打印信息。

const workspaceId: number = 100;
try {
  await spaceManager.removeWorkspace(workspaceId);
  console.info('Succeeded in removing workspace');
} catch (err) {
  console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
}
查询工作空间
设置工作空间信息
