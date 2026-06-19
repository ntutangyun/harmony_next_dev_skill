# 接入购买

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-integrate-purchase_

场景介绍

在应用内购买场景中，用户会采用一次性付款的方式购买消耗型商品或非消耗型商品。请结合实际业务场景选择提供的商品类型。

在接入消耗型/非消耗型商品购买能力前，需要提前配置商品信息。用户在应用内购买时，应用拉起IAP Kit的收银台，收银台处会展示商品名称、商品价格等信息，用户根据需求完成商品购买。

提供优惠

为了提供更有吸引力的消耗型/非消耗型商品购买，华为应用内支付支持开发者配置优惠促销（自定义人群促销）。

可以针对用户群体、优惠地域进行自定义选择，支持开发者进行个性化的优惠活动配置。开发者可以在发起购买前，查询该商品的优惠活动信息，在最终发起购买时，将优惠活动信息传递到华为应用内支付，最终将优惠活动信息展示给用户。

说明

当前优惠促销涉及生成优惠签名购买参数处理，推荐具备服务器的开发者接入使用。

优惠促销无使用次数限制。

约束与限制

消耗型/非消耗型商品购买能力支持Phone、Tablet、PC/2in1设备，并且从5.1.0（18）版本开始，新增支持Wearable设备。从5.1.1(19）版本开始，新增支持TV设备，从26.0.0版本开始，新增支持Car设备。

业务流程

说明

如下业务流程对于单机应用同样适用。在单机应用中，应用服务器和应用客户端的交互放在应用客户端完成，应用服务器和IAP服务器交互的部分可不处理。

展示商品

应用客户端向IAP Kit发起queryEnvironmentStatus请求，检查当前用户登录的华为账号所在的服务地是否在IAP Kit支持结算的国家/地区中。

如果接口返回错误码“1001860054：用户账号所在服务地不在IAP Kit支持结算的国家/地区中”，应用需隐藏相关IAP功能入口。

应用客户端向IAP Kit发起queryProducts请求来获取在AppGallery Connect上配置的商品信息。

应用客户端根据返回的商品信息展示可供购买的商品列表，包含商品名称、价格等信息。

购买及结果确认

用户发起购买后，应用客户端向IAP Kit发起createPurchase购买请求或通过IAP嵌入式收银台组件发起购买请求（只支持TV），请求中携带商品ID、商品类型等信息。IAP Kit创建订单并展示收银台。

购买结果确认。如购买成功，可通过应用客户端或应用服务器接收购买结果，建议通过应用服务器接收购买结果。

方式一：通过客户端接收购买结果

用户购买成功时，IAP Kit返回包含订单信息的PurchaseData数据。

应用客户端向应用服务器上报PurchaseData数据。

应用服务器需对PurchaseData.jwsPurchaseOrder进行解码验签，成功后可得到PurchaseOrderPayload的JSON字符串。

（建议）方式二：通过服务器接收购买结果

为了提高安全性，开发者可以接入服务端关键事件通知，在用户购买成功时，IAP服务器将发送订单关键事件通知。

应用服务器可从NotificationPayload.NotificationMetaData中解析出purchaseToken和purchaseOrderId信息，并通过服务端订单状态查询接口向IAP服务器查询最新的订单信息，进一步确认订单的准确性。

IAP服务器返回订单信息jwsPurchaseOrder。

应用服务器需对jwsPurchaseOrder进行解码验签，成功后可得到PurchaseOrderPayload的JSON字符串。

说明

如果购买失败，请参见权益发放处理，及时发放权益。

发放权益

确认购买成功后，需要处理权益发放。检查当前PurchaseOrderPayload是否已发放权益，未发放则发放相关权益，并记录对应的订单信息（PurchaseOrderPayload），用于后续检查权益发放状态。

应用客户端向应用服务器查询订单的发货状态。

应用服务器返回对应的发货状态以及订单信息（PurchaseOrderPayload）。

发货成功后应用客户端向IAP Kit发送finishPurchase请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。

应用成功执行此步骤后，IAP服务器会将相应商品标记为已发货状态。对于消耗型商品，IAP服务器会将相应商品重新设置为可购买状态，用户即可再次购买该商品。对于非消耗型商品，用户购买后永久拥有，无法再次购买该商品。

说明

此步骤也可放到应用服务器处理。应用服务器可通过请求服务端订单确认发货接口来确认发货，完成购买流程。

确保在发货成功之后再执行此步骤，否则可能导致IAP服务器已经确认发货但是应用没有发货的问题。

开发步骤

[h2]展示商品

检查应用引入IAP Kit的可用性。

在使用应用内支付之前，应用客户端需要向IAP Kit发送queryEnvironmentStatus请求，以此判断用户当前登录的华为账号所在的服务地是否在IAP Kit支持结算的国家/地区中。

说明

当前IAP Kit支持结算的国家/地区仅有中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  queryEnvironmentStatus(context: common.UIAbilityContext) {
    iap.queryEnvironmentStatus(context).then(() => {
      // 请求成功
      console.info('Succeeded in querying environment status.');
    }).catch((err: BusinessError) => {
      // 请求失败
      // 如果接口返回错误码“1001860054 用户账号所在服务地不在IAP Kit支持结算的国家/地区中”，应用需隐藏相关IAP功能入口
      console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}

展示商品列表。

应用客户端通过queryProducts来获取在AppGallery Connect上配置的商品信息。发起请求时，需在请求参数QueryProductsParameter中携带相关的商品ID，并根据实际配置指定其商品类型productType。

当接口请求成功时，IAP Kit将返回商品信息Product的列表。 应用可以使用Product包含的商品价格、名称和描述等信息，向用户展示可供购买的商品列表。

说明

queryProducts每次只能查询一种商品类型的商品，每次最多查询200个商品，否则请求将报错。

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  queryProducts(context: common.UIAbilityContext) {
    const queryProductParam: iap.QueryProductsParameter = {
      // iap.ProductType.CONSUMABLE：消耗型商品
      // iap.ProductType.NONCONSUMABLE：非消耗型商品
      productType: iap.ProductType.CONSUMABLE,
      // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
      productIds: ['ohos_consume_001']
    };
    iap.queryProducts(context, queryProductParam).then(() => {
      // 请求成功
      console.info('Succeeded in querying products.');
      // 展示商品信息
      // ...
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}

[h2]发起购买

用户发起购买时，应用客户端向IAP Kit发送createPurchase请求来拉起IAP Kit收银台或通过IAP嵌入式收银台组件发起购买请求（只支持TV）。发起请求时，需在请求参数PurchaseParameter中携带此前已在华为AppGallery Connect网站上配置并生效的商品ID，并根据实际配置指定其productType。

如需单次购买多个商品（仅消耗型商品），可在PurchaseParameter中拼接quantity参数，quantity取值范围1-10。

说明

开发过程中易出现频繁调用接口的现象，建议控制接口调用频度，具体可参见1001860004 接口访问过频。

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  createPurchase(context: common.UIAbilityContext) {
    const createPurchaseParam: iap.PurchaseParameter = {
      // iap.ProductType.CONSUMABLE：消耗型商品
      // iap.ProductType.NONCONSUMABLE：非消耗型商品
      productType: iap.ProductType.CONSUMABLE,
      // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
      productId: 'ohos_consume_001'
    };
    iap.createPurchase(context, createPurchaseParam).then((result) => {
      console.info('Succeeded in creating purchase.');
      // 购买成功，处理购买结果
      // dealPurchaseResult实现请参见下一步
      this.dealPurchaseResult(result);
    }).catch((err: BusinessError) => {
      // 购买失败
      console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
      // dealPurchaseError实现请参见下一步
      this.dealPurchaseError(err);
    })
  }

  build() {}
}

[h2]购买结果处理

【结果1：购买成功】

说明

为了提高安全性，建议应用服务器接入服务端关键事件通知以接收购买成功结果并通过应用服务器来处理解码验签、完成购买等操作。

请务必确保发货成功后再执行完成购买步骤，本步骤可通过请求服务端订单确认发货接口来确认发货，完成购买流程。

以下内容为通过客户端接收购买结果及处理的步骤说明。

当用户购买成功时，应用客户端将接收到一个CreatePurchaseResult对象，其purchaseData字段包括了此次购买的结果信息。

对purchaseData.jwsPurchaseOrder进行解码验签，验证成功可得到PurchaseOrderPayload的JSON字符串。建议应用客户端将purchaseData发送至应用服务器，在应用服务器执行此操作。

验签成功后，如果PurchaseOrderPayload.purchaseOrderRevocationReasonCode为空，则代表购买成功，即可发放相关权益。

建议先检查此笔订单权益的发放状态，未发放则发放权益，成功后记录PurchaseOrderPayload等信息，用于后续检查权益发放状态。

完成购买。

发放权益后，应用客户端需要发送finishPurchase请求确认发货，以此通知IAP服务器更新商品的发货状态，完成购买流程。发送finishPurchase请求时，需在请求参数FinishPurchaseParameter中携带PurchaseOrderPayload中的productType、purchaseToken、purchaseOrderId。

应用成功执行此步骤后，IAP服务器会将相应商品标记为已发货状态。对于消耗型商品，IAP服务器会将相应商品重新设置为可购买状态，用户即可再次购买该商品。对于非消耗型商品，用户购买后永久拥有，无法再次购买该商品。

说明

JWSUtil为自定义类，可参见示例代码。

import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// JWSUtil为自定义类
import { JWSUtil } from '../common/JWSUtil';

@Entry
@Component
struct Index {
  /**
   * 购买结果处理
   *
   * @param result 商品购买结果
   */
  dealPurchaseResult(context: common.UIAbilityContext, result: iap.CreatePurchaseResult) {
    const jwsPurchaseOrder: string = JSON.parse(result.purchaseData).jwsPurchaseOrder;
    if (!jwsPurchaseOrder) {
      return;
    }
    // 对jwsPurchaseOrder进行解码验签
    const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
    // 需自定义PurchaseOrderPayload类，包含的信息请参见PurchaseOrderPayload
    const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
    // 处理发货
    // ...
    // 发货成功后向IAP Kit发送finishPurchase请求，确认发货，完成购买
    // finishPurchase请求的参数来源于purchaseOrderPayload
    this.finishPurchase(context, purchaseOrderPayload);
  }

  /**
   * 确认发货，完成购买
   *
   * @param purchaseOrder 订单信息，来源于购买请求
   */
  finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
    const finishPurchaseParam: iap.FinishPurchaseParameter = {
      productType: Number(purchaseOrder.productType),
      purchaseToken: purchaseOrder.purchaseToken,
      purchaseOrderId: purchaseOrder.purchaseOrderId
    };
    iap.finishPurchase(context, finishPurchaseParam).then(() => {
      // 请求成功
      console.info('Succeeded in finishing purchase.');
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}

【结果2：购买失败】

当用户购买失败时，需要针对code为iap.IAPErrorCode.PRODUCT_OWNED和iap.IAPErrorCode.SYSTEM_ERROR的场景，检查是否需要补发货，确保权益发放，具体请参见权益发放。

import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';

dealPurchaseError(err: BusinessError) {
  if (err.code === iap.IAPErrorCode.PRODUCT_OWNED || err.code === iap.IAPErrorCode.SYSTEM_ERROR) {
    // 参见权益发放检查是否需要补发货，确保权益发放
    // ...
  }
}

## Code blocks

### Code block 1

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  queryEnvironmentStatus(context: common.UIAbilityContext) {
    iap.queryEnvironmentStatus(context).then(() => {
      // 请求成功
      console.info('Succeeded in querying environment status.');
    }).catch((err: BusinessError) => {
      // 请求失败
      // 如果接口返回错误码“1001860054 用户账号所在服务地不在IAP Kit支持结算的国家/地区中”，应用需隐藏相关IAP功能入口
      console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}
```

### Code block 2

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  queryProducts(context: common.UIAbilityContext) {
    const queryProductParam: iap.QueryProductsParameter = {
      // iap.ProductType.CONSUMABLE：消耗型商品
      // iap.ProductType.NONCONSUMABLE：非消耗型商品
      productType: iap.ProductType.CONSUMABLE,
      // productIds中的商品需要替换成开发者在AppGallery Connect网站配置的商品
      productIds: ['ohos_consume_001']
    };
    iap.queryProducts(context, queryProductParam).then(() => {
      // 请求成功
      console.info('Succeeded in querying products.');
      // 展示商品信息
      // ...
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}
```

### Code block 3

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  createPurchase(context: common.UIAbilityContext) {
    const createPurchaseParam: iap.PurchaseParameter = {
      // iap.ProductType.CONSUMABLE：消耗型商品
      // iap.ProductType.NONCONSUMABLE：非消耗型商品
      productType: iap.ProductType.CONSUMABLE,
      // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
      productId: 'ohos_consume_001'
    };
    iap.createPurchase(context, createPurchaseParam).then((result) => {
      console.info('Succeeded in creating purchase.');
      // 购买成功，处理购买结果
      // dealPurchaseResult实现请参见下一步
      this.dealPurchaseResult(result);
    }).catch((err: BusinessError) => {
      // 购买失败
      console.error(`Failed to create purchase. Code is ${err.code}, message is ${err.message}`);
      // dealPurchaseError实现请参见下一步
      this.dealPurchaseError(err);
    })
  }

  build() {}
}
```

### Code block 4

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// JWSUtil为自定义类
import { JWSUtil } from '../common/JWSUtil';

@Entry
@Component
struct Index {
  /**
   * 购买结果处理
   *
   * @param result 商品购买结果
   */
  dealPurchaseResult(context: common.UIAbilityContext, result: iap.CreatePurchaseResult) {
    const jwsPurchaseOrder: string = JSON.parse(result.purchaseData).jwsPurchaseOrder;
    if (!jwsPurchaseOrder) {
      return;
    }
    // 对jwsPurchaseOrder进行解码验签
    const purchaseStr = JWSUtil.decodeJwsObj(jwsPurchaseOrder);
    // 需自定义PurchaseOrderPayload类，包含的信息请参见PurchaseOrderPayload
    const purchaseOrderPayload = JSON.parse(purchaseStr) as PurchaseOrderPayload;
    // 处理发货
    // ...
    // 发货成功后向IAP Kit发送finishPurchase请求，确认发货，完成购买
    // finishPurchase请求的参数来源于purchaseOrderPayload
    this.finishPurchase(context, purchaseOrderPayload);
  }

  /**
   * 确认发货，完成购买
   *
   * @param purchaseOrder 订单信息，来源于购买请求
   */
  finishPurchase(context: common.UIAbilityContext, purchaseOrder: PurchaseOrderPayload) {
    const finishPurchaseParam: iap.FinishPurchaseParameter = {
      productType: Number(purchaseOrder.productType),
      purchaseToken: purchaseOrder.purchaseToken,
      purchaseOrderId: purchaseOrder.purchaseOrderId
    };
    iap.finishPurchase(context, finishPurchaseParam).then(() => {
      // 请求成功
      console.info('Succeeded in finishing purchase.');
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to finish purchase. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {}
}
```

### Code block 5

```
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';

dealPurchaseError(err: BusinessError) {
  if (err.code === iap.IAPErrorCode.PRODUCT_OWNED || err.code === iap.IAPErrorCode.SYSTEM_ERROR) {
    // 参见权益发放检查是否需要补发货，确保权益发放
    // ...
  }
}
```
