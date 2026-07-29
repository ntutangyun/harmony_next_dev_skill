# 属性设置(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-set-property-arkts_

从API版本26.0.0开始，huksExternalCrypto提供设置属性的功能接口。应用可通过setProperty接口设置指定资源的属性值，由CryptoExtensionAbility实现方提供，推荐使用GMT 0016-2023中定义的SKF接口名作为属性ID。具体的场景介绍及规格，请参考通用查询介绍及规格。

开发步骤

获取资源ID。可通过openAuthorizeDialog获取keyUri作为resourceId，或通过getResourceId获取外部密钥管理扩展的资源ID。

调用setProperty设置属性值。

开发案例

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function setProperty(resourceId: string, propertyId: string): Promise<void> {
  try {
    await huksExternalCrypto.setProperty(resourceId, propertyId)
      .then(() => {
        console.info('promise: setProperty success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: setProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: setProperty input arg invalid.');
  }
}

## Code blocks

### Code block 1

```
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function setProperty(resourceId: string, propertyId: string): Promise<void> {
  try {
    await huksExternalCrypto.setProperty(resourceId, propertyId)
      .then(() => {
        console.info('promise: setProperty success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: setProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: setProperty input arg invalid.');
  }
}
```
