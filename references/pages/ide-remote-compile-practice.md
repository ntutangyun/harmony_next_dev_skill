# 内存优化：远程编译实践

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-remote-compile-practice_

概述

远程编译是一种将构建任务从本地机器迁移至远程服务端执行的开发优化方案，适用于项目规模较大、本地内存不足以支撑完整编译的场景。通过远程编译，可将内存压力转移至性能更强的服务器，保证本地开发的流畅性。

工作流程

本地通过rsync服务将代码和构建信息同步至远程服务器，服务端完成编译构建后，再将构建产物同步回本地。客户端轮询监控构建状态，等待构建完成。

整个过程中，实际编译工作由服务端承担，本地仅负责发起构建和接收结果，无需保留完整的编译中间产物，从而有效释放本地内存资源。

使用示例

此示例通过rsync+Hvigor插件+Python脚本实现远程编译，仅供参考，开发者也可以通过其他方式实现远程编译。

在使用本文提供的能力之前，开发者需要具备rsync和Python开发的基础知识。

[h2]客户端配置

客户端位于开发机器，负责将代码和构建信息同步至远程服务器。以下文件需开发者手动创建，存放路径不限，可根据实际情况放置于任意目录。

// 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
{
  "rsyncType": "client",   // 标识当前为客户端配置
  "monitor": {
    "trigger_file": "/path/to/client/trigger.json"  // 构建信息文件路径，客户端监控此文件中的构建状态变化，本文以trigger.json为例
  },
  "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=90000 --exclude-from=/path/to/client/exclude.txt /path/to/project rsync://user@server_ip:873/basetest",  // 将本地源码同步至远程服务器的rsync命令
  "origin": {
    "base_dir": "/path/to/project" // 项目路径
  },
  "output": {
    "host": "server_ip"  // 服务端IP
  }
}

// 根据实际情况填写
.git/
.idea/
node_modules/
oh_modules/
**/build
**/build/**
**/.hvigor/**
.appanalyzer

// rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
use chroot = false
strict modes = false
hosts allow = *
log file = rsyncd.log
pid file = rsyncd.pid
port = 873
uid = your_user
gid = your_group
[basetest]
path = /path/to/project/parent
read only = false
[client]
path = /path/to/client/config
read only = no

说明

此示例使用process.argv解析构建参数生成构建命令，需要开发者将本地守护进程关闭，才能正确读取到参数；或可以直接将构建命令写在插件中调用即可，获取构建命令的方式不限，可根据实际情况处理。

在工程级hvigorfile.ts中导入remote-plugin.ts。

import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { remoteBuildPlugin } from '/path/to/remote-plugin';  // 修改为实际的路径

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [
    remoteBuildPlugin()
  ]       /* Custom plugin to extend the functionality of Hvigor. */
}

# 配置加载
load_client2_config()        # 解析config.json，提取配置
build_remote_spec()          # 构造rsync目标地址

# JSON操作
read_json() / write_json()   # 读取/写入JSON文件
update_trigger_status()      # 更新trigger.json状态

# 锁管理
acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

# 代码同步
sync_to_remote()             # rsync同步代码到服务端

# 文件监控
monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
to_cygdrive_path()           # Windows路径转换为cygdrive格式

# 错误处理
write_console_file()         # 写入错误日志到console.file

# 程序入口
main()                       # 程序入口，启动监控循环

启动客户端rsync服务和Python脚本。

[h2]服务端配置

// 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
{
  "rsyncType": "server",   // 标识当前为服务端配置
  "monitor": {
    "trigger_file": "/path/to/server/trigger.json"  // 构建信息文件路径，服务端监控此文件中的构建状态变化，本文以trigger.json为例
  },
  "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=9000 --exclude-from=/path/to/server/exclude.txt /path/to/project rsync://user@client_ip:873/basetest",  // 将服务端构建产物、日志等同步至客户端的rsync命令
  "build": {
    "base_path": "/path/to/project"  // 项目路径
  },
  "output": {
    "host": "client_ip",  // 服务端IP
  }
}

// 请根据实际情况填写
.git/
.idea/
*.iml
node_modules/
oh_modules/
*.log

// rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
syslog facility = 0
log file = /path/to/server/log/rsyncd.log
uid = your_user
gid = your_group
use chroot = no
port = 873
strict modes = false
timeout = 60000
# 模块配置
[basetest]
path = /path/to/project/parent
read only = no
[server]
path = /path/to/server/config
read only = no

# 配置加载
load_server2_config()        # 解析config.json，提取配置
build_remote_spec()          # 构造rsync目标地址

# JSON操作
read_json() / write_json()   # 读取/写入JSON文件
update_trigger_status()      # 更新trigger.json状态

# 锁管理
acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

# 构建执行
execute_node_build()         # 执行构建命令，支持超时控制
terminate_process_tree()     # 终止构建进程树

# 产物同步
sync_to_remote()             # rsync同步产物到客户端

# 文件监控
monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
to_cygdrive_path()           # Windows路径转换为cygdrive格式

# 错误处理
write_console_file()         # 写入错误日志到console.file

# 程序入口
main()                       # 程序入口，启动监控循环

启动服务端rsync服务和Python脚本。

[h2]启动构建

启动rsync服务和Python脚本后，在本地启动构建，即可自动转移到远端服务器进行构建。查看日志信息如下说明远程编译启动成功。

[h2]示例代码

远程编译

## Code blocks

### Code block 1

```
// 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
{
  "rsyncType": "client",   // 标识当前为客户端配置
  "monitor": {
    "trigger_file": "/path/to/client/trigger.json"  // 构建信息文件路径，客户端监控此文件中的构建状态变化，本文以trigger.json为例
  },
  "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=90000 --exclude-from=/path/to/client/exclude.txt /path/to/project rsync://user@server_ip:873/basetest",  // 将本地源码同步至远程服务器的rsync命令
  "origin": {
    "base_dir": "/path/to/project" // 项目路径
  },
  "output": {
    "host": "server_ip"  // 服务端IP
  }
}
```

### Code block 2

```
// 根据实际情况填写
.git/
.idea/
node_modules/
oh_modules/
**/build
**/build/**
**/.hvigor/**
.appanalyzer
```

### Code block 3

```
// rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
use chroot = false
strict modes = false
hosts allow = *
log file = rsyncd.log
pid file = rsyncd.pid
port = 873
uid = your_user
gid = your_group
[basetest]
path = /path/to/project/parent
read only = false
[client]
path = /path/to/client/config
read only = no
```

### Code block 4

```
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { remoteBuildPlugin } from '/path/to/remote-plugin';  // 修改为实际的路径

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [
    remoteBuildPlugin()
  ]       /* Custom plugin to extend the functionality of Hvigor. */
}
```

### Code block 5

```
# 配置加载
load_client2_config()        # 解析config.json，提取配置
build_remote_spec()          # 构造rsync目标地址

# JSON操作
read_json() / write_json()   # 读取/写入JSON文件
update_trigger_status()      # 更新trigger.json状态

# 锁管理
acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

# 代码同步
sync_to_remote()             # rsync同步代码到服务端

# 文件监控
monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
to_cygdrive_path()           # Windows路径转换为cygdrive格式

# 错误处理
write_console_file()         # 写入错误日志到console.file

# 程序入口
main()                       # 程序入口，启动监控循环
```

### Code block 6

```
// 示例中仅提供主要的字段说明，其他字段可参考示例代码，需要将路径、IP等替换为实际的内容
{
  "rsyncType": "server",   // 标识当前为服务端配置
  "monitor": {
    "trigger_file": "/path/to/server/trigger.json"  // 构建信息文件路径，服务端监控此文件中的构建状态变化，本文以trigger.json为例
  },
  "rsyncCommand": "rsync -rltvz --no-o --no-g --timeout=9000 --exclude-from=/path/to/server/exclude.txt /path/to/project rsync://user@client_ip:873/basetest",  // 将服务端构建产物、日志等同步至客户端的rsync命令
  "build": {
    "base_path": "/path/to/project"  // 项目路径
  },
  "output": {
    "host": "client_ip",  // 服务端IP
  }
}
```

### Code block 7

```
// 请根据实际情况填写
.git/
.idea/
*.iml
node_modules/
oh_modules/
*.log
```

### Code block 8

```
// rsyncd.conf配置并非固定不变，此示例仅供当前远程编译参考使用，根据实际环境修改参数取值
syslog facility = 0
log file = /path/to/server/log/rsyncd.log
uid = your_user
gid = your_group
use chroot = no
port = 873
strict modes = false
timeout = 60000
# 模块配置
[basetest]
path = /path/to/project/parent
read only = no
[server]
path = /path/to/server/config
read only = no
```

### Code block 9

```
# 配置加载
load_server2_config()        # 解析config.json，提取配置
build_remote_spec()          # 构造rsync目标地址

# JSON操作
read_json() / write_json()   # 读取/写入JSON文件
update_trigger_status()      # 更新trigger.json状态

# 锁管理
acquire_lock() / release_lock()  # 基于.lock文件的互斥锁，防止并发构建

# 构建执行
execute_node_build()         # 执行构建命令，支持超时控制
terminate_process_tree()     # 终止构建进程树

# 产物同步
sync_to_remote()             # rsync同步产物到客户端

# 文件监控
monitor_trigger_file()       # 监控trigger.json变化（watchdog或轮询fallback）
to_cygdrive_path()           # Windows路径转换为cygdrive格式

# 错误处理
write_console_file()         # 写入错误日志到console.file

# 程序入口
main()                       # 程序入口，启动监控循环
```
