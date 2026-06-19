# ohpm config

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-config_

设置ohpm用户级配置项。

命令格式

ohpm config set <key> <value>
ohpm config get <key>
ohpm config delete <key>
ohpm config list
ohpm config encrypt [options]

说明

配置文件中信息以键值对<key> = <value>形式存在。

功能描述

ohpm 从命令行和 .ohpmrc 文件中获取其配置设置。有关更多 .ohpmrc 文件信息和可用配置选项，请参阅 ohpmrc 章节。

注意

ohpm config 仅支持配置项字段（默认项字段请查阅 ohpmrc 章节），且仅支持修改用户级目录下的 .ohpmrc 文件。

子命令

[h2]set

ohpm config set <key> <value>

在用户级目录下 .ohpmrc 文件中，以键值对<key> = <value>形式写入数据。

示例

ohpm config set log_level debug

成功执行后，在用户目录/.ohpm/.ohpmrc文件中将显示log_level=debug。

[h2]get

ohpm config get <key>

将从命令行，项目级 .ohpmrc 文件，用户级 .ohpmrc 文件（优先级依次递减）中获取的值进行标准输出。

如果未提供键值，则此命令执行效果与命令 ohpm config list 相同。

示例1

ohpm config get log_level

info

示例2

ohpm config get log_level

debug

示例3

ohpm config get

; "user" config from C:\Users\username\.ohpm\.ohpmrc

registry="http://localhost:8088/repos/ohpm"
strict_ssl = false
log_level = "debug"

; "user" config from C:\Users\username\.ohpm\.ohpmrc
; node bin location = C:\Program Files\nodejs\node.exe
; node version = v18.19.1
; ohpm local prefix = C:\Users\username
; ohpm version = 5.1.2-rc.2
; cwd = C:\Users\username
; HOME = C:\Users\username

[h2]list

ohpm config list
alias: ls

显示所有配置项。

示例

ohpm config list 或者 ohpm config ls

; "user" config from C:\Users\username\.ohpm\.ohpmrc

registry="http://localhost:8088/repos/ohpm"
strict_ssl = false
log_level = "debug"

; "user" config from C:\Users\username\.ohpm\.ohpmrc
; node bin location = C:\Program Files\nodejs\node.exe
; node version = v18.19.1
; ohpm local prefix = C:\Users\username
; ohpm version = 5.1.2-rc.2
; cwd = C:\Users\username
; HOME = C:\Users\username

[h2]delete

ohpm config delete <key>

删除用户级目录下 ohpmrc 文件中指定的键值。

示例

registry=http://localhost:8088/repos/ohpm
strict_ssl=false
log_level=debug

ohpm config delete registry

strict_ssl=false
log_level=debug

[h2]encrypt

ohpm config encrypt [options]

使用加密组件加密标准输入的数据，并输出密文到标准输出。

首次使用：

示例

ohpm config encrypt --crypto_path D:\path\to\empty_dir

ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
ohpm INFO: The crypto component has been created successfully.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

crypto_path=D:\path\to\empty_dir

非首次使用：

若不指定 --crypto_path，则自动从 .ohpmrc 文件中读取配置（优先级：项目级 > 用户级 .ohpmrc），必须保证路径存在且包含有效加密组件。

若报错提示加密组件错误，可重新执行ohpm config encrypt --crypto_path <string> 命令。

示例

ohpm config encrypt

Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

密文使用：

生成的加密结果可以配置到项目级或用户级 .ohpmrc 文件中，用于敏感配置项。

Options

[h2]json

默认值：false

类型： Boolean

别名：j

可以在 config list 命令后面配置 -j或者--json 参数，以 json 格式输出所有配置项及默认值。

// 示例
// 1.执行list命令并以json形式输出
ohpm config list -j 或 ohpm config list --json
// 2.命令执行结果
{
  "registry": "http://localhost:8088/repos/ohpm",
  "strict_ssl": false,
  "log_level": "info",
  ......
}

[h2]crypto_path

默认值：无

类型：string

指定加密组件路径用于数据加密。针对指定路径的不同情况，说明如下：

若指定路径不存在，自动创建目录并生成新加密组件；

若路径为空目录，将自动在目录中生成新加密组件；

若路径已存在有效加密组件，则使用现有组件加密。

// 示例1
// 1.执行 encrypt --crypto_path <string> 命令，指定的路径为空目录
ohpm config encrypt --crypto_path D:\path\to\empty_dir
// 2.成功执行后，在指定路径生成新的加密组件，并对用户输入内容进行加密，其中用户输入内容不可见
ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
ohpm INFO: The crypto component has been created successfully.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

// 示例2
// 1.执行 encrypt --crypto_path <string> 命令，指定的路径为有效的加密组件
ohpm config encrypt --crypto_path D:\path\to\crypto_dir
// 2.成功执行后，对用户输入内容进行加密，其中用户输入内容不可见
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

[h2]log_level

默认值：无

类型：string

从ohpm 6.0.2.636版本开始，可以在命令后配置--log_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

[h2]debug

默认值：false

类型：Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。

## Code blocks

### Code block 1

```
ohpm config set <key> <value>
ohpm config get <key>
ohpm config delete <key>
ohpm config list
ohpm config encrypt [options]
```

### Code block 2

```
ohpm config set <key> <value>
```

### Code block 3

```
ohpm config set log_level debug
```

### Code block 4

```
ohpm config get <key>
```

### Code block 5

```
ohpm config get log_level
```

### Code block 6

```
info
```

### Code block 7

```
ohpm config get log_level
```

### Code block 8

```
debug
```

### Code block 9

```
ohpm config get
```

### Code block 10

```
; "user" config from C:\Users\username\.ohpm\.ohpmrc

registry="http://localhost:8088/repos/ohpm"
strict_ssl = false
log_level = "debug"

; "user" config from C:\Users\username\.ohpm\.ohpmrc
; node bin location = C:\Program Files\nodejs\node.exe
; node version = v18.19.1
; ohpm local prefix = C:\Users\username
; ohpm version = 5.1.2-rc.2
; cwd = C:\Users\username
; HOME = C:\Users\username
```

### Code block 11

```
ohpm config list
alias: ls
```

### Code block 12

```
ohpm config list 或者 ohpm config ls
```

### Code block 13

```
; "user" config from C:\Users\username\.ohpm\.ohpmrc

registry="http://localhost:8088/repos/ohpm"
strict_ssl = false
log_level = "debug"

; "user" config from C:\Users\username\.ohpm\.ohpmrc
; node bin location = C:\Program Files\nodejs\node.exe
; node version = v18.19.1
; ohpm local prefix = C:\Users\username
; ohpm version = 5.1.2-rc.2
; cwd = C:\Users\username
; HOME = C:\Users\username
```

### Code block 14

```
ohpm config delete <key>
```

### Code block 15

```
registry=http://localhost:8088/repos/ohpm
strict_ssl=false
log_level=debug
```

### Code block 16

```
ohpm config delete registry
```

### Code block 17

```
strict_ssl=false
log_level=debug
```

### Code block 18

```
ohpm config encrypt [options]
```

### Code block 19

```
ohpm config encrypt --crypto_path D:\path\to\empty_dir
```

### Code block 20

```
ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
ohpm INFO: The crypto component has been created successfully.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
```

### Code block 21

```
crypto_path=D:\path\to\empty_dir
```

### Code block 22

```
ohpm config encrypt
```

### Code block 23

```
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
```

### Code block 24

```
// 示例
// 1.执行list命令并以json形式输出
ohpm config list -j 或 ohpm config list --json
// 2.命令执行结果
{
  "registry": "http://localhost:8088/repos/ohpm",
  "strict_ssl": false,
  "log_level": "info",
  ......
}
```

### Code block 25

```
// 示例1
// 1.执行 encrypt --crypto_path <string> 命令，指定的路径为空目录
ohpm config encrypt --crypto_path D:\path\to\empty_dir
// 2.成功执行后，在指定路径生成新的加密组件，并对用户输入内容进行加密，其中用户输入内容不可见
ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
ohpm INFO: The crypto component has been created successfully.
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

// 示例2
// 1.执行 encrypt --crypto_path <string> 命令，指定的路径为有效的加密组件
ohpm config encrypt --crypto_path D:\path\to\crypto_dir
// 2.成功执行后，对用户输入内容进行加密，其中用户输入内容不可见
Please enter the password to be encrypted:
ohpm INFO: encrypted result:
security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
```
