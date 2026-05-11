# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/development-preparation_

在模块的module.json5中配置所需申请的权限，其中跨应用关联权限ohos.permission.APP_TRACKING_CONSENT为user_grant权限，reason和abilities标签必填，配置方式参见requestPermissions标签说明。

示例代码如下所示：

{
  "module": {
    "requestPermissions": [
      {
        "name": "ohos.permission.APP_TRACKING_CONSENT",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when": "inuse"
        }
      },
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
Ads Kit术语
流量变现服务开发
