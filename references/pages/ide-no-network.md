# 离线环境配置指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-network_

如果开发者所使用的电脑处于完全无网络的离线环境中，需要先在一台可访问网络的电脑上准备好以下文件，将这些文件拷贝到无网络电脑中。

安装hypium

工程模板的工程级oh-package.json5文件中默认配置了hypium依赖，因此需要安装hypium，如果配置了其他依赖，也可参考以下步骤安装。

{
  "dependencies": {
    "@ohos/hypium": "1.0.18"
  }
}

配置环境变量并打开命令行工具，执行ohpm install命令，会生成oh_modules文件夹和oh-package-lock.json5文件。

将oh_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。

说明

有网环境和无网环境下使用的ohpm版本需保持一致，否则可能导致oh-package-lock.json5文件不生效。

安装三方库

方式一：使用ohpm-repo搭建私仓，将需要依赖的三方包发布至私仓中，并将.ohpmrc文件中的registry配置项的值替换为该私仓地址，以此从私仓中获取依赖。

{
  "dependencies": {
    "@ohos/hypium": "1.0.17",
    "@ohos/lottie": "^2.0.0"
  }
}

打开命令行工具，执行ohpm install命令，会生成oh_modules文件夹和oh-package-lock.json5文件。

将oh_modules文件夹和oh-package-lock.json5文件拷贝到无网络电脑的工程根目录下。

注意

使用方法二时，需要确保可访问网络的电脑与无网络电脑中ohpm版本是一致的，以避免因oh-package-lock.json5文件版本不匹配而导致oh-package-lock.json5文件失效的问题。

部署模拟器

请参考离线部署模拟器。

## Code blocks

### Code block 1

```
{
  "dependencies": {
    "@ohos/hypium": "1.0.18"
  }
}
```

### Code block 2

```
{
  "dependencies": {
    "@ohos/hypium": "1.0.17",
    "@ohos/lottie": "^2.0.0"
  }
}
```
