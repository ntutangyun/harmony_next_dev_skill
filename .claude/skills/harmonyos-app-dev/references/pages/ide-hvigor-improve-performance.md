# 并行构建

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-improve-performance_

大部分工程都包含了多个子工程，其中一些子工程是相互独立的，也就是说，它们之间没有状态共享。在大多数情况下，通过并行构建可以有效地减少多个子工程的整体构建时间。然而，在特定的情况下，如子工程之间存在大量的依赖关系，可能无法显著缩短构建时间。节省的具体时间取决于您的工程结构和子工程之间的依赖关系。

Hvigor默认开启并行构建，您也可以通过以下几种方式来控制是否启用并行构建：

通过DevEco Studio菜单栏构建：
点击File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor，勾选或取消勾选字段Execute tasks in parallel mode(may require larger heap size)。
通过命令行构建：
执行命令，其中<task>替换为具体任务名：
// 启用并行构建
hvigorw <task> --parallel
// 关闭并行构建
hvigorw <task> --no-parallel
在hvigor-config.json5中配置execution.parallel选项。
守护进程
增量构建
