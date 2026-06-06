# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-prepare_

在申请权限前，请保证符合权限使用的基本原则。随后在工程模块对应的module.json5配置文件中"requestPermissions"标签下声明实际所需的开发权限。使用文件访问与处置能力，则应申请ohos.permission.SCAN_REMEDIATE_VIRUS权限，此权限仅面向企业杀毒软件开放申请。权限申请代码示例如下：

"requestPermissions": [
  {
    "name": "ohos.permission.SCAN_REMEDIATE_VIRUS"
  }
]
Enterprise Threat Protection Kit简介
文件访问与处置
