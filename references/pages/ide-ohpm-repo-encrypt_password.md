# ohpm

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-encrypt_password_

必须在encrypt_password命令后面配置--crypto_path <string>参数，指定加密组件的路径。如果是完整组件，将用该组件对键入的密码内容进行加密。如果是一个空目录，则命令将生成新的加密组件并对键入的密码内容进行加密。

示例

执行以下命令：

ohpm-repo encrypt_password --crypto_path D:\encryptPath

结果示例：

ohpm-repo --version
ohpm-repo pack
