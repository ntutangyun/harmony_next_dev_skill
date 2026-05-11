# 调试概述

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-device_

DevEco Studio提供了丰富的HarmonyOS应用/元服务调试能力，支持JS、ArkTS、C/C++单语言调试和ArkTS/JS+C/C++跨语言调试能力，并且支持三方库源码调试，帮助开发者更方便、高效地调试应用/元服务。

HarmonyOS应用/元服务调试支持使用真机设备、模拟器、预览器调试。接下来以使用真机设备为例进行说明，详细的调试流程如下图所示。关于模拟器和预览器的调试请参考使用模拟器运行应用和使用预览器调试应用。

配置签名信息：使用真机设备进行调试前需要对HAP进行签名。
设置调试代码类型：调试类型默认为Detect Automatically。
设置HAP安装方式：选择先卸载应用/元服务后再重新安装或覆盖安装。
启动调试：启动debug调试或attach调试。
应用调试
自定义运行/调试配置
