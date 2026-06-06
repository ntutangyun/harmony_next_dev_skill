# 使能工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-enable-workspace_

enableWorkspace(enable: boolean): Promise<void>	使能工作空间。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用enableWorkspace接口，使能工作空间，并且查看打印信息。

const enable: boolean = true;
try {
  await spaceManager.enableWorkspace(enable);
  console.info('Succeeded in enabling workspace');
} catch (err) {
  console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
}
创建工作空间
查询工作空间
