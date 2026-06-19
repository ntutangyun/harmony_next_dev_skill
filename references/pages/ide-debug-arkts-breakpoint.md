# 使用断点

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-breakpoint_

DevEco Studio ArkTS支持行断点、日志断点等多种不同类型的断点，这些断点可以触发不同的操作。

行断点

行断点是最常见的类型，用于在指定的代码行暂停应用的执行，在暂停时，您可以检查变量，对表达式求值，然后逐行执行，以确定运行时错误的原因。

如需添加行断点，请按以下步骤操作：

找到您要暂停执行的代码行。

当您设置断点时，相应的代码行旁边会出现一个红点，如图。

在设置的断点红点处，单击鼠标右键，在Condition中可以设置条件断点，此类断点仅会在满足特定条件时才会暂停应用。

当应用运行到代码处，会在代码处停住，并高亮显示。

日志断点

在BreakPoints某个断点的配置中，勾选以下类型的Log，可以使进程运行到断点时在Console窗口打印相应日志。

勾选"Breakpoint hit"message，程序运行到断点时，打印“Breakpoint reached”。

勾选Stack trace，程序运行到断点时，打印当前线程的堆栈。

勾选Evaluate and log，并添加表达式，程序运行到断点时，打印表达式的值。

说明

未勾选Enable的断点不会打印日志，未勾选Suspend execution的断点会打印日志，不满足所设置的Condition的断点不会打印日志。

临时断点

在BreakPoints某个断点的配置中，勾选Remove once hit，该断点只生效一次，生效后该断点会被删除。

函数断点

从DevEco Studio 6.0.0 Beta2版本开始，支持在ArkTS代码中设置函数断点。

函数断点也叫方法断点或符号断点，使用函数名设置断点，当程序运行到对应函数时，中断进程。

在BreakPoints中，点击+ > ArkTS Symbolic Breakpoints，在弹出窗口中填写函数名，添加函数断点。

说明

DevEco Studio 6.0.1 Release及以下版本，调试过程中如果命中在C++断点，则无法添加和移除ArkTS函数断点，6.0.2 Beta1及以上版本，支持添加和移除。

异常断点

异常断点会在应用执行时发生异常的地方暂停应用。

在BreakPoints中，勾选ArkTS/JS Exception Breakpoints，开启异常断点。

当调试应用程序中出现异常时，会在异常处高亮，并且代码左侧有标志，并展示当前Frames和Variable，以及错误信息。

断点管理

在设置的程序断点红点处，单击鼠标右键。然后单击More或按快捷键Ctrl+Shift+F8（macOS为Shift+Command+F8），可以管理断点。

或者在“Debug”窗口中点击View Breakpoints 图标。
