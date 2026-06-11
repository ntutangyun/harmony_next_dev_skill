# 如果使用多网并发能力超过剩余配额限制，会发生什么

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-2_

配额（次数或时长）耗尽会限制使用，多网会自动释放，应用可以在netHandover.on('multiPathStateChange')中监听到多网退出回调。如果此时再请求多网会抛出错误码，应用可以在netHandover.requestMultiPath()的错误码中判断错误类型。应用配额以24小时的周期进行刷新。
