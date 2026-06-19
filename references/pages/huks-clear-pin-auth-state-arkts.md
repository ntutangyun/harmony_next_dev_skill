# 清除Ukey PIN码认证状态(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-clear-pin-auth-state-arkts_

从API版本26.0.0开始，huksExternalCrypto提供清除Ukey PIN码认证状态功能接口。应用在密钥操作完成后或需要重置认证状态时，可以调用该接口清除指定资源的PIN码认证状态。具体的场景介绍及规格，请参考Ukey PIN码认证介绍及规格。

开发步骤

获取资源ID。可通过openAuthorizeDialog获取keyUri作为resourceId，或通过getResourceId获取外部密钥管理扩展的资源ID。

调用clearUkeyPinAuthState清除PIN码认证状态。

开发案例

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 清除PIN码认证状态
async function clearUkeyPinAuthState(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.clearUkeyPinAuthState(resourceId)
      .then(() => {
        console.info('promise: clearUkeyPinAuthState success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: clearUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: clearUkeyPinAuthState input arg invalid.');
  }
}

## Code blocks

### Code block 1

```
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 清除PIN码认证状态
async function clearUkeyPinAuthState(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.clearUkeyPinAuthState(resourceId)
      .then(() => {
        console.info('promise: clearUkeyPinAuthState success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: clearUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: clearUkeyPinAuthState input arg invalid.');
  }
}
```
