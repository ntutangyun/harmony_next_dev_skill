# 添加Ability

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-ability_

Ability是应用/元服务所具备的能力的抽象，应用的一个Module可以包含一个或多个Ability，元服务仅包含一个Ability。应用/元服务先后提供了两种应用模型：

FA（Feature Ability）模型： API 7开始支持的模型，已经不再主推。

Stage模型包含两种Ability组件类型：

UIAbility组件：包含UI界面，提供展示UI的能力，主要用于和用户交互。详细介绍请参见UIAbility组件概述。

ExtensionAbility组件：提供特定场景的扩展能力，满足更多的使用场景。详细介绍请参见ExtensionAbility概述。元服务暂不支持使用ExtensionAbility组件。

Stage模型添加Ability

[h2]在模块中添加UIAbility

选中对应的模块，单击鼠标右键，选择New > Ability。

[h2]在模块中添加Extension Ability

从DevEco Studio 6.1.0 Beta2版本开始，支持在API 23及以上Car设备工程的模块中添加RemoteNotificationAbility。

EmbeddedUIExtensionAbility：用于提供跨进程界面嵌入的能力。

BackupAbility：用于提供备份及恢复应用数据的能力。

WorkScheduler：用于提供延迟任务的相关能力。

RemoteNotificationAbility：用于提供获取场景化消息数据和生命周期销毁的回调的通知能力，当前仅支持在Phone、Tablet、2in1、Car设备中使用。

Driver：用于提供驱动相关扩展框架。仅在当前工程的设备类型只含有2in1设备时，支持创建该类型。

EmbeddedUIExtensionAbility：用于提供跨进程界面嵌入的能力。

WorkScheduler：用于提供延迟任务的相关能力。

FA模型添加Ability

[h2]创建Particle Ability

Ability name：Ability类名称，由大小写字母、数字和下划线组成。

Language：该Ability使用的开发语言。

单击Finish完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。

[h2]创建Feature Ability

Ability name：Ability类名称，由大小写字母、数字和下划线组成。

Launcher ability：表示该Ability在终端桌面上是否有启动图标，一个HAP可以有多个启动图标，来启动不同的FA。

Language：该Ability使用的开发语言。

单击Finish完成Ability的创建，可以在工程目录对应的模块中查看和编辑Ability。
