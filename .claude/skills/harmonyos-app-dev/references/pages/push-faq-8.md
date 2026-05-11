# 场景化消息中的请求URL版本问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-8_

场景化消息请求体结构中，请求URL版本为V3（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）时，仅支持给HarmonyOS Next/5.x及之后的系统版本推送通知；版本为V2（https://push-api.cloud.huawei.com/v2/[projectId]/messages:send）时，仅支持给HarmonyOS 3.x/4.x的系统版本推送通知。

请使用V3版本的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。

应用内通话消息来电横幅问题
应用处于后台时应用内如何接收消息
