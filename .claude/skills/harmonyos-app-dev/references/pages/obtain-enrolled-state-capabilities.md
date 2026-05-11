# 查询用户注册凭据的状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-enrolled-state-capabilities_

getEnrolledState(authType : UserAuthType): EnrolledState	根据指定的认证类型，查询用户注册凭据的状态，用于感知注册凭据变化。
开发步骤

申请权限：ohos.permission.ACCESS_BIOMETRIC。

指定认证类型（UserAuthType），调用getEnrolledState接口查询用户注册凭据的状态。

以查询用户人脸注册凭据的状态为例：

obtainingEnrolledCredentialInformation() {
  try {
    let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE);
    Logger.info('get current enrolled state successfully.');
    return enrolledState.credentialDigest;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(`get current enrolled state failed, code is ${err?.code}, message is ${err?.message}`);
    return false;
  }
}
Index.ets
示例代码
查询用户注册凭据的状态
切换自定义认证
使用嵌入式用户身份认证控件
