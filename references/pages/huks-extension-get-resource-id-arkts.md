# 获取资源ID(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-get-resource-id-arkts_

在外部密钥管理扩展场景下，资源ID用于标识外部密钥管理扩展的具体资源（如Ukey设备、容器、密钥等）。从API版本26.0.0开始，应用可通过getResourceId获取资源ID，并使用该资源ID执行密钥生成与导入导出、通用查询、PIN码认证及清除PIN码认证状态等后续操作。

开发步骤

准备提供者名称（providerName），建议包含厂商信息，全局唯一。长度最大为128字节。

构造必选参数：

通过HUKS_EXT_CRYPTO_TAG_ABILITY_NAME传入CryptoExtensionAbility名称。

通过HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME传入Bundle名称。

通过HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO传入厂商自定义的资源信息。

调用getResourceId获取资源ID。

开发案例

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 提供者名称，建议包含厂商信息，全局唯一，长度最大为128字节
let providerName: string = 'testProviderName';
// Ability名称
let abilityName: string = 'CryptoExtension';
// Bundle名称
let bundleName: string = 'com.example.cryptoapplication';
// 资源信息，格式和内容由厂商自定义
let resourceInfo: string = 'vendor_defined_resource_info';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function getResourceId(): Promise<string> {
  try {
    /* 1.构造必选参数 */
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: StringToUint8Array(abilityName)
      },
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME,
        value: StringToUint8Array(bundleName)
      },
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO,
        value: StringToUint8Array(resourceInfo)
      }
    ];

    /* 2.调用getResourceId */
    await huksExternalCrypto.getResourceId(providerName, extProperties)
      .then((resourceId) => {
        console.info(`promise: getResourceId success, resourceId: ${resourceId}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: getResourceId failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: getResourceId input arg invalid.');
  }
}

## Code blocks

### Code block 1

```
import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 提供者名称，建议包含厂商信息，全局唯一，长度最大为128字节
let providerName: string = 'testProviderName';
// Ability名称
let abilityName: string = 'CryptoExtension';
// Bundle名称
let bundleName: string = 'com.example.cryptoapplication';
// 资源信息，格式和内容由厂商自定义
let resourceInfo: string = 'vendor_defined_resource_info';

function StringToUint8Array(str: string) {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function getResourceId(): Promise<string> {
  try {
    /* 1.构造必选参数 */
    const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
        value: StringToUint8Array(abilityName)
      },
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_BUNDLE_NAME,
        value: StringToUint8Array(bundleName)
      },
      {
        tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_RESOURCE_INFO,
        value: StringToUint8Array(resourceInfo)
      }
    ];

    /* 2.调用getResourceId */
    await huksExternalCrypto.getResourceId(providerName, extProperties)
      .then((resourceId) => {
        console.info(`promise: getResourceId success, resourceId: ${resourceId}`);
      }).catch((error: BusinessError) => {
        console.error(`promise: getResourceId failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: getResourceId input arg invalid.');
  }
}
```
