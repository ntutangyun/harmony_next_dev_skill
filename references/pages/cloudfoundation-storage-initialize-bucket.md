# 初始化存储实例

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-initialize-bucket_

约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已开通云存储服务。

操作步骤

调用cloudStorage.bucket初始化一个存储实例。

导入相关模块。

import { cloudStorage } from '@kit.CloudFoundationKit';

使用以下任意一种方式初始化实例。

使用默认实例

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

使用指定的实例

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket('bucket001-2wezr'); // 指定bucket001-2wezr实例

注意

以“使用指定的实例”方式初始化云存储实例，请确保当前云侧存在该存储实例，否则后续操作将出现找不到存储实例的错误。在云侧创建新的存储实例，可参考存储实例管理。

## Code blocks

### Code block 1

```
import { cloudStorage } from '@kit.CloudFoundationKit';
```

### Code block 2

```
let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
```

### Code block 3

```
let bucket: cloudStorage.StorageBucket = cloudStorage.bucket('bucket001-2wezr'); // 指定bucket001-2wezr实例
```
