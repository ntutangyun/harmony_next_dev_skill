# 单点部署

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-deploy-single-instance_

说明

ohpm-repo私仓不允许在Linux或macOS系统中使用root用户启动，请使用普通用户安装运行。

安装ohpm-repo工具

说明

ohpm-repo和Node.js的配套版本如下：

ohpm-repo 5.4.4之后版本，推荐使用Node.js 24.x版本。

ohpm-repo 5.4.4及之前版本，当数据存储类型为mysql且文件存储类型为sftp模式时，支持Node.js版本范围为[18.x,22.x]。

下载ohpm-repo工具包，点击链接获取。

解压ohpm-repo私仓工具包。

ohpm-repo -v

终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。

注意

针对Linux和Mac系统，建议使用bash作为命令行界面。

listen: <部署ohpm-repo机器的ip>:8088

检查deploy_root配置：如果选择不配置，会存储在默认地址中。禁止该路径配置为ohpm-repo解压根目录。

数据存储db模块使用filedb：

db:
  type: filedb
  config:
    path: ./db

文件存储store模块使用fs：

store:
  type: fs
  config:
    path: ./storage
    #server: http://localhost:8088

检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址，不配置取默认值，具体请参考server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改server的host为本机指定的ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<指定部署机器的ip/域名>:8088。

说明

如果为ohpm-repo服务配置了反向代理服务器，则store.config.server必须填写为反向代理服务器的ip/域名地址，且需要配置use_reverse_proxy值为true。

config.yaml中各项配置的详细描述请见：配置文件。

ohpm-repo install

说明

不配置参数--config，默认使用ohpm-repo根目录中conf目录内自带的配置文件config.yaml。

启动成功日志信息示例如下：

PS D:\> ohpm-repo install
[2025-08-26T14:29:15.153] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
[2025-08-26T14:29:15.178] [INFO] default - initialize encryption component successfully.
[2025-08-26T14:29:15.179] [INFO] default - initialize "file database" successfully.
[2025-08-26T14:29:15.184] [INFO] default - initialize "file storage" successfully.
[2025-08-26T14:29:15.194] [INFO] console - install successfully.
[2025-08-26T14:29:15.195] [INFO] default - "deploy_root" environment variables: "OHPM_REPO_DEPLOY_ROOT = C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo".

说明

Windows系统： 关闭当前窗口，重新开启一个窗口。

Linux系统或Mac系统： 在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc 或者 . ~/.bashrc ；当shell为zsh时，执行source ~/.zshrc 或者 . ~/.zshrc 。

启动ohpm-repo

执行start命令启动ohpm-repo。

ohpm-repo start

启动成功日志信息如下：

PS D:\> ohpm-repo start
[2025-08-26T14:31:22.209] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
[2025-08-26T14:31:22.211] [INFO] default - config file path: "C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo\conf\config.yaml".
[2025-08-26T14:31:22.216] [INFO] default - initialize "file database" successfully.
[2025-08-26T14:31:22.217] [INFO] default - initialize "file storage" successfully.
[2025-08-26T14:31:22.237] [INFO] console - http address - localhost:8088 - ohpm-repo/5.1.5.

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
  type: filedb
  config:
    path: ./db
```

### Code block 4

```
store:
  type: fs
  config:
    path: ./storage
    #server: http://localhost:8088
```

### Code block 5

```
ohpm-repo install
```

### Code block 6

```
PS D:\> ohpm-repo install
[2025-08-26T14:29:15.153] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
[2025-08-26T14:29:15.178] [INFO] default - initialize encryption component successfully.
[2025-08-26T14:29:15.179] [INFO] default - initialize "file database" successfully.
[2025-08-26T14:29:15.184] [INFO] default - initialize "file storage" successfully.
[2025-08-26T14:29:15.194] [INFO] console - install successfully.
[2025-08-26T14:29:15.195] [INFO] default - "deploy_root" environment variables: "OHPM_REPO_DEPLOY_ROOT = C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo".
```

### Code block 7

```
ohpm-repo start
```

### Code block 8

```
PS D:\> ohpm-repo start
[2025-08-26T14:31:22.209] [WARN] default - "listen" protocol is set to 'http' in "config.yaml" file, which is insecure, advise to use the more secure 'https' protocol instead.
[2025-08-26T14:31:22.211] [INFO] default - config file path: "C:\Users\xxx\AppData\Roaming\Huawei\ohpm-repo\conf\config.yaml".
[2025-08-26T14:31:22.216] [INFO] default - initialize "file database" successfully.
[2025-08-26T14:31:22.217] [INFO] default - initialize "file storage" successfully.
[2025-08-26T14:31:22.237] [INFO] console - http address - localhost:8088 - ohpm-repo/5.1.5.
```
