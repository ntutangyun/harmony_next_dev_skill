# 使能工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-enable-workspace_

场景介绍

Enterprise Space Kit为应用提供使能双空间的能力。需要先使能工作空间才可以创建个人空间。

接口说明

详细接口说明可参考接口文档。

接口名	描述
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

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const enable: boolean = true;
try {
  await spaceManager.enableWorkspace(enable);
  console.info('Succeeded in enabling workspace');
} catch (err) {
  console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
}
```
