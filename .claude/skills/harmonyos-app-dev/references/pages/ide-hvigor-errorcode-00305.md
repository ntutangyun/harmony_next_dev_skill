# 语法错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00305_

用户手动删除编译后模块的.cxx目录，并且在build-profile.json5中arguments字段下配置“--version”、“

--help”、“--usage”等查询类参数。

处理步骤

删除arguments字段下的“--version”、“--help”、“--usage”等查询类参数。

00305013 存在无效的tag标签

错误信息

Invalid tag XXX at YYY.

错误描述

存在无效的tag标签。

可能原因

YYY文件中tag标签存在不符合要求的字符。

处理步骤

确保tag标签以字母或数字开头，长度不超过60个字符，只能由字母、数字、句点（.）、中划线（-）、下划线（_）组成，且不能配置为'latest'。

00305014 出现了“未知类型”错误

错误信息

A 'unknown type name' error has occurred.

错误描述

出现了“未知类型”错误。

可能原因

代码中存在类型未定义、未包含相关头文件或者头文件路径不正确。

处理步骤

根据以下指导排查：CPP编译报错“A 'unknown type name' error has occurred”。

00305015 解析错误

错误信息

以实际错误信息为准。

错误描述

以实际错误描述为准。

可能原因

通常为源码文件中路径解析错误。

处理步骤

根据错误提示信息修改。

资源缺失错误码
规格错误码
