# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-preparations_

应用在使用Weather Service Kit能力前，需在应用的module.json5配置文件中声明所需权限。涉及的权限包括：

ohos.permission.INTERNET：用于请求对应天气相关数据。
{
  "module": {
    // ...
    "requestPermissions": [
    {
      "name": "ohos.permission.INTERNET",
      // ...
    }
    // ...
    ]
  }
}
配置Profile文件

在接口调用过程中，天气服务会对您的Profile文件进行鉴权。因此，您需要在开通天气服务后，按照配置签名信息的流程，申请并配置签名信息。

（可选）申请位置权限

获取用户当前位置的天气数据，需要调用Location Kit（位置服务）获取当前位置经纬度信息，使用前参考申请权限。

Weather Service Kit简介
获取天气数据
