# 基础内存：Allocation分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations_

功能介绍

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

Allocation模板支持的泳道包括：Memory、ArkTS Allocation、ArkTS Snapshot、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources、Graphic Memory。同时，Allocation模板支持离线符号解析能力，相关能力介绍请参考离线符号解析。

说明

任务分析前，需创建Allocation分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

内存分析介绍

内存分析数据筛选

启动时内存分析

案例：Native内存泄漏分析
