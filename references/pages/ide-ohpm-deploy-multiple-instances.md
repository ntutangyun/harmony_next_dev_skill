# 多实例部署

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-deploy-multiple-instances_

说明

ohpm-repo私仓不允许在Linux或macOS系统中使用root用户启动，请使用普通用户安装运行。

只有db存储为mysql且store存储为sftp或者custom时，才支持多实例方式部署。本章节多实例部署以db存储为mysql，store存储为sftp为例。

环境准备

准备mysql数据库服务；

准备至少一个sftp存储服务，ohpm-repo最大支持连接3个sftp服务；

安装Node.js，并完成环境变量的配置。具体安装请参考Node.js官方网站。

说明

确保sftp服务端口能够被外部机器访问。

sftp服务的读写用户应该指定相同的存储根目录。

ohpm-repo 5.4.4之后版本，推荐使用Node.js 24.x版本。

ohpm-repo 5.4.4及之前版本，当数据存储类型为mysql且文件存储类型为sftp模式时，支持Node.js版本范围为[18.x,22.x]。

安装ohpm-repo工具

ohpm-repo -v

终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。

注意

针对Linux和Mac系统，建议使用bash作为命令行界面。

listen: <部署ohpm-repo机器的ip>:8088

检查deploy_root配置：如果选择不配置，会存储在默认地址中。禁止该路径配置为ohpm-repo解压根目录。

db:
  type: mysql
  config:
    host: "localhost"
    port: 3306
    username: "tctAdmin"
    password: "password"
    database: "repo"

store:
  type: sftp
  config:
    location:
      -
        name: test_one_sftp
        host: "localhost"
        port: 22
        read_username: "read"
        read_password: "password"
        write_username: "write"
        write_password: "password"
        path: /source22
      -
        name: test_two_sftp
        host: "localhost"
        port: 24
        read_username: "read"
        read_password: "password"
        write_username: "write"
        write_password: "password"
        path: /source24
    #server: http://localhost:8088

注意

1、ohpm-repo文件的存储路径为： <sftp服务器配置的存储根目录> +<store配置的path路径>，其中path只支持相对路径，必须以/开头。例如sftp服务器存储根目录为/user/sftp/data，store中path配置的路径为/source，故最终ohpm-repo文件存储路径为/user/sftp/data/source。

2、多实例部署ohpm-repo时，必须配置反向代理服务器，转发客户端请求到部署的多个ohpm-repo实例服务器中，故store.config.server必须手动配置为反向代理服务器的域名/ip地址，且需要配置use_reverse_proxy值为true。

ohpm-repo install

说明

不配置参数--config，则默认使用ohpm-repo解压目录中conf目录内自带的配置文件config.yaml。

安装成功日志信息如下：

说明

Windows系统： 关闭当前窗口，重新开启一个窗口。

Linux系统或Mac系统： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc 或者 . ~/.bashrc ；当shell为zsh时，执行source ~/.zshrc 或者 . ~/.zshrc 。

部署首个节点

进入ohpm-repo解压目录的bin目录中，命令行启动ohpm-repo。

ohpm-repo start

启动成功日志信息如下：

打包和部署

为帮助更方便地完成多实例部署，已提供打包和部署命令。

[h2]打包

在完成了多实例配置并首次启动过ohpm-repo服务实例的机器上，执行ohpm-repo pack <deploy_root>。

ohpm-repo pack D:\ohpm-repo

说明

该命令用来打包备份ohpm-repo的<deploy_root>/conf，<deploy_root>/meta目录，并在命令行工作目录下生成压缩包。

打包成功日志信息如下：

[h2]部署

将pack命令的产物拷贝到其他机器中。在解压ohpm-repo压缩包后，使用ohpm-repo deploy <file_path>命令部署新的实例。

ohpm-repo deploy D:\ohpm-repo\bin\pack_1695805599689.zip --deploy_root D:\new-ohpm-repo\ohpm-repo-deploy

说明

<file_path>： 参数指定备份压缩包地址。

--deploy_root： 指定部署根目录，用于存储ohpm-repo启动时生成的文件，默认使用 <现有用户home目录>/ohpm-repo。

部署成功日志信息如下：

部署成功后可执行ohpm-repo start启动ohpm-repo。

配置自动重启（可选）

为ohpm-repo实例配置系统重启时自动重启的功能。

说明

在进行该配置前需要将ohpm-repo工具bin目录配置到系统环境变量path中。

[h2]Linux

touch run-repo.sh

说明

当mysql或sftp服务与ohpm-repo部署在同一服务器上时，请将mysql和sftp的启动命令放在ohpm-repo start命令之前。

#!/bin/bash
ohpm-repo start

chmod +x run-repo.sh

crontab -e

@reboot /bin/sh run-repo.sh >/dev/null 2>&1

其中run-repo.sh表示要执行的脚本路径；>/dev/null 2>&1表示将输出重定向到空设备，即不输出任何信息。

现在，每次系统启动时，都会自动执行run-repo.sh脚本中的命令。

[h2]Windows

说明

当mysql或sftp服务与ohpm-repo部署在同一服务器上时，请将mysql和sftp的启动命令放在ohpm-repo start命令之前。

@echo off
call ohpm-repo start
exit

现在，每次系统启动时，都会自动执行run-repo.bat脚本中的命令。

## Code blocks

### Code block 1

```
ohpm-repo -v
```

### Code block 2

```
listen: <部署ohpm-repo机器的ip>:8088
```

### Code block 3

```
db:
  type: mysql
  config:
    host: "localhost"
    port: 3306
    username: "tctAdmin"
    password: "password"
    database: "repo"
```

### Code block 4

```
store:
  type: sftp
  config:
    location:
      -
        name: test_one_sftp
        host: "localhost"
        port: 22
        read_username: "read"
        read_password: "password"
        write_username: "write"
        write_password: "password"
        path: /source22
      -
        name: test_two_sftp
        host: "localhost"
        port: 24
        read_username: "read"
        read_password: "password"
        write_username: "write"
        write_password: "password"
        path: /source24
    #server: http://localhost:8088
```

### Code block 5

```
ohpm-repo install
```

### Code block 6

```
ohpm-repo start
```

### Code block 7

```
ohpm-repo pack D:\ohpm-repo
```

### Code block 8

```
ohpm-repo deploy D:\ohpm-repo\bin\pack_1695805599689.zip --deploy_root D:\new-ohpm-repo\ohpm-repo-deploy
```

### Code block 9

```
touch run-repo.sh
```

### Code block 10

```
#!/bin/bash
ohpm-repo start
```

### Code block 11

```
chmod +x run-repo.sh
```

### Code block 12

```
crontab -e
```

### Code block 13

```
@reboot /bin/sh run-repo.sh >/dev/null 2>&1
```

### Code block 14

```
@echo off
call ohpm-repo start
exit
```
