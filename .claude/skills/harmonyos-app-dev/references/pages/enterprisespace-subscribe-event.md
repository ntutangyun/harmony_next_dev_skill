# 订阅空间事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-subscribe-event_

Enterprise Space Kit为应用提供订阅空间事件的能力，当前支持订阅空间切换事件。应用订阅空间切换事件后，当空间切换时，会告知应用，并执行应用自定义的动作。

接口说明

详细接口说明可参考接口文档。

接口名	描述
subscribeEvent(eventId: EventType[], callback: AsyncCallback<EventData>): number	订阅空间事件，在相关事件触发时，通知应用侧。使用callback异步回调。
开发步骤

导入Enterprise Space Kit模块和相关依赖模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用subscribeEvent接口，设置订阅空间事件，并查看打印信息。

try {
  const subscribeId = spaceManager.subscribeEvent([spaceManager.EventType.EVENT_WORKSPACE_SWITCHED],
    (error: BusinessError, data: spaceManager.EventData) => {
      if (error) {
        console.error(`error info:${error?.code}, err message:${error?.message}`);
      } else {
        console.info(`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}`);
      }
    });
  console.info(`Succeeded in subscribing event. subscribeId: ${subscribeId}`);
} catch (err) {
  console.error(`Failed to subscribe event. Code: ${err.code}, message: ${err.message}`);
}
设置工作空间资料照片
取消订阅空间事件
