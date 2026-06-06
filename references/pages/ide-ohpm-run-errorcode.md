# ohpm run错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-run-errorcode_

脚本中包含多个用逻辑符（||、&&）连接的ohpm命令，如"testLogic": "ohpm run testFail || ohpm run testSuc && ohpm run testSuc"。

处理步骤

脚本中仅包含一个ohpm命令。

00611009 包解析失败

错误信息

Parse Pkg Error.

错误描述

解析包失败。

可能原因

oh-package-lock.json5文件格式不正确。

处理步骤

检查oh-package-lock.json5文件是否符合规定的格式，具体请参考oh-package.json5。

00611010 prefix命令执行失败

错误信息

Prefix Invalid Error.

错误描述

--prefix选项错误。

可能原因

指定路径下未包含oh-package.json5文件。

处理步骤

确认指定路径下包含oh-package.json5文件。

00611011 未能找到指定的包管理配置文件

错误信息

Pkg UnExist Error.

错误描述

未能找到指定的包管理配置文件。

可能原因

当前目录中不存在oh-package.json5文件。

处理步骤

确保当前目录中存在oh-package.json5文件。

00611012 脚本别名不存在

错误信息

Script UnExist Error.

错误描述

脚本别名不存在。

可能原因

执行脚本别名未在oh-package.json5文件中声明。

处理步骤

检查oh-package.json5文件，确保脚本别名已正确声明并且格式正确。

00611013 脚本内容为空

错误信息

Script Empty Error.

错误描述

执行脚本为空错误。

可能原因

脚本内容为空。

处理步骤

检查脚本内容，确保其包含有效命令。

00611014 脚本内容无效

错误信息

Script Invalid Error.

错误描述

脚本无效错误。

可能原因

脚本内容无效。

处理步骤

检查脚本内容，确保已正确配置。

00611015 脚本内容错误

错误信息

Script Content Error.

错误描述

脚本内容错误。

可能原因

如果别名中引用了 -- 标识符，则只能执行一个ohpm run命令。

处理步骤

检查脚本别名的配置，确保 -- 标识符仅用于单个ohpm run命令。

00611016 循环调用

错误信息

Directed Cycle Error.

错误描述

循环调用无法正常执行脚本。

可能原因

脚本包含循环调用，如"scriptName1": "ohpm run scriptName2","scriptName2": "ohpm run scriptName2"。

处理步骤

检查脚本配置，确保脚本调用关系无循环。

00611017 脚本参数不正确

错误信息

Invalid Header Param Error.

错误描述

脚本参数不正确。

可能原因

脚本参数以-或--开头，如ohpm run scriptName1 -- arg1=1 --arg2=2。

处理步骤

检查脚本参数，确保-或--开头，如--debug。

00611018 无效参数

错误信息

Invalid Param Error.

错误描述

无效参数。

可能原因

使用了无效参数。

处理步骤

检查脚本参数格式，参数以短横线-或双短横线--开头，后跟参数名称和对应的值，确保其符合要求，如：--key value（如script --name Alice）、--key=value（如script --age=25）、--key=a=b（如script --config=a=b,c=d）。

00611019 传递参数配置无效

错误信息

Invalid Param Config Error.

错误描述

配置无效参数。

可能原因

配置传递参数命令时，未以-- 开头。

处理步骤

传递参数配置时，确保以--开头，以指示需要添加或覆盖的参数。具体请参考传递参数。

ohpm cache clean错误码
ohpm ping错误码
