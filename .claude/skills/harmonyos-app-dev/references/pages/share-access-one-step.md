# 目标设备接收分享数据一步直达体验

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-one-step_

一步直达	自定义类型（除系统已预置的utd类型之外）	文件管理“华为分享”目录。	有可打开应用直接打开，无可打开应用弹出提示。
沙箱接收	仅支持文件类型（包含系统已预置的文件类型及自定义类型文件）	应用沙箱指定目录。	应用自行处理预览方式。
指定应用直达

从6.0.0(20) Beta3版本开始，碰一碰分享支持指定应用拉起的能力。

除以上系统默认直达方式外，同开发者账号下应用支持以下拉起规则：

同包名应用优先直达。若接收端已安装和发送端相同的应用，且支持拉起（满足隐式匹配原理）该应用，则优先拉起同包名应用。

同开发者账号(developerId相同)下的应用可通过module.json5配置文件配置实现优先拉起指定应用。

能力限制

仅支持同开发者账号（developerId相同）下的应用。

不支持媒体类文件和压缩包类型的分享数据。

不支持多文件（2个及以上）的分享数据。

仅支持碰一碰分享能力。

配置示例

通过在配置文件（src/main/module.json5）中配置metadata标签实现。

shareType：用于分组匹配，当发送端应用和接收端应用配置相同的shareType值时，匹配规则才可生效。仅支持配置一项，配置多项时，仅第一项生效。

shareBundleName：指定打开应用的包名，可配置多项。当shareType相同时，按数组排列顺序匹配第一个已安装且支持拉起（满足隐式匹配原理）的应用，并优先拉起该应用。

{
  "module": {
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "startWindowIcon": "$media:launcher",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": [
              "entity.system.home",
            ],
            "actions": [
              "ohos.want.action.viewData"
            ],
            "uris": [
              {
                "scheme": "file",
                "linkFeature": "FileOpen",
                "type": "org.openxmlformats.wordprocessingml.document",
                "maxFileSupported": 1
              }
            ],
            "domainVerify": true
          }
        ]
      },
    ],
    "metadata": [
      {
        "name": "shareType",
        "value": "sharekitModel",
      },
      {
        "name": "shareBundleName",
        "value": "com.example.sharekitPhone",
      },
      {
        "name": "shareBundleName",
        "value": "com.example.sharekitPc",
      }
    ]
  }
}
宿主应用发起分享需使用精细化的utd类型
系统分享
