# 如何感知指纹登录中间认证失败结果

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-useriam-get-auth-result_

问题现象

指纹验证错误5次后回调错误码12500003并锁定认证，导致无法精准判断是否达到5次错误以自动关闭指纹登录功能。

背景知识

提供用户认证能力，应用于设备解锁、支付、应用登录等场景。

start接口用于开始认证流程。此接口需要配置ohos.permission.ACCESS_BIOMETRIC权限。

on('authTip')接口可用于订阅认证中间状态，例如认证失败、临时冻结（连续比对失败5次）。

解决方案

在手机设置中录入个人指纹，完成指纹验证功能设置。

申请权限：ohos.permission.ACCESS_BIOMETRIC。

查询认证能力是否支持，需要根据错误码的不同，给予用户不同的提示。

订阅认证中间状态和认证结果，并开始认证，根据返回的中间状态和结果进行对应处理。
