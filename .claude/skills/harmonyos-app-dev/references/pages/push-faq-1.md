# 如何处理推送消息时遇到的问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-1_

优先检查消息推送接口URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）是否正确。

请使用v3版本的推送接口URL，不要使用v1或v2版本的推送接口URL，详情请参见场景化消息中的请求URL版本问题。
请检查推送接口地址中的projectId，确保与您当前应用所属的项目保持一致，若不一致请更新推送接口URL中的projectId，并重新生成鉴权令牌，应用重新获取Push Token，再进行消息推送。

若调用消息推送接口返回了错误码，请参见业务响应码进行排查。

若调用消息推送接口返回成功，但设备未展示消息，请参见“如何处理云侧推送消息成功端侧消息未展示的问题”进行排查。

Push Kit常见问题
关于云侧接口推送成功但设备收不到推送消息的问题
