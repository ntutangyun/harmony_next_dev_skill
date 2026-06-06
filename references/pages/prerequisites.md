# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/prerequisites_

在开发具备用户身份认证的应用前，需要先申请权限ohos.permission.ACCESS_BIOMETRIC，应用才能使用生物特征识别能力（如人脸、指纹）进行身份认证。

该权限授权方式为system_grant（系统授权），开发者只需要在module.json5配置文件的requestPermissions标签中声明权限，即可获取系统授权。具体声明指导请参考申请应用权限-声明权限。

用户身份认证开发指导
查询支持的认证能力
