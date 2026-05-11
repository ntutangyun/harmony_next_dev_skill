# 配置应用

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-config-app_

工程“AppScope/app.json5”下的bundleName需要与开发者在AppGallery Connect中创建应用时的包名保持一致。

配置内容示例如下：

{
  "app": {
    // bundleName需要与开发者在AppGallery Connect中创建应用时的包名保持一致
    "bundleName": "com.huawei.***.***.demo",
    // ...
  }
}
配置应用身份信息

登录AppGallery Connect平台，在“开发与服务”中选择目标项目，通过“项目设置 > 常规 > 应用”获取目标应用的Client ID。

说明

下图中的APPID可用于服务器API接口请求。

如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者添加公钥指纹以及配置应用身份信息。

在工程“entry/src/main/module.json5”的module节点增加如下client_id属性配置，用于数字商品服务接口的应用身份鉴权。

"module":{
  "type": "***",
  "name": "***",
  "description": "***",
  "mainElement": "***",
  "deviceTypes": [***],
  // ...
  "metadata": [
  {
    "name": "client_id",
    "value": "***"
  },
  // ...
  ]
}
开通相关服务和配置参数
配置数字商品
