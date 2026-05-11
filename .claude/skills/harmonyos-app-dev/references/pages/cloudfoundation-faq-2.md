# 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2_

upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

解决措施

出现此问题，可按照如下步骤排查和解决：

请确认应用的签名方式正确。当前Cloud Foundation Kit支持关联注册应用进行自动签名和手动签名两种方式。

请确认已通过AuthProvider获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。

使用云存储上传文件失败，提示“404:Product does not exist”
调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
