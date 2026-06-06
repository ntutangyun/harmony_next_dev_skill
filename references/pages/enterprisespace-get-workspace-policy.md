# 查询工作空间策略

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-workspace-policy_

Enterprise Space Kit为应用提供查询工作空间策略的能力。从6.0.2(22)版本开始支持深度冻结策略“lockdown”，从6.1.0(23)版本开始支持个人空间创建引导页展示策略“spaceguide”。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getWorkspacePolicy(key: string, workspaceId?: number): Promise<number>	查询工作空间策略并返回结果。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块和相关依赖模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口getWorkspacePolicy，查询空间策略，并且查看打印信息。

const key: string = 'lockdown';
const workspaceId: number = 100;
try {
  const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
  console.info(`Succeeded in getting workspace policy. value: ${value}`);
} catch (err) {
  console.error(`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
}
设置工作空间策略
设置深度冻结豁免名单
