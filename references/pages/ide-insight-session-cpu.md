# CPU活动分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu_

功能介绍

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

CPU模板支持的泳道包括：Energy、CPU Core、Process。本文介绍CPU Core、Process泳道，Energy泳道的详细信息请参考能耗诊断：Energy分析。

说明

任务分析前，需创建CPU分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

查看各CPU使用情况

Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。

Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。

说明

将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

查询进程详情

单击工具控制栏中的按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render_service进程的trace数据。

说明

中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

说明

并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

查看Trace详情

说明

如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。

从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。
