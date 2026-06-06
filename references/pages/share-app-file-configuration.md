# 应用共享目录配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-app-file-configuration_

从API version 23开始，系统新增支持共享目录配置功能。在应用文件分享场景中，开发者可配置共享目录范围，防止应用敏感数据泄露。

开发步骤

开发者可在应用模块级配置文件src/main/module.json5的module标签中添加shareFiles标签，以实现对沙箱共享目录权限的限制。若未配置共享目录，则默认允许应用共享其自身沙箱内的文件。

shareFiles标签

{
  "module": {
    // ...
    "shareFiles": "$profile:share_files", // 资源配置，指向profile下面定义的配置文件share_files.json
    // ...
  }
}

在开发视图的resources/base/profile下面定义配置文件share_files.json，以标识当前模块所有共享路径的权限信息。

文件名share_files可修改为任意合法文件名，但需要和shareFiles标签配置的文件名一致。

share_files标签说明

属性名称	含义	数据类型	必填
scopes	允许共享的范围，详见scopes标签说明。	对象数组	否

scopes标签说明

属性名称	含义	数据类型	必填
path	

共享路径配置，当前仅支持el2目录，scopes中的path不可重复。支持的取值如下：

- /base/files

- /base/preferences

- /base/haps

	string	scopes存在时必填
permission	

共享路径权限。支持的取值如下：

- r：只读。

- r+w：读写。

	string	scopes存在时必填
说明

应用更新时如涉及配置变更，将依据新配置进行管控，已分享文件的临时权限不受影响。

share_files.json示例：

{
  "share_files": {
    "scopes": [
      {
        "path": "/base/files",
        "permission": "r+w"
      }
    ]
  }
}
应用文件分享
应用数据备份恢复
