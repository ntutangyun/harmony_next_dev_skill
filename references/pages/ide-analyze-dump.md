# 解析应用dump文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump_

应用崩溃时支持生成dump文件，具体请参考OH_HiAppEvent_SetEventConfig接口说明。从26.0.0版本开始，DevEco Studio支持dump文件进行解析，并展示异常堆栈，帮助开发者快速分析定位问题。

操作步骤

说明

应用运行崩溃时产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。因此，此处选择的so目录，必须是该应用在构建时存放so文件的原始目录。若替换为其他时间或通过其他构建生成的so目录，会因符号不一致导致无法解析。

点击Settings，可设置进制、偏移量和内存数量。
