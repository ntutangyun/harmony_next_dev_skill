# 在端侧调用云存储

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudstorage_

前提条件

请确保云存储服务已经开通。

使用云存储功能，需要获取用户凭据。请确保您已配置AccessToken。

操作步骤

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';

const bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

bucket.uploadFile(getContext(this), {
  localPath: cacheFilePath,
  cloudPath: cloudPath,
}).then(task => {
  // add task event listener
  this.addEventListener(task, this.onUploadCompleted(cloudPath, cacheFilePath));
  // start task
  task.start();
}).catch((err: BusinessError) => {
  hilog.error(HILOG_DOMAIN, TAG, 'uploadFile failed, error code: %{public}d, message: %{public}s',
    err.code, err.message);
  this.isUploading = false;
});

## Code blocks

### Code block 1

```
import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
```

### Code block 2

```
const bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
```

### Code block 3

```
bucket.uploadFile(getContext(this), {
  localPath: cacheFilePath,
  cloudPath: cloudPath,
}).then(task => {
  // add task event listener
  this.addEventListener(task, this.onUploadCompleted(cloudPath, cacheFilePath));
  // start task
  task.start();
}).catch((err: BusinessError) => {
  hilog.error(HILOG_DOMAIN, TAG, 'uploadFile failed, error code: %{public}d, message: %{public}s',
    err.code, err.message);
  this.isUploading = false;
});
```
