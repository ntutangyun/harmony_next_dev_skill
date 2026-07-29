# 获取云侧文件列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-list-files_

开发者可以获取指定云侧目录下所有的文件信息，包括文件存储目录、文件名称等。

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

调用StorageBucket.list获取云侧指定目录的文件列表。

bucket.list('', {
  maxResults: 1,
}).then((result: Object) => {
  hilog.info(0x0000, 'Storage', `Succeeded in listing file  ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to list file  code: ${err.code}, message: ${err.message}`);
});

获取文件列表信息结构如下：

{
  directories: ["empty-dir1\/", "screenshot\/"],
  files: ["IMG_20240229_103118.jpg", "IMG_20240318_093732.jpg"]
}

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
bucket.list('', {
  maxResults: 1,
}).then((result: Object) => {
  hilog.info(0x0000, 'Storage', `Succeeded in listing file  ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to list file  code: ${err.code}, message: ${err.message}`);
});
```

### Code block 3

```
{
  directories: ["empty-dir1\/", "screenshot\/"],
  files: ["IMG_20240229_103118.jpg", "IMG_20240318_093732.jpg"]
}
```
