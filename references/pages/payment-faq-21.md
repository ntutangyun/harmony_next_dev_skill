# 请求接口加签验证中，如果请求头“PayMercAuth”中bodySign字段为空值，会做验签吗？还是会先校验字段？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-21_

鉴权请求头“PayMercAuth”会先校验相关字段再做验签。bodySign字段设置为空值，Payment Kit服务器不会做验签，直接响应异常给商户。

请求头PayMercAuth中的callerId和请求体中的mercNo或者combineMercNo是什么关系？
不更换商户订单号重复发起退款，返回000000，不返回退款金额的原因是什么？
