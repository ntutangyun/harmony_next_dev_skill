# 编译构建常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-faqs_

构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”
构建报错“input module releaseType is different”
构建报错“debug is different”
构建报错“proxy data is duplicated”
编译报错“Init keystore failed: parseAlgParameters failed: ObjectIdentifier()”
编译报错“generate SignerBlock failed”
编译报错“java.io.IOException: DerValue.getOID, not an OID 49”
编译报错“JS heap out of memory”
Linux环境下编译报错“JS heap out of memory”
编译报错“Cannot find module XXX or its corresponding type declarations”
编译报错“Module 'xxx' has no exported member 'yyy'”
编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
编译报错“Failed to get a resolved OhmUrl by filepath xx”
编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
C++工程编译导致电脑卡顿的处理建议
CPP编译报错"A 'undefined symbol' error has occurred"
CPP编译报错"A 'unknown type name' error has occurred"
JDK版本不匹配导致编译失败
LABEL_VALUE_ERROR处理指导
应用/元服务的启动界面信息缺失，提示"Schema validate failed"报错
编译报错“Schema validate failed”
编译报错“No available entry module found”
编译报错“keystore password was incorrect”
编译报错“please check deviceType or distroFilter of the module”
编译报错“Failed to generate test project build system”
C/C++项目三方依赖库未打包入HAP
Static Library模块中src/main/cpp目录下的文件未打包进HAR
工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
编译报错“ninja: error: mkdir(xxx): No such file or directory”
编译报错“(is the command line too long?)”
编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”
编译报错 “Unknown resource name”
构建报错“Task xxx was not found in the project xxx”
编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
编译报错“Only one default card can be configured in the form_config.json file”
编译报错“In the form_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty”
编译报错“The path XX is not writable. please choose a new location”
编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”
编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”
如何配置oh-package.json5动态依赖
如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题
如何解决编译报错“Could not resolve 'xxx' from”，但'xxx'目录存在的问题
用户目录下没有npmrc文件
如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题
如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题
如何解决编译报错“Error: the name 'XXX' can only contain [a-zA-Z0-9_].”的问题
如何解决三方包require语句报错
如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
如何解决编译报错“Declaration merging is not supported(arkts-no-decl-merging)” 或 “Cannot redeclare block-scoped variable 'xxx'”的问题
如何解决编译报错“ The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary.”的问题
如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题
如何解决编译报错“Cannot add xxxx items to index”的问题
编译初始化报错“resource busy or locked, open 'xxx\outputs\build-logs\build.log'”
Mac环境下加载动态库，签名拦截导致未生效
展开章节
如何解决编译过程内存过高

问题现象

编译构建时，内存或CPU占用过高，导致出现DevEco Studio运行卡顿、延迟等现象。

解决措施

在执行hvigor构建的过程中，通过减少内存中的缓存数据、减少线程数量，可以减少编译过程中的内存占用。

可以在hvigor-config.json5中添加配置。

"properties": {
  // 配置为0，表示不启用内存缓存配置，默认为4，数值越低，内存中缓存数据越少
  "hvigor.pool.cache.capacity": 0,
  // 默认配置为cpu核数-1， 包含ohos.arkCompile.maxSize，值越小，占用内存越少
  "hvigor.pool.maxSize" : 5,
  // 默认配置值为5, 值越小，占用内存越少
  "ohos.arkCompile.maxSize": 3,
  // 默认配置值为true, 表示开启内存缓存，占用内存较多，配置为false，关闭内存缓存，占用内存较少
  "hvigor.enableMemoryCache": false
},
说明

当配置项"hvigor.pool.maxSize"和"ohos.arkCompile.maxSize"的值改小，"hvigor.enableMemoryCache"改为false后，可能会导致编译时长增加，请耐心等待。

如果以上修改没有取得明显的效果，可以使用非并行的模式来执行编译。
在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor”，取消勾选“Execute tasks in parallel mode (may require larger heap size)”。

流水线场景中，在命令行最后增加 --no-parallel，示例：
hvigorw assembleHap --no-parallel

说明

使用非并行模式编译，内存占用会减少，但可能会导致编译时长增加，请耐心等待。

使用日志记录
编译构建错误码
