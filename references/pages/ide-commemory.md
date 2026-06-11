# UI组件内存：ComMemory分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commemory_

从DevEco Studio 6.1.1 Beta1版本开始，DevEco Profiler新增ComMemory模板，可以分析UI界面各组件内存的分配情况，帮助定位UI组件内存泄漏问题。

操作步骤

在“Details”页签中显示当前快照的详细信息；点击Open按钮，将在ArkUI Inspector中打开相应的.arkli文件。

默认勾选“Show Component Size”，显示各组件的内存占用情况。点击，可勾选“Show Recursive Size”，显示各组件为根的子树的内存占用情况。

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

在中间栏点击可以将包含内存信息的组件树快照导出到本地。
