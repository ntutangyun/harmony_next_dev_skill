# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-preparations_

在申请权限前，请确保符合权限使用的基本原则。然后在工程模块对应的module.json5配置文件中"requestPermissions"标签下申请实际所需的开发权限。

应用能力	需要权限
文件分级管控	

ohos.permission.FILE_GUARD_MANAGER

ohos.permission.SET_FILE_GUARD_POLICY


企业恢复密钥	ohos.permission.ENTERPRISE_RECOVERY_KEY

例如：

"requestPermissions": [
  {
    "name": "ohos.permission.FILE_GUARD_MANAGER"
  },
  {
    "name": "ohos.permission.SET_FILE_GUARD_POLICY"
  },
  {
    "name": "ohos.permission.ENTERPRISE_RECOVERY_KEY"
  }
]
Enterprise Data Guard Kit简介
文件分级管控
