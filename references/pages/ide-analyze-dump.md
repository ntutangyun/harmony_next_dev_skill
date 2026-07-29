# 解析应用minidump文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump_

应用崩溃时支持生成minidump文件，具体请参考OH_HiAppEvent_SetEventConfig接口说明。从26.0.0版本开始，DevEco Studio支持对minidump文件进行解析，并展示异常堆栈，帮助开发者快速分析定位问题。

操作步骤

说明

应用运行崩溃时产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。若使用源码变更后重新构建生成的so目录，可能会因符号不一致导致解析结果不准确或解析失败。

点击Settings，可设置进制、偏移量和内存数量。
