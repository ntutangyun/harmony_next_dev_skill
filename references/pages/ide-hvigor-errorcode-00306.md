# 规格错误码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-errorcode-00306_

00306045 当compatibleSdkVersion为5.0.0(12)及以上时useNormalizedOHMUrl才可配置为true
00306046 useNormalizedOHMUrl为false时不支持字节码HAR
00306047 多个HSP模块依赖同一个HAR
00306048 当前API版本不支持配置autoLazyImport
00306049 模块中存在重复的文件
00306050 FA模型的项目不允许依赖外部项目模块
00306051 Stage模型的项目不允许依赖FA模型的模块
00306052 不能依赖工程外的HAP模块
00306053 ohpm安装依赖失败
00306054 构建任务的命令无效
00306055 工程外的模块缺少配置
00306056 hvigor守护进程异常退出
00306057 executableBinaryPaths-path的值应该是相对路径
展开章节
00306001 文件路径长度超过最大限制

错误信息

The length of path exceeds the maximum length: XXX.

错误描述

文件路径长度超过最大限制。

可能原因

文件路径总长度超过了操作系统的限制。

处理步骤

缩短工程根路径。
简化工程名称。
简化模块名称。
简化target名称。
语法错误码
权限错误码
