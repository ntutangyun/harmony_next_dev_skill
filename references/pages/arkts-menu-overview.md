# 菜单概述

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-menu-overview_

不依赖UI组件的全局菜单 (openMenu)	用于在无法直接访问UI组件的场景向用户提供可执行操作，例如在事件回调中展示操作选项等。
规格约束
bindMenu通过调用isShow参数或bindContextMenu调用isShown参数弹出时，需要等待页面全部构建完成才能展示。因此isShow或isShown不能在页面构建中设置为true，否则会导致menu弹窗显示位置及形状错误。
openMenu的弹出需要传入有效的TargetInfo，否则无法弹出气泡。
其他规格约束，具体可参考菜单控制、openMenu说明。
生命周期

正常时序依次为：aboutToAppear>>onWillAppear>>onAppear>>onDidAppear>>aboutToDisappear>>onWillDisappear>>onDisappear>>onDidDisappear。

名称	类型	说明
aboutToAppear	() => void	菜单显示动效前的事件回调。
onAppear	() => void	菜单弹出后的事件回调。
aboutToDisappear	() => void	菜单退出动效前的事件回调。
onDisappear	() => void	菜单消失后的事件回调。
onWillAppear	Callback<void>	

菜单显示动效前的事件回调。

说明： aboutToAppear是初始化时触发调用，onWillAppear是在动画执行前触发调用，onWillAppear在aboutToAppear之后执行。


onDidAppear	Callback<void>	

菜单弹出后的事件回调。

说明：

1. 快速点击按钮时，菜单会快速弹出、消失，此时onWillDisappear可能会在onDidAppear前生效。

2. 当菜单入场动效未完成时关闭菜单，该回调不会触发。

3. onAppear和onDidAppear触发时机相同，onDidAppear在onAppear后生效。


onWillDisappear	Callback<void>	

菜单退出动效前的事件回调。

说明：

1. 快速点击按钮时，菜单会快速弹出、消失，此时onWillDisappear可能会在onDidAppear前生效。

2. aboutToDisappear和onWillDisappear触发时机相同，onWillDisappear在aboutToDisappear后生效。


onDidDisappear	Callback<void>	

菜单消失后的事件回调。

说明： onDisappear和onDidDisappear触发时机相同，onDidDisappear在onDisappear后生效。

菜单
菜单控制（Menu）
