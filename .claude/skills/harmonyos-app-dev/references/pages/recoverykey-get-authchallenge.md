# 获取挑战值

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-get-authchallenge_

recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
    console.info(`Succeeded in getting challenge.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
  });
}
获取重置锁屏密码的企业恢复密钥
挑战值签名
