# 获取云侧文件的元数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-getmetadata_

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已初始化存储实例。

已上传指定文件至云侧。

操作步骤

调用StorageBucket.getMetadata获取指定云侧文件的元数据信息。

完整示例代码如下：

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();


@Component
export struct testPage {
  build() {
  }


  // 获取元数据
  getMetaData() {
    // 获取云存储默认实例中screenshot/screenshot_20250115_155321.jpg文件的元数据信息
    storageBucket.getMetadata('screenshot/screenshot_20250115_155321.jpg').then((metadata: cloudStorage.Metadata) => {
      hilog.info(0x0000, 'testTag', `Succeeded in getting metadata: ${JSON.stringify(metadata)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `Failed to get metadata, code: ${err.code}, message: ${err.message}`);
    })
  }
}
获取云侧文件列表
设置云侧文件的元数据
