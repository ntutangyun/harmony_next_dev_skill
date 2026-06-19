# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-prepare_

申请资质

在开发应用前，需要在AppGallery Connect中配置项目和应用信息。包括：

注册账号和企业开发者实名认证。

创建项目和创建HarmonyOS应用。

申请企业应用发布证书和申请企业应用发布Profile。

申请权限

在申请权限前，请保证符合权限使用的基本原则。随后在工程模块对应的module.json5配置文件中"requestPermissions"标签下声明实际所需的开发权限。使用病毒检测与处置能力，则应申请ohos.permission.SCAN_REMEDIATE_VIRUS权限，此权限仅面向企业杀毒软件开放申请。权限申请代码示例如下：

"requestPermissions": [
  {
    "name": "ohos.permission.SCAN_REMEDIATE_VIRUS"
  }
]

## Code blocks

### Code block 1

```
"requestPermissions": [
  {
    "name": "ohos.permission.SCAN_REMEDIATE_VIRUS"
  }
]
```
