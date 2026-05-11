# 收银台支付报错“应用信息校验不通过，请联系商家处理”？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-25_

本地调试的签名证书配置是否为手动签名并且是从AppGallery Connect下载的，参见应用/服务手动签名。证书下载后，可打开调试Profile（.p7b）文件，搜索“app-identifier”字段，如果对应的值和预下单请求或orderStr中传递的appId不一致，则证书生成错误，需重新生成证书及配置。

检查是否配置添加了公钥指纹，参见添加公钥指纹。

检查一下orderStr中merc_no、app_id、auth_id等参数是否正确，merc_no和auth_id是否匹配。

服务商模式接入，切换到商户应用/元服务拉起收银台时，需要把app_id改成商户相应的appId，并在平台类商户/服务商预下单接口通过subAppId字段同步传递。

使用“hdc hilog > 日志路径”抓取运行日志，参考错误码及日志来分析具体的报错异常。

下载账单文件后，应该使用哪种格式来解析日期？
商户号绑定AppID提示“主体不一致”？
