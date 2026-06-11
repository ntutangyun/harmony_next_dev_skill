# 查看ArkUI状态变量

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state_

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击Layout Settings，勾选ArkUI State，打开ArkUI状态变量面板。

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

说明

打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。

同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
