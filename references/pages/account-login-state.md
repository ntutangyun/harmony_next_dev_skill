# 订阅华为账号的登录/登出事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-login-state_

场景介绍

应用在前台时可以订阅Account Kit提供的华为账号登录/登出广播事件，来感知华为账号的登录状态，实现用户登录/登出应用的逻辑。应用也可通过getHuaweiIDState实时查询华为账号登录状态。

事件说明

以下是华为账号登录/登出发送的广播事件。

事件名称	描述
COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN	表示分布式账号登录成功的动作。华为账号登录成功也会发这个广播事件。
COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT	表示分布式账号登出成功的动作。华为账号登出成功也会发这个广播事件。

开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成配置签名和指纹、配置Client ID。此场景无需申请账号权限。

开发步骤

导入commonEventManager模块及相关公共模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

创建订阅者，并处理订阅结果。

// 订阅者信息
const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: [commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN,
    commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT]
};
 let subscriber: commonEventManager.CommonEventSubscriber | null = null;

// 创建订阅者
commonEventManager.createSubscriber(subscribeInfo)
  .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
    subscriber = commonEventSubscriber;
    // 订阅公共事件
    commonEventManager.subscribe(subscriber,
      (error: BusinessError, data: commonEventManager.CommonEventData) => {
        if (error) {
          hilog.error(0x0000, 'testTag',
            `Failed to subscribe, code is ${error.code}, message is ${error.message}`);
        } else {
          hilog.info(0x0000, 'testTag', 'Succeeded in subscribing.');
          if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN) {
            // 订阅到华为账号登录事件
          }
          if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT) {
            // 订阅到华为账号登出事件
          }
        }
      });
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to createSubscriber. Code: ${err.code}, message: ${err.message}`);
  });

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
```

### Code block 2

```
// 订阅者信息
const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: [commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN,
    commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT]
};
 let subscriber: commonEventManager.CommonEventSubscriber | null = null;

// 创建订阅者
commonEventManager.createSubscriber(subscribeInfo)
  .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
    subscriber = commonEventSubscriber;
    // 订阅公共事件
    commonEventManager.subscribe(subscriber,
      (error: BusinessError, data: commonEventManager.CommonEventData) => {
        if (error) {
          hilog.error(0x0000, 'testTag',
            `Failed to subscribe, code is ${error.code}, message is ${error.message}`);
        } else {
          hilog.info(0x0000, 'testTag', 'Succeeded in subscribing.');
          if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN) {
            // 订阅到华为账号登录事件
          }
          if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT) {
            // 订阅到华为账号登出事件
          }
        }
      });
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to createSubscriber. Code: ${err.code}, message: ${err.message}`);
  });
```
