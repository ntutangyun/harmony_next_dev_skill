# ArkUI分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis_

ArkUI分析用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：

场景1：布局嵌套过多引起的性能问题；

场景2：数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；

场景3：父组件中的子组件重复绑定同一个状态变量进行更新；

场景4：未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝。

ArkUI Component 泳道：查看组件绘制耗时

开发者通过ArkUI Component泳道可以直观感知组件绘制频率、耗时等统计情况。

在时间轴上拖拽鼠标选定要查看的时间段。

说明

由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

ArkUI State 泳道分析

点击ArkUI模板创建session并启动录制，录制过程中触发组件刷新。

Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。

说明

如需查看其他泳道信息，请参考Frame分析。

由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
