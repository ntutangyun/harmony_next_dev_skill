# 1.0.1升级至2.X.X/5.X.X版本

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-upgrade-101_to_2xx_

升级至2.X.X版本与升级至5.X.X版本步骤一致，本文以升级至2.X.X版本为例。

须知

在升级之前，请务必备份好ohpm-repo 私仓工具中的历史数据，避免因升级操作失误，导致数据丢失。备份的内容包括ohpm-repo中<deploy_root>部署根目录内的数据、db元数据以及store三方包数据，详细可参考数据备份。

旧版本服务停止：如果旧版本的服务还在运行，升级版本前请停止，进入1.0.1版本ohpm-repo私仓工具包解压目录下的bin目录，执行stop。

ohpm-repo stop

注意

若您想在其他目录使用ohpm-repo，请将对应版本ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中。

ohpm-repo -v

终端输出版本号2.X.X，则表示解压成功。

说明

如果ohpm-repo版本1.0.1使用的配置文件，配置项均为默认项，则无需移植配置文件信息，直接执行下一步启动操作。

旧版本1.0.1配置文件路径为：`<deploy_root>/conf/config.yaml`；新版本2.X.X配置文件路径为：<2.X.X版本ohpm-repo解压目录>/conf/config.yaml。

windows系统: ~/AppData/Roaming/Huawei/ohpm-repo

其他操作系统：~/ohpm-repo

listen：旧版本listen值拷贝替换到新版本listen中。如果旧版本是在执行start时指定的listen值，需要把对应的listen值填入新版本配置文件中，新版本中listen值不支持命令行指定。

# 旧版本 `1.0.1`
https:
  key: ./ssl/server.key
  cert: ./ssl/server.crt

# 新版本 `2.X.X`
https_key: ./ssl/server.key
https_cert: ./ssl/server.crt

说明

版本1.1.0开始，新增参数api_timeout。

版本升级时，参数信息会有变化，具体信息可在<解压目录>/conf/config.yaml文件中获取。

# 旧版本 `1.0.1`
server:
  max_package_size: 10
  max_extract_size: 50
  max_extract_file_num: 10240
  user_rate_limit: 100
  fetch_timeout: 60
  keep_alive_timeout: 60
  upload_lock_hour: 24
  upload_max_times: 100

# 新版本 `2.X.X`
max_package_size: 10
max_extract_size: 50
max_extract_file_num: 10240
user_rate_limit: 100
fetch_timeout: 60
keep_alive_timeout: 60
api_timeout: 60
upload_lock_hour: 24
upload_max_times: 100

# 旧版本 `1.0.1`
db:
  plugin_name: ohpm-repo-plugin-filedb
  plugin_config:
    path: ./db

# 新版本 `2.X.X`
db:
  type: filedb
  config:
    path: ./db

注意

在ohpm-repo 2.0.0版本中，listen的默认值已更改为listen: 0.0.0.0:8088，如果listen的host配置为0.0.0.0，则字段store.config.server不可省略，必须配置为详细地址，例如http://localhost:8088。

# 旧版本 `1.0.1`
store:
  plugin_name: ohpm-repo-plugin-fs
  plugin_config:
    path: ./storage
    #server: http://localhost:8088

# 新版本 `2.X.X`
store:
  type: fs
  config:
    path: ./storage
    #server: http://localhost:8088

# 旧版本 `1.0.1`
uplink:
  store_path: ./uplink
  cache_time: 168

# 新版本 `2.X.X`
uplink_store_path: ./uplink
uplink_cache_time: 168

解压与替换配置信息：按照步骤1-4，解压和拷贝替换配置文件信息。

建立新部署目录：判断指定的新部署目录<new_deploy_root>是否存在，不存在则新建，新部署目录需存在且为空。

拷贝数据文件：拷贝旧版本部署目录<deploy_root>下的全部文件至新部署目录<new_deploy_root>中。

修改新版本ohpm-repo配置文件：打开新版本ohpm-repo 2.0.0的解压目录，进入conf目录下，修改新配置文件config.yaml，修改配置项deploy_root为新的部署目录<new_deploy_root>。

注意

在使用新部署目录时，旧版本部署目录中meta文件一定要迁移到新版本部署目录中，否则使用meta加密组件加密的数据无法被正确解密。

ohpm-repo install

结果示例：

说明

Windows系统： 关闭当前窗口，重新开启一个窗口

Linux系统或Mac系统：在命令行中执行刷新命令：source ~/.bashrc或者. ~/.bashrc。

ohpm-repo start

结果示例：

说明

版本升级之前，如果浏览器中已访问ohpm-repo页面，版本升级之后请刷新ohpm-repo页面。

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
# 旧版本 `1.0.1`
https:
  key: ./ssl/server.key
  cert: ./ssl/server.crt

# 新版本 `2.X.X`
https_key: ./ssl/server.key
https_cert: ./ssl/server.crt
```

### Code block 4

```
# 旧版本 `1.0.1`
server:
  max_package_size: 10
  max_extract_size: 50
  max_extract_file_num: 10240
  user_rate_limit: 100
  fetch_timeout: 60
  keep_alive_timeout: 60
  upload_lock_hour: 24
  upload_max_times: 100

# 新版本 `2.X.X`
max_package_size: 10
max_extract_size: 50
max_extract_file_num: 10240
user_rate_limit: 100
fetch_timeout: 60
keep_alive_timeout: 60
api_timeout: 60
upload_lock_hour: 24
upload_max_times: 100
```

### Code block 5

```
# 旧版本 `1.0.1`
db:
  plugin_name: ohpm-repo-plugin-filedb
  plugin_config:
    path: ./db

# 新版本 `2.X.X`
db:
  type: filedb
  config:
    path: ./db
```

### Code block 6

```
# 旧版本 `1.0.1`
store:
  plugin_name: ohpm-repo-plugin-fs
  plugin_config:
    path: ./storage
    #server: http://localhost:8088

# 新版本 `2.X.X`
store:
  type: fs
  config:
    path: ./storage
    #server: http://localhost:8088
```

### Code block 7

```
# 旧版本 `1.0.1`
uplink:
  store_path: ./uplink
  cache_time: 168

# 新版本 `2.X.X`
uplink_store_path: ./uplink
uplink_cache_time: 168
```

### Code block 8

```
ohpm-repo install
```

### Code block 9

```
ohpm-repo start
```
