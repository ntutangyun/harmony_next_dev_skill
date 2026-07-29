# 调试Native子进程

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-child-process_

从26.0.0 Beta2版本开始，DevEco Studio支持对Native子进程进行调试，包括OH_Ability_StartNativeChildProcess和OH_Ability_CreateNativeChildProcess接口创建的Native子进程。

使用约束

支持API 26.0.0及以上版本的2in1设备。

通过OH_Ability_StartNativeChildProcess接口创建Native子进程时，不支持调试隔离模式（NCP_ISOLATION_MODE_ISOLATED = 1）的Native子进程。

通过OH_Ability_CreateNativeChildProcess接口创建Native子进程时，不支持调试独立uid的Native子进程。

调试方式

通过attach方式对Native子进程进行调试，在attach窗口中直接选择子进程进行调试。

或者先attach调试主进程，再点击调试面板的，打开attach窗口选择子进程进行调试。
