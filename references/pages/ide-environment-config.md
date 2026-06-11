# 配置代理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config_

DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。

一般来说，如果使用的是个人或家庭网络，是不需要配置代理信息的，部分企业网络受限的情况下，才需要配置代理信息。

诊断开发环境

为了您开发应用/元服务的良好体验，DevEco Studio提供了开发环境诊断的功能，帮助您识别开发环境是否完备。您可以在欢迎页面单击Diagnose进行诊断。如果您已经打开了工程开发界面，也可以在菜单栏单击Help > Diagnostic Tools > Diagnose Development Environment进行诊断。

DevEco Studio开发环境诊断项包括电脑的配置、网络的连通情况等。如果检测结果为未通过，请根据检查项的描述和修复建议进行处理。

配置Proxy代理

Host name：代理服务器主机名或IP地址。

Port number：代理服务器对应的端口号。

No proxy for：不需要通过代理服务器访问的URL或者IP地址（地址之间用英文逗号分隔）。

Login：访问代理服务器的用户名。

Password：访问代理服务器的密码。

Remember：勾选，记住密码。

配置完成后，单击Check connection，输入网络地址（如：https://developer.huawei.com），检查网络连通性。提示“Connection successful”表示代理设置成功。

配置NPM代理

Hvigor、ohpm在初始化时需要从npm仓库下载依赖，如果需要代理才能访问网络，请配置npm的代理。

registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/

proxy=http://user:password@proxy.proxyserver.com:port
https-proxy=http://user:password@proxy.proxyserver.com:port

说明

如果password中存在特殊字符，如@、#、*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

!：%21

@：%40

#：%23

$：%24

&：%26

*：%2A

在系统或者用户的PATH变量中，添加Node.js安装位置的路径（默认路径为$DevEco Studio安装目录\tools\node下）。

export NODE_HOME=/home/xx/Downloads/node-vxx.xx.x-linux-x64  #本处路径请替换为Node.js的安装路径（默认路径为$DevEco Studio安装目录\tools\node下）
export PATH=$NODE_HOME/bin:$PATH

npm info express

执行结果如下图所示，则说明代理设置成功。

配置OHPM代理

在欢迎页单击Customize > All settings… > Build, Execution, Deployment > Ohpm > Optimize config，进入OHPM代理设置界面。

在打开了工程的情况下，可以单击File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Ohpm > Optimize config，进入OHPM代理设置界面。

具体配置如下：

https://ohpm.openharmony.cn/ohpm/

http://user:password@proxy.proxyserver.com

Enable Https Proxy：同步配置HTTPS Proxy信息。

填写并勾选以上信息后，点击OK。

说明：ohpm默认校验registry仓库地址证书。如果环境检查中ohpm registry access出现'SELF_SIGNED_CERT_IN_CHAIN'或'UNABLE_TO_VERIFY_LEAF_SIGNATURE'等证书校验错误时，请查看FAQ-问题现象2解决证书校验错误问题。

在此界面配置的代理信息将写入“users/用户名/.ohpm”目录下的.ohpmrc文件。因此也可直接修改“users/用户名/.ohpm”目录下的.ohpmrc文件进行配置。

进入C:/Users/用户名目录/.ohpm，打开.ohpmrc文件。如果该目录下没有.ohpmrc文件，请新建一个。

registry=https://ohpm.openharmony.cn/ohpm/

http_proxy=http://user:password@proxy.proxyserver.com:port
https_proxy=http://user:password@proxy.proxyserver.com:port

说明

如果password中存在特殊字符，如@、#、*等符号，可能导致配置不生效，建议将特殊字符替换为ASCII码，并在ASCII码前加百分号%。常用符号替换为ASCII码对照表如下：

!：%21

@：%40

#：%23

$：%24

&：%26

*：%2A

在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量中，在系统或者用户的PATH变量中，添加ohpm安装位置下bin文件夹的路径。默认路径为：DevEco Studio安装目录\tools\ohpm。

export OHPM_HOME=/home/xx/Downloads/ohpm  #本处路径请替换为ohpm的安装路径。默认路径为:/home/xx/Downloads/DevEco Studio安装目录\tools\ohpm
export PATH=$OHPM_HOME/bin:$PATH

ohpm info @ohos/lottie

执行结果如下图所示，则说明代理设置成功。

## Code blocks

### Code block 1

```
registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/
```

### Code block 2

```
proxy=http://user:password@proxy.proxyserver.com:port
https-proxy=http://user:password@proxy.proxyserver.com:port
```

### Code block 3

```
export NODE_HOME=/home/xx/Downloads/node-vxx.xx.x-linux-x64  #本处路径请替换为Node.js的安装路径（默认路径为$DevEco Studio安装目录\tools\node下）
export PATH=$NODE_HOME/bin:$PATH
```

### Code block 4

```
npm info express
```

### Code block 5

```
https://ohpm.openharmony.cn/ohpm/
```

### Code block 6

```
http://user:password@proxy.proxyserver.com
```

### Code block 7

```
registry=https://ohpm.openharmony.cn/ohpm/
```

### Code block 8

```
http_proxy=http://user:password@proxy.proxyserver.com:port
https_proxy=http://user:password@proxy.proxyserver.com:port
```

### Code block 9

```
export OHPM_HOME=/home/xx/Downloads/ohpm  #本处路径请替换为ohpm的安装路径。默认路径为:/home/xx/Downloads/DevEco Studio安装目录\tools\ohpm
export PATH=$OHPM_HOME/bin:$PATH
```

### Code block 10

```
ohpm info @ohos/lottie
```
