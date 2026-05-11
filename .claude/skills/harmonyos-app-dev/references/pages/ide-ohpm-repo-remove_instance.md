# ohpm

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-remove_instance_

该命令会停止当前运行的ohpm-repo服务，同时删除本机在mysql和sftp中的实例信息。命令要求数据存储db模块必须使用mysql，文件存储store模块必须使用sftp或custom。

示例

执行以下命令：

ohpm-repo remove_instance

结果示例：

ohpm-repo check_storage
数据迁移相关命令
