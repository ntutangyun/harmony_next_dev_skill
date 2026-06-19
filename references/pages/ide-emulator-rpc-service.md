# 远程控制模拟器

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-rpc-service_

从26.0.0 Beta1版本开始，支持使用emulator-rpc-service命令行工具对模拟器进行远程控制，开发者可以在本地电脑上访问并控制远程服务器上已启动RPC服务器模式的模拟器，支持Windows、macOS和Linux平台。

工作流程

使用emulator-rpc-service工具对模拟器进行远程控制的工作流程如下：

工作流程主要包括：

启动RPC服务器模式：在目标服务器上，启动模拟器RPC服务器模式，以便客户端连接使用。

客户端创建会话：客户端通过指定服务端IP和端口号，以及安全认证命令，创建会话连接到服务端。

执行命令：客户端和服务端成功连接后，客户端可查询会话信息和模拟器实例信息，执行模拟器启动停止、场景化等命令，操控服务端上已存在的模拟器。

环境准备

emulator-rpc-service命令行在DevEco Studio安装目录的tools/emulator目录下，或Command Line Tools安装目录的emulator目录下，此处以DevEco Studio为例，有两种执行命令的方式。

方式一：在命令行终端中进入emulator目录下，执行命令。

在系统或者用户的PATH变量中，添加emulator-rpc-service的路径{DevEco Studio安装目录}/tools/emulator，配置完成后重新打开命令行窗口使环境变量生效。

export PATH={DevEco Studio安装目录}/tools/emulator:$PATH

使用约束

使用前必须保证客户端和服务端都存在emulator-rpc-service，即已下载DevEco Studio或Command Line Tools。

确保防火墙允许指定端口的通信。

确保当前用户有执行命令的权限和目录读写权限。

命令

[h2]启动RPC服务器模式

在目标服务器上，启动模拟器RPC服务器模式，包括无认证模式和认证模式，建议使用认证模式。

# 无认证模式
emulator-rpc-service -server -port {端口} --no-auth
# 认证模式
emulator-rpc-service -server -port {端口} -token {令牌} -pem_root_certs {根证书路径} -pem_private_key {私钥路径} -pem_cert_chain {证书链路径}

参数：

参数名	说明
-server	必选参数，启动RPC服务器模式。
-port	必选参数，指定服务器端口号，指定范围0-65535。
--no-auth	可选参数，使用无认证模式启动RPC服务器。
-token	可选参数，使用认证模式启动RPC服务器，指定认证token。要求证书是支持双向认证的。
-pem_root_certs	可选参数，使用认证模式后必选，指定根证书路径。
-pem_private_key	可选参数，使用认证模式后必选，指定私钥路径。
-pem_cert_chain	可选参数，使用认证模式后必选，指定证书链路径。

[h2]创建会话

客户端创建会话连接到服务端，会话创建后会一直保持连接，直到手动删除或客户端退出。

# 无认证模式
emulator-rpc-service -session {会话名称} -ip {IP地址} -port {端口} --no-auth
# 认证模式
emulator-rpc-service -session {会话名称} -ip {IP地址} -port {端口} -token {令牌} -pem_root_certs {根证书路径} -pem_private_key {私钥路径} -pem_cert_chain {证书链路径}

参数：

参数名	说明
-session	必选参数，指定会话名称，会话名称在同一客户端中必须唯一，长度1-60个字符，仅允许字母、数字、下划线。
-ip	必选参数，指定RPC服务器的ip地址。
-port	必选参数，指定RPC服务器的端口号。
--no-auth	可选参数，使用无认证模式访问RPC服务器。
-token	可选参数，使用认证模式访问RPC服务器，指定认证token。要求证书是支持双向认证的。
-pem_root_certs	可选参数，使用认证模式后必选，指定根证书路径。
-pem_private_key	可选参数，使用认证模式后必选，指定私钥路径。
-pem_cert_chain	可选参数，使用认证模式后必选，指定证书链路径。

[h2]查询会话信息

查看当前已创建的所有会话及其状态。

emulator-rpc-service -list -details

参数：

参数名	说明
-list	必选参数，查询所有会话和状态，以及可控制的模拟器实例名称。
-details	可选参数，查询所有会话和状态，以及可控制的模拟器实例的详细信息，详细信息的含义请参考查看模拟器实例。

[h2]删除会话

emulator-rpc-service -session {会话名称} -delete

参数：

参数名	说明
-session	必选参数，指定会话名称。
-delete	必选参数，删除指定的会话。

[h2]执行远程命令

通过已建立的会话向模拟器发送控制命令。

emulator-rpc-service -session {会话名称} shell "{模拟器命令}"

参数：

参数名	说明
-session	必选参数，指定会话名称。
shell	必选参数，指定需要执行的命令，目前远程命令仅支持启动、停止模拟器和场景化模拟命令。

示例：

emulator-rpc-service -session mysession shell "-start 'my Emulator' -noWindow"

[h2]获取帮助

emulator-rpc-service -h
emulator-rpc-service -help
emulator-rpc-service --help

完整工作流程示例

使用认证模式连接并控制模拟器。

# 启动RPC服务器模式，假设服务器IP为192.168.1.100
emulator-rpc-service -server -port 6555 -token mytoken -pem_root_certs /path/to/root.pem -pem_private_key /path/to/client.key -pem_cert_chain /path/to/client.pem
# 客户端创建会话，连接到服务端
emulator-rpc-service -session mysession -ip 192.168.1.100 -port 6555 -token mytoken -pem_root_certs /path/to/root.pem -pem_private_key /path/to/client.key -pem_cert_chain /path/to/client.pem
# 查询所有会话
emulator-rpc-service -list
# 启动服务端模拟器
emulator-rpc-service -session mysession shell "-start 'MyPhone' -noWindow"
# 使用模拟器场景化命令
emulator-rpc-service -session mysession shell "-instance 'MyPhone' -rotation right"
# 关闭服务端模拟器
emulator-rpc-service -session mysession shell "-stop 'MyPhone'"
# 删除会话
emulator-rpc-service -session mysession -delete

## Code blocks

### Code block 1

```
export PATH={DevEco Studio安装目录}/tools/emulator:$PATH
```

### Code block 2

```
# 无认证模式
emulator-rpc-service -server -port {端口} --no-auth
# 认证模式
emulator-rpc-service -server -port {端口} -token {令牌} -pem_root_certs {根证书路径} -pem_private_key {私钥路径} -pem_cert_chain {证书链路径}
```

### Code block 3

```
# 无认证模式
emulator-rpc-service -session {会话名称} -ip {IP地址} -port {端口} --no-auth
# 认证模式
emulator-rpc-service -session {会话名称} -ip {IP地址} -port {端口} -token {令牌} -pem_root_certs {根证书路径} -pem_private_key {私钥路径} -pem_cert_chain {证书链路径}
```

### Code block 4

```
emulator-rpc-service -list -details
```

### Code block 5

```
emulator-rpc-service -session {会话名称} -delete
```

### Code block 6

```
emulator-rpc-service -session {会话名称} shell "{模拟器命令}"
```

### Code block 7

```
emulator-rpc-service -session mysession shell "-start 'my Emulator' -noWindow"
```

### Code block 8

```
emulator-rpc-service -h
emulator-rpc-service -help
emulator-rpc-service --help
```

### Code block 9

```
# 启动RPC服务器模式，假设服务器IP为192.168.1.100
emulator-rpc-service -server -port 6555 -token mytoken -pem_root_certs /path/to/root.pem -pem_private_key /path/to/client.key -pem_cert_chain /path/to/client.pem
# 客户端创建会话，连接到服务端
emulator-rpc-service -session mysession -ip 192.168.1.100 -port 6555 -token mytoken -pem_root_certs /path/to/root.pem -pem_private_key /path/to/client.key -pem_cert_chain /path/to/client.pem
# 查询所有会话
emulator-rpc-service -list
# 启动服务端模拟器
emulator-rpc-service -session mysession shell "-start 'MyPhone' -noWindow"
# 使用模拟器场景化命令
emulator-rpc-service -session mysession shell "-instance 'MyPhone' -rotation right"
# 关闭服务端模拟器
emulator-rpc-service -session mysession shell "-stop 'MyPhone'"
# 删除会话
emulator-rpc-service -session mysession -delete
```
