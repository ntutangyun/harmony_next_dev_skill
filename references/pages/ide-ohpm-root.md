# ohpm root

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-root_

可以在 root 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件，将会打印该根目录中有效的 oh_modules 目录路径信息。

log_level
默认值：无
类型： String

从ohpm 6.0.2.636版本开始，可以在 root 命令后配置--log_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

debug
默认值：false
类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

示例

项目结构为：

在entry模块的src目录下执行：

ohpm root

结果示例：

ohpm update
ohpm version
