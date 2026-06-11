# 快速开始

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-quickstart_

说明

ohpm-repo私仓不允许在Linux或macOS系统中使用root用户启动，请使用普通用户安装运行。

如何安装

ohpm-repo依赖于Node运行，请提前安装Nodejs，并完成环境变量的配置，推荐Node.js18.x版本。具体安装请参考Node.js官方网站。

下载ohpm-repo私仓工具包。请在下载中心获取最新的ohpm-repo，并根据下载中心页面工具完整性指导进行完整性校验。

解压ohpm-repo私仓工具包。

请将ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中，执行如下查询命令:

ohpm-repo -v

注意

针对Linux和Mac系统，建议使用bash或zsh作为命令行界面。如果使用其他类型shell，写入ohpm-repo部署根目录deploy_root的环境变量时，默认写入.bashrc文件中。

在启动ohpm-repo前，需要先按照如下方式完成配置修改：进入ohpm-repo解压目录的conf目录内，打开config.yaml配置文件。

说明

ohpm-repo成功启动后修改配置文件方法：

首次启动ohpm-repo时执行install命令已指定配置文件：找到指定的配置文件进行文件内容修改，然后重新执行install指定修改后的配置文件，再执行start启动ohpm-repo。

首次启动ohpm-repo时执行install命令未指定配置文件：默认使用ohpm-repo压缩包解压路径下conf目录中的配置文件，修改该文件内容，然后重新执行install和start操作。

检查listen配置，默认配置为localhost:8088，表示仅支持监听本机地址；如果希望其他机器通过ip/域名访问，则建议修改listen配置为ohpm-repo部署机器的ip：

listen: <部署ohpm-repo机器的ip>:8088

检查deploy_root配置：如果不配置，会存储在默认地址中。该路径不允许配置为ohpm-repo解压根目录。

db：元数据存储	与db所适配的store类型
fileDB	file storage
mysql	file storage，sftp storage， custom storage

检查是否配置了store.config.server，用于指定ohpm-repo仓库内容的下载地址、不配置取默认值，详情见：server: 仓库内容的下载地址。如果listen的host为0.0.0.0，且本机存在多个网络接口，那么该值必须配置，建议手动修改host为本机指定的ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<指定部署机器的ip/域名>:8088。

说明

如果为ohpm-repo服务配置了反向代理服务器，则该地址需要填写为反向代理服务器的地址。

如果ohpm-repo以多实例方式启动，必须配置反向代理服务器，多个实例之间需要统一的下载地址。

config.yaml中各项配置的详细描述请见：配置文件。

进入ohpm-repo工具包解压目录中的bin目录下，执行安装命令:

ohpm-repo install

结果实例：

Windows系统：关闭当前窗口，重新开启一个窗口。

Linux/Mac系统：在命令行中执行刷新命令：当shell为bash时执行source ~/.bashrc或者. ~/.bashrc；当shell为zsh时执行source ~/.zshrc或者. ~/.zshrc。

如何启动

ohpm-repo安装成功后，进入ohpm-repo工具包解压目录下的bin目录下，执行如下命令，启动ohpm-repo：

ohpm-repo start

启动成功，将会出现以下日志信息：

说明

ohpm-repo首次启动时，默认创建一个管理员账号，账号名称：admin，密码：12345Qq!。该账号在首次登录时，需要修改其密码，请修改密码后，重新登录该账号。

从ohpm-repo获取三方库

可以为所有项目配置该私有仓，例如执行以下命令：

ohpm config set registry <配置的ohpm-repo私仓服务地址>/repos/ohpm
ohpm install

或者在命令行中配置参数--registry使用，例如以下命令：

ohpm install @ohos/lottie --registry <配置的ohpm-repo私仓服务地址>/repos/ohpm

说明

<配置的ohpm-repo私仓服务地址>：配置文件中store.config.server的地址信息，例如：store.config.server:为http://127.0.0.1:8088，故registry为：http://127.0.0.1:8088/repos/ohpm。如果store.config.server没有配置，取默认值。

将三方库发布到ohpm-repo

三方库包含静态共享包HAR包和动态共享包HSP包，可以通过ohpm命令行工具和使用Web页面两种方式发布。

说明

从ohpm命令行工具1.3.0版本和ohpm-repo私仓1.1.0版本开始，支持动态共享包HSP包以.tgz文件形式发布到ohpm-repo，之前版本仅支持发布以.har文件形式的静态共享包。

[h2]使用命令行工具发布

ssh-keygen -m PEM -t RSA -b 4096 -f <your_key_path>

说明

<your_key_path>：配置公钥和私钥的名称和存放路径，仅包含名称时，以当前命令行工作路径为存储目录。

OHPM包管理器只支持加密密钥认证，请在生成公私钥时输入密码。

示例：

ssh-keygen -m PEM -t RSA -b 4096 -f D:\path\my_key_path

说明

公钥和私钥存储在D盘的path目录下，公钥和私钥名称分别为my_key_path.pub和my_key_path。

ohpm config set key_path <your_key_path>

ohpm config set publish_id <your_publish_id>

执行 ''ohpm publish <HAR包路径>'' 命令发布HAR包，<HAR包路径> 指向的文件后缀需为.har文件的具体路径。例如执行以下命令：

ohpm config set publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
ohpm publish demo.har

或在命令行中配置参数--publish_registry使用，例如以下命令：

ohpm publish demo.har --publish_registry <ohpm-repo私仓管理地址>/repos/ohpm

动态共享包HSP包不能直接发布在ohpm-repo内，需要先转换为.tgz包，转换方法见：编译HSP模块。TGZ包的发布流程同HAR一致。

执行 ''ohpm publish <TGZ包路径>'' 命令发布TGZ包，< TGZ 包路径> 指向的文件后缀需为.tgz文件的具体路径。例如执行以下命令：

ohpm config set publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
ohpm publish demo.tgz

或在命令行中配置参数--publish_registry使用，例如以下命令：

ohpm publish demo.tgz --publish_registry <ohpm-repo私仓管理地址>/repos/ohpm

说明

开发HAR包和HSP包，HSP生成.tgz包和.tgz格式共享包转换为.har格式等更详细内容请参考：开发及引用共享包。

listen的host不为0.0.0.0时， 管理地址使用listen的完整格式，例如：当listen：localhost:8088，此处ohpm-repo私仓管理地址应填写：http://localhost:8088。

listen的host为0.0.0.0时，host需更改为ohpm-repo私仓部署机器的ip/域名，例如：当listen：0.0.0.0:8088，此处ohpm-repo私仓管理地址应填写：http://<ohpm-repo私仓部署机器的ip/域名>:8088。

[h2]使用Web页面发布

在Web页面用管理员账号登录ohpm-repo私仓管理地址，在个人中心 > 仓库管理中，点击管理三方包 > 上传三方包，包的后缀名必须为.har或者.tgz。

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
ohpm-repo install
```

### Code block 4

```
ohpm-repo start
```

### Code block 5

```
ohpm config set registry <配置的ohpm-repo私仓服务地址>/repos/ohpm
ohpm install
```

### Code block 6

```
ohpm install @ohos/lottie --registry <配置的ohpm-repo私仓服务地址>/repos/ohpm
```

### Code block 7

```
ssh-keygen -m PEM -t RSA -b 4096 -f <your_key_path>
```

### Code block 8

```
ssh-keygen -m PEM -t RSA -b 4096 -f D:\path\my_key_path
```

### Code block 9

```
ohpm config set key_path <your_key_path>
```

### Code block 10

```
ohpm config set publish_id <your_publish_id>
```

### Code block 11

```
ohpm config set publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
ohpm publish demo.har
```

### Code block 12

```
ohpm publish demo.har --publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
```

### Code block 13

```
ohpm config set publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
ohpm publish demo.tgz
```

### Code block 14

```
ohpm publish demo.tgz --publish_registry <ohpm-repo私仓管理地址>/repos/ohpm
```
