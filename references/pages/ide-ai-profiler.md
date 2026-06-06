# 智慧调优

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler_

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄露次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

操作步骤
首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

方式一：若Launch、Frame、Allocation、Snapshot模板已录制完成，点击Session窗口中该条会话上的图标，即可开始智慧调优分析。录制方法具体请参考性能问题定位：深度录制。

方式二：切换至Assistant窗口，点击Create Session开始录制调优任务；或点击Open File按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

对于方式二，在Assistant页面，点击Create Session按钮，从Launch、Frame、Snapshot、Allocation中选择一个分析模板。

说明

使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

等待AI完成初步分析。左键点击高亮的泳道名称，点击Analyze进一步分析该阶段的具体内存信息，点击View Lane在右侧查看具体的泳道信息。

点击Analyze后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

编译报错智能分析
应用UI生成
