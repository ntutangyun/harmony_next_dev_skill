# 获取Command Line Tools

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-get_

Command Line Tools集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、堆栈解析hstack、命令行构建hvigorw、三方依赖管理ohpm和SDK中包含的一系列工具，本文主要讲解codelinter、hstack、hvigorw等工具的使用方式，关于SDK中包含的工具的使用指导请参考SDK命令行工具。

下载Command Line Tools

请前往下载中心获取命令行工具Command Line Tools，并根据下载中心页面工具完整性指导进行完整性校验。

说明

HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。

配置环境变量

将命令行工具进行解压，codelinter、ohpm等工具存放在Command Line Tools的bin目录下，需要将该目录配置到PATH环境变量中。

[h2]Windows

命令行工具解压后，将${Command Line Tools解压路径}\command-line-tools\bin目录配置到系统或者用户的PATH环境变量中，配置完成后重新打开命令行窗口。

例如将命令行工具解压到D盘根目录，示例如下。

[h2]macOS/Linux

将下载后的命令行工具解压到本地。

echo $SHELL

vi ~/.bash_profile

vi ~/.zshrc

单击字母“i”，进入Insert模式。

export PATH=${Command Line Tools解压路径}/command-line-tools/bin:$PATH

编辑完成后，单击Esc键，退出编辑模式，然后输入“:wq”，单击Enter键保存。

source ~/.bash_profile

source ~/.zshrc

说明

如需验证是否配置成功，可以使用相关命令验证，例如执行codelinter -v指令，检查是否可以正确获取codelinter工具版本。

## Code blocks

### Code block 1

```
echo $SHELL
```

### Code block 2

```
vi ~/.bash_profile
```

### Code block 3

```
vi ~/.zshrc
```

### Code block 4

```
export PATH=${Command Line Tools解压路径}/command-line-tools/bin:$PATH
```

### Code block 5

```
source ~/.bash_profile
```

### Code block 6

```
source ~/.zshrc
```
