# 配置签名和指纹

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-sign-fingerprints_

检查是否需要配置公钥指纹：应用仅接入未成年人模式或compatibleSdkVersion>=20不需要配置公钥指纹，其他场景均需配置。

检查公钥指纹是否配置成功：请在开发与服务中选择对应的项目和应用，检查是否已成功配置该应用的公钥指纹。

公钥指纹最迟会在25小时后生效。

（可选） 配置公钥指纹10分钟后，您可通过修改应用工程中app.json5配置文件的versionCode触发公钥指纹生效。

图1 修改前

图2 修改后

申请账号权限
配置Client ID
