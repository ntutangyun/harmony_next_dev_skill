# Code Scanner代码检查

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-scanner_

从26.0.0 Beta1开始，DevEco Studio新增Code Scanner功能，用于检查整个项目的资源泄漏问题。开发者可根据扫描结果中的告警提示，手动修复代码缺陷，在代码开发阶段，确保代码质量。

操作步骤

点击扫描规则名称可在右侧查看规则功能描述和Code Example（包括正例和反例），可根据其中的建议修改工程代码，在Severity处可设置规则的告警级别（error，warn，fatal），默认为error。

说明

对于ArkTS工程，需勾选ARKTS下的扫描规则；对于C++工程，需勾选CPP下的扫描规则。

在菜单栏点击Code > Code Scanner > Scan，开始全量代码扫描。

Severity统计了所有告警数量，点击All、Fatal、Error、Warn可分别查看对应告警级别的具体信息。点击Filter by scene下拉菜单，可以筛选不同规则的检查结果。单击告警文件可以查看告警信息和对应配置的规则。双击某条告警结果，可以跳转到对应代码缺陷位置；选中告警结果时，可以在右侧Execution Trace窗口查看告警原因和问题的来源到问题的发生点的可能的执行流。
