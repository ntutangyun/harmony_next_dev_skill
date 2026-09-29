# 快速入门

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-install_

环境准备

DevEco CLI支持在Windows、macOS和Linux上运行。

从1.3.0版本开始支持在Linux上运行。

[h2]环境搭建

下载和安装DevEco Studio 6.0.0及以上版本。

安装Node.js，推荐使用22及以上版本。

说明

在Linux环境运行时，需要手动配置环境变量来指定工具链路径。

export DEVECO_CLI_CLI_PATH=/opt/command-line-tools

[h2]检验环境是否搭建成功

在终端Shell中，验证Node.js环境：

node -v
npm -v

安装和更新

npm install -g @deveco/deveco-cli@stable

安装DevEco CLI（尝鲜版）

npm install -g @deveco/deveco-cli

devecocli --version

devecocli update

说明

安装命令中的@stable标签是可选项，带有@stable标签表示下载安装稳定版本，未带有@stable标签表示下载安装最新版本。

首次使用

## Code blocks

### Code block 1

```
export DEVECO_CLI_CLI_PATH=/opt/command-line-tools
```

### Code block 2

```
node -v
npm -v
```

### Code block 3

```
npm install -g @deveco/deveco-cli@stable
```

### Code block 4

```
npm install -g @deveco/deveco-cli
```

### Code block 5

```
devecocli --version
```

### Code block 6

```
devecocli update
```
