# 调用安装预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-installprefetch_

导入相关模块。

import { GlobalContext } from '../common/GlobalContext';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { PrefetchWrapper } from '../PrefetchUtil/PrefetchWrapper';

初始化全局上下文。

// 初始化全局上下文
GlobalContext.initContext(this.context);

在EntryAbility.ets文件的onCreate中调用预加载实现类PrefetchWrapper的doInstallPrefetch方法。方法内部会调用getPrefetchResult获取安装预加载缓存数据。

说明

安装预加载缓存数据，仅允许调用一次，被调用后将被销毁。

应用安装开始时，系统会拉取安装预加载云侧数据并缓存到本地。

PrefetchWrapper.getInstance().doInstallPrefetch();

说明

调用安装预加载过程中，可参考FAQ定位预加载问题。

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
PrefetchWrapper.getInstance().doInstallPrefetch();
```
