# 获取解密硬盘数据的企业恢复密钥

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyfordecryptdata_

企业恢复密钥仅可被获取一次，获取到企业恢复密钥后，可在持有企业私钥的设备上解密，并进行相应的存储。如果需要再次获取，需要先调用删除企业恢复密钥能力，再调用该能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>	使用Promise方式获取恢复密钥。
开发步骤

导入模块。

import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';

调用接口getEnterpriseRecoveryKey，传入需要获取企业恢复密钥的用户ID，获取企业恢复密钥。

async function testGetEnterpriseRecoveryKey() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
      console.info(`Succeeded in getting enterprise recovery key.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (e) {
    console.error(`Failed to testGetEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
  }
}
企业恢复密钥
获取重置锁屏密码的企业恢复密钥
