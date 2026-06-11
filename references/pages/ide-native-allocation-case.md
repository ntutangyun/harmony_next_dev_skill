# 案例：Native内存泄漏分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case_

本案例介绍如何判断应用存在Native内存泄漏。

6.1.0(23) Beta1以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

6.1.0(23) Beta1及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

初步识别内存问题

当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

当从实时监控页面初步判断应用可能存在内存问题后，通过深度录制抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。

说明

其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

点击三角按钮即开始录制。

录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。

当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用Allocation模板进行下一步分析。

使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

[h2]录制模板数据

连接设备后，点击应用选择框选择需要录制的应用，选择Allocation模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。

说明

如果要分析启动内存，单击Allocation任务后的按钮。

说明

默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

[h2]分析Native数据

框选All Heap中的Native Heap子泳道。

All Allocations：框选的时间段的所有分配内存信息。

Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。

Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

说明

Category中亮色代表开发者调用栈，灰色代表系统调用栈。

栈帧中主要为Native栈，为便于开发者分析Native的函数热点，工具提供了符号导入的能力，若需要查看这部分信息，需要导入相应版本的带符号的so库（具体参考离线符号解析）。

使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

[h2]录制Allocation模板数据

连接设备后，点击应用选择框选择需要录制的应用，选择Allocation模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。

说明

如果要分析启动内存，单击Allocation任务后的按钮。

说明

默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

[h2]分析Native数据

框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

All Allocations：框选的时间段的所有分配内存信息。

Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。

Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

说明

Category中亮色代表开发者调用栈，灰色代表系统调用栈。

栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考离线符号解析）。
