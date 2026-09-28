# 解析应用minidump/coredump文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump_

从26.0.0版本开始，DevEco Studio支持对应用minidump/coredump文件进行解析，展示堆栈信息，帮助开发者快速定位问题。

获取dump文件

minidump文件：获取方式请参考OH_HiAppEvent_SetEventConfig接口说明。

应用需要在module.json5中配置ohos.permission.ALLOW_COREDUMP权限，配置方式请参考声明权限。

解析dump文件

说明

应用产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。若使用源码变更后重新构建生成的so目录，可能会因符号不一致导致解析结果不准确或解析失败。

点击Settings，可设置进制、偏移量和展示的内存字节数量。
