# 三方库源码调试

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-source-code-debugging_

三方共享包分为静态共享包HAR和动态共享包HSP，两种共享包的源码调试方式有所区别，具体请查看以下指导。

区分字节码HAR和源码HAR

HAR包分为字节码HAR和源码HAR，同时满足以下两个条件的是字节码HAR，否则是源码HAR，更多关于如何构建源码HAR和字节码HAR的指导请查看构建HAR。

查看HAR包的ets目录下存在.abc文件。

字节码HAR调试

[h2]C++代码调试

如果HAP/HSP引用字节码HAR包，同时HAR包中包含C++代码，参考以下步骤对该HAR包进行调试。

说明

在工程级或模块级build-profile.json5中添加strip字段并设置为false，可以生成带调试信息的so文件，具体请参考配置CPP。

settings set -- target.source-map {old-path} {new-path}

old-path：编译时的文件路径。

new-path：本地的源码文件路径。

[h2]ArkTS代码调试

假如在工程A（HAR包工程）中以debug模式编译得到字节码HAR包，工程B（主工程）中引用该字节码HAR包，并且本地有HAR包的源码，要调试该字节码HAR，有两种方式：在主工程中调试或在HAR包工程中调试。

说明

release模式编译的字节码HAR不支持调试。

导入成功后，由于debug模式编译的字节码HAR中包含sourceMap，调试时默认会关联当前工程的源码，此时可以在HAR模块上直接添加断点。

在HAR包工程新建一个entry类型的demo主模块，如果主模块已存在则跳过本步骤。

// demo主模块的oh-package.json5
"dependencies": {
  "@ohos/test_stage_ets_library": "file:./lib/test_stage_ets_library.har",
}

说明

如果在demo主模块的oh-package.json5中，配置对字节码HAR模块的依赖，如file:../test_stage_ets_library，调试时可能导致断点无效。

在HAR包工程主模块中调用HAR模块的接口，确保编译后主模块的sourceMap文件中包含HAR模块的相关信息。

remoteUrl：应用程序加载HAR包的前缀路径。

localUrl：本地生成sourceMap中HAR的前缀路径。

说明

如果在HAR包工程中同时配置Symbol Directories和Ets Source Pairs，可同时attach调试ArkTS和C++断点。

源码HAR调试

[h2]C++代码调试

如果HAP/HSP引用源码HAR包，同时HAR包中包含C++代码，可参考字节码HAR进行调试。

[h2]ArkTS代码调试

工程中引用源码HAR包，对该HAR包进行调试，根据本地是否有源码，调试方式分别如下：

方式一：参考字节码HAR调试。

HSP源码调试

如果要调试HSP源码，需要将源码置于本地工程模块下，参考字节码HAR的方式一进行调试。

## Code blocks

### Code block 1

```
settings set -- target.source-map {old-path} {new-path}
```

### Code block 2

```
// demo主模块的oh-package.json5
"dependencies": {
  "@ohos/test_stage_ets_library": "file:./lib/test_stage_ets_library.har",
}
```
