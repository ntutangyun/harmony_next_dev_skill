# 数据备份

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-data-backup_

数据迁移或者版本升级之前请务必进行数据备份，以免重要数据丢失，无法回滚。备份的内容包括ohpm-repo中<deploy_root>部署根目录内的数据、db元数据以及store三方包数据。

备份deploy_root部署根目录

说明

<deploy_root>：ohpm-repo部署根目录，默认的路径为：

windows系统：~/AppData/Roaming/Huawei/ohpm-repo

其他操作系统：~/ohpm-repo

ohpm-repo在版本1.1.0之前不支持配置<deploy_root>，都采用默认值，若您的ohpm-repo支持且配置了<deploy_root>，请找到对应目录，并使用常用的压缩工具打包备份该目录。

注意

如果配置文件中db，storage，logs和uplink的存储路径可配置，且存储位置不在ohpm-repo部署根目录<deploy_root>中，请找到对应目录进行数据备份。

备份<包存储目录>和<mysql>

说明

如果您使用的是本地存储（配置文件中db为filedb本地存储，store为fs本地存储），在备份<deploy_root>时已经完成db和store的备份，请忽略该步骤。
