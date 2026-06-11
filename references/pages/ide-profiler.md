# DevEco Profiler调优工具简介

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler_

为了帮助开发者更高效地进行性能问题的分析，DevEco Studio提供了场景化调优工具DevEco Profiler，希望为开发者带来高效、直通代码行的调优体验。开发者可以使用DevEco Profiler完成不同应用模型和场景下的完整性能数据采集，通过简单的工具操作即可完成数据采集，这些数据将帮助开发者洞悉应用在相应场景下的运行细节。

工具整体设计遵循了Top-Down的设计理念和数据展示范式。被采集的数据经由工具分析，会由浅到深的以一条条泳道的形式直观地呈现到界面上，DevEco Profiler提供深入具体函数运行热点、CPU调度细节的分析能力，帮助用户搭建HarmonyOS应用性能模型。

说明

DevEco Profiler工具支持使用USB连接方式或使用无线连接方式的真机设备进行调优分析，不支持模拟器调优。

macOS 12及以上系统版本支持使用DevEco Profiler工具。

您可以通过如下三种方式打开Profiler：

在DevEco Studio顶部菜单栏中选择“View -> Tool Windows -> Profiler”。

在DevEco Studio底部工具栏中单击“Profiler”。

界面布局

会话区

数据区
