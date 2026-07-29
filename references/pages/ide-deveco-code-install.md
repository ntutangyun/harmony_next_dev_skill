# 下载与安装

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-install_

环境准备

[h2]环境要求

DevEco Code支持在Windows和macOS上运行，具体运行环境要求如下。

Windows运行环境：

类别	要求
操作系统	Windows 11 22H2及以上版本
RAM	8GB及以上（以短会话、单模块代码编辑场景为主）16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主）
磁盘空间	8GB及以上 若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上
终端Shell	PowerShell5.1及以上版本，推荐使用PowerShell7及以上版本

macOS运行环境：

类别	要求
操作系统	macOS 15 Sequoia及以上版本
CPU	Intel芯片或M系列Apple芯片，推荐使用M系列Apple芯片
RAM	8GB及以上（以短会话、单模块代码编辑场景为主）16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主）
磁盘空间	8GB及以上 若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上
终端Shell	Zsh（Z Shell）

[h2]搭建环境

DevEco Code通过npm分发，安装前请先准备以下环境：

安装Node.js，推荐使用22及以上版本。

（可选）安装DevEco Studio 6.1.0及以上版本，不安装会影响HarmonyOS工程的编译构建、推包等。

macOS：/Applications/DevEco-Studio.app

Windows：C:\Program Files\Huawei\DevEco Studio

[h2]检验环境是否搭建成功

在终端Shell中，验证Node.js环境：

node -v
npm -v

安装

npm install -g @deveco/deveco-code@stable

安装（尝鲜版）

npm install -g @deveco/deveco-code

说明

安装时默认使用npm 官方源，指定淘宝镜像源时命令为npm install -g @deveco/deveco-code --registry=https://registry.npmmirror.com。

安装命令中的标签@stable是可选项，加标签@stable表示下载安装稳定版本，不加标签@stable表示下载安装最新版本。

deveco --version

更新与卸载

deveco upgrade

deveco uninstall   // 卸载运行时数据和安装包，适用于彻底清除所有数据的场景
npm uninstall -g @deveco/deveco-code   // 保留运行时数据，只卸载安装包，适用于保留配置项卸载重装的场景

启动与登录

deveco

deveco auth logout

## Code blocks

### Code block 1

```
node -v
npm -v
```

### Code block 2

```
npm install -g @deveco/deveco-code@stable
```

### Code block 3

```
npm install -g @deveco/deveco-code
```

### Code block 4

```
deveco --version
```

### Code block 5

```
deveco upgrade
```

### Code block 6

```
deveco uninstall   // 卸载运行时数据和安装包，适用于彻底清除所有数据的场景
npm uninstall -g @deveco/deveco-code   // 保留运行时数据，只卸载安装包，适用于保留配置项卸载重装的场景
```

### Code block 7

```
deveco
```

### Code block 8

```
deveco auth logout
```
