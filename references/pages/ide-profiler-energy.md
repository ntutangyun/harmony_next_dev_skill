# 能耗诊断：Energy分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy_

功能介绍

从DevEco Studio 5.1.0 Release版本开始，DevEco Profiler提供Energy模板，帮助用户在应用运行过程中查看能耗信息，包括不同器件的能耗、整机温度以及能耗异常帧，从而方便用户对能耗问题进行调优。

Energy模板支持的泳道包括：Energy Anomaly、Temperature、Energy、Frame、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍Energy Anomaly、Temperature、Energy泳道，其他泳道的详细信息请参考对应模板内容。

Frame泳道的介绍请参考Frame分析。

ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

说明

TV设备暂不支持使用Energy模板进行应用性能分析。

任务分析前，需创建Energy分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

定位能耗问题

录制结束等待处理数据完成。默认包含Energy Anomaly、Temperature以及Energy三条能耗相关泳道。

Energy Anomaly泳道

用于展示能耗相关的异常帧信息。该泳道暂不支持在Wearable设备上进行应用性能分析。

Temperature泳道

用于展示整机的温度信息。该泳道暂不支持在2in1设备上进行应用性能分析。

Energy泳道

用于展示各器件的能耗信息及整机电流信息。

可在Energy泳道中查看录制范围内具体器件消耗的电量，器件包含：CPU、*Display（屏幕显示耗电量）、GPU、Location（定位模块耗电量）、Camera（相机耗电量）、Bluetooth（蓝牙功能耗电量）、Flashlight（闪光灯功能耗电量）、Audio（声音模块耗电量）、Wifi（无线功能耗电量）、Modem（信号模块耗电量）。*Device表示整机电流消耗情况。
