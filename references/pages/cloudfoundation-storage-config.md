# 设置云存储配置项

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-config_

约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

操作步骤

在“entry/src/main/module.json5”文件中添加网络权限。

"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET"
  }
]

（可选）如果存在需要登录应用才能使用云存储的场景（如上传下载文件），您需要执行如下操作：

通过AuthProvider获取用户凭据。

调用init()方法进行初始化时，传入获取的凭据。

（可选）自定义初始化参数。

如开发者需要自定义云存储接口使用的网络类型或任务模式等初始化参数，可参考如下配置。

import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';

// 设置云存储只使用wifi网络
cloudCommon.init({
  storageOptions: {
    network: request.agent.Network.WIFI
  }
})

import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';

// 设置云存储上传下载任务为前台模式
cloudCommon.init({
  storageOptions: {
    mode: request.agent.Mode.FOREGROUND
  }
})

## Code blocks

### Code block 1

```
"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET"
  }
]
```

### Code block 2

```
import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';

// 设置云存储只使用wifi网络
cloudCommon.init({
  storageOptions: {
    network: request.agent.Network.WIFI
  }
})
```

### Code block 3

```
import { cloudCommon } from '@kit.CloudFoundationKit';
import { request } from '@kit.BasicServicesKit';

// 设置云存储上传下载任务为前台模式
cloudCommon.init({
  storageOptions: {
    mode: request.agent.Mode.FOREGROUND
  }
})
```
