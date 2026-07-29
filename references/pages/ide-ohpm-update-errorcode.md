# ohpm update错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-update-errorcode_

00606001 执行命令时带版本号

错误信息

Has Version.

错误描述

update时带版本号。

可能原因

执行ohpm update library时带版本号，如ohpm update library@2.0.0。

处理步骤

更新命令中不应包含版本号，仅指定包名ohpm update library。

00606002 执行tag-filter命令时使用非标准的正则

错误信息

Tag Filter Non Standard Regex.

错误描述

tag-filter命令使用非标准正则。

可能原因

执行ohpm update --tag-filter <regex>命令时，使用非标准正则。如ohpm update library --tag-filter [a-z，其中 [a-z 表示非法正则表达式，正确正则参数为[a-z]。

处理步骤

检查和修改为标准正则。
