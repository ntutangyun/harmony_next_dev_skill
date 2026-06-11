# 开发Hvigor任务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task_

了解任务

任务是Hvigor构建过程中的基本执行单元，通常包含一段可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。

UP-TO-DATE

任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。

示例：

> hvigor UP-TO-DATE ::PackageApp...

Finished

任务执行完成标识，表示任务已执行完成。

示例：

> hvigor Finished ::PackageApp... after 310 ms

注册任务

使用HvigorNode节点对象注册任务。

// 导入模块
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);

// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('this is Task');
  }
});

使用hvigor命令行工具执行任务：

hvigorw customTask

## Code blocks

### Code block 1

```
> hvigor UP-TO-DATE ::PackageApp...
```

### Code block 2

```
> hvigor Finished ::PackageApp... after 310 ms
```

### Code block 3

```
// 导入模块
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
```

### Code block 4

```
// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);

// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('this is Task');
  }
});
```

### Code block 5

```
hvigorw customTask
```
