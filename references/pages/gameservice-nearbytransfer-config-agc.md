# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc_

创建游戏

若在华为应用市场发布游戏，或使用AGC控制台提供的服务，需要前往AGC控制台创建游戏类应用，具体操作请参见创建项目和创建HarmonyOS应用。其中：

“应用类型”：选择“HarmonyOS应用”。

“应用分类”：选择“游戏”。

生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性，请参见配置签名信息完成配置。

配置APP ID和相关权限

登录AppGallery Connect平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的APP ID。

在工程的entry模块module.json5文件中，新增metadata并配置app_id，同时新增requestPermissions并配置如下权限。

"module": {
  "name": "entry",
  "type": "entry",
  "description": "xxxx",
  "mainElement": "xxxx",
  "deviceTypes": [
    "phone"
  ],
  "deliveryWithInstall": true,
  "pages": "$profile:main_pages",
  "abilities": [],
  "metadata": [ // 配置如下信息
    {
      "name": "app_id",
      "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
    }
  ],
   "requestPermissions": [ // 配置权限
     {
       "name": "ohos.permission.INTERNET" // 允许使用Internet网络权限
     },
     {
       "name": "ohos.permission.GET_NETWORK_INFO"  // 允许应用获取数据网络信息权限
     },
     {
       "name": "ohos.permission.SET_NETWORK_INFO" // 允许应用配置数据网络权限
     },
     {
       "name": "ohos.permission.DISTRIBUTED_DATASYNC", // 允许不同设备间的数据交换权限
       "reason": "$string:distributed_permission",
       "usedScene": {
         "abilities": [
           "EntryAbility"
         ],
         "when": "inuse"
       }
     }
   ]
}

## Code blocks

### Code block 1

```
"module": {
  "name": "entry",
  "type": "entry",
  "description": "xxxx",
  "mainElement": "xxxx",
  "deviceTypes": [
    "phone"
  ],
  "deliveryWithInstall": true,
  "pages": "$profile:main_pages",
  "abilities": [],
  "metadata": [ // 配置如下信息
    {
      "name": "app_id",
      "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
    }
  ],
   "requestPermissions": [ // 配置权限
     {
       "name": "ohos.permission.INTERNET" // 允许使用Internet网络权限
     },
     {
       "name": "ohos.permission.GET_NETWORK_INFO"  // 允许应用获取数据网络信息权限
     },
     {
       "name": "ohos.permission.SET_NETWORK_INFO" // 允许应用配置数据网络权限
     },
     {
       "name": "ohos.permission.DISTRIBUTED_DATASYNC", // 允许不同设备间的数据交换权限
       "reason": "$string:distributed_permission",
       "usedScene": {
         "abilities": [
           "EntryAbility"
         ],
         "when": "inuse"
       }
     }
   ]
}
```
