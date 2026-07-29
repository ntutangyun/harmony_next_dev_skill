# 获取挑战值

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-get-authchallenge_

场景介绍

请求获取挑战值，在发起更新企业公钥证书、删除已有企业恢复密钥流程前，需要获取挑战值，并进行签名，以确认企业身份。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getAuthChallenge(): Promise<Uint8Array>	使用Promise方式获取挑战值。

开发步骤

导入模块。

import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

调用接口getAuthChallenge，获取挑战值。

const TAG: string = 'EnterpriseRecoveryKey_GetChallenge';
const DOMAIN: number = 0x0000;

/**
 * 获取挑战值。使用Promise异步回调。
 */
function getAuthChallenge() {
  recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
    hilog.info(DOMAIN, TAG, `Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
  });
}

## Code blocks

### Code block 1

```
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'EnterpriseRecoveryKey_GetChallenge';
const DOMAIN: number = 0x0000;

/**
 * 获取挑战值。使用Promise异步回调。
 */
function getAuthChallenge() {
  recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
    hilog.info(DOMAIN, TAG, `Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
  });
}
```
