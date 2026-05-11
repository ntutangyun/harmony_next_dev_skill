# 密钥导出(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-arkts_

业务需要获取持久化存储的非对称密钥的公钥时使用，当前支持ECC/RSA/ED25519/X25519/SM2的公钥导出。

说明

轻量级智能穿戴仅支持RSA公钥导出。

从API 23开始支持群组密钥特性。

开发步骤

指定密钥别名，密钥别名命名规范参考密钥生成介绍及算法规格。

调用接口exportKeyItem，传入参数keyAlias和options。options为预留参数，当前可传入空。

返回值为HuksReturnResult类型对象，获取的公钥明文在outData字段中，以标准的X.509规范的DER格式封装，具体请参考公钥材料格式。

import { huks } from '@kit.UniversalKeystoreKit';


/* 1. 设置密钥别名 */
let keyAlias = 'keyAlias';
/* option对象传空 */
let emptyOptions: huks.HuksOptions = {
properties: []
};


let properties1: huks.HuksParam[] = [
  {
    tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS_ALG_DH
  },
  {
    tag: huks.HuksTag.HUKS_TAG_PURPOSE,
    value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
  },
  {
    tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
    value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048
  }
];


let huksOptions: huks.HuksOptions = {
  properties: properties1,
  inData: new Uint8Array([])
}


/* 3.生成密钥 */
function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}


async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
  console.info(`enter promise generateKeyItem`);
  try {
    await generateKeyItem(keyAlias, huksOptions)
      .then((data) => {
        console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
      })
      .catch((error: Error) => {
        console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
      });
    return 'Success';
  } catch (error) {
    console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
    return 'Failed';
  }
}


async function testGenKey(): Promise<string> {
  let ret = await publicGenKeyFunc(keyAlias, huksOptions);
  return ret;
}


function check(): string {
  try {
    /* 1. 生成密钥 */
    testGenKey()
    /* 2. 导出密钥 */
    huks.exportKeyItem(keyAlias, emptyOptions, (error, data) => {
      if (error) {
        console.error(`callback: exportKeyItem failed, ` + error);
      } else {
        console.info(`callback: exportKeyItem success, data = ${JSON.stringify(data)}`);
      }
    });
    return 'Success';
  } catch (error) {
    console.error(`callback: exportKeyItem input arg invalid, ${JSON.stringify(error)}`);
    return 'Failed';
  }
}
KeyExport.ets
密钥导出
密钥导出(C/C++)
