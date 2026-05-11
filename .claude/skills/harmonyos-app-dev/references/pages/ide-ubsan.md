# 使用UBSan检测未定义行为

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ubsan_

代码中出现未定义行为，最初可能不会产生任何问题，但是随着代码的复杂度提高，未定义行为可能造成程序崩溃或发生错误，检测出根源会变得更加困难。UBSan（Undefined Behavior Sanitizer）可以检测代码中出现的未定义行为，帮助用户清除未定义行为引起的运行时错误。

常见的未定义行为有：

除数为零。
使用未对齐的指针，或未对齐的引用。
浮点数转换导致的溢出。
访问空指针。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

使用约束

ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

开启UBSan

可通过以下两种方式开启UBSan。

方式一

点击Run > Edit Configurations > Diagnostics，勾选Undefined Behavior Sanitizer开启检测。

方式二
在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：
"arguments": "-DOHOS_ENABLE_UBSAN=ON"

使用UBSan
运行或调试当前应用。
当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考UBSan异常检测类型。
说明

无论编译模式是debug或release，均有链接可直接跳转至源码。

使用TSan检测线程错误
方舟运行时检测
