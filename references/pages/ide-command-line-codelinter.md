# 代码检查工具（codelinter）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codelinter_

codelinter同时支持使用命令行执行代码检查与修复，可将codelinter工具集成到门禁或持续集成环境中。

codelinter命令行格式为：

codelinter [options] [dir]

options：可选配置，请参考表1。

dir：待检查的工程根目录；为可选参数，如不指定，默认为当前上下文目录。

指令	说明
--config/-c <filepath>	指定执行codelinter检查的规则配置文件，<filepath>指定执行检查的规则配置文件位置。
--fix	设置codelinter检查同时执行QuickFix。
--format/-f	设置检查结果的输出格式。目前支持default/json/xml/html四种格式；不指定时，默认是default格式（文本格式）。
--output/-o <filepath>	指定检查结果保存位置，且命令行窗口不展示检查结果。<filepath>指定存放代码检查结果的文件路径，支持使用相对/绝对路径。不使用--output指令时，检查结果默认会显示在命令行窗口中。
--version/-v	查看codelinter版本。
--product/-p <productName>	指定当前生效的product。 <productName> 为生效的product名称。
--incremental/-i	对Git工程中的增量文件（包含新增/修改/重命名的文件）执行Code Linter检查。
--language/-l <language>	设置codelinter语言为cn或en。默认为en。
--help/-h	查询codelinter命令行帮助。
--exit-on/-e <levels>	指定哪些告警级别需要返回非零退出码，告警级别包括：error、warn和suggestion。若需要指定多个告警级别，级别间需要用英文逗号分开。 退出码的计算方式为：用一个3位的二进制数从高到低分别表示error、warn、suggestion告警级别。若在命令行中配置告警级别，并且代码检查结果中也包含该告警级别，则该二进制值为1，否则均为0。将二进制数转换为十进制数，则是退出码。 例如： 命令配置为--exit-on error，代码检查结果包括error、warn、suggestion三类告警，则退出码的二进制数为100，十进制数为4。命令配置为--exit-on error，代码检查结果包括warn、suggestion两类告警，则退出码的二进制数为000，十进制数为0。

codelinter // 进行codelinter检查

codelinter -c filepath // 指定执行检查的规则配置文件位置

codelinter -c filepath --fix // 对工程中的告警进行修复

codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录

codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录

codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径

codelinter [dir] -f json  //[dir]为待检查的工程根目录

codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径

## Code blocks

### Code block 1

```
codelinter [options] [dir]
```

### Code block 2

```
codelinter // 进行codelinter检查
```

### Code block 3

```
codelinter -c filepath // 指定执行检查的规则配置文件位置
```

### Code block 4

```
codelinter -c filepath --fix // 对工程中的告警进行修复
```

### Code block 5

```
codelinter dir [filepath] [dir1] // 指定执行检查的工程目录或文件路径。支持同时配置多个文件/文件夹路径。 filepath为待检查的文件所在位置，dir、dir1指定待检查的工程目录
```

### Code block 6

```
codelinter -c filepath dir // filepath为指定的规则配置文件所在位置，dir指定执行检查的工程根目录
```

### Code block 7

```
codelinter -c filepath dir --fix // 对指定工程中的告警进行修复。支持配置同时多个工程路径
```

### Code block 8

```
codelinter [dir] -f json  //[dir]为待检查的工程根目录
```

### Code block 9

```
codelinter [dir] -f json -o filepath2     // [dir]为待检查的工程根目录，filepath2为指定存放代码检查结果的文件路径
```
