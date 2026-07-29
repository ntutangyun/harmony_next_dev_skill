# 获取星闪合作设备集合信息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-cdsm-information_

场景介绍

从6.1.1(24)开始支持获取星闪合作设备集合信息。

合作设备集合是由多个成员设备协同提供特定服务的整体，例如一副星闪耳机包含左右两个耳机单元。当配对的外设属于某个合作设备集合时，通过getPairedDevices接口仅能获取该集合中首个配对的成员设备，无法直接获取其他成员设备信息。作为集合使用者，可通过主动查询或订阅通知的方式，获取该合作设备集合内所有成员设备的完整信息。

更多技术细节可参考星闪标准《星闪无线通信系统 基础应用层 合作设备集合管理》。

接口说明

提供获取合作设备集合信息的方式，主动查询和订阅信息变化。

接口名	描述
createCdsmClient(address: string): CdsmClient	创建合作设备集合客户端实例。
getCdsmInfo(): CdsmInfo	主动查询合作设备集合里所有成员设备的信息。
onCdsmInfoChange(callback: Callback<CdsmInfo>): void	订阅远端设备合作设备集合信息变化事件。使用callback异步回调。
offCdsmInfoChange(callback?: Callback<CdsmInfo>): void	取消订阅远端设备合作设备集合信息变化事件。使用callback异步回调。

开发步骤

导入相关模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { cdsm, manager, remoteDevice } from '@kit.NearLinkKit';

创建合作设备集合客户端实例，参数addr是通过getPairedDevices获取的设备地址，并且此设备是合作设备集合的成员设备。

@State deviceAddress: string = '00:11:22:33:AA:FF';
cdsmClient: cdsm.CdsmClient | null = null;
// ...
try {
  this.cdsmClient = cdsm.createCdsmClient(this.deviceAddress);
  hilog.info(this.domainId, this.logTag, `Create CDSM client: ${JSON.stringify(this.cdsmClient)}`);
  // ...
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

主动查询合作设备集合里所有成员设备的信息。

try {
  if (this.cdsmClient) {
    let cdsmInformation: cdsm.CdsmInfo = this.cdsmClient.getCdsmInfo();
    hilog.info(this.domainId, this.logTag, `CDSM info: ${JSON.stringify(cdsmInformation)}`);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

通过注册的方式订阅合作设备集合成员设备的信息变化。

let cdsmCallback: (data: cdsm.CdsmInfo) => void = (data: cdsm.CdsmInfo) => {
  hilog.info(this.domainId, this.logTag, `CDSM info changed: ${JSON.stringify(data)}`);
  // ...
};
try {
  if (this.cdsmClient) {
    this.cdsmClient.onCdsmInfoChange(cdsmCallback);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

取消订阅合作设备集合成员设备的信息变化。

try {
  if (this.cdsmClient) {
    this.cdsmClient.offCdsmInfoChange();
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
import { cdsm, manager, remoteDevice } from '@kit.NearLinkKit';
```

### Code block 2

```
@State deviceAddress: string = '00:11:22:33:AA:FF';
cdsmClient: cdsm.CdsmClient | null = null;
// ...
try {
  this.cdsmClient = cdsm.createCdsmClient(this.deviceAddress);
  hilog.info(this.domainId, this.logTag, `Create CDSM client: ${JSON.stringify(this.cdsmClient)}`);
  // ...
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 3

```
try {
  if (this.cdsmClient) {
    let cdsmInformation: cdsm.CdsmInfo = this.cdsmClient.getCdsmInfo();
    hilog.info(this.domainId, this.logTag, `CDSM info: ${JSON.stringify(cdsmInformation)}`);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 4

```
let cdsmCallback: (data: cdsm.CdsmInfo) => void = (data: cdsm.CdsmInfo) => {
  hilog.info(this.domainId, this.logTag, `CDSM info changed: ${JSON.stringify(data)}`);
  // ...
};
try {
  if (this.cdsmClient) {
    this.cdsmClient.onCdsmInfoChange(cdsmCallback);
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 5

```
try {
  if (this.cdsmClient) {
    this.cdsmClient.offCdsmInfoChange();
    // ...
  }
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```
