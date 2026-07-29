# 获取云侧文件下载地址

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-getdownloadurl_

文件上传至云侧后，开发者可以获取云侧文件的下载地址，将下载地址放到网站中提供文件下载的体验。

约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已初始化存储实例。

已上传指定文件至云侧。

操作步骤

导入相关模块。

import { cloudStorage } from '@kit.CloudFoundationKit';
// ...
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

调用StorageBucket.getDownloadURL接口获取云侧文件的下载地址。

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
bucket.getDownloadURL(UI.uploadFileName).then((downloadURL: string) => {
  hilog.info(0x0000, 'Storage', `Succeeded in getting dwonLoadURL: ${downloadURL}`);
}).catch((err: BusinessError) => {
  hilog.info(0x0000, 'Storage', `Failed to get DownloadURL code: ${err.code}, message: ${err.message}`);
});

## Code blocks

### Code block 1

```
import { cloudStorage } from '@kit.CloudFoundationKit';
// ...
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
bucket.getDownloadURL(UI.uploadFileName).then((downloadURL: string) => {
  hilog.info(0x0000, 'Storage', `Succeeded in getting dwonLoadURL: ${downloadURL}`);
}).catch((err: BusinessError) => {
  hilog.info(0x0000, 'Storage', `Failed to get DownloadURL code: ${err.code}, message: ${err.message}`);
});
```
