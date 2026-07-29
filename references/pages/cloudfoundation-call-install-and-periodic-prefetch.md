# 调用全部预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-install-and-periodic-prefetch_

导入相关模块。

import { GlobalContext } from '../common/GlobalContext';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { PrefetchWrapper } from '../PrefetchUtil/PrefetchWrapper';

初始化全局上下文。

// 初始化全局上下文
GlobalContext.initContext(this.context);

在EntryAbility.ets文件的onCreate中调用预加载实现类PrefetchWrapper的doPrefetch方法。应用安装后首次打开时，跳转应用详情页调用跳链安装预加载，跳转首页调用安装预加载；应用安装后非首次打开时，则调用周期性预加载。

PrefetchWrapper.getInstance().doPrefetch();

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
PrefetchWrapper.getInstance().doPrefetch();
```
