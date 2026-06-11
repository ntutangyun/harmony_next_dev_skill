# 应用处于后台时应用内如何接收消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-9_

应用处于后台时仅有如下两个场景可以在应用内接收消息：

若应用需要实现语音播报等能力时，服务端可发送语音播报消息（即push-type为2）。该场景中客户端应用内消息接收请参考RemoteNotificationExtensionAbility中接口调用示例。

若应用需要实现网络音视频通话能力时，服务端可发送应用内通话消息（即push-type为10）。该场景中客户端应用内消息接收请参考VoIPExtensionAbility中接口调用示例。

当应用处于内容不频繁更新，不会显示通知、播放铃声或改变应用角标场景时，服务端可发送后台消息（即push-type为6），若proxyData为“ENABLE”时，Push Kit将后台消息写入到数据库中，不会拉起应用进程。
