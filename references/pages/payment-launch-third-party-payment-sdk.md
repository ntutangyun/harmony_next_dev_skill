# 基于接口拉起方式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-launch-third-party-payment-sdk_

说明

当前基于接口拉起方式拉起三方支付收银台支持的支付方式参见PayMethod。

基于接口拉起三方支付收银台起始版本为：6.0.0(20)。

拉起支付宝支付需要配置服务器域名：https://mobilegw.alipay.com。

商户客户端根据Payment Kit接口返回的支付信息PayResult(混合支付场景）/PickerResult（纯外部支付场景），按照三方支付平台接入要求构建三方支付信息payInfo调用ThirdPayClient.pay接口拉起三方支付收银台。

拉起三方支付收银台示例代码如下：

import { BusinessError } from '@kit.BasicServicesKit';
import { thirdPaymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  thirdPaymentServicePayPromise() {
    thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, "appid_123456");
    // 请使用开发者自己的三方支付信息（payInfo）
    const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
    thirdPayClient.pay(payInfo).then(() => {
        // 支付成功
        console.info('succeeded in paying.');
      }).catch((error: BusinessError) => {
        // 支付失败
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('thirdPaymentServicePayPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.thirdPaymentServicePayPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}

拉起三方支付收银台可同步通过调用ThirdPayClient.handlePayCallback接口（用户支付完成后，会将支付操作结果回调给商户客户端），获取三方支付处理结果，完成支付操作处理。参考示例代码如下：

import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility, Want } from '@kit.AbilityKit';
// 需要从thirdPayClient对象定义的代码文件中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
import { thirdPayClient } from '../pages/thirdPaymentServicetest';

// 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
export default class EntryAbility extends UIAbility {
  onNewWant(want: Want): void {
    // 需要和拉起支付收银台的三方支付客户端对象为同一个
    if (thirdPayClient) {
      console.info('clientForThirdPayment handlePayCallback');
      let handlePayCallback = thirdPayClient.handlePayCallback(want);
      console.info(`clientForThirdPayment handlePayCallback result: ${handlePayCallback}`);
    }
  }
}

商户客户端收到三方支付回调通知或主动查询订单支付结果成功后，按照三方支付平台要求完成订单支付后的下一步业务处理，如对返回的支付结果信息验签等。

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { thirdPaymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  thirdPaymentServicePayPromise() {
    thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, "appid_123456");
    // 请使用开发者自己的三方支付信息（payInfo）
    const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
    thirdPayClient.pay(payInfo).then(() => {
        // 支付成功
        console.info('succeeded in paying.');
      }).catch((error: BusinessError) => {
        // 支付失败
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('thirdPaymentServicePayPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.thirdPaymentServicePayPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

### Code block 2

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIAbility, Want } from '@kit.AbilityKit';
// 需要从thirdPayClient对象定义的代码文件中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
import { thirdPayClient } from '../pages/thirdPaymentServicetest';

// 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
export default class EntryAbility extends UIAbility {
  onNewWant(want: Want): void {
    // 需要和拉起支付收银台的三方支付客户端对象为同一个
    if (thirdPayClient) {
      console.info('clientForThirdPayment handlePayCallback');
      let handlePayCallback = thirdPayClient.handlePayCallback(want);
      console.info(`clientForThirdPayment handlePayCallback result: ${handlePayCallback}`);
    }
  }
}
```
