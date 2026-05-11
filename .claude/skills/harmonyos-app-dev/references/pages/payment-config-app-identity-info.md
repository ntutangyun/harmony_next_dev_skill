# 端侧应用配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-app-identity-info_

在HarmonyOS应用/元服务“AppScope/app.json5”下的bundleName配置需要与开发者在AppGallery Connect中创建应用时的包名保持一致。

配置内容示例如下：

{
  "app": {
    "bundleName": "com.huawei.******.******.demo",
  }
}
配置应用属性

在HarmonyOS应用/元服务“entry/src/main/module.json5”文件中module的metadata节点下增加client_id和app_id属性配置。

配置内容示例如下：

{
    "module": {
        "metadata": [
            {
                "name": "app_id",
                "value": "..."
            },
            {
                "name": "client_id",
                "value": "..."
            },
        ]
    }
}

其中app_id的value值为应用的APP ID（在AppGallery Connect网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“APP ID”的值），详见下图的标号1处。

其中client_id的value值为应用的OAuth 2.0客户端ID（在AppGallery Connect网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“OAuth 2.0客户端ID（凭据）：Client ID”的值），详见下图的标号2处。

准备证书
云侧服务准备
