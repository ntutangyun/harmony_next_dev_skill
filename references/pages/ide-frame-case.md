# 案例：使用Frame模板分析应用卡顿问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-frame-case_

本案例介绍如何判断应用存在卡顿帧，再通过调用栈和trace信息分析应用运行逻辑，找出应用卡顿的原因。

应用卡顿分析基础功能请参考Frame分析。

分析步骤

分析应用卡顿类问题步骤如下：

确认是否存在卡顿帧。

若存在卡顿帧，根据调用栈和trace等信息进一步确定问题点。

分析Frame数据

[h2]分析应用是否存在卡顿

说明

在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

AppDeadlineMissed：App侧的卡顿。

Expected Duration：一帧绘制的期望耗时。与fps的大小有关，如fps为120，对应的Vsync周期为8.3ms，即App侧/Render Service侧的帧耗时，一般需要在8.3ms以内。

Actual Duration：一帧绘制的实际耗时。

如下图，可以看到该帧的期望耗时为8ms 330μs，实际耗时为44ms54μs，远远超过了期望耗时，因此被识别为卡顿帧。

框选该异常帧时间范围，结合ArkTS Callstack泳道、Callstack泳道和Trace等信息进一步分析异常点。

[h2]案例：分析应用卡顿原因

找到并框选要分析的异常帧，查看ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看主线程调用栈，即线程号与进程号一致的ArkVM子泳道。可以看到ArkTS侧一些方法的耗时。

(program)代表程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或者Native调用ArkTS情况，一般很难通过这里分析出有效的信息，需要切换到Callstack泳道看具体的调用栈信息。

说明

也可通过底部的“Call Trees”选择框来隐藏系统调用栈，减少干扰信息。

说明

一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。不建议图片加载较长时间时使用同步加载。
