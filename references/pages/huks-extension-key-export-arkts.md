# 公钥导出(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-extension-key-export-arkts_

从API版本26.0.0开始，在外部密钥管理扩展场景下，公钥导出能力支持从扩展设备导出指定密钥的公钥。导出的公钥可用于证书申请、密钥协商等场景。

具体的场景介绍请参考密钥生成与导入导出介绍。

开发步骤

通过openAuthorizeDialog获取keyUri作为resourceId，或通过getResourceId获取外部密钥管理扩展的资源ID。

调用openResource打开资源。

调用exportKeyItem导出公钥，密钥参数中需指定HUKS_TAG_KEY_CLASS为HUKS_KEY_CLASS_EXTENSION，表示该密钥由外部密钥管理扩展管理。

调用closeResource关闭资源。

开发案例

import { huks, huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.openResource(resourceId)
      .then(() => {
        console.info('promise: openResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: openResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: openResource input arg invalid.');
  }
}

async function exportPublicKey(keyAlias: string): Promise<Uint8Array> {
  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    const exportProperties: Array<huks.HuksParam> = [
      {
        tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
        value: huks.HuksKeyClass.HUKS_KEY_CLASS_EXTENSION
      }
    ];
    const exportOptions: huks.HuksOptions = {
      properties: exportProperties
    };
    await huks.exportKeyItem(keyAlias, exportOptions)
      .then((data) => {
        publicKey = data.outData as Uint8Array;
        console.info('promise: exportKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: exportKeyItem input arg invalid.');
  }
  return publicKey;
}

async function closeResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.closeResource(resourceId)
      .then(() => {
        console.info('promise: closeResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: closeResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: closeResource input arg invalid.');
  }
}

async function extensionKeyExport(): Promise<Uint8Array> {
  /* 1.准备资源ID */
  const resourceId = 'your_resource_id';

  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    /* 2.打开资源 */
    await openResource(resourceId);

    /* 3.导出公钥 */
    publicKey = await exportPublicKey(resourceId);
    console.info(`promise: public key length: ${publicKey.length}`);

    /* 4.关闭资源 */
    await closeResource(resourceId);

    console.info('promise: extensionKeyExport completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyExport input arg invalid.');
  }
  return publicKey;
}

## Code blocks

### Code block 1

```
import { huks, huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function openResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.openResource(resourceId)
      .then(() => {
        console.info('promise: openResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: openResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: openResource input arg invalid.');
  }
}

async function exportPublicKey(keyAlias: string): Promise<Uint8Array> {
  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    const exportProperties: Array<huks.HuksParam> = [
      {
        tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
        value: huks.HuksKeyClass.HUKS_KEY_CLASS_EXTENSION
      }
    ];
    const exportOptions: huks.HuksOptions = {
      properties: exportProperties
    };
    await huks.exportKeyItem(keyAlias, exportOptions)
      .then((data) => {
        publicKey = data.outData as Uint8Array;
        console.info('promise: exportKeyItem success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: exportKeyItem input arg invalid.');
  }
  return publicKey;
}

async function closeResource(resourceId: string): Promise<void> {
  try {
    await huksExternalCrypto.closeResource(resourceId)
      .then(() => {
        console.info('promise: closeResource success.');
      }).catch((error: BusinessError) => {
        console.error(`promise: closeResource failed, errCode : ${error.code}, errMsg : ${error.message}`);
      });
  } catch (error) {
    console.error('promise: closeResource input arg invalid.');
  }
}

async function extensionKeyExport(): Promise<Uint8Array> {
  /* 1.准备资源ID */
  const resourceId = 'your_resource_id';

  let publicKey: Uint8Array = new Uint8Array([]);
  try {
    /* 2.打开资源 */
    await openResource(resourceId);

    /* 3.导出公钥 */
    publicKey = await exportPublicKey(resourceId);
    console.info(`promise: public key length: ${publicKey.length}`);

    /* 4.关闭资源 */
    await closeResource(resourceId);

    console.info('promise: extensionKeyExport completed successfully.');
  } catch (error) {
    console.error('promise: extensionKeyExport input arg invalid.');
  }
  return publicKey;
}
```
