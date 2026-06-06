# 运行应用时提示“appid **** is not in white list, to skip”

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-3_

确认日志中提示的APP ID前缀与云侧创建应用的实际APP ID是否一致。若两者不一致，可能使用了错误的签名方式。请更改为关联注册应用进行自动签名或者手动签名方式。

手机端进入“设置->系统->日期和时间”，关闭“自动设置”开关，将“日期”往后加1天，然后卸载应用重新安装，应用会自动更新白名单。

如何通过应用侧日志定位预加载问题
运行应用时报“XXX Read timed out”异常
