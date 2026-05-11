# ohpm install错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-install-errorcode_

工程级build-profile.json5文件中useNormalizedOHMUrl或 .ohpmrc文件中enforce_dependency_key设置为true后，ohpm会校验配置的本地依赖名称与其对应的包名是否一致，若不一致会导致命令执行失败。

处理步骤

检查依赖项列表，确保所有依赖项中包名与实际包名一致。

00604007 必选字段为空错误

错误信息

Field IS Empty Error.

错误描述

Field必选字段为空错误。

可能原因

oh-package.json5中必填字段未填。

处理步骤

检查oh-package.json5中必填字段，确保其包含有效值。

00604008 未找到最大的依赖版本

错误信息

Internal Program Error.

错误描述

未找到最大版本。

可能原因

有多个依赖版本时，未找到最大版本。

处理步骤

检查包依赖关系，确保没有依赖包冲突或不兼容的情况。具体请参考模块内依赖版本冲突。

00633001 在命令行中指定的路径不存在

错误信息

Target Path UnExist Error.

错误描述

在命令行中指定的路径不存在。

可能原因

当使用--target_path选项时，指定的target_path不存在或不正确错误。

处理步骤

检查命令行，确保目标路径存在并且正确，更多说明请参考target_path。

00622020 输入的parameterFile文件或地址不存在

错误信息

Option Specified Parameter File Not Found.

错误描述

parameterFile未找到。

可能原因

配置的parameterFile文件或地址不存在错误。

处理步骤

检查和确保parameterFile文件路径正确。

00638002 包名不规范

错误信息

Invalid Group Option.

错误描述

包名不规范。

可能原因

包名的第一个字符必须是小写字母（a-z），且只能包含小写字母（a-z）、数字（0-9）、中划线（-）和下划线（_），长度不超过36个字符。

处理步骤

检查包名，确保正确。

ohpm info错误码
ohpm list错误码
