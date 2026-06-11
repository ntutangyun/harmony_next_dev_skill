# 自定义.hvigor目录路径

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-path_

.hvigor目录默认位于用户目录下：

Windows：C:\Users\username\.hvigor

macOS：/Users/username/.hvigor

root用户：/root/.hvigor

非root用户：/home/username/.hvigor

若默认目录的磁盘空间不足，开发者需要自定义.hvigor目录路径，可通过以下方式自行配置。

说明

自定义.hvigor目录时，不能包含空格。

在系统或者用户的变量中，添加自定义.hvigor目录的绝对路径。

变量名：HVIGOR_USER_HOME

变量值：自定义存放.hvigor目录的绝对路径。如D:\HvigorUserHome

launchctl setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径

该设置方式在重启电脑后将失效。

说明

在macOS上设置系统变量的方式因系统版本不同而存在多种差异，以下仅为在macOS上为DevEco Studio设置系统变量的一种示例，具体设置方式以系统版本为准。

在/etc/launchd.conf（若该文件不存在，可自行创建）中添加如下内容。

setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径

设置完成后，重启电脑后才可生效。

打开终端工具，执行以下命令。

vim ~/.bashrc

export HVIGOR_USER_HOME=/home/xx  #本处路径请替换为.hvigor目录的绝对路径

保存并关闭文件，使用source命令重新加载.bashrc配置文件。

source ~/.bashrc

## Code blocks

### Code block 1

```
launchctl setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径
```

### Code block 2

```
setenv HVIGOR_USER_HOME /Users/xx #本处路径请替换为.hvigor目录的绝对路径
```

### Code block 3

```
vim ~/.bashrc
```

### Code block 4

```
export HVIGOR_USER_HOME=/home/xx  #本处路径请替换为.hvigor目录的绝对路径
```

### Code block 5

```
source ~/.bashrc
```
