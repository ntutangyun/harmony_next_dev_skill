# 资源管理介绍及规格

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-resource-management-overview_

约定外部密钥管理扩展（例如Ukey）中使用resourceId唯一标识资源。该resourceId目前支持以下两种获取方式：

证书管理服务获取：通过查询证书操作返回。每个证书链对应1个resourceId。适用于浏览器双向SSL认证等需要证书选择的场景。

getResourceId接口获取：从API版本26.0.0开始，可通过getResourceId接口获取。适用于密钥生成、密钥导入等不需要证书选择的场景。

应用拿到resourceId后，需要打开资源，然后才可以进行后续密钥操作。操作完成后需要关闭资源。该接口会回调onClearUkeyPinAuthState清理该资源关联的PIN认证状态，以及会回调onFinishSession清理该资源关联的会话handle。

说明

操作密钥之前，必须先打开资源。如果涉及私钥签名等高权限操作，需要验证完PIN码后，才能继续执行，否则会导致资源状态异常。

用户操作之后，必须手动关闭资源，避免资源泄漏。
