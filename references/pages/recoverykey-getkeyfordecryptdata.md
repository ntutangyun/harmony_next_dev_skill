# 获取解密硬盘数据的企业恢复密钥

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyfordecryptdata_

场景介绍

为应用提供获取企业恢复密钥的能力，在企业公钥证书配置成功后，可直接获取企业恢复密钥，用于解密已加密的硬盘数据。

说明

企业恢复密钥仅可被获取一次，获取到企业恢复密钥后，可在持有企业私钥的设备上解密，并进行相应的存储。如果需要再次获取，需要先调用删除企业恢复密钥能力，再调用该能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>	使用Promise方式获取企业恢复密钥。

开发步骤

导入模块。

import { buffer } from '@kit.ArkTS';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

调用接口getEnterpriseRecoveryKey，传入需要获取企业恢复密钥的用户ID，获取企业恢复密钥。

const TAG: string = 'EnterpriseRecoveryKey_GetRecoveryKey';
const DOMAIN: number = 0x0000;

/**
 * 获取解密硬盘数据的企业恢复密钥。使用Promise异步回调。
 */
function getEnterpriseRecoveryKey() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.getOsAccountLocalId().then((userId: number) => {
    hilog.info(DOMAIN, TAG, `getEnterpriseRecoveryKey userId: ${userId}.`);
    recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key.`);
      hilog.info(DOMAIN, TAG,
        `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
          .toString('hex')}`);
      hilog.info(DOMAIN, TAG,
        `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
      hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
      hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
    });
  });
}

## Code blocks

### Code block 1

```
import { buffer } from '@kit.ArkTS';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'EnterpriseRecoveryKey_GetRecoveryKey';
const DOMAIN: number = 0x0000;

/**
 * 获取解密硬盘数据的企业恢复密钥。使用Promise异步回调。
 */
function getEnterpriseRecoveryKey() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.getOsAccountLocalId().then((userId: number) => {
    hilog.info(DOMAIN, TAG, `getEnterpriseRecoveryKey userId: ${userId}.`);
    recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key.`);
      hilog.info(DOMAIN, TAG,
        `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
          .toString('hex')}`);
      hilog.info(DOMAIN, TAG,
        `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
      hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
      hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
    });
  });
}
```
