# 集成游戏资源加速ExtensionAbility方法，未配置游戏资源加速ExtensionAbility组件类型信息，导致功能未生效

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-2_

bundle[xxx] do not have Asset Acceleration Extension Ability.

请开发者在“src/main/module.json5”的extensionAbilities层级中添加资源加速ExtensionAbility信息。

"extensionAbilities": [
  {
    "name": "AssetAccelExtAbility", // 游戏资源加速ExtensionAbility组件的名称。
    "srcEntry": "./ets/extensionability/AssetAccelExtAbility.ets", // 游戏资源加速ExtensionAbility组件所对应的代码路径。
    "type": "assetAcceleration"
  }
]
上传至华为CDN的资源包文件支持哪些格式类型
集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效
