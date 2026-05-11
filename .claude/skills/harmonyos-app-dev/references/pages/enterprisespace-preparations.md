# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-preparations_

在申请权限前，请保证符合权限使用的基本原则。并且在工程模块对应的module.json5配置文件中"requestPermissions"标签下声明所需的权限。

表1 权限说明

应用能力	使用场景	需要权限
空间互传	使用空间互传API设置、获取审计信息。	ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT
空间管理	下发空间生命周期策略需要申请该权限。	ohos.permission.ENTERPRISE_MANAGE_LOCAL_PUBLICSPACES
空间管理	查询空间信息需要申请该权限。	ohos.permission.QUERY_LOCAL_WORKSPACES
空间管理	企业应用订阅企业数字空间相关事件需要申请该权限。	ohos.permission.ENTERPRISE_WORKSPACES_EVENT_SUBSCRIBE

示例：

"requestPermissions": [
  {
    "name": "ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT"
  },
  {
    "name": "ohos.permission.ENTERPRISE_MANAGE_LOCAL_PUBLICSPACES"
  },
  {
    "name": "ohos.permission.QUERY_LOCAL_WORKSPACES"
  },
  {
    "name": "ohos.permission.ENTERPRISE_WORKSPACES_EVENT_SUBSCRIBE"
  }
]
Enterprise Space Kit简介
空间互传
