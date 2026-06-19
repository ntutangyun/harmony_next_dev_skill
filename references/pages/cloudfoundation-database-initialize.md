# 初始化数据库访问

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-initialize_

约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已引入对象类型文件。

操作步骤

设置云数据库配置项。

在“entry/src/main/module.json5”文件中添加网络权限。

"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET"
  }
]

（可选）如果存在需要登录应用才能操作数据库的场景（如新增或删除数据），您需要执行如下操作：

通过AuthProvider获取用户凭据。

调用init()方法进行初始化时，传入获取的凭据。

在业务代码中，使用AGC开发平台上创建的存储区“QuickStartDemo”类初始化DatabaseZone。

import { cloudDatabase } from '@kit.CloudFoundationKit';

let databaseZone = cloudDatabase.zone('QuickStartDemo');

说明

cloudDatabase.zone方法接收的入参为“存储区名称”，即cloudDBZoneName，请参见新增存储区章节。

存储区最多创建4个，超过4个会导致云数据库访问失败。

如果需要使用数据库查询方法，可以使用类（此处以BookInfo为例）初始化DatabaseQuery。

import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的相对路径

let condition = new cloudDatabase.DatabaseQuery(BookInfo);

说明

后续“databaseZone”、“condition”都需要在每个查询中独立使用，可以参考此章节创建，下文代码中不再重复创建的操作。

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
import { cloudDatabase } from '@kit.CloudFoundationKit';

let databaseZone = cloudDatabase.zone('QuickStartDemo');
```

### Code block 3

```
import { BookInfo } from 'xx/BookInfo'; // xx是BookInfo文件的相对路径

let condition = new cloudDatabase.DatabaseQuery(BookInfo);
```
