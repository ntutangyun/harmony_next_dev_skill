# 关于实况窗生命周期的问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-3_

如何实现“App进程结束时，关闭构建的实况窗”

当App进程结束时，可以在UIAbility生命周期的onDestroy()方法内调用liveViewManager.stopLiveView方法，设置参数PrimaryData实例的keepTime值为0，即可实现立即关闭实况窗。

说明

若因App进程异常终止场景导致无法调用到应用的onDestroy()方法，则实况窗不会消失。

从26.0.0版本开始，新增支持在创建实况窗时，应用可通过指定实况生命周期模式实现自动关闭实况窗。可以在创建liveViewManager.startLiveView实况窗时，设置参数LiveView实例的lifeCycleMode值为AUTO_STOP_WHEN_APP_TERMINATE，即可在应用进程结束后自动关闭实况窗。

如何实现“通过指定实况窗最长存活时间实现自动关闭构建的实况窗

从6.1.1(24)版本起，为了在应用无法主动结束实况的情况下控制实况窗的最长存活时间，应用可在创建时，通过设置PrimaryData实例的aliveTime属性来实现自动关闭功能。

本地更新如何获取实况窗实例以及实况窗被清除后的限制

本地更新实况窗时，可以通过liveViewManager.getActiveLiveView函数获取活动的LiveView实例。

如果想要结束实况窗，建议使用liveViewManager.stopLiveView方法。如果实况窗被notificationManager.cancel或notificationManager.cancelAll清除后，无论是Live View Kit还是Push Kit，无法再次通过该id更新或结束实况窗。

再次创建该id的实况窗时，Live View Kit可以通过该id再次创建实况窗，Push Kit在12小时内无法通过该id再次创建实况窗。
