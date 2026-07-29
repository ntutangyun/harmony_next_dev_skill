# 获取重置锁屏密码的企业恢复密钥

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-getkeyforresetpin_

场景介绍

为企业用户提供获取企业恢复密钥的能力，可以在用户忘记锁屏密码时，使用该企业恢复密钥重置用户的锁屏密码。

接口说明

详细接口说明可参考接口文档。

接口名	描述
verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>	使用Promise方式验证企业用户身份。
verifyUserByDialog(userId: number): Promise<void>	通过Dialog弹框验证企业用户身份。
getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>	使用Promise方式获取用于重置锁屏密码的企业恢复密钥。

开发步骤

导入模块。

import { buffer } from '@kit.ArkTS';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

通过验证锁屏密码，获取重置锁屏密码的恢复密钥。调用接口verifyUserIdentityEnterprise验证用户的锁屏密码，需提供用户ID、用户类型及用户锁屏密码，并在30秒内调用接口getEnterpriseRecoveryKeyForResettingPin以获取用于重置锁屏密码的企业恢复密钥。若超时后调用，系统会返回异常代码1014400001。

const TAG: string = 'EnterpriseRecoveryKey_ResetPinCodeRecoveryKey';
const DOMAIN: number = 0x0000;

/**
 * 通过验证锁屏密码，获取重置锁屏密码的恢复密钥。使用Promise异步回调。
 * @param pinCode 用户输入的锁屏密码
 */
async function testGetEnterpriseRecoveryKeyForPin(pinCode: string) {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
    hilog.info(DOMAIN, TAG, `getOsAccountType,userId: ${userId}, accountType: ${accountType}`);
    let userType: number = accountType.valueOf();

    recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in verifying user identity.`);
      recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
        .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
          hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key for resetting pin.`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
              .toString('hex')}`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG,
            `Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
        })
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to verify user identity. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to getEnterpriseRecoveryKeyForPin. Code: ${e.code}, message: ${e.message}`);
  }
}

通过弹框验证锁屏密码，获取重置锁屏密码的恢复密钥。调用接口verifyUserByDialog，通过Dialog弹框在5分钟内输入锁屏密码，点击确认后，并在30秒内调用接口getEnterpriseRecoveryKeyForResettingPin以获取用于重置锁屏密码的企业恢复密钥。若超时后调用，系统会返回异常代码1014400001。

const TAG: string = 'EnterpriseRecoveryKey_ResetPinCodeRecoveryKey';
const DOMAIN: number = 0x0000;

// ...
/**
 * 通过弹框验证锁屏密码，获取重置锁屏密码的恢复密钥。使用Promise异步回调。
 */
async function testGetEnterpriseRecoveryKeyForPinByDialog() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
    hilog.info(DOMAIN, TAG, `getOsAccountType,userId: ${userId}, accountType: ${accountType}`);
    let userType: number = accountType.valueOf();

    recoveryKey.verifyUserByDialog(userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in verifying user identity by dialog.`);
      recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
        .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
          hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key for resetting pin.`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
              .toString('hex')}`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG,
            `Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
        })
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to verify user identity by dialog. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG,
      `Failed to getEnterpriseRecoveryKeyForPinByDialog. Code: ${e.code}, message: ${e.message}`);
  }
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
const TAG: string = 'EnterpriseRecoveryKey_ResetPinCodeRecoveryKey';
const DOMAIN: number = 0x0000;

/**
 * 通过验证锁屏密码，获取重置锁屏密码的恢复密钥。使用Promise异步回调。
 * @param pinCode 用户输入的锁屏密码
 */
async function testGetEnterpriseRecoveryKeyForPin(pinCode: string) {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
    hilog.info(DOMAIN, TAG, `getOsAccountType,userId: ${userId}, accountType: ${accountType}`);
    let userType: number = accountType.valueOf();

    recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in verifying user identity.`);
      recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
        .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
          hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key for resetting pin.`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
              .toString('hex')}`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG,
            `Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
        })
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG, `Failed to verify user identity. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to getEnterpriseRecoveryKeyForPin. Code: ${e.code}, message: ${e.message}`);
  }
}
```

### Code block 3

```
const TAG: string = 'EnterpriseRecoveryKey_ResetPinCodeRecoveryKey';
const DOMAIN: number = 0x0000;

// ...
/**
 * 通过弹框验证锁屏密码，获取重置锁屏密码的恢复密钥。使用Promise异步回调。
 */
async function testGetEnterpriseRecoveryKeyForPinByDialog() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
    hilog.info(DOMAIN, TAG, `getOsAccountType,userId: ${userId}, accountType: ${accountType}`);
    let userType: number = accountType.valueOf();

    recoveryKey.verifyUserByDialog(userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in verifying user identity by dialog.`);
      recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
        .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
          hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise recovery key for resetting pin.`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
              .toString('hex')}`);
          hilog.info(DOMAIN, TAG,
            `EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
          hilog.info(DOMAIN, TAG, `EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG,
            `Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
        })
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to verify user identity by dialog. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG,
      `Failed to getEnterpriseRecoveryKeyForPinByDialog. Code: ${e.code}, message: ${e.message}`);
  }
}
```
