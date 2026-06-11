# 创建工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-create-workspace_

场景介绍

Enterprise Space Kit为应用提供创建工作空间的能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
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

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
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
```
