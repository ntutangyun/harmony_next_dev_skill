# ohpm命令公共错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-errorcode-universal_

00617101 获取包信息失败

错误信息

Fetch Pkg Info Failed.

错误描述

获取包信息失败。

可能原因

未配置仓库地址。

处理步骤

在.ohpmrc文件中配置registry字段，或执行命令"ohpm config set registry https://ohpm.openharmony.cn/ohpm/"配置仓库地址。

00617102 检查仓库失败

错误信息

Check Registry Failed.

错误描述

检查仓库失败。

可能原因

执行ohpm info、ohpm install命令时，配置的registry参数错误。

处理步骤

检查和确保仓库地址为中心仓地址或私仓地址。

00608001 oh-package.json5文件不存在

错误信息

Pkg Not Found.

错误描述

找不到三方库。

可能原因

工程目录下不存在oh-package.json5文件。

处理步骤

确保工程目录下存在oh-package.json5文件，再执行命令。

00608002 文件不存在

错误信息

File Not Found.

错误描述

文件不存在。

可能原因

在指定目录下未找到文件。

处理步骤

确认目录下存在文件后再执行命令。

00608003 读取文件时发生错误

错误信息

File Read Error.

错误描述

读取文件时发生错误。

可能原因

读取配置等文件失败。

处理步骤

查看是否被占用后，重新读取。

00625003 文件不存在

错误信息

File Not Exist.

错误描述

文件不存在。

可能原因

读取文件不存在。

处理步骤

查看文件是否存在，重新读取。

00631002 仓库请求失败

错误信息

Registry Request Error.

错误描述

仓库请求失败。

可能原因

执行ohpm publish、ohpm dist-tags命令时，配置的publish_registry参数错误。

处理步骤

检查和确保仓库地址为中心仓地址或私仓地址。

00640001 系统错误

错误信息

System Error.

错误描述

系统错误。

可能原因

系统错误，例如内存错误等。

处理步骤

检查日志文件，寻找错误信息定位根源。

00670002 路径大小写敏感错误

错误信息

Path Case Sensitivity Error.

错误描述

路径大小写敏感错误。

可能原因

工程中文件的配置路径和文件的实际路径大小写不一致。

处理步骤

修改工程中配置的文件路径，使其与文件的实际路径一致；或者设置.ohpmrc文件中的case_sensitive_check为false，不检测文件路径大小写。更多请参考case_sensitive_check。
