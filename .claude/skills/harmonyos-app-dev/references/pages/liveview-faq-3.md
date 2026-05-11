# 关于实况窗生命周期的问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-3_

当App关闭时，可以调用liveViewManager.stopLiveView方法，设置参数PrimaryData实例的keepTime值为0，即可实现立即关闭实况窗。

如何实现“自动关闭构建的实况窗”

从6.1.1(24)版本起，应用可在创建或更新实况窗时，通过设置PrimaryData实例的aliveTime属性来实现自动关闭功能。

本地更新如何获取实况窗实例以及实况窗被清除后的限制

本地更新实况窗时，可以通过liveViewManager.getActiveLiveView函数获取活动的LiveView实例。

如果想要结束实况窗，建议使用liveViewManager.stopLiveView方法。如果实况窗被notificationManager.cancel或notificationManager.cancelAll清除后，无论是Live View Kit还是Push Kit，无法再次通过该id更新或结束实况窗。

再次创建该id的实况窗时，Live View Kit可以通过该id再次创建实况窗，Push Kit在12小时内无法通过该id再次创建实况窗。

三方开发框架接入的问题
关于实况窗模板使用的问题
