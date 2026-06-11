# 调用跳链安装预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-chain-install-prefetch_

在项目的EntryAbility.ets文件中导入预加载实现类PrefetchWrapper，并在onCreate中调用PrefetchWrapper的doLinkPrefetch方法。方法内部会先调用popDeferredLink接口获取延迟链接，再调用getPrefetchResult获取跳链安装预加载缓存数据。

说明

跳链安装预加载缓存的是应用详情页数据，仅允许调用一次，被调用后将被销毁。

import { GlobalContext } from '../common/GlobalContext';
import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  GlobalContext.initContext(this.context); // 初始化全局上下文
  PrefetchWrapper.getInstance().doLinkPrefetch();
}

## Code blocks

### Code block 1

```
import { GlobalContext } from '../common/GlobalContext';
import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  GlobalContext.initContext(this.context); // 初始化全局上下文
  PrefetchWrapper.getInstance().doLinkPrefetch();
}
```
