# 关闭指定生物类型认证能力

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-del-bio_

场景介绍

当用户期望关闭指定生物特征认证能力时，可以通过指定已开通的生物特征信息，关闭指定的生物类型认证能力。

约束与限制

本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口checkConfirmUITextFormat查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。

本功能需企业开发者应用服务器端完成接口接入，以配合端云协同认证流程。

业务流程

接口说明

接口及使用方法请参见API参考。

接口名	描述
disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>	解绑指定生物类型认证能力。

开发步骤

导入trustedAuthentication 和相关依赖模块。

import { resourceManager } from '@kit.LocalizationKit'
import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { trustedAuthentication } from '@kit.DeviceSecurityKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起解绑指定生物类型认证能力请求。

发起关闭指定生物类型认证能力请求前，需从服务器获取当前账号在设置数字盾密码时获取的authID。

调用数字盾解绑指定生物类型认证能力接口发起关闭对应生物类型认证能力申请。

async disableTrustedBioAuthentication(assetName: string, authType: number): Promise<void> {
  try {
    let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
    let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray); // 实际填充为从服务器获取到的账号对应的credentialID值
    await trustedAuthentication.disableTrustedBioAuthentication(credentialID, authType);
    hilog.info(0x0000, 'testTag', 'unBound success');
  } catch (error) {
    hilog.error(0x0000, 'testTag', 'unBound fail', JSON.stringify(error));
    throw new Error('unBound fail' + (error as BusinessError).message);
  }
}

在接收到端侧解绑成功结果后，开发者需要同步将服务器绑定的生物特征信息解绑。

## Code blocks

### Code block 1

```
import { resourceManager } from '@kit.LocalizationKit'
import { huks } from '@kit.UniversalKeystoreKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { trustedAuthentication } from '@kit.DeviceSecurityKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';
```

### Code block 2

```
async disableTrustedBioAuthentication(assetName: string, authType: number): Promise<void> {
  try {
    let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
    let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray); // 实际填充为从服务器获取到的账号对应的credentialID值
    await trustedAuthentication.disableTrustedBioAuthentication(credentialID, authType);
    hilog.info(0x0000, 'testTag', 'unBound success');
  } catch (error) {
    hilog.error(0x0000, 'testTag', 'unBound fail', JSON.stringify(error));
    throw new Error('unBound fail' + (error as BusinessError).message);
  }
}
```
