# 空间事件订阅

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-event-subscription_

从6.0.0(20)开始，支持订阅和取消订阅空间事件的能力。

场景介绍

Enterprise Space Kit为应用提供订阅空间事件的能力。订阅空间切换事件后，应用将在空间切换时收到通知，并执行预设的自定义动作。同时，也提供取消订阅空间事件的能力，支持应用在特定场景下灵活管理空间事件的订阅状态。

接口说明

详细接口说明可参考接口文档。

接口名	描述
subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number	订阅空间事件，在相关事件触发时，通知应用侧。
unsubscribeEvent(subscribeId: number): void	取消订阅空间事件，在相关事件触发时，不再通知应用侧。

开发步骤

1.导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

2.订阅空间切换事件和取消订阅空间事件。

@Entry
@Component
struct Index {
  // 订阅空间事件
  subscribe() {
    let eventIds: spaceManager.EventType[] = [spaceManager.EventType.EVENT_WORKSPACE_SWITCHED];
    let callBack = (error: BusinessError, data: spaceManager.EventData) => {
      if (error) {
        console.error(`error info:${error?.code}, err message:${error?.message}`);
      } else {
        console.info(`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
        // 处理事件
      }
    };

    try {
      const subscribeId = spaceManager.subscribeEvent(eventIds, callBack);
      console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
    } catch (err) {
      console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
    }
    // 订阅成功处理
  }

  // 取消订阅空间事件
  unSubscribe() {
    let subscribeId = 100;
    try {
      spaceManager.unsubscribeEvent(subscribeId);
      console.info(`Succeeded in unsubscribing event.`);
    } catch (err) {
      console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('订阅空间事件')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.subscribe();
          })
      }

      Row() {
        Button('取消订阅空间事件')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.unSubscribe();
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
  // 订阅空间事件
  subscribe() {
    let eventIds: spaceManager.EventType[] = [spaceManager.EventType.EVENT_WORKSPACE_SWITCHED];
    let callBack = (error: BusinessError, data: spaceManager.EventData) => {
      if (error) {
        console.error(`error info:${error?.code}, err message:${error?.message}`);
      } else {
        console.info(`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
        // 处理事件
      }
    };

    try {
      const subscribeId = spaceManager.subscribeEvent(eventIds, callBack);
      console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
    } catch (err) {
      console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
    }
    // 订阅成功处理
  }

  // 取消订阅空间事件
  unSubscribe() {
    let subscribeId = 100;
    try {
      spaceManager.unsubscribeEvent(subscribeId);
      console.info(`Succeeded in unsubscribing event.`);
    } catch (err) {
      console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('订阅空间事件')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.subscribe();
          })
      }

      Row() {
        Button('取消订阅空间事件')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.unSubscribe();
          })
      }
    }
  }
}
```
