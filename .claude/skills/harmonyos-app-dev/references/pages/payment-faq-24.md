# 下载账单文件后，应该使用哪种格式来解析日期？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-24_

不建议用Excel文件格式去解析，Excel打开后可能会被默认格式化处理，导致通过Excel打开文件后，单元格日期格式显示为 “yyyy/MM/dd HH:mm”，双击后显示 “yyyy/MM/dd HH:mm:ss”，以“yyyy/MM/dd HH:mm:ss”格式解析不出来，以“yyyy/MM/dd HH:mm”格式可以解析。

建议使用csv文件格式，yyyy/MM/dd HH:mm:ss时间格式做解析。

Payment Kit的退款操作，除了通过接入指导中的退款接口退款，还有财务功能相关平台吗？能从这个平台进行退款？
收银台支付报错“应用信息校验不通过，请联系商家处理”？
