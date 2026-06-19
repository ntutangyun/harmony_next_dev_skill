# 调用周期性预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-periodicprefetch_

在项目的EntryAbility.ets文件中导入预加载实现类PrefetchWrapper，并在onCreate中调用PrefetchWrapper的doPeriodicPrefetch方法。方法内部会先调用registerPrefetchTask方法注册周期性预加载任务，12h后将调用getPrefetchResult获取周期性预加载数据。

说明

系统会结合应用活跃情况进行任务清理。应用不活跃后，如果当前时间 – 任务注册时间 > 72h，则任务将直接从队列移除。移除任务时不立即清理已加载的数据，数据会被定期清理，应用启动时仍然可尝试获取此前已加载的缓存数据，并结合数据时间戳决定是否呈现内容。

获取周期性预加载数据的间隔周期是12h，如果打开应用的时间间隔低于12h，可能将无法获取到最新的预加载数据。

由于系统每隔12h才会拉取一次周期性预加载数据，不方便调试周期性预加载功能，为此，系统提供了命令行工具，可以实时拉取周期性预加载数据。

import { GlobalContext } from '../common/GlobalContext';
import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  GlobalContext.initContext(this.context); // 初始化全局上下文
  PrefetchWrapper.getInstance().doPeriodicPrefetch();
}

## Code blocks

### Code block 1

```
import { GlobalContext } from '../common/GlobalContext';
import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  GlobalContext.initContext(this.context); // 初始化全局上下文
  PrefetchWrapper.getInstance().doPeriodicPrefetch();
}
```
