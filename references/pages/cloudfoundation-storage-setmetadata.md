# 设置云侧文件的元数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-setmetadata_

文件元数据包含云侧文件名、文件大小、文件类型等常用属性，也包括用户自定义的文件属性。

文件保存至云侧后，开发者可以设置文件的自定义属性。

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

调用StorageBucket.setMetadata设置云侧文档的元数据信息。

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
hilog.info(0x0000, 'Storage', `promise setMetadata  cloudPath: ${UI.uploadFileName}`);
bucket.setMetadata(UI.uploadFileName, {
  customMetadata: {
    key1: 'value1',
    key2: 'value2'
  }
}).then((result: Object) => {
  hilog.info(0x0000, 'Storage', `Succeeded in setting Metadata  ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to set Metadata code: ${err.code}, message: ${err.message}`);
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
hilog.info(0x0000, 'Storage', `promise setMetadata  cloudPath: ${UI.uploadFileName}`);
bucket.setMetadata(UI.uploadFileName, {
  customMetadata: {
    key1: 'value1',
    key2: 'value2'
  }
}).then((result: Object) => {
  hilog.info(0x0000, 'Storage', `Succeeded in setting Metadata  ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to set Metadata code: ${err.code}, message: ${err.message}`);
});
```
