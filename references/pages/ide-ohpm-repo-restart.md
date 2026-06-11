# ohpm-repo restart

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restart_

重新启动ohpm-repo服务。

前提条件

已成功执行install命令，并按要求刷新环境变量。

命令格式

ohpm-repo restart

功能描述

停止当前ohpm-repo服务，重新启动一个新的ohpm-repo服务。

说明

启动时将ohpm-repo服务的pid存放到<deploy_root>/runtime/.pid文件，其中<deploy_root>为ohpm-repo私仓部署目录。

示例

执行以下命令：

ohpm-repo restart

结果示例：

## Code blocks

### Code block 1

```
ohpm-repo restart
```

### Code block 2

```
ohpm-repo restart
```
