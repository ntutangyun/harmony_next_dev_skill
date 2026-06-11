# 移除已申请的权限

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-remove-permissions_

因应用功能调整或有其他变动时，如需移除应用已获取的某个权限，可参照下述方式执行操作。

在工程的module.json5中删除该权限的使用声明。

重新打包应用。

构建出来的应用将不包含该权限。

说明

对于受控开放权限、企业类应用可用权限、MDM应用可用权限这三类权限，应用重新打包后，Profile文件仍留存原有权限，不影响应用上架。平台审核将以module.json5中的权限设置为准。
