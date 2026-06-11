# 引用及管理共享包

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-import_

引用三方HAR，包括从ohpm仓库进行安装、从本地文件夹和本地压缩包中进行安装三种方式。

ohpm config set registry your_registry1,your_registry2

说明：ohpm支持多个仓库地址，采用英文逗号分隔。

方式一：在菜单栏点击Tools > OHPM Index，进入DevEco Studio内置的OpenHarmony开源中心仓，选择需要的三方包，详情请参考使用OpenHarmony开源中心仓管理三方包。仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

cd path/to/your/project/entry
ohpm install @ohos/lottie

"dependencies": {
  "@ohos/lottie": "^2.0.0"
}

依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装到该模块的oh_modules目录下。

ohpm install

cd path/to/your/project/entry
ohpm install path/to/foo

"dependencies": {
  "foo": "file:path/to/foo"  // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
}

依赖设置完成后，需要执行ohpm install命令安装依赖包，模块foo的源码会安装在entry模块的oh_modules目录下。

ohpm install

cd path/to/your/project/entry
ohpm install path/to/package.har

cd path/to/your/project/entry
ohpm install path/to/package.tgz

"dependencies": {
  "package": "file:path/to/package.har" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径。
}

说明

代码片段中package.har为三方包文件名；"package"为引用该三方包所使用的依赖名称，建议与三方包包名，即三方包的oh-package.json5文件中的name字段保持一致。

"dependencies": {
  "package": "file:path/to/package.tgz" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
}

依赖设置完成后，需要执行ohpm install命令安装依赖包，依赖包会安装在该模块的oh_modules目录下。

ohpm install

另外，在安装或卸载共享包时，可在模块或工程的oh-package.json5文件中增加钩子设置，以管理install、uninstall命令的生命周期，配置示例如下：

 "hooks": {
    "preInstall": "echo 00 preInstall", // install命令执行之前
    "postInstall": "echo 00 postInstall", // install命令执行之后
    "preUninstall": "echo 00 preUninstall", // uninstall命令执行之前
    "postUninstall": "echo 00 postUninstall"  // uninstall命令执行之后
  }

说明

目前只支持执行当前模块或工程的oh-package.json5文件中hooks，不支持执行依赖中hooks。

在引用共享包时，请注意当前只支持在模块和工程下的oh-package.json5文件中声明dependencies依赖，才会被当做依赖使用，并在编译构建过程中进行相应的处理。

使用OpenHarmony开源中心仓管理三方包

说明

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

从DevEco Studio 6.0.0 Beta5版本开始，新增OHPM Index入口，提供OpenHarmony开源中心仓的高效筛选和管理能力，提升开发者选型开发效率，消减因软件信息不对称导致的选型使用风险，快速选择与定位所需的开源三方库。

在菜单栏点击Tools > OHPM Index，进入OpenHarmony开源中心仓。

三方包安装完成后，在工程级oh-package.json5文件中可以看到已安装的三方包名称及版本信息，oh_modules中将同时添加该三方包。

## Code blocks

### Code block 1

```
ohpm config set registry your_registry1,your_registry2
```

### Code block 2

```
cd path/to/your/project/entry
ohpm install @ohos/lottie
```

### Code block 3

```
"dependencies": {
  "@ohos/lottie": "^2.0.0"
}
```

### Code block 4

```
ohpm install
```

### Code block 5

```
cd path/to/your/project/entry
ohpm install path/to/foo
```

### Code block 6

```
"dependencies": {
  "foo": "file:path/to/foo"  // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
}
```

### Code block 7

```
ohpm install
```

### Code block 8

```
cd path/to/your/project/entry
ohpm install path/to/package.har
```

### Code block 9

```
cd path/to/your/project/entry
ohpm install path/to/package.tgz
```

### Code block 10

```
"dependencies": {
  "package": "file:path/to/package.har" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径。
}
```

### Code block 11

```
"dependencies": {
  "package": "file:path/to/package.tgz" // 此处也可以是以当前oh-package.json5所在目录为起点的相对路径
}
```

### Code block 12

```
ohpm install
```

### Code block 13

```
 "hooks": {
    "preInstall": "echo 00 preInstall", // install命令执行之前
    "postInstall": "echo 00 postInstall", // install命令执行之后
    "preUninstall": "echo 00 preUninstall", // uninstall命令执行之前
    "postUninstall": "echo 00 postUninstall"  // uninstall命令执行之后
  }
```
