# 在端侧调用云存储

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudstorage_

import { BusinessError, request } from '@kit.BasicServicesKit';
初始化云存储实例。
const bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
调用云存储接口，如uploadFile接口。“src/main/ets/pages/CloudStorage.ets”代码片段节选如下，更完整的接口信息请参考Cloud Foundation Kit API参考-云存储模块。
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

在端侧访问云数据库
（可选）通过CloudDev面板获取云开发资源支持
