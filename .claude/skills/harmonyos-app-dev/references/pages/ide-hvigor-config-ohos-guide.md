# 能力说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-guide_

每个module下的oh-package.json5文件中的dependency、devDependency、dynamicDependency以及version。

目前可以通过hvigor对象提供的上下文直接获取和修改配置以实现动态配置构建配置、并使能到构建的过程与结果中。

在hvigorfile.ts或hvigorconfig.ts文件中，可以使用Hvigor提供的API接口来实现此能力。

相比于下面的overrides的能力来说，通过hook以及插件上下文来动态修改签名和编译配置更为灵活和易于理解，功能也更为全面，推荐采用此种方式。具体使用方式请参考通过hook以及插件上下文动态配置构建配置(推荐使用)。

在hvigorfile.ts中通过overrides关键字导出动态配置

在hvigorfile.ts中，我们约定在导出的对象中的config.ohos属性里接收编译的配置：

export default {  
    system: hapTasks,  
    config: {  
        ohos: {
            ...
        }    
    }
}

目前可以在工程级的hvigorfile.ts的config.ohos中配置的字段：

overrides：定义需要覆盖的字段，会在构建过程中覆盖原有的对应配置项。
signingConfig：签名配置，对应build-profile.json5里的signingConfigs配置项。
type
material
certpath
storePassword
keyAlias
keyPassword
profile
signAlg
storeFile
appOpt：对应app.json5里的配置项字段。
bundleName
bundleType
icon
label
vendor
versionCode
versionName

目前可以在模块级的hvigorfile.ts的config.ohos中配置的字段：

overrides：定义需要覆盖的字段，会在构建过程中覆盖原有的对应配置项。
buildOption：对应build-profile.json5里的buildOption配置项。
arkOptions
externalNativeOptions
napiLibFilterOption
nativeLib
resOptions
sourceOption

配置在overrides项中的参数，其优先级会高于在配置项中的对应字段。

动态修改编译配置
实践说明
