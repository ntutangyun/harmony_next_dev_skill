# 权益发放

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-delivering-subscriptions_

对生效中的订阅发放权益

[h2]场景介绍

用户购买自动续期订阅商品后，若订阅处于生效状态，开发者需要及时给用户发放对应权益。

在应用启动时，获取用户当前处于生效状态的订阅列表，处理此部分订阅的权益发放。建议先检查当前订阅对应权益的发放状态，未发放再补充发放权益。在权益发放成功后，向IAP确认发货，完成购买。

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

[h2]业务流程

应用客户端向IAP Kit发起queryPurchases请求，查询用户生效中的订阅列表。

IAP Kit返回PurchaseData列表。PurchaseData为JWS格式的字符串，承载了相关的订阅信息。

应用客户端向应用服务器上报PurchaseData列表。

应用服务器需对每个PurchaseData.jwsSubscriptionStatus进行解码验签，验证成功可得到对应的SubGroupStatusPayload的JSON字符串。

处理权益发放。检查SubGroupStatusPayload.lastSubscriptionStatus.lastPurchaseOrder是否已发放权益，未发放则需发放相关权益，并记录对应的订单信息（PurchaseOrderPayload）。

说明

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

应用客户端向应用服务器查询订单的发货状态。

应用服务器返回对应的发货状态以及订单信息（PurchaseOrderPayload）。

发放权益后应用客户端向IAP Kit发送finishPurchase请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行finishPurchase之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端订阅确认发货接口来确认发货，完成购买流程。

说明

对于自动续期订阅商品，如果不执行此步骤，会导致后续自动续期无法扣费 ，以及同一个订阅组不同自动续期订阅商品无法切换等问题。

[h2]开发步骤

应用客户端向IAP Kit发起queryPurchases请求，获取生效中的订阅列表。

在请求参数QueryPurchasesParameter中指定productType为iap.ProductType.AUTORENEWABLE，同时指定queryType为iap.PurchaseQueryType.CURRENT_ENTITLEMENT。当接口请求成功时，IAP Kit将返回一个QueryPurchaseResult对象，该对象包含承载了订阅信息的PurchaseData的列表。

验证订单信息。对每个purchaseData.jwsSubscriptionStatus进行解码验签，验证成功可得到SubGroupStatusPayload的JSON字符串。建议应用客户端将purchaseData发送至应用服务器，在应用服务器执行此操作。

为了提高安全性，可从SubGroupStatusPayload.lastSubscriptionStatus.lastPurchaseOrder中解析出purchaseToken和purchaseOrderId信息，并通过服务端订阅状态查询接口向IAP服务器查询最新的订阅状态信息，进一步确认订阅信息的准确性。

展示订阅状态。

如果SubGroupStatusPayload.lastSubscriptionStatus.status=1，表示订阅处于生效状态。

如果SubGroupStatusPayload.lastSubscriptionStatus.status=1且SubGroupStatusPayload.lastSubscriptionStatus.renewalInfo.autoRenewStatusCode值为1时，表示订阅处于自动续期状态。此状态的商品无法再次购买，需要屏蔽相关的购买入口。

权益发放。获取SubGroupStatusPayload.lastSubscriptionStatus.lastPurchaseOrder（下文标记为PurchaseOrderPayload），处理权益发放。

可先检查此笔订单权益的发放状态，未发放则补充发放权益，成功后记录PurchaseOrderPayload等信息，用于后续检查权益发放状态。

说明

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

在发放权益后，如果PurchaseOrderPayload.finishStatus不为1，应用需调用finishPurchase接口确认发货，完成购买流程。

发起请求时，需在请求参数FinishPurchaseParameter中携带PurchaseOrderPayload中的productType、purchaseToken、purchaseOrderId。请求成功后，IAP服务器会将相应商品标记为已发货。

说明

此步骤也可放到应用服务器处理。应用服务器可通过请求服务端订阅确认发货接口来确认发货，完成购买流程。

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

  queryPurchases(context: common.UIAbilityContext) {
    const param: iap.QueryPurchasesParameter = {
      productType: iap.ProductType.AUTORENEWABLE,
      queryType: iap.PurchaseQueryType.CURRENT_ENTITLEMENT
    };
    iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
      console.info('Succeeded in querying purchases.');
      const purchaseDataList: string[] = res.purchaseDataList;
      if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
        return;
      }
      for (let i = 0; i < purchaseDataList.length; i++) {
        const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
        if (!jwsSubscriptionStatus) {
          continue;
        }
        // 对jwsSubscriptionStatus进行解码验签
        const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
        // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
        const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
        const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
        if (!lastSubscriptionStatus) {
          continue;
        }

        // 根据status判断订阅的状态
        const status = lastSubscriptionStatus.status;
        // 更新商品的订阅状态
        // ...

        // 处理权益发放
        const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
        if (purchaseOrderPayload === undefined) {
          continue;
        }
        if (status === '1') {
          // 订阅处于生效状态
          // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
          // ...
        }
        // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
        if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
          this.finishPurchase(context, purchaseOrderPayload);
        }
      }
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
    })
  }

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

确保权益发放

用户购买自动续期订阅成功或者自动续期成功后，开发者需要及时给用户发放相关权益。但实际应用场景中，若出现异常（网络错误等）将导致应用无法知道用户实际是否支付成功，从而无法及时发放权益，即出现掉单情况。

为了确保权益发放，需要在createPurchase请求返回iap.IAPErrorCode.PRODUCT_OWNED或iap.IAPErrorCode.SYSTEM_ERROR时检查用户是否存在已购但未确认发货的商品，如果存在则发放相关权益，然后向IAP Kit确认发货，完成购买。

[h2]业务流程

应用客户端向IAP Kit发起queryPurchases请求，查询用户已购买但未确认发货的订阅列表。

IAP Kit返回PurchaseData列表。PurchaseData为JWS格式的字符串，承载了相关的订阅信息。

应用客户端向应用服务器上报PurchaseData列表。

应用服务器需对每个PurchaseData.jwsSubscriptionStatus进行解码验签，验证成功可得到对应的SubGroupStatusPayload的JSON字符串。

处理权益发放。检查SubGroupStatusPayload.lastSubscriptionStatus.lastPurchaseOrder是否已发放权益，未发放则需发放相关权益，并记录对应的订单信息（PurchaseOrderPayload）。

说明

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

应用客户端向应用服务器查询订单的发货状态。

应用服务器返回对应的发货状态以及订单信息（PurchaseOrderPayload）。

发放权益后应用客户端向IAP Kit发送finishPurchase请求，以此通知IAP服务器更新商品的发货状态，完成购买流程。应用成功执行finishPurchase之后，IAP服务器会将相应商品标记为已发货状态。此步骤也可放到应用服务器处理。应用服务器可通过请求服务端订阅确认发货接口来确认发货，完成购买流程。

说明

对于自动续期订阅商品，如果不执行此步骤，会导致后续自动续期无法扣费 ，以及同一个订阅组不同自动续期订阅商品无法切换等问题。

[h2]开发步骤

应用客户端向IAP Kit发起queryPurchases请求，获取用户已购但未确认发货的订阅列表。

在请求参数QueryPurchasesParameter中指定productType为iap.ProductType.AUTORENEWABLE，同时指定queryType为iap.PurchaseQueryType.UNFINISHED。当接口请求成功时，IAP Kit将返回一个QueryPurchaseResult对象，该对象包含承载了订阅信息的PurchaseData的列表。

验证订单信息。对每个purchaseData.jwsSubscriptionStatus进行解码验签，验证成功可得到SubGroupStatusPayload的JSON字符串。建议应用客户端将purchaseData发送至应用服务器，在应用服务器执行此操作。

为了提高安全性，可从SubGroupStatusPayload.lastSubscriptionStatus.lastPurchaseOrder中解析出purchaseToken和purchaseOrderId信息，并通过服务端订阅状态查询接口向IAP服务器查询最新的订阅状态信息，进一步确认订阅信息的准确性。

处理权益发放。

如果SubGroupStatusPayload.lastSubscriptionStatus.status=1，表示订阅处于生效状态。需要对生效状态的订阅处理权益发放。建议先检查此笔订单权益的发放状态，未发放则补充发放权益，成功后记录PurchaseOrderPayload等信息，用于后续检查权益发放状态。

建议单机应用将用户权益和订阅状态关联。如果订阅处于生效状态，始终为用户发放权益。

在发放权益后，如果PurchaseOrderPayload.finishStatus不为1，应用需调用finishPurchase接口确认发货，完成购买流程。

发起请求时，需在请求参数FinishPurchaseParameter中携带PurchaseOrderPayload中的productType、purchaseToken、purchaseOrderId。请求成功后，IAP服务器会将相应商品标记为已发货。

说明

此步骤也可放到应用服务器处理。应用服务器可通过请求服务端订阅确认发货接口来确认发货，完成购买流程。

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

  queryPurchases(context: common.UIAbilityContext) {
    const param: iap.QueryPurchasesParameter = {
      productType: iap.ProductType.AUTORENEWABLE,
      queryType: iap.PurchaseQueryType.UNFINISHED
    };
    iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
      console.info('Succeeded in querying purchases.');
      const purchaseDataList: string[] = res.purchaseDataList;
      if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
        return;
      }
      for (let i = 0; i < purchaseDataList.length; i++) {
        const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
        if (!jwsSubscriptionStatus) {
          continue;
        }
        // 对jwsSubscriptionStatus进行解码验签
        const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
        // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
        const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
        const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
        if (!lastSubscriptionStatus) {
          continue;
        }

        // 根据status判断订阅的状态
        const status = lastSubscriptionStatus.status;
        // 更新商品的订阅状态
        // ...

        // 处理权益发放
        const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
        if (purchaseOrderPayload === undefined) {
          continue;
        }
        if (status === '1') {
          // 订阅处于生效状态
          // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
          // ...
        }
        // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
        if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
          this.finishPurchase(context, purchaseOrderPayload);
        }
      }
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
    })
  }

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

## Code blocks

### Code block 1

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// JWSUtil为自定义类
import { JWSUtil } from '../common/JWSUtil';

@Entry
@Component
struct Index {

  queryPurchases(context: common.UIAbilityContext) {
    const param: iap.QueryPurchasesParameter = {
      productType: iap.ProductType.AUTORENEWABLE,
      queryType: iap.PurchaseQueryType.CURRENT_ENTITLEMENT
    };
    iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
      console.info('Succeeded in querying purchases.');
      const purchaseDataList: string[] = res.purchaseDataList;
      if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
        return;
      }
      for (let i = 0; i < purchaseDataList.length; i++) {
        const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
        if (!jwsSubscriptionStatus) {
          continue;
        }
        // 对jwsSubscriptionStatus进行解码验签
        const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
        // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
        const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
        const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
        if (!lastSubscriptionStatus) {
          continue;
        }

        // 根据status判断订阅的状态
        const status = lastSubscriptionStatus.status;
        // 更新商品的订阅状态
        // ...

        // 处理权益发放
        const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
        if (purchaseOrderPayload === undefined) {
          continue;
        }
        if (status === '1') {
          // 订阅处于生效状态
          // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
          // ...
        }
        // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
        if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
          this.finishPurchase(context, purchaseOrderPayload);
        }
      }
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
    })
  }

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

### Code block 2

```
import { iap } from '@kit.IAPKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// JWSUtil为自定义类
import { JWSUtil } from '../common/JWSUtil';

@Entry
@Component
struct Index {

  queryPurchases(context: common.UIAbilityContext) {
    const param: iap.QueryPurchasesParameter = {
      productType: iap.ProductType.AUTORENEWABLE,
      queryType: iap.PurchaseQueryType.UNFINISHED
    };
    iap.queryPurchases(context, param).then((res: iap.QueryPurchaseResult) => {
      console.info('Succeeded in querying purchases.');
      const purchaseDataList: string[] = res.purchaseDataList;
      if (purchaseDataList === undefined || purchaseDataList.length <= 0) {
        return;
      }
      for (let i = 0; i < purchaseDataList.length; i++) {
        const jwsSubscriptionStatus: string = JSON.parse(purchaseDataList[i]).jwsSubscriptionStatus;
        if (!jwsSubscriptionStatus) {
          continue;
        }
        // 对jwsSubscriptionStatus进行解码验签
        const subscriptionStatus: string = JWSUtil.decodeJwsObj(jwsSubscriptionStatus);
        // 需自定义SubGroupStatusPayload类，包含的信息请参见SubGroupStatusPayload
        const subGroupStatusPayload: SubGroupStatusPayload = JSON.parse(subscriptionStatus);
        const lastSubscriptionStatus = subGroupStatusPayload.lastSubscriptionStatus;
        if (!lastSubscriptionStatus) {
          continue;
        }

        // 根据status判断订阅的状态
        const status = lastSubscriptionStatus.status;
        // 更新商品的订阅状态
        // ...

        // 处理权益发放
        const purchaseOrderPayload = lastSubscriptionStatus.lastPurchaseOrder;
        if (purchaseOrderPayload === undefined) {
          continue;
        }
        if (status === '1') {
          // 订阅处于生效状态
          // 处理权益发放。检查此笔订单权益的发放状态，未发放则补充发放权益
          // ...
        }
        // 发放权益后向IAP Kit发送finishPurchase请求，确认发货，完成购买
        if (purchaseOrderPayload && purchaseOrderPayload.finishStatus !== '1') {
          this.finishPurchase(context, purchaseOrderPayload);
        }
      }
    }).catch((err: BusinessError) => {
      // 请求失败
      console.error(`Failed to query purchases. Code is ${err.code}, message is ${err.message}`);
    })
  }

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
