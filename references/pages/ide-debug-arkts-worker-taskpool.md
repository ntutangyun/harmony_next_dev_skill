# 调试场景说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-worker-taskpool_

DevEco Studio支持对ArkTS代码进行调试，包括以下场景。

在Worker/TaskPool代码中添加断点进行调试。

对Extension Ability生命周期函数进行调试，具体请参考extension调试。

部分设备上，UIAbility支持以独立进程的方式运行并调试，具体请参考多进程调试。

在Native代码中，通过创建ArkTS运行时的方式调用ArkTS方法，在ArkTS代码中添加断点即可进行调试。（设备系统版本需要升级到6.0.0.35及以上）
