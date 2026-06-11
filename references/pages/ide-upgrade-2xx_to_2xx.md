# 2.X.X/5.X.X升级至更高版本

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-upgrade-2xx_to_2xx_

如需将ohpm-repo版本2.X.X/5.X.X版本升级到更高版本，可参考此文档。

须知

1. 在升级之前，请务必备份好ohpm-repo私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括<deploy_root>ohpm-repo部署根目录内数据，db元数据以及store三方包数据，详细可参考数据备份 。

2. 如果您想要改变db元数据和store三方包的存储方式，可在正确升级后参考数据迁移文档指导修改。

ohpm-repo stop

注意

如果部署的是多实例，升级前需要停下所有机器中的ohpm-repo服务，再进行升级操作。

若想在其他目录使用ohpm-repo，请将对应版本ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中。

ohpm-repo -v

终端输出为新版本的版本号，则表示解压成功。

找到ohpm-repo旧版本的配置文件：如果旧版本未指定配置文件，使用默认配置文件：旧版本ohpm-repo解压根目录/conf/config.yaml。

拷贝旧版本配置文件至新版本：复制旧版本的配置文件到新版ohpm-repo解压目录下的conf文件夹，覆盖新版本中的默认配置文件。

升级ohpm-repo：按照步骤1-4，解压ohpm-repo并拷贝替换配置文件信息。

建立新部署目录：判断指定的新部署目录<new_deploy_root>是否存在，不存在则新建，新部署目录需存在且为空。

拷贝数据文件：拷贝旧版本部署目录<deploy_root>下的全部文件至新部署目录中。

修改新版本ohpm-repo配置文件：打开新版本ohpm-repo的解压根目录，进入conf目录下，修改配置文件config.yaml中配置项deploy_root为新的部署目录<new_deploy_root>。

注意

在使用新部署目录时，旧版本的部署目录中meta文件必须要迁移到新版本部署目录中，否则将导致使用meta加密组件加密的数据无法被正确解密。

ohpm-repo install

结果示例：

Windows系统： 关闭当前窗口，重新开启一个窗口。

Linux/Mac系统：

5.0.1之前版本：在命令行中执行刷新命令：source ~/.bashrc或者.~/.bashrc ；

5.0.1及以后版本：

在命令行中执行刷新命令：当shell为bash时，执行source ~/.bashrc或者. ~/.bashrc ；当shell为zsh时，执行source ~/.zshrc或者.~/.zshrc 。

ohpm-repo start

结果示例：

说明

版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。

多实例部署机器快速升级：在多实例部署中，其他机器同步骤1-6进行快速升级操作。

## Code blocks

### Code block 1

```
ohpm-repo stop
```

### Code block 2

```
ohpm-repo -v
```

### Code block 3

```
ohpm-repo install
```

### Code block 4

```
ohpm-repo start
```
