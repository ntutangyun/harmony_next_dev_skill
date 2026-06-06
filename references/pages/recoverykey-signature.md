# 挑战值签名

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature_

--BEGIN EC PARAMETERS-----\n" +
      "************\n" +
      "-----END EC PARAMETERS-----\n" +
      "-----BEGIN EC PRIVATE KEY-----\n" +
      "**********************************************************************"  +
      "-----END EC PRIVATE KEY-----";
    // 替换成企业的公钥
    let publicKey: string = "-----BEGIN PUBLIC KEY-----\n" +
      "****************************************************************\n" +
      "************************************************************\n" +
      "-----END PUBLIC KEY-----\n" +
      "-----BEGIN CERTIFICATE-----\n" +
      "****************************************************************\n" +
      "*******\n" +
      "-----END CERTIFICATE-----\n";
    let input1: cryptoFramework.DataBlob = { data };
    let signAlg = "ECC_BrainPoolP256r1|SHA256";
    let signer = cryptoFramework.createSign(signAlg);
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator("ECC_BrainPoolP256r1");
    let keyPair = await asyKeyGenerator.convertPemKey(publicKey, privateKey);
    await signer.init(keyPair.priKey);
    let signData = await signer.sign(input1);
    // 对签名的数据进行验签
    let verifier = cryptoFramework.createVerify(signAlg);
    verifier.initSync(keyPair.pubKey);
    let res = verifier.verifySync(input1, signData);
    console.info(`signature verify result: ${res}.`);
    return signData.data;
  }


  public static async sign(data: Uint8Array) : Promise<Uint8Array> {
    let signInnerResult = await SignUtil.signInner(data);
    let result: Uint8Array = new Uint8Array(64);


    let index = 0;
    let length = 0;
    let offset = 0;
    while (index < signInnerResult.length) {
      if (signInnerResult[index] === 0x02) {
        length = index + 1 < signInnerResult.length ? signInnerResult[index + 1] : 0;
        let end = index + 2 + length;
        if (end <= signInnerResult.length) {
          let copyArr = signInnerResult.subarray(end - 32, end);
          result.set(copyArr, offset);
          offset += 32;
        }
        index += 34;
      } else {
        index++;
      }
    }
    return result;
  }
}
生成挑战值的签名（更新企业公钥）

在更新企业公钥证书场景下，先获取挑战值，将下面方法中的certificate和ecPubNewStrBase64替换为企业的新证书和新公钥，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { SignUtil } from './SignUtil';


async function updateEnterpriseCertificate() {
  // 替换成企业的新证书
  const certificate =
    "-----BEGIN CERTIFICATE-----\n" +
      "****************************************************************\n" +
      "*******\n" +
      "-----END CERTIFICATE-----\n";


  const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
  const buffer = new ArrayBuffer(4);
  const view = new DataView(buffer);
  view.setUint32(0, 0x98010000);
  const command: Uint8Array = new Uint8Array(buffer);
  // 替换成企业的新公钥
  const ecPubNewStrBase64 =
    "****************************************************************\n";
  let publicKey: Uint8Array = base64ToStringUint8Array(ecPubNewStrBase64);
  publicKey = publicKey.subarray(publicKey.length - 65, publicKey.length);
  let signData: Uint8Array = new Uint8Array(challenge.length + command.length + publicKey.length);
  signData.set(challenge, 0);
  signData.set(command, challenge.length);
  signData.set(publicKey, challenge.length + command.length);
  let signature: Uint8Array = await SignUtil.sign(signData);


  const cert: Uint8Array = stringToUint8(certificate!);
  recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
    console.info(`Succeeded in updating certificate.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}.`);
  });
}


function stringToUint8(str: string): Uint8Array {
  let result: Uint8Array = new Uint8Array([]);
  try {
    result = new util.TextEncoder('utf-8').encodeInto(str);
  } catch (error) {
    console.error(`Failed to encode to uint8. Code: ${error.code}, message: ${error.message}`);
  }
  return result;
}


function base64ToStringUint8Array(base64String: string): Uint8Array {
  let base64 = new util.Base64Helper();
  let uint8Array = base64.decodeSync(base64String, util.Type.BASIC);
  return uint8Array;
}
生成挑战值的签名（删除企业恢复密钥）

在删除企业恢复密钥场景下，先获取挑战，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { SignUtil } from './SignUtil';


async function deleteEnterpriseRecoveryKey() {
  const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
  let signResult = await SignUtil.sign(challenge);
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId = await accountManager.getOsAccountLocalId();
  recoveryKey.deleteEnterpriseRecoveryKey(userId, signResult).then((ret: number) => {
    console.info(`Succeeded in deleting enterprise recovery key.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete enterprise recovery key. Code: ${err.code}, message: ${err.message}.`);
  });
}
获取挑战值
更新企业公钥证书
