# IFAA免密身份认证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-ifaa_

场景介绍

开通：提供移动端开通生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已有的生物特征类型进行开通，会开通移动端对应生物特征类型的IFAA免密身份认证能力。

认证：提供移动端认证生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征进行认证，认证成功；使用未开通的生物特征进行认证，认证失败。

注销：提供移动端注销生物特征（指纹/3D人脸）IFAA免密身份认证的能力。使用用户已开通的生物特征类型进行注销，会注销移动端对应生物特征类型的IFAA免密身份认证能力。

相关权限

获取生物识别权限：ohos.permission.ACCESS_BIOMETRIC。

约束与限制

开发者应用已接入IIFAA联盟，可以从IIFAA中心服务器获取签名数据。

移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...
function getAvailableStatus() {
  try {
    // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
    console.info('current auth trust level is supported');
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  }
}

移动端设备使用此服务时需要处于联网状态。

IFAA服务会将匿名化的指纹ID和面容ID等个人信息返回至三方应用，以提供绑定具体生物特征的免密认证能力。应用将个人信息上云前，需要向用户明示并且取得同意，详细请参考个人数据处理说明。

业务流程

接口说明

表1 开通、认证、注销的所需要的接口

接口名	描述
register(registerData: Uint8Array): Promise<Uint8Array>	开通指定用户的指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。
auth(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array>	使用指定用户的生物信息类型进行IFAA免密身份认证。
deregisterSync(deregisterData: Uint8Array): void	注销指定用户指定生物信息类型（指纹/3D人脸）的IFAA免密身份认证能力。
getAnonymousIdSync(userToken: Uint8Array): Uint8Array	获取IFAA免密认证的匿名化ID。

开发步骤

导入相关模块。

import { ifaa } from '@kit.OnlineAuthenticationKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

注册IFAA免密身份认证。

try {
  // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
  let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}
try {
  // 开发者需使用getAnonymousIdSync从服务端获取签名后的开通数据
  // 开发者将开通数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvRegisterFp，再使用ifaa.register接口。
  let registerPromise: Promise<Uint8Array> = ifaa.register(tlvRegisterFp);
  registerPromise.then(registerResult => {
    console.info('Succeeded in doing register.');
    // 开通成功，开发者获取ifaa.register结果并处理。
    // ...
  }).catch((err: BusinessError) =>{
    console.error(`Failed to call register. Code: ${err.code}, message: ${err.message}`);
    // 开通失败，开发者获取ifaa.register错误并处理。
  });
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to register. Code is ${err.code}, message is ${err.message}`);
}

使用IFAA免密身份认证进行认证。

// 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
let getAnonIdResult: Uint8Array;
try {
  getAnonIdResult = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}

// 开发者需使用getAnonymousIdSync从服务端获取签名后的认证数据
// 获取此次免密支付的challenge
let ifaaChallenge: Uint8Array = new Uint8Array([0]);
try {
  ifaaChallenge = ifaa.preAuthSync();
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to pre auth. Code is ${err.code}, message is ${err.message}`);
}
let authParam: userAuth.AuthParam = {
  challenge: ifaaChallenge,
  authType: [userAuth.UserAuthType.FINGERPRINT],
  authTrustLevel: userAuth.AuthTrustLevel.ATL4
};

try {
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
  userAuthInstance.on('result', {
    onResult(result) {
      let authToken = result.token;
      try {
        // 生物特征认证成功后，调用IFAA认证
        console.info('IFAA auth start');
        // 开发者将认证数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvAuthFp，再使用ifaa.authSync接口。
        // 开发者根据业务需求选择同步/异步接口
        let authResult: Uint8Array = ifaa.authSync(authToken, tlvAuthFp);
        console.info('authSyn authResult' + authResult);
        // 开发者处理authResult
        // ...
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to call auth. Code is ${err.code}, message is ${err.message}`);
        // ...
      }
    }
  });
  userAuthInstance.start();
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to user auth. Code is ${err.code}, message is ${err.message}`);
}

注销IFAA免密身份认证。

// 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
try {
  let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}

// 开发者需使用getAnonymousId的结果从服务端获取签名后的注销数据
// 开发者将注销数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvDeregisterRp，再使用ifaa.deregisterSync接口。
try {
  ifaa.deregisterSync(tlvDeregisterRp);
  // ...
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to deregister. Code is ${err.code}, message is ${err.message}`);
  // ...
}

常见问题

现象描述：开通IFAA免密身份认证失败。

可能原因：移动端设备没有联网。

处理步骤：移动端设备连接WIFI或热点，再次尝试。

## Code blocks

### Code block 1

```
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...
function getAvailableStatus() {
  try {
    // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
    console.info('current auth trust level is supported');
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  }
}
```

### Code block 2

```
import { ifaa } from '@kit.OnlineAuthenticationKit';
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 3

```
try {
  // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
  let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}
try {
  // 开发者需使用getAnonymousIdSync从服务端获取签名后的开通数据
  // 开发者将开通数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvRegisterFp，再使用ifaa.register接口。
  let registerPromise: Promise<Uint8Array> = ifaa.register(tlvRegisterFp);
  registerPromise.then(registerResult => {
    console.info('Succeeded in doing register.');
    // 开通成功，开发者获取ifaa.register结果并处理。
    // ...
  }).catch((err: BusinessError) =>{
    console.error(`Failed to call register. Code: ${err.code}, message: ${err.message}`);
    // 开通失败，开发者获取ifaa.register错误并处理。
  });
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to register. Code is ${err.code}, message is ${err.message}`);
}
```

### Code block 4

```
// 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
let getAnonIdResult: Uint8Array;
try {
  getAnonIdResult = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}

// 开发者需使用getAnonymousIdSync从服务端获取签名后的认证数据
// 获取此次免密支付的challenge
let ifaaChallenge: Uint8Array = new Uint8Array([0]);
try {
  ifaaChallenge = ifaa.preAuthSync();
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to pre auth. Code is ${err.code}, message is ${err.message}`);
}
let authParam: userAuth.AuthParam = {
  challenge: ifaaChallenge,
  authType: [userAuth.UserAuthType.FINGERPRINT],
  authTrustLevel: userAuth.AuthTrustLevel.ATL4
};

try {
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
  userAuthInstance.on('result', {
    onResult(result) {
      let authToken = result.token;
      try {
        // 生物特征认证成功后，调用IFAA认证
        console.info('IFAA auth start');
        // 开发者将认证数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvAuthFp，再使用ifaa.authSync接口。
        // 开发者根据业务需求选择同步/异步接口
        let authResult: Uint8Array = ifaa.authSync(authToken, tlvAuthFp);
        console.info('authSyn authResult' + authResult);
        // 开发者处理authResult
        // ...
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to call auth. Code is ${err.code}, message is ${err.message}`);
        // ...
      }
    }
  });
  userAuthInstance.start();
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to user auth. Code is ${err.code}, message is ${err.message}`);
}
```

### Code block 5

```
// 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
try {
  let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
}

// 开发者需使用getAnonymousId的结果从服务端获取签名后的注销数据
// 开发者将注销数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvDeregisterRp，再使用ifaa.deregisterSync接口。
try {
  ifaa.deregisterSync(tlvDeregisterRp);
  // ...
} catch (error) {
  const err = error as BusinessError;
  console.error(`Failed to deregister. Code is ${err.code}, message is ${err.message}`);
  // ...
}
```
