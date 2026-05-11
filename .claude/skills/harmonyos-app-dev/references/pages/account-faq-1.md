# 1001500001 应用指纹证书校验失败的可能原因和解决办法

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-1_

检查module type为entry的模块下的module.json5配置文件中的Client ID是否正确，请参考配置Client ID。

检查AppGallery Connect上是否正确配置应用的指纹证书，详情请见添加公钥指纹。

证书更换后，重新配置更换后的证书指纹。

配置公钥指纹10分钟后，您可通过修改应用工程 > app.json5中的versionCode触发公钥指纹生效。具体修改方法见下图所示。

调试证书切换为发布证书或发布证书切换为调试证书，需要升级应用的版本号（修改应用工程 > app.json5中的versionCode），具体修改方法见下图所示。

图1 修改前

图2 修改后

请使用手动签名方式进行签名，详情请参考配置签名和指纹章节。

Account Kit常见问题
1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
