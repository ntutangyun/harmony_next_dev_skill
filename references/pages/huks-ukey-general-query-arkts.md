# 通用查询(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-general-query-arkts_

从API 22开始，huksExternalCrypto提供通用查询功能接口。该接口可以用于从UKey中获取设备标识、App标识以及其他通用属性信息，完成属性查询操作。具体的场景介绍请参考获取属性介绍及规格。

开发步骤

获取属性

通过证书管理系统能力提供的证书选择接口获取keyUri作为resourceId，并打开资源。

构造输入参数propertyId和可选输入参数param。

调用getProperty获取属性信息。

开发案例

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getProperty(): Promise<Array<huksExternalCrypto.HuksExternalCryptoParam>> {
  // 1. 获取resourceId, 假设获取的resourceId如下，并已经打开该资源
  const testResourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });

  // 2. 构造输入参数propertyId和可选参数param
  let propertyId = "SKF_EnumDev";
  const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

  // 3. 调用getProperty获取属性信息
  console.info(`promise: await huksExternalCrypto getProperty`);
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
      }).catch((error: BusinessError) => {
        console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
  return extProperties;
}

## Code blocks

### Code block 1

```
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getProperty(): Promise<Array<huksExternalCrypto.HuksExternalCryptoParam>> {
  // 1. 获取resourceId, 假设获取的resourceId如下，并已经打开该资源
  const testResourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });

  // 2. 构造输入参数propertyId和可选参数param
  let propertyId = "SKF_EnumDev";
  const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

  // 3. 调用getProperty获取属性信息
  console.info(`promise: await huksExternalCrypto getProperty`);
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
      }).catch((error: BusinessError) => {
        console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
      })
  } catch (error) {
    console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
  }
  return extProperties;
}
```
