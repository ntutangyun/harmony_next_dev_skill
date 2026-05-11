# 弹窗组件常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-component-faq_

Popup气泡的默认显示区域是绑定组件以外的窗口区域，框架内部会根据可用空间自动调整气泡位置，而非严格按照开发者设置的placement位置显示。

Popup气泡优先在开发者设置的placement位置显示，当空间不足时会按以下策略自动避让。

Popup气泡的默认显示区域是绑定组件以外的窗口区域，如下示意图所示：

如果设置的位置可用空间不够完整显示气泡，ArkUI框架会判断该位置的镜像位置是否可以显示。例如Placement.Bottom的镜像位置是Placement.Top，Placement.Left的镜像位置是Placement.Right。

如果镜像位置的空间仍然不足，会切换到另一轴方向的位置显示，即跨轴避让（cross-axis fallback）。例如垂直方向（Top/Bottom）都不够时，会尝试水平方向（Left/Right），反之亦然。

如果四周空间均不足以完整显示气泡，则默认气泡会遮挡绑定组件进行显示。如果开发者不期望遮挡绑定组件，可通过设置avoidTarget属性为AvoidanceMode.AVOID_AROUND_TARGET来解决，此时气泡在剩余空间不足的情况下会进行压缩以避免遮挡绑定组件。

参考链接

Popup控制
按钮与选择组件常见问题
使用文本常见问题
