# 单点部署

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-deploy-single-instance_

ohpm-repo依赖于Node运行，请提前安装Nodejs，并完成环境变量的配置，推荐Node.js18.x版本。具体安装请参考Node.js官方网站。

下载ohpm-repo工具包，点击链接获取。

解压ohpm-repo私仓工具包。

请将ohpm-repo工具包解压目录中bin目录的路径配置到系统环境变量path中，执行如下查询命令:
ohpm-repo -v

终端输出版本号（如：2.0.0），则表示安装包解压无问题。如有报错，请参考FAQ解决。

注意

针对Linux和Mac系统，建议使用bash作为命令行界面。

进入ohpm-repo解压目录的conf目录中，修改配置文件config.yaml：
检查listen配置，默认配置为localhost:8088 ，表示仅支持监听本机地址；如果希望其他机器通过ip/域名访问，则建议修改listen配置为ohpm-repo部署机器的ip：
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
进入ohpm-repo解压目录的bin目录下，执行安装命令:
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
安装成功后，必须根据给出的提示信息及时刷新环境变量，针对Windows系统和Linux/Mac系统，有不同处理方式：
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
部署指导
多实例部署
