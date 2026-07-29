# 跨空间消息提醒

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-cross-space-notification_

从26.0.0开始，支持跨空间消息提醒的能力。

场景介绍

Enterprise Space Kit为应用提供跨空间消息提醒的能力，支持企业空间与个人空间之间的双向通知互通：企业应用可主动触达个人空间，个人空间的应用也能将关键信息同步至企业空间。

企业管理员可调用配置接口控制“设置 > 通知和状态栏 > 通知管理”路径下的开关，以及是否隐藏通知内容，同时还能通过查询接口实时获取当前的配置状态。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setNotificationConfig(configs: NotificationConfig[]): Promise<void>	设置跨空间消息提醒配置。
getNotificationConfig(): Promise<NotificationConfig[]>	获取跨空间消息提醒配置。

开发步骤

import { spaceManager } from '@kit.EnterpriseSpaceKit';

@Entry
@Component
struct Index {
  // 设置跨空间消息提醒配置
  async setNotificationConfig() {
    const configs: spaceManager.NotificationConfig[] = [
      {
        workspaceId: 100,
        appIdentifier: 'com.example.app',
        notificationState: spaceManager.NotificationSwitch.ON,
        visibilityState: spaceManager.NotificationVisibilitySwitch.NOTIFICATION_VISIBLE,
        allowVisibilityChange: spaceManager.NotificationVisibilityControl.ALLOW_CHANGE
      }
    ];
    try {
      await spaceManager.setNotificationConfig(configs);
      console.info(`Succeeded in setting notification config.`);
    } catch (err) {
      console.error(`Failed to set notification config. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 获取跨空间消息提醒配置
  async getNotificationConfig() {
    try {
      const configs: spaceManager.NotificationConfig[] = await spaceManager.getNotificationConfig();
      console.info(`Succeeded in getting notification config. configs: ${JSON.stringify(configs)}`);
    } catch (err) {
      console.error(`Failed to get notification config. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('设置跨空间消息提醒配置')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setNotificationConfig();
          })
      }

      Row() {
        Button('获取跨空间消息提醒配置')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getNotificationConfig();
          })
      }
    }
  }
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
@Entry
@Component
struct Index {
  // 设置跨空间消息提醒配置
  async setNotificationConfig() {
    const configs: spaceManager.NotificationConfig[] = [
      {
        workspaceId: 100,
        appIdentifier: 'com.example.app',
        notificationState: spaceManager.NotificationSwitch.ON,
        visibilityState: spaceManager.NotificationVisibilitySwitch.NOTIFICATION_VISIBLE,
        allowVisibilityChange: spaceManager.NotificationVisibilityControl.ALLOW_CHANGE
      }
    ];
    try {
      await spaceManager.setNotificationConfig(configs);
      console.info(`Succeeded in setting notification config.`);
    } catch (err) {
      console.error(`Failed to set notification config. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 获取跨空间消息提醒配置
  async getNotificationConfig() {
    try {
      const configs: spaceManager.NotificationConfig[] = await spaceManager.getNotificationConfig();
      console.info(`Succeeded in getting notification config. configs: ${JSON.stringify(configs)}`);
    } catch (err) {
      console.error(`Failed to get notification config. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('设置跨空间消息提醒配置')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setNotificationConfig();
          })
      }

      Row() {
        Button('获取跨空间消息提醒配置')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getNotificationConfig();
          })
      }
    }
  }
}
```
