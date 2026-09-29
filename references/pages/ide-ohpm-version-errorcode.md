# ohpm version错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-version-errorcode_

00607001 参数无效

错误信息

Invalid Version Arg.

错误描述

参数无效。

可能原因

在模块目录中，执行ohpm version <newversion>时，输入非法的语义化版本，如ohpm version a.b.c。

处理步骤

检查配置的参数，确保newversion为一个合法的语义化版本。

00607002 版本号无效

错误信息

Invalid Origin Version.

错误描述

版本号无效。

可能原因

在模块级oh-package.json5文件中配置的version字段为非法的语义化版本，如"version": "a.b.c"。

处理步骤

修改模块级oh-package.json5文件中的version字段，确保其为合法的语义化版本。

00607003 版本号未配置

错误信息

Not Exist.

错误描述

版本不存在。

可能原因

未配置依赖包的版本号。

处理步骤

在oh-package.json5文件中添加version字段，并填写有效值。

00607004 版本号无变化

错误信息

No Change.

错误描述

无变化。

可能原因

模块级oh-package.json5中version字段未更改。如当前version为1.0.0，执行ohpm version 1.0.0命令。

处理步骤

检查模块级oh-package.json5中version的版本号，确保其与当前版本不同。

00607005 命令执行错误

错误信息

Forbidden Opt.

错误描述

禁止的操作。

可能原因

在项目根目录下执行ohpm version [options] [<newversion> | major | minor | patch]。

处理步骤

不支持在项目根目录下执行该命令，需要在模块下执行该命令。
