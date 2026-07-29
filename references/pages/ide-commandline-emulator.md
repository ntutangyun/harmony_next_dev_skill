# 模拟器工具（Emulator）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-emulator_

从6.1.0 Release版本开始，Command Line Tools集成Emulator工具，支持Windows和macOS平台，可独立进行模拟器创建、启动、关闭、镜像下载等操作。

从26.0.0 Beta1版本开始，支持在Linux平台上使用Emulator，具体使用方式请参考使用Linux版本Emulator工具。

说明

在macOS上使用命令行工具时，如果弹框提示Emulator无法验证开发者，可以在系统的设置 > 隐私与安全性中选择仍要打开Emulator，或者使用DevEco Studio目录下的Emulator工具。

环境准备

Emulator工具在command-line-tools安装目录的emulator目录下，有两种执行命令的方式。

方式一：在命令行终端中进入emulator目录下，执行命令。

在系统或者用户的PATH变量中，添加路径{command-line-tools安装目录}/emulator，配置完成后重新打开命令行窗口使环境变量生效。

打开命令行终端，执行以下命令。

export PATH={command-line-tools安装目录}/emulator:$PATH

模拟器命令

Emulator命令请参考通过命令行使用模拟器。

在模拟器上推包调试

可通过hdc工具在模拟器上进行推包调试。

hdc list targets

hdc tconn 127.0.0.1:5555

连接成功后，通过hdc在模拟器上安装、卸载应用等，更多使用方式请参考SDK命令行工具。

使用Linux版本Emulator工具

从26.0.0 Beta1版本开始，支持在Linux平台使用模拟器工具。

[h2]环境准备

当前仅支持Ubuntu 18.04及以上的Linux系统，使用前需要安装相关的依赖，以Ubuntu 18.04操作系统为例，执行命令：

apt install -y libatomic1 libpulse0 libegl1 libgbm1 libgl1 libpng16-16 libfontconfig1 libfreetype6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libsm6 libice6 libxkbcommon-x11-0 libxkbcommon0 libglib2.0-0

[h2]使用约束

Linux模拟器依赖系统kvm能力，需要手动将Emulator程序当前用户加入/dev/kvm所在的组中。

Linux模拟器图形渲染依赖/dev/dri下的设备渲染节点，如card0、renderD128等，需要手动将Emulator程序当前用户加入相关节点的用户组中。

如需使用第三方远程桌面工具操作Linux，请确保工具可使用的图形驱动支持OpenGL4.1或以上版本。

[h2]模拟器命令差异

针对无图形界面的Linux环境，启动模拟器命令必须添加-noWindow参数。除此之外，其他命令和Windows/macOS相同，详细命令请参考通过命令行使用模拟器。

## Code blocks

### Code block 1

```
export PATH={command-line-tools安装目录}/emulator:$PATH
```

### Code block 2

```
hdc list targets
```

### Code block 3

```
hdc tconn 127.0.0.1:5555
```

### Code block 4

```
apt install -y libatomic1 libpulse0 libegl1 libgbm1 libgl1 libpng16-16 libfontconfig1 libfreetype6 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libsm6 libice6 libxkbcommon-x11-0 libxkbcommon0 libglib2.0-0
```
