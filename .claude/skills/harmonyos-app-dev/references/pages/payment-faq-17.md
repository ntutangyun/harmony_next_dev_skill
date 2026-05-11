# 商户侧没有传营销信息，支付回调里面为什么会有营销信息？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-17_

营销活动不需要商户侧传递，拉起收银台前华为支付会根据用户和商户去获取华为支付侧配置的营销活动信息展示在收银台，若用户使用了营销活动，支付结果就会返回营销信息。

商户提供的回调通知接口在Payment Kit生产环境需要加网络允许清单吗？如何验证提供的回调地址Payment Kit服务器访问是否正常？
App和元服务接口入参除了appId不同，其他如商户号、证书、密钥这些可以使用相同的吗？
