# 权限错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00307_

00307001 创建或写文件失败

错误信息

EPERM: operation not permitted,create XXX failed.

错误描述

创建或写文件XXX失败。

可能原因

缺少创建或写文件的权限。

处理步骤

确保用户具有创建文件、写文件的权限。

00307003 HSP依赖包的bundleType不正确

错误信息

The currentBundleType is shared, but the Package XXX bundleType is not shared.

错误描述

当前的bundleType为shared，但是包XXX的bundleType不是shared。

可能原因

当前工程app.json5中的bundleType设置为shared，但是依赖包的bundleType不是shared。

处理步骤

移除依赖包XXX。

00307005 文件被占用

错误信息

The file is occupied.

错误描述

文件被占用导致构建进程无法对文件进行操作。

可能原因

工程中的文件被其他进程占用或保护（如杀毒软件、加密软件等），导致DevEco Studio工具中的进程无法获取相应文件的权限。

处理步骤

排查报错文件是否被其他进程占用，工程目录、DevEco Studio的安装目录是否有特殊的权限控制。

可尝试将杀毒软件临时关闭来验证报错是否由杀毒软件导致。
