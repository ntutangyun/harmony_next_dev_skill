# GPU活动分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu_

功能介绍

从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

GPU模板支持的泳道包括：Counters、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍Counters泳道，其他泳道的详细信息请参考对应模板内容。

ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

[h2]约束与限制

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

仅支持Phone设备。

操作步骤

GPU分析任务支持在录制前单击指定要录制的泳道。单击工具控制栏中的按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
