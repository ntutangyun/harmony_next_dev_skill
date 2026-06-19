# ArkUI分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis_

功能介绍

ArkUI模板用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：布局嵌套过多引起的性能问题；数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；父组件中的子组件重复绑定同一个状态变量进行更新；未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝等。

ArkUI模板支持的泳道包括：APP Frame、ArkUI Component、ArkUI State、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍ArkUI Component、ArkUI State泳道，其他泳道的详细信息请参考对应模板内容。

APP Frame泳道的介绍请参考Frame分析。

ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

说明

任务分析前，需创建ArkUI分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

查看组件绘制耗时

开发者通过ArkUI Component泳道可以直观感知组件绘制频率、耗时等统计情况。

在时间轴上拖拽鼠标选定要查看的时间段。

说明

由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

查看状态变量变化

说明

由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
