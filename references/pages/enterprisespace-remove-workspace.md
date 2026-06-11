# 移除工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-remove-workspace_

场景介绍

Enterprise Space Kit为企业用户提供移除工作空间的能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
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

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const workspaceId: number = 100;
try {
  await spaceManager.removeWorkspace(workspaceId);
  console.info('Succeeded in removing workspace');
} catch (err) {
  console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
}
```
