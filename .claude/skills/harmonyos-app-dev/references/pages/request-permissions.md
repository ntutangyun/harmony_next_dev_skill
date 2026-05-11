# 申请授权

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-permissions_

在开发过程中，开发者首先需要明确涉及的敏感权限，并在config.json中声明这些权限。然后在运行时通过requestPermissionsFromUser接口，以动态弹窗的方式向用户申请授权。

在config.json声明需要的权限，在module下添加"reqPermissions"，并写入对应权限。

例如申请访问日历权限：

需要申请ohos.permission.DISTRIBUTED_DATASYNC权限，配置方式请参见声明权限。
同时需要在应用首次启动时弹窗向用户申请授权，使用方式请参见向用户申请授权。
窗口属性
跳转规则
