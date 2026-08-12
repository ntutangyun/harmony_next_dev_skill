# 指纹登录怎么检测设备指纹是否发生变化

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-useriam-fingerprint-change_

问题现象

出于安全风险管控需求，当设备指纹信息发生变更时，系统需禁用指纹登录功能。本文将介绍如何检测指纹变更。

背景知识

UserAuthenticationKit（用户认证服务）提供了基于用户在设备本地注册的锁屏口令、人脸和指纹来认证用户身份的能力。

userAuth.getEnrolledState接口提供查询凭据注册状态的能力，其返回值EnrolledState表示用户注册凭据的状态。结构如下：

名称	类型	说明
credentialDigest	number	注册的凭据摘要，在凭据增加时随机生成。
credentialCount	number	注册的凭据数量。

解决方案

业务在首次开通指纹登录时，指定了认证类型（UserAuthType），调用getEnrolledState接口查询用户凭据的状态，并将该状态储存。

当调用者需要感知用户凭据变化时，取出上次存储的凭据状态，与当前调用getEnrolledState接口获取的用户注册凭据状态做对比。若不同则说明指纹发生变更，处理完成后更新存储凭据状态覆盖原状态。凭据状态对比规则如下：

credentialDigest和credentialCount均相同，说明本机指纹未发生变化。

credentialDigest不同，无论credentialCount是否相同，说明本机指纹有新增或变更。

credentialDigest不变，credentialCount减小，说明本机指纹有删除。

用户认证完整代码示例请参考用户身份认证开发步骤。
