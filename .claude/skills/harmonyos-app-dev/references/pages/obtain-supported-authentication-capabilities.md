# 查询支持的认证能力

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-authentication-capabilities_

getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void	根据指定的认证类型、认证等级，检测当前设备是否支持相应的认证能力。
开发步骤

申请权限：ohos.permission.ACCESS_BIOMETRIC。

指定认证类型（UserAuthType）和认证等级（AuthTrustLevel），调用getAvailableStatus接口查询当前的设备是否支持相应的认证能力。

认证可信等级的详细介绍请参见认证可信等级划分原则。

以查询设备是否支持认证可信等级≥ATL3的人脸认证功能为例：

obtainingSupported() {
  try {
    // 查询认证能力是否支持
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
    Logger.info('current auth trust level is supported.');
    return true;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`current auth trust level is not supported, code is ${err?.code}, message is ${err?.message}`);
    return false;
  }
}
Index.ets
示例代码
查询支持的认证能力
开发准备
发起认证
