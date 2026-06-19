# UI组件内存：ComMemory分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory_

功能介绍

从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

ComMemory模板支持的泳道包括：Memory、ArkUI Snapshot、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory。本文介绍ArkUI Snapshot泳道，其他泳道的详细信息请参考对应模板内容。

Memory、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory泳道的介绍请参考基础内存：Allocation分析。

ArkTS Snapshot泳道的介绍请参考内存泄漏：Snapshot分析。

说明

任务分析前，需创建ComMemory分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

查看组件树和组件信息

Details区域显示当前快照的详细信息，点击Open，将在ArkUI Inspector中打开相应的.arkli文件。

默认勾选Show Component Size和Show Free-Node Components，Show Component Size显示各组件的内存占用情况，Show Free-Node Components显示游离组件（未在组件树上的组件）。点击，勾选Show Recursive Size，显示各组件为根的子树的内存占用情况。

Current：当前组件ArkTS内存和Native内存的占用情况。

ArkTS：当前组件对应的ArkTS堆快照对象的Retained Size。

Native：当前组件新增占用的Native内存。

Subtree：当前组件及其子组件的Current内存之和。

nativeCount：当前组件存活的Native分配内存个数。

arktsCount：当前组件的ArkTS堆快照对象个数。

recursive：递归统计信息。

ShowAllocationDetail：显示当前组件的Allocation详情。

ShowSnapshotDetail：显示当前组件的Snapshot详情，系统组件不显示该项。

ShowRecursiveAllocationDetail：显示当前组件及其子组件的Allocation详情。

ShowRecursiveSnapshotDetail：显示当前组件及其子组件的Snapshot详情。

memory字段表示该状态变量在对应组件的ArkTS堆快照中的Retained Size，更多请参考查看UI组件的状态变量。

在中间栏点击可以将包含内存信息的组件树快照导出到本地。

.arkli文件对比

从26.0.0 Beta1版本开始，支持对比.arkli文件，通过对比快速定位异常增多的组件。

Details区域显示当前快照的详细信息，点击Open，将在ArkUI Inspector中打开相应的.arkli文件。

说明

Target文件需要先点击Open按钮在ArkUI Inspector中打开，否则在下拉框中选不到。
