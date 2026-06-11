# ohpm unpublish错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-unpublish-errorcode_

00610001 执行下架命令时未指定版本号

错误信息

Delete All Version Pkg Not Force.

错误描述

未强制下架不同版本的包。

可能原因

下架时未指定版本号，且未使用强制下架。

处理步骤

如果未指定版本，默认下架三方库的所有版本，并且需要加上 -f 配置参数。
