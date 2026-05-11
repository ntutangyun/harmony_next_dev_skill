# 更新企业公钥证书

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-update_

updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>	使用Promise方式更新证书。
开发步骤

导入模块。

import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

先调用接口getAuthChallenge，获取挑战值并签名，传入挑战值的签名和企业公钥证书，再调用接口updateEnterpriseCertificate，更新企业公钥证书。

function testUpdateEnterpriseCertificate() {
  // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
  let signature: Uint8Array = new Uint8Array([0]);
  // 在实际应用中，cert 应需替换为企业证书数据。
  let cert: Uint8Array = new Uint8Array([0]);
  recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
    console.info(`Succeeded in updating certificate.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
  });
}
挑战值签名
删除企业恢复密钥
