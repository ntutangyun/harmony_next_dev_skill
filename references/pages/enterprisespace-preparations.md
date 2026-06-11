# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-preparations_

环境准备

HarmonyOS系统：HarmonyOS 6.0.0 Release及以上。

DevEco Studio版本：DevEco Studio 6.0.0 Release及以上。

HarmonyOS SDK版本：HarmonyOS 6.0.0 Release SDK及以上。

申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

注册账号和企业开发者实名认证。

创建项目和创建HarmonyOS应用。

申请企业MDM应用发布证书和申请企业MDM应用发布Profile。

申请接口所需权限

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

## Code blocks

### Code block 1

```
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
```
