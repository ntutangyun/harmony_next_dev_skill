# 查询是否支持星闪

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-issupported_

场景介绍

从6.1.0(23)版本开始，新增查询是否支持星闪的能力。由于并非所有设备都支持星闪，使用星闪相关功能前可以主动查询当前设备是否支持星闪。

接口说明

提供查询当前设备是否支持星闪的方式。

接口名	描述
isNearLinkSupported(): boolean	主动查询当前设备是否支持星闪。

开发步骤

说明

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，查看当前设备是否支持星闪。

如果在不支持星闪的设备上调用星闪相关接口，可能会返回801错误码。

导入相关模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { manager } from '@kit.NearLinkKit';

发起当前设备是否支持星闪的状态查询。

try {
  let supported: boolean = manager.isNearLinkSupported();
  // ...
  if (supported) {
    hilog.info(this.domainId, this.logTag, `NearLink is supported on this device.`);
    // ...
  } else {
    hilog.info(this.domainId, this.logTag, `NearLink is not supported on this device.`);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { manager } from '@kit.NearLinkKit';
```

### Code block 2

```
try {
  let supported: boolean = manager.isNearLinkSupported();
  // ...
  if (supported) {
    hilog.info(this.domainId, this.logTag, `NearLink is supported on this device.`);
    // ...
  } else {
    hilog.info(this.domainId, this.logTag, `NearLink is not supported on this device.`);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```
