# ohpm unpublish错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-unpublish-errorcode_

00610001 执行下架命令时未指定版本号

错误信息

Delete All Version Pkg Not Force.

错误描述

未强制下架不同版本的包。

可能原因

执行ohpm unpublish pkg命令时，未指定三方库版本号，且未配置强制下架参数--force。

处理步骤

未指定三方库版本时，需添加--force参数，强制下架该库所有版本。
