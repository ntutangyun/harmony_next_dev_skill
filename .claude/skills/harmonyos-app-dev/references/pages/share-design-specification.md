# 目标应用设计规范

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-design-specification_

当应用实现了用于接收分享内容的UIAbility或者UIExtensionAbility后，可在配置文件（src/main/module.json5）的skills配置中注册。并配置actions为ohos.want.action.sendData。

当分享内容类型为应用所支持的类型时，应用图标将出现在分享面板的分享方式区内。

应用可以针对不同的ability，设置不同的名称和图标。

示例：

"abilities": [
  {
    "name": "TestUIAbility",
    "srcEntry": "./ets/entryability/TestUIAbility.ets",
    "label": "$string:EntryAbility_label", // ability名称
    "icon": "$media:layered_image", // ability图标
    "description": "$string:EntryAbility_desc",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "skills": [
      {
        "actions": [
          "ohos.want.action.sendData"
        ],
        "uris": [
          {
            "scheme": "file",
            "utd": "general.text",
            "maxFileSupported": 1
          }
        ]
      }
    ]
  }
],
"extensionAbilities": [
  {
    "name": "TestShareAbility",
    "srcEntry": "./ets/abilities/TestShareAbility.ts",
    "type": "share", // 支持分享数据处理
    "exported": true,
    "label": "$string:xx_label", // ability名称
    "icon": "$media:icon", // ability图标
    "description": "$string:TestShareAbility_desc",
    "skills": [
      {
        "actions": [
          "ohos.want.action.sendData"
        ],
        "uris": [
          {
            "scheme": "file",
            "utd": "general.text",
            "maxFileSupported": 1
          }
        ]
      }
    ]
  }
]
共享联系人信息到分享推荐区
常见分享场景
