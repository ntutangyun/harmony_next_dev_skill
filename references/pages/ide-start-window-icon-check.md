# @performance/start

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-start-window-icon-check_

1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon

2、entry/src/main/resources/base/media目录下对应的图片文件分辨率小于等于256*256

反例

1、entry/src/main/module.json5中的mainElement对应的ability中配置了startWindowIcon

2、entry/src/main/resources/base/media目录下对应的图片文件分辨率大于256*256

规则集
plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/sparse-array-check
@performance/state-variable-usage-in-ui-format-check
