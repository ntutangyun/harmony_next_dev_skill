# 为通知添加行为意图

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-with-wantagent_

应用向Ability Kit申请WantAgent，并将WantAgent封装至通知中。当发布通知时，用户便可以通过点击通知栏中的消息或按钮，拉起目标应用组件或发布公共事件。

携带了actionButtons的通知示意图如下。

运行机制

接口说明
接口名	描述
publish(request: NotificationRequest): Promise<void>	发布通知。
getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void	创建WantAgent。
开发步骤

导入模块。

import { notificationManager } from '@kit.NotificationKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;
AddWantAgent.ets

创建WantAgentInfo信息。

场景一：创建拉起UIAbility的WantAgent的WantAgentInfo信息。

let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的wantAgent对象，后续使用其完成触发的动作。


// 通过WantAgentInfo的operationType设置动作类型
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: '',
      bundleName: 'com.sample.eventnotification', // 需要替换为对应的bundleName。
      abilityName: 'EntryAbility', // 需要替换为对应的abilityName。
      action: '',
      entities: [],
      uri: '',
      parameters: {}
    }
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
};

场景二：创建发布公共事件的WantAgent的WantAgentInfo信息。

let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的WantAgent对象，后续使用其完成触发的动作。


// 通过WantAgentInfo的operationType设置动作类型
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      action: 'event_name', // 设置事件名
      parameters: {},
    }
  ],
  actionType: wantAgent.OperationType.SEND_COMMON_EVENT,
  requestCode: 0,
  actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG],
};
AddWantAgent.ets

调用getWantAgent()方法进行创建WantAgent。

// 创建WantAgent
wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
  if (err) {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
  wantAgentObj = data;


  // ...
});
AddWantAgent.ets

构造NotificationRequest对象，并发布携带WantAgent的通知。

说明

如果封装WantAgent至通知消息中，可以点击通知触发WantAgent。当通知消息存在actionButtons时，点击通知会先显示actionButtons，再次点击通知触发WantAgent。

如果封装WantAgent至通知按钮中，点击通知后，该通知下方会出现通知按钮，可以点击按钮触发WantAgent。

// 构造NotificationActionButton对象
let actionButton: notificationManager.NotificationActionButton = {
  title: 'open_the_app',
  // wantAgentObj使用前需要保证已被赋值（即步骤3执行完成）
  // 通知按钮的WantAgent
  wantAgent: wantAgentObj!
};


// 构造NotificationRequest对象
let notificationRequest: notificationManager.NotificationRequest = {
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'one_button_notify',
      text: 'Click on this notification twice to open the app',
      additionalText: 'Test_AdditionalText',
    },
  },
  id: 6,
  // 通知消息的WantAgent
  wantAgent: wantAgentObj!,
  // 通知按钮
  actionButtons: [actionButton],
};


notificationManager.publish(notificationRequest, (err: BusinessError) => {
  if (err) {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
});
AddWantAgent.ets
示例代码
自定义通知
为通知添加自定义铃声
更新通知

## Code blocks

### Code block 1

```
import { notificationManager } from '@kit.NotificationKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;
```

### Code block 2

```
let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的wantAgent对象，后续使用其完成触发的动作。


// 通过WantAgentInfo的operationType设置动作类型
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: '',
      bundleName: 'com.sample.eventnotification', // 需要替换为对应的bundleName。
      abilityName: 'EntryAbility', // 需要替换为对应的abilityName。
      action: '',
      entities: [],
      uri: '',
      parameters: {}
    }
  ],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG]
};
```

### Code block 3

```
let wantAgentObj: WantAgent | null = null; // 用于保存创建成功的WantAgent对象，后续使用其完成触发的动作。


// 通过WantAgentInfo的operationType设置动作类型
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      action: 'event_name', // 设置事件名
      parameters: {},
    }
  ],
  actionType: wantAgent.OperationType.SEND_COMMON_EVENT,
  requestCode: 0,
  actionFlags: [wantAgent.WantAgentFlags.CONSTANT_FLAG],
};
```

### Code block 4

```
// 创建WantAgent
wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError, data: WantAgent) => {
  if (err) {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to get want agent. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in getting want agent.');
  wantAgentObj = data;


  // ...
});
```

### Code block 5

```
// 构造NotificationActionButton对象
let actionButton: notificationManager.NotificationActionButton = {
  title: 'open_the_app',
  // wantAgentObj使用前需要保证已被赋值（即步骤3执行完成）
  // 通知按钮的WantAgent
  wantAgent: wantAgentObj!
};


// 构造NotificationRequest对象
let notificationRequest: notificationManager.NotificationRequest = {
  content: {
    notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: 'one_button_notify',
      text: 'Click on this notification twice to open the app',
      additionalText: 'Test_AdditionalText',
    },
  },
  id: 6,
  // 通知消息的WantAgent
  wantAgent: wantAgentObj!,
  // 通知按钮
  actionButtons: [actionButton],
};


notificationManager.publish(notificationRequest, (err: BusinessError) => {
  if (err) {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to publish notification. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in publishing notification.');
});
```
