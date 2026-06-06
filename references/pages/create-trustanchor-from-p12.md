# 证书链校验时从p12文件构造TrustAnchor对象数组

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-trustanchor-from-p12_

基于现有的p12文件数据，调用cert.createTrustAnchorsWithKeyStore创建X509TrustAnchor数组对象，并返回结果。

import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';


function test() {
  // ...
  try {
    cert.createTrustAnchorsWithKeyStore(p12Data, '123456').then((data) => {
      console.info('createTrustAnchorsWithKeyStore result: success, the num of result is :' + data.length);
    }).catch((err: BusinessError) => {
      console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${error.code}, message: ${error.message}`);
  }
}
CreateTrustanchorFromP12.ets
证书吊销列表对象的创建、解析和校验
证书链校验器对象的创建和校验
