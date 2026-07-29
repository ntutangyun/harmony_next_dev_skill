# 调用跳链安装预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-chain-install-prefetch_

导入相关模块。

import { GlobalContext } from '../common/GlobalContext';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { PrefetchWrapper } from '../PrefetchUtil/PrefetchWrapper';

初始化全局上下文。

// 初始化全局上下文
GlobalContext.initContext(this.context);

在EntryAbility.ets文件的onCreate中调用预加载实现类PrefetchWrapper的doLinkPrefetch方法。方法内部会先调用popDeferredLink接口获取延迟链接，再调用getPrefetchResult获取跳链安装预加载缓存数据。

说明

跳链安装预加载缓存的是应用详情页数据，仅允许调用一次，被调用后将被销毁。

PrefetchWrapper.getInstance().doLinkPrefetch();

## Code blocks

### Code block 1

```
import { GlobalContext } from '../common/GlobalContext';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { PrefetchWrapper } from '../PrefetchUtil/PrefetchWrapper';
```

### Code block 2

```
// 初始化全局上下文
GlobalContext.initContext(this.context);
```

### Code block 3

```
PrefetchWrapper.getInstance().doLinkPrefetch();
```
