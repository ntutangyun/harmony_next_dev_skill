# Launch模板基本操作

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch_

功能介绍

开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。

Launch模板支持的泳道包括：Launch、Frame、ArkTS Callstack、Callstack、Network Traffic、Network Request、CPU Core、Process。本文介绍Launch泳道，其他泳道的详细信息请参考对应模板内容。

Frame泳道的介绍请参考Frame分析。

ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

Network Traffic、Network Request泳道的介绍请参考网络诊断：Network分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

说明

任务分析前，需创建Launch分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制；或在会话区选择Open File，导入历史数据。

不支持命令拉起的Release应用，不能进行Launch分析。

锁屏状态下可进行Launch录制。

启动模式介绍

录制前应用的启动模式分为自动启动和手动启动，可点击图标切换两种不同模式：

若选择自动启动模式，当用户使用Launch模板并开始录制时，将自动重启所选应用。

若选择手动启动模式，在开始录制时，只会自动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

查看启动过程中各阶段的耗时情况

展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息，单击跳转按钮，可直接跳转至相关线程打点任务中。

Category：该ets文件在应用启动过程中是否被使用。

Weight：该ets文件加载子节点文件（不包括自身）的总耗时。

Self：该ets文件自身加载的耗时。

Import Count：该ets文件被其他文件导入的次数。

File Name：该ets文件的名称。

Path：该ets文件构建产物的路径。

说明

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中ETS文件的加载情况。

分析静态资源库加载耗时

展开Launch泳道，其中的Static Initialization子泳道展示启动过程中各静态资源库的加载耗时。

针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。

查看核心线程在CPU Core的运行情况

展开Launch泳道，其中的Running CPU Cores子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。

查看启动过程相关的线程Trace数据

展开Launch泳道，除Static Initialization和Running CPU Cores子泳道外，还包含启动过程的关键线程的状态和Trace数据。

Details区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。

Thread States区域展示线程的状态统计信息。

Thread Usage区域展示线程的使用情况。

Slice List区域展示所选对象的切片统计信息。

Load Statistics区域展示所选对象的中载和重载信息。
