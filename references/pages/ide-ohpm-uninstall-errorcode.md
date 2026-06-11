# ohpm uninstall错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-uninstall-errorcode_

00605001 未配置包名称

错误信息

No Pkg.

错误描述

uninstall时未配置包名称。

可能原因

卸载不存在的依赖包。

处理步骤

根据oh-package.json5文件中配置的依赖进行卸载，确认卸载的依赖包在文件中已配置。

00605002 配置版本号错误

错误信息

Has Version.

错误描述

配置版本号。

可能原因

执行卸载命令时，配置包版本号。

处理步骤

执行卸载命令时，不配置包版本号。

00617301 从本地文件夹获取源代码包时失败

错误信息

Fetch Source Code Failed.

错误描述

从本地文件夹获取源代码包时失败。

可能原因

指定的路径不存在，导致无法获取源代码包。

处理步骤

检查路径，确保路径存在且正确。
