# 环境准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-environment-preparation_

开发环境与运行环境合设场景：开发环境和运行环境在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境，同时在该环境上进行代码开发与编译。

开发环境与运行环境分设场景：开发环境和运行环境不在同一台机器上，开发者使用连接上Kirin AI处理器的机器作为运行环境；使用其他独立机器进行代码开发与编译，作为开发环境。

说明

开发运行环境需要满足以下要求：

ubuntu版本大于等于22.04，ubuntu架构为x86_64， python版本在3.7与3.10之间（包含），gcc/g++版本大于等于7.0。

设备连接与调试参考hdc。

进行自定义算子开发前，需要完成驱动及DDK的安装。

下载tools_ascendc，并在Linux环境上解压。

说明

在Windows平台解压会导致软链接失效。

下载需要的平台插件包，在linux开发环境上解压，并将需要的平台插件拷贝到${install_path}/ddk/tools/platform下。其中${install_path}为tools包的解压目录。拷贝后的目录结构如下。

tools
├── platform
│   ├── kirin9020
│   ├── kirinx90

进入目录ddk/tools/tools_ascendc，修改安装脚本权限，执行安装脚本进行安装，命令如下。

cd ddk/tools/tools_ascendc
chmod +x install.sh
source ./install.sh

在使用tools工具前，需要先设置环境变量，执行source ${install_path}/ddk/tools/tools_ascendc/set_ascendc_env.sh。

例如安装目录为/usr/local/：

source  /usr/local/ddk/tools/tools_ascendc/set_ascendc_env.sh

python软件依赖，执行步骤3的安装脚本install.sh时会自动安装。若执行ascendebug时提示无对应模块，可执行下表中的命令手动安装。

表1 第三方软件

第三方软件	用途	如何安装
toml	加载和转储TOML文件的功能。	pip3 install toml
jinja2	CPU调测模板使用。	pip3 install jinja2
numpy	精度比对时使用。	pip3 install numpy
torch	输入、输出数据格式转换使用。	pip3 install torch
sympy	用于进行符号计算	pip3 install sympy
paramiko	与远程linux环境连接	pip3 install paramiko
protobuf	模型解析	pip3 install protobuf
AscendC简介
快速入门
