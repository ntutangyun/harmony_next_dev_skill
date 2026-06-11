# 发布共享包

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish_

发布打包的HAR，可供其他开发者安装和引用。接下来将介绍如何发布HAR共享包。

说明

OpenHarmony三方库中心仓仅支持HAR共享包发布，不支持HSP共享包发布。如需在应用内共享HSP，可将HSP共享包发布至私仓使用，请参考ohpm私仓搭建工具。

新建README.md文件：在README.md文件中必须包含包的介绍和引用方式，还可以根据包的内容添加更详细介绍。

新建CHANGELOG.md文件：填写HAR的版本更新记录。

添加LICENSE文件：LICENSE许可文件。

说明

若修改了HAR包模块级oh-package.json5文件中version字段信息，请先执行Build > Clean Project指令，再重新进行Build全量构建。

ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh_ohpm/mykey

说明

~/.ssh_ohpm/mykey 为私钥文件 mykey 的文件路径，按照实际情况指定。指定的私钥存储目录必须存在。

追加了.pub后缀的相应公钥文件会存放在和私钥相同的目录下。

OHPM包管理器只支持加密密钥认证，请在生成公私钥时输入密码。

ohpm config set key_path  ~/.ssh_ohpm/mykey

ohpm config set publish_id your_publish_id

ohpm publish <HAR路径>

## Code blocks

### Code block 1

```
ssh-keygen -m PEM -t RSA -b 4096 -f ~/.ssh_ohpm/mykey
```

### Code block 2

```
ohpm config set key_path  ~/.ssh_ohpm/mykey
```

### Code block 3

```
ohpm config set publish_id your_publish_id
```

### Code block 4

```
ohpm publish <HAR路径>
```
