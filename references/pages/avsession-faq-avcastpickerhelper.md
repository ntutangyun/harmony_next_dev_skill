# 使用AVCastPickerHelper接口常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-faq-avcastpickerhelper_

本文汇总音视频应用在使用AVCastPickerHelper接口过程中遇到的典型问题及其定位与解决方法。开发者可结合媒体会话管理错误码和HiLog日志进一步定位问题。

pickerStateChange监听回调被重复触发

问题现象

注册了多次on('pickerStateChange')，每次状态变化都收到多个回调。

可能原因

若未先注销旧监听而重复调用on('pickerStateChange')，新旧监听均会触发回调。

解决措施

若只需执行最新监听，请先调用off('pickerStateChange')注销已有监听后，再重新注册。
