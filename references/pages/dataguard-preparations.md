# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataguard-preparations_

环境准备

HarmonyOS系统：HarmonyOS NEXT Developer Beta1及以上。

DevEco Studio版本：DevEco Studio NEXT Developer Beta1及以上。

HarmonyOS SDK版本：HarmonyOS NEXT Developer Beta1 SDK及以上。

申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

注册账号和企业开发者实名认证。

创建项目和创建HarmonyOS应用。

申请企业MDM应用发布证书和申请企业MDM应用发布Profile。

申请权限

在申请权限前，请确保符合权限使用的基本原则。然后在工程模块对应的module.json5配置文件中"requestPermissions"标签下申请实际所需的开发权限。

应用能力	需要权限
文件分级管控	ohos.permission.FILE_GUARD_MANAGER ohos.permission.SET_FILE_GUARD_POLICY
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

## Code blocks

### Code block 1

```
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
```
