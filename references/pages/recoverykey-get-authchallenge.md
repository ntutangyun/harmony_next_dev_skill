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

import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用接口getAuthChallenge，获取挑战值。

function testGetAuthChallenge() {
  recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
    console.info(`Succeeded in getting challenge.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
  });
}

## Code blocks

### Code block 1

```
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
function testGetAuthChallenge() {
  recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
    console.info(`Succeeded in getting challenge.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
  });
}
```
