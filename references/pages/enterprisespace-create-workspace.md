# 创建工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-create-workspace_

createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>	创建工作空间并返回结果。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用createWorkspace接口，创建工作空间，并且查看打印信息。

const localName: string = '111111';
const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
const params: spaceManager.CreateWorkspaceParams = {
  shortName: 'test'
};
try {
  const workspaceInfo: spaceManager.WorkspaceInfo = await spaceManager.createWorkspace(localName, workspaceType, params);
  console.info(`Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
} catch (err) {
  console.error(`Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
}
空间管理
使能工作空间
