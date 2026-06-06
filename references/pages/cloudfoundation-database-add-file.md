# 引入对象类型文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-file_

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已新增对象类型。

已新增存储区。

操作步骤

将对象类型中导出的json格式文件命名为schema.json，拷贝到DevEco Studio项目的“AppScope/resources/rawfile”或者“entry/src/main/resources/rawfile”目录下。在编译构建过程中，AppScope目录下的资源文件会合入到模块的资源文件中，详细信息请参见资源分类。

按照AGC控制台上创建的对象类型“BookInfo”在代码工程中创建BookInfo.ets文件，文件内容参考以下代码。

说明

在AGC控制台创建的字段类型与ArkTS数据类型的匹配关系如下：

String、Text对应string。

Boolean对应boolean。

Byte、ByteArray对应Uint8Array。

Short、Integer、Long、Float、Double、IntAutoIncrement、LongAutoIncrement对应number。

Date对应Date。

import { cloudDatabase } from '@kit.CloudFoundationKit';


class BookInfo extends cloudDatabase.DatabaseObject{
  public naturalbase_ClassName(): string {
    return "BookInfo";
  }
  public id: number | undefined;
  public bookName: string | undefined;
  public author: string | undefined;
  public price: number | undefined;
  public borrowerId: number | undefined;
  public borrowerName: string | undefined;
  public borrowerTime: Date | undefined;
}


export { BookInfo };
新增存储区
初始化数据库访问
