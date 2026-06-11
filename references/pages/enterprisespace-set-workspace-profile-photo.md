# 设置工作空间资料照片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-profile-photo_

场景介绍

Enterprise Space Kit为应用提供设置工作空间资料照片的能力。所有工作空间都可以设置资料照片。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>	设置工作空间资料照片。使用Promise异步回调。

开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用setWorkspaceProfilePhoto接口，设置工作空间资料照片，并且查看打印信息。

const workspaceId: number = 100;
const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO******Jggg==}';
try {
  await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
  console.info('Succeeded in setting workspace profile photo');
} catch (err) {
  console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const workspaceId: number = 100;
const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO******Jggg==}';
try {
  await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
  console.info('Succeeded in setting workspace profile photo');
} catch (err) {
  console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
}
```
