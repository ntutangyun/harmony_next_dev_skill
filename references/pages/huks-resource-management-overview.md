# 资源管理介绍及规格

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-resource-management-overview_

约定外部密钥管理扩展（例如Ukey）中使用resourceId唯一标识资源。该resourceId目前支持通过查询证书操作返回。每个证书链对应1个resourceId。应用拿到resourceId后，需要打开资源，然后才可以进行后续密钥操作。操作完成后需要关闭资源。

说明
操作密钥之前，必须先打开资源。如果涉及私钥签名等高权限操作，需要验证完PIN码后，才能继续执行，否则会导致资源状态异常。
用户操作之后，必须手动关闭资源，避免资源泄漏。
资源管理
打开资源/关闭资源(C/C++)
