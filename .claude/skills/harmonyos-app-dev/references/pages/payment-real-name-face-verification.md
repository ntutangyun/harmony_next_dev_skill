# 人脸核身实人验证场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-face-verification_

startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>;	拉起用户人脸核身实人验证（人脸验证）页面。
开发步骤
发起人脸核身预验证（服务器开发）

调用人脸核身实人预验证接口获取预验证ID后返回给端侧拉起人脸核身实人验证页面。服务器开发步骤可参考实名信息验证/授权场景服务器开发实现。

拉起人脸核身实人验证（端侧开发）

开发者客户端使用后端服务返回的预验证ID作为参数调用startFaceVerification接口拉起用户人脸核身实人验证页面。当接口通过.then()方法返回时，则表示当前接口请求成功，通过.catch()方法返回表示接口请求失败。当此次请求有异常时，可通过error.code获取错误码，错误码相关信息请参见错误码。示例代码如下：

import { BusinessError } from '@kit.BasicServicesKit';
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';
 
@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartFaceVerificationPromise() {
    // use your own preVerifyId
    let preVerifyId = '后端服务获取有效的预验证ID';
    realNameService.startFaceVerification(this.context, preVerifyId)
      .then((verifyResultId: string ) => {
        // face verification success
        console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
      })
      .catch((error: BusinessError) => {
        // failed to face verification
        console.error(`failed to face verification, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }
 
  build() {
    Column() {
      Button('requestStartFaceVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartFaceVerificationPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
查询人脸核身实人验证结果（服务器开发）

调用人脸核身实人验证接口查询验证结果。

实名信息验证/授权场景
身份验证服务调用记录查看
