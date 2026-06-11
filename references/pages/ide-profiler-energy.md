# 能耗诊断：Energy分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy_

从DevEco Studio 5.1.0 Release版本开始，DevEco Profiler提供Energy模板，帮助用户在应用运行过程中查看能耗信息，包括不同器件的能耗、整机温度以及能耗异常帧，从而方便用户对能耗问题进行调优。此外，Energy模板还集成了Frame、Time、CPU场景分析任务的功能，方便开发者在分析能耗问题的同时同步对比同一时段的其他资源占用情况。

说明

TV设备暂不支持使用Energy模板进行应用性能分析。

定位能耗问题

创建Energy模板任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

Energy Anomaly泳道：展示能耗相关的异常帧信息。该泳道暂不支持在Wearable设备上进行应用性能分析；

Temperature泳道：展示整机的温度信息。该泳道暂不支持在2in1设备上进行应用性能分析；

Energy泳道：展示各器件的能耗信息及整机电流信息。

点击Temperature泳道，鼠标悬浮于泳道上可以查看对应时间范围的温度以及温度等级，帮助用户明确温度是否有明显上升，从而进行进一步的能耗定位。观察下方Detail区域，可以看到所选范围内的平均温度、最大温度以及最小温度。

框选Energy泳道数据，Energy Detail中呈现框选时间段内的详情信息。根据不同器件的消耗可结合Callstack泳道的调用栈信息进行进一步分析。

说明

从DevEco Studio 6.1.0 Beta1版本开始，支持查看能耗异常原因、能耗异常数量。

2in1设备暂不支持查看RS Empty Run和GPU Consumption。
