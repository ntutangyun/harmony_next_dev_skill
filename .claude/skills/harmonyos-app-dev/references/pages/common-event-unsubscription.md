# 取消动态订阅公共事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-unsubscription_

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>)	取消订阅公共事件。
开发步骤

导入模块。

import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = 'ProcessModel';
const DOMAIN_NUMBER: number = 0xFF00;
CreatSubscribeInfo.ets

根据动态订阅公共事件章节的步骤来订阅某个事件。

调用CommonEvent中的unsubscribe()方法取消订阅某事件。

// subscriberCustom为订阅事件时创建的订阅者对象
if (subscriberCustom !== null) {
  commonEventManager.unsubscribe(subscriberCustom, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN_NUMBER, TAG,
        `Failed to unsubscribe. code is ${err.code}, message is ${err.message}`);
    } else {
      hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in unsubscribing.`);
      subscriberCustom = null;
    }
  })
}
CreatSubscribeInfo.ets
动态订阅公共事件
发布公共事件
