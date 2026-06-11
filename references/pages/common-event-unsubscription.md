# 取消动态订阅公共事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-event-unsubscription_

场景介绍

动态订阅者完成业务需求后，应主动取消订阅。通过调用unsubscribe()方法，取消订阅事件。

接口说明

接口名	接口描述
unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>)	取消订阅公共事件。

开发步骤

导入模块。

import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'ProcessModel';
const DOMAIN_NUMBER: number = 0xFF00;

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

## Code blocks

### Code block 1

```
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'ProcessModel';
const DOMAIN_NUMBER: number = 0xFF00;
```

### Code block 2

```
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
```
