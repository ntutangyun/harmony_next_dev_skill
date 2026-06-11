# 三方支付问题处理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-third-party-faq_

接入微信H5 支付，支付完成后会停留在微信里面，没有自动返回应用，需要用户手动返回？

支付完成需回调页面可参见这里。

目前deeplink拉起微信支付时，支付成功后可能停留在微信支付界面，无法自动返回应用。可通过基于接口拉起方式拉起三方支付收银台，支持微信支付成功后自动关闭并返回应用。
