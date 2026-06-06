# （可选）数字人民币接入准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-digital-cny-pay-preparations_

数字人民币支付仅支持通过运营机构或受理服务机构申请的商户接入，在开发前需要先完成商户入网（可拨打数字人民币客服热线956196根据指引完成商户入网）。

商户入网后，数字人民币的运营机构会分配对应的商户号和APPID，商户号和APPID是开放API接口请求的必要入参。

应用配置

在构建的开发者应用/元服务“entry/src/main/module.json5”文件中添加钱包schemes配置信息，配置内容示例如下：

{
  "module": {
    "querySchemes": [
      "wallet"
    ]
  }
}
云侧服务准备
（可选）用户身份验证服务接入准备
