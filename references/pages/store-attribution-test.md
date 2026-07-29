# 接入调试功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-test_

应用归因服务为开发者提供接入调试能力，支持开发者在接入过程中进行自助调试，通过调用调试接口验证接入的准确性及归因结果回传等基础能力，从而提升接入效率。

场景介绍

应用归因服务接入调试功能支持的场景如下：

校验接口调用是否准确

调用调试接口，校验接口请求及业务逻辑，如参数校验、签名校验等，并提示相应错误码，支持开发者自行发现问题。

主动触发归因接口回传

开发者设置归因数据后，调用调试接口主动、实时触发归因结果回传，验证完整的归因流程。

接口说明

应用归因服务接入调试功能提供以下接口，具体API说明详见接口文档。

接口名	描述
validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void>	验证归因来源接口，用于媒体App/分发平台验证adSourceInfo入参的合法性。
setPostback(postbackInfo: PostbackInfo): Promise<void>	设置归因结果回传接口，用于应用生态伙伴： - 验证triggerData是否合法。 - 设置调试使用的回传数据。
flushPostbacks(adTechId: string): Promise<void>	主动、实时触发归因结果回传接口，用于应用生态伙伴验证接收及处理回传的逻辑是否正确。

开发步骤

[h2]验证归因来源

导入相关模块。

import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { SignUtil } from '../common/utils/SignUtil';
import { util } from '@kit.ArkTS';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';

构造参数，入参为AdSourceInfo、publickey。

// 应用归因服务云平台注册角色时提供的公钥和对应的私钥。
let privateKey: string = '';
let publicKey: string = '';
// 可以使用虚拟的adTechId，长度固定为8个字符。
let adTechId: string = '1******8';
// 广告平台创建的广告任务ID。
// 自API 12起，campaignId长度小于等于6个字符
// 自API 22起，campaignId长度小于等于9个字符
let campaignId: string = '';
let osApiVersion: number = deviceInfo.sdkApiVersion;
if (osApiVersion >= 22) {
    campaignId = '1*******9';
} else {
    campaignId = '1****6';
}
// 开发者应用上架华为应用市场的appId，不带C
let destinationId: string = '1******8';
// 归因监测平台id
let mmpIds: string[] = ['1******8', '2******9'];
// 分发平台关注的业务信息
let serviceTag: string = 'testServiceTag';
// 用于计算签名的随机数，不带'-'
let nonce: string = util.generateRandomUUID().replace(/-/g, '');
// 时间戳.
let timestamp: number = Date.now()
let adSourceInfo: attributionTestManager.AdSourceInfo = {
    adTechId: adTechId,
    campaignId: campaignId,
    destinationId: destinationId,
    // 曝光.
    sourceType: attributionTestManager.SourceType.IMPRESSION,
    mmpIds: mmpIds,
    serviceTag: serviceTag,
    nonce: nonce,
    timestamp: timestamp,
    // 签名值.
    signature: await SignUtil.getSign(this.getUIContext(),
        SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp),
        privateKey)
};

调用attributionTestManager.validateSource方法验证归因来源。

try {
    // ...
    await attributionTestManager.validateSource(adSourceInfo, publicKey);
    hilog.info(0, TAG, 'validateSource success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `validateSource error. code is ${error.code}, message is ${error.message}`);
    // ...
}

[h2]设置归因结果回传

导入相关模块。

import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';

构造参数，入参为PostbackInfo。

// 广告平台创建的广告任务ID。
// 自API 12起，campaignId长度小于等于6个字符
// 自API 22起，campaignId长度小于等于9个字符
let campaignId: string = '';
let osApiVersion: number = deviceInfo.sdkApiVersion;
if (osApiVersion >= 22) {
    campaignId = '1*******9';
} else {
    campaignId = '1****6';
}
let postbackInfo: attributionTestManager.PostbackInfo = {
    // 分发平台对应的归因角色ID，在应用归因云侧注册应用生态伙伴角色时，由应用归因服务分配
    adTechId: '1******8',
    campaignId: campaignId,
    // 开发者应用上架华为应用市场的appId，不带C
    destinationId: '1******8',
    // 媒体应用id
    sourceId: '1******8',
    // 分发平台关注的业务信息
    serviceTag: 'testServiceTag',
    triggerData: 123,
    businessScene: 5,
    // 需要回传服务器地址
    postbackUrl: 'xxx.com'
};

调用attributionTestManager.setPostback方法设置归因结果回传数据。

try {
    // ...
    await attributionTestManager.setPostback(postbackInfo);
    hilog.info(0, TAG, 'setPostback success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `setPostback error. code is ${error.code}, message is ${error.message}`);
    // ...
}

[h2]触发归因结果回传

导入相关模块。

import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';

构造参数adTechId。

let adTechId: string = '1******8';

调用attributionTestManager.flushPostbacks方法触发归因结果回传。

try {
    // ...
    await attributionTestManager.flushPostbacks(adTechId);
    hilog.info(0, TAG, 'flushPostbacks success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `flushPostbacks error. code is ${error.code}, message is ${error.message}`);
    // ...
}

## Code blocks

### Code block 1

```
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { SignUtil } from '../common/utils/SignUtil';
import { util } from '@kit.ArkTS';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';
```

### Code block 2

```
// 应用归因服务云平台注册角色时提供的公钥和对应的私钥。
let privateKey: string = '';
let publicKey: string = '';
// 可以使用虚拟的adTechId，长度固定为8个字符。
let adTechId: string = '1******8';
// 广告平台创建的广告任务ID。
// 自API 12起，campaignId长度小于等于6个字符
// 自API 22起，campaignId长度小于等于9个字符
let campaignId: string = '';
let osApiVersion: number = deviceInfo.sdkApiVersion;
if (osApiVersion >= 22) {
    campaignId = '1*******9';
} else {
    campaignId = '1****6';
}
// 开发者应用上架华为应用市场的appId，不带C
let destinationId: string = '1******8';
// 归因监测平台id
let mmpIds: string[] = ['1******8', '2******9'];
// 分发平台关注的业务信息
let serviceTag: string = 'testServiceTag';
// 用于计算签名的随机数，不带'-'
let nonce: string = util.generateRandomUUID().replace(/-/g, '');
// 时间戳.
let timestamp: number = Date.now()
let adSourceInfo: attributionTestManager.AdSourceInfo = {
    adTechId: adTechId,
    campaignId: campaignId,
    destinationId: destinationId,
    // 曝光.
    sourceType: attributionTestManager.SourceType.IMPRESSION,
    mmpIds: mmpIds,
    serviceTag: serviceTag,
    nonce: nonce,
    timestamp: timestamp,
    // 签名值.
    signature: await SignUtil.getSign(this.getUIContext(),
        SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp),
        privateKey)
};
```

### Code block 3

```
try {
    // ...
    await attributionTestManager.validateSource(adSourceInfo, publicKey);
    hilog.info(0, TAG, 'validateSource success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `validateSource error. code is ${error.code}, message is ${error.message}`);
    // ...
}
```

### Code block 4

```
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';
```

### Code block 5

```
// 广告平台创建的广告任务ID。
// 自API 12起，campaignId长度小于等于6个字符
// 自API 22起，campaignId长度小于等于9个字符
let campaignId: string = '';
let osApiVersion: number = deviceInfo.sdkApiVersion;
if (osApiVersion >= 22) {
    campaignId = '1*******9';
} else {
    campaignId = '1****6';
}
let postbackInfo: attributionTestManager.PostbackInfo = {
    // 分发平台对应的归因角色ID，在应用归因云侧注册应用生态伙伴角色时，由应用归因服务分配
    adTechId: '1******8',
    campaignId: campaignId,
    // 开发者应用上架华为应用市场的appId，不带C
    destinationId: '1******8',
    // 媒体应用id
    sourceId: '1******8',
    // 分发平台关注的业务信息
    serviceTag: 'testServiceTag',
    triggerData: 123,
    businessScene: 5,
    // 需要回传服务器地址
    postbackUrl: 'xxx.com'
};
```

### Code block 6

```
try {
    // ...
    await attributionTestManager.setPostback(postbackInfo);
    hilog.info(0, TAG, 'setPostback success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `setPostback error. code is ${error.code}, message is ${error.message}`);
    // ...
}
```

### Code block 7

```
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
// ...
import { attributionTestManager } from '@kit.AppGalleryKit';
```

### Code block 8

```
let adTechId: string = '1******8';
```

### Code block 9

```
try {
    // ...
    await attributionTestManager.flushPostbacks(adTechId);
    hilog.info(0, TAG, 'flushPostbacks success.');
    // ...
} catch (error) {
    hilog.error(0, TAG, `flushPostbacks error. code is ${error.code}, message is ${error.message}`);
    // ...
}
```
