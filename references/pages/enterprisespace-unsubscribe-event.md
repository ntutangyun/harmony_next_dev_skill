# 取消订阅空间事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-unsubscribe-event_

场景介绍

Enterprise Space Kit为应用提供取消订阅空间事件的能力，支持应用在特定场景下灵活管理空间事件的订阅状态。例如，当应用需要关闭、某个功能模块不再使用时，可通过调用该方法主动取消对特定空间事件的订阅。

接口说明

详细接口说明可参考接口文档。

接口名	描述
unsubscribeEvent(subscribeId:number): void	取消订阅空间事件，在相关事件触发时，不再通知应用侧。

开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用unsubscribeEvent接口，取消订阅空间事件，并查看打印信息。

const subscribeId: number = 100;
try {
  spaceManager.unsubscribeEvent(subscribeId);
  console.info('Succeeded in unsubscribing event');
} catch (err) {
  console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
const subscribeId: number = 100;
try {
  spaceManager.unsubscribeEvent(subscribeId);
  console.info('Succeeded in unsubscribing event');
} catch (err) {
  console.error(`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}`);
}
```
