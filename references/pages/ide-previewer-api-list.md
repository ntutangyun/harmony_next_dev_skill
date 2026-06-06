# 支持使用预览器的API清单

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-api-list_

如果Http请求需要配置代理才能访问，API 12及以上的预览器支持使用系统的http_proxy/https_proxy/no_proxy环境变量。

数据管理

模块

	

API




@ohos.data.preferences (用户首选项)

	

data_preferences.getPreferences




data_preferences.deletePreferences




data_preferences.removePreferencesFromCache




Preferences




ValueType

文件管理

从DevEco Studio 6.0.0 Beta5版本开始，仅支持在预览/预览调试Stage模型的HAP/HSP时，使用文件管理的相关API，并且需要先打开Enable file operation开关。

模块

	

API




@ohos.file.fs (文件管理)

	

fs.open




fs.close




fs.fdatasync




fs.fsync




fs.read




fs.write




fs.mkdir




fs.mkdtemp




fs.rename




fs.rmdir




fs.unlink




fs.stat




fs.truncate

使用预览器调试应用
配置调试签名
