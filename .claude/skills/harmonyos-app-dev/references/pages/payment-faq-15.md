# 同一次支付请求接收到多次回调通知，怎么解决？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-15_

同一次支付请求接收到多次回调是开发者返回的响应报错，导致重试。请检查返回的响应格式是不是application/json以及响应的报文是不是 {"resultCode":"000000","resultDesc":"Success."} ，具体可参考通知回调接口说明。

自验证回调接口是否可正常接收响应，如Payment Kit服务器请求响应连接超时也会触发重试回调。

部分提供通知回调的API接口中的callbackUrl参数是否可以自定义？回调通知的报文是否支持商户自定义？
商户提供的回调通知接口在Payment Kit生产环境需要加网络允许清单吗？如何验证提供的回调地址Payment Kit服务器访问是否正常？
