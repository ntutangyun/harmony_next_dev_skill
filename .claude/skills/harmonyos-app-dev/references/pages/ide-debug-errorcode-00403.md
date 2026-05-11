# 调试失败错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-errorcode-00403_

The JSON content is empty when the sourceMaps.map file is read.

错误描述

读取sourceMaps.map文件时，JSON内容为空。

可能原因

sourceMaps.map文件内容为空。

处理步骤

点击菜单栏Build > Clean Project清理缓存后重试。

00403030 连接WebSocket失败

错误信息

Failed to connect to the WebSocket. Restart the debugging. If the problem persists, restart DevEco Studio and start debugging again.

错误描述

无法连接到WebSocket。请重新启动调试。如果问题仍然存在，请重启DevEco Studio并重新启动调试。

可能原因

连接WebSocket失败。
如果是2in1设备，可能是应用开启了应用加速服务。

处理步骤

请重新启动调试。如果问题仍然存在，请重启DevEco Studio并重新启动调试。
如果是2in1设备，请在设备的设置 > 应用加速服务中，查看应用是否开启了应用加速服务，并关闭应用的加速服务。
00403031 进程pid无效

错误信息

The process has invalid pid.

错误描述

进程pid无效。

可能原因

获取进程pid失败。

处理步骤

请重新启动调试。

00403032 连接调试服务器失败

错误信息

Failed to connect to the debug server. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

错误描述

无法连接到调试服务器。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

可能原因

连接panda server失败。

处理步骤

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

00403033 获取ROM镜像版本失败

错误信息

Failed to obtain the ROM image version.

错误描述

获取ROM镜像版本失败。

可能原因

设备连接异常。

处理步骤

重新连接设备，或者执行hdc kill -r重启hdc后再重试。

00403043 预览器启动失败

错误信息

Failed to start the Previewer. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

错误描述

预览器启动失败。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

可能原因

预览调试启动失败。

处理步骤

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

00403044 仿真器启动失败

错误信息

Failed to start the simulator. Try again. If the issue persists, collect logs and choose Help > Contact Support for assistance.

错误描述

仿真器启动失败。请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

可能原因

仿真器启动失败。

处理步骤

请重试。如果问题仍然存在，请收集日志并选择“帮助”>“联系支持”以获取帮助。

00403045 编译失败

错误信息

Compilation failed.

错误描述

编译失败。

可能原因

编译失败。

处理步骤

点击菜单栏Build > Clean Project清理缓存后重试。

00403046 找不到Jerry适配器文件

错误信息

Jerry adapter file not found.

错误描述

找不到Jerry适配器文件。

可能原因

安装目录下找不到Jerry适配器文件。

处理步骤

在官网上重新下载DevEco Studio。

00403047 node路径无效

错误信息

Node path is invalid.

错误描述

Node路径无效。

可能原因

无法获取node路径。

处理步骤

检查DevEco Studio安装目录的tools目录下是否存在node工具，如果不存在，在官网上重新下载DevEco Studio。

00403048 无法启动webpack

错误信息

Unable to start webpack.

错误描述

无法启动webpack。

可能原因

webpack服务启动失败。

处理步骤

点击菜单栏Build > Clean Project清理缓存后重试，如果未解决，重启DevEco Studio。

00403049 预览插件未完全安装

错误信息

The Previewer plugin not fully installed. Please verify.

错误描述

预览插件未完全安装。请确认。

可能原因

预览插件未完全安装。

处理步骤

在官网上重新下载DevEco Studio。

00403050 Jerry适配器无法连接到服务器

错误信息

Jerry Adapter fails to connect to the engine.

错误描述

Jerry适配器无法连接到服务器。

可能原因

Jerry调试连接失败。

处理步骤

点击菜单栏Build > Clean Project清理缓存后重试，如果未解决，重启DevEco Studio。

00403051 Jerry调试引擎异常停止

错误信息

Adapter server or engine stopped abnormally.

错误描述

Jerry调试引擎异常停止。

可能原因

Jerry调试引擎异常停止。

处理步骤

点击菜单栏Build > Clean Project清理缓存后重试，如果未解决，重启DevEco Studio。

热重载和增量调试错误码
hdc命令失败错误码
