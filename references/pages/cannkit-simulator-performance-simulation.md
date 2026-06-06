# Simulator性能仿真功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-simulator-performance-simulation_

------------------------------------------------------------------------------------
   Loop           ExpectOut        RealOut         FpDiff         RateDiff
 ---------------------------------------------------------------------------------------
 00000001         0.0395813       0.0395813       0.0000000       0.0000000
 00000002         0.0160980       0.0160980       0.0000000       0.0000000
 00000003         -0.0443420      -0.0443420      0.0000000       0.0000000
 00000004         -0.0847778      -0.0847778      0.0000000       0.0000000
 00000005         -0.0066605      -0.0066605      0.0000000       0.0000000
 00000006         0.0880737       0.0880737       0.0000000       0.0000000
 00000007         0.0848389       0.0848389       0.0000000       0.0000000
 00000008         0.1083374       0.1083374       0.0000000       0.0000000
 00000009         0.0838623       0.0838623       0.0000000       0.0000000
 00000010         0.0887451       0.0887451       0.0000000       0.0000000
 00000011         0.0572205       0.0572205       0.0000000       0.0000000
 00000012         0.0741577       0.0741577       0.0000000       0.0000000
 00000013         -0.0762329      -0.0762329      0.0000000       0.0000000
 00000014         -0.0957642      -0.0957642      0.0000000       0.0000000
 00000015         0.0102234       0.0102234       0.0000000       0.0000000
   ...               ...             ...             ...             ...
 ---------------------------------------------------------------------------------------
 DiffThd           PctThd          PctRlt          Result
 ---------------------------------------------------------------------------------------
 0.0050            99.50%          100.000000%     Pass
 Success Success Success Success Success

表1 精度比对结果说明

信息项	说明
data_cmp mean	运行输出数据的均值信息。
data_gd mean	标杆数据的均值信息。
split_count	统计输出数据的个数。
max_diff_hd	输出数据和golden数据的最大误差值阈值。
详细对比数据展示（部分）	Loop（数据位置）、ExpectOut（期望输出值）、RealOut（实际输出值）、FpDiff （绝对误差值）、RateDiff（相对误差值）。
整体对比结果展示	DiffThd（相对误差值阈值）、PctThd （精度达标数据占比阈值）、PctRlt（实际精度达标数据占比）、Result（对比结果）。
Error Line展示项	若精度比对结果为Failed，会追加展示部分误差较大的数据的详细信息。

（可选）查看dump结果

若开启DumpTensor功能或DumpAccChkPoint功能，结果文件存放在dump目录下，详细结果介绍参见产物说明。

Model仿真打点
功能介绍

算子进行CAModel仿真时，可对算子任意运行阶段进行打点，从而分析不同指令的流水图，以便进一步性能调优。

说明

Kirin9020/KirinX90暂不支持使用该方法进行调优。

使用方法

先在Kernel代码中的目标指令位置分别打上TRACE_START/TRACE_STOP，示例如下，起始/终止接口的说明详见Trace接口说明。

TRACE_START(0x1);
DataCopy(zGm, zLocal, this->totalLength);
TRACE_STOP(0x1);

参考使用方法（命令行）中的命令行方式，执行算子仿真流程。

在CAModel仿真结果trace图上查看打点结果。

如下图所示，其中USER_DEFINE_1_DELAY表示DataCopy指令下发到指令开始执行的时间，USER_DEFINE_1表示指令执行的时间。

图1 仿真打点示意图

Trace接口说明

TRACE_START接口说明如下。

函数原型： #define TRACE_START(apid)

函数功能： 起始位置打点。

参数(IN)： apid，当前预留了十个开发者自定义的类型：

0x0：USER_DEFINE_0
0x1：USER_DEFINE_1
0x2：USER_DEFINE_2
0x3：USER_DEFINE_3
0x4：USER_DEFINE_4
0x5：USER_DEFINE_5
0x6：USER_DEFINE_6
0x7：USER_DEFINE_7
0x8：USER_DEFINE_8
0x9：USER_DEFINE_9

参数(OUT)： NA

返回值： NA

使用约束：

TRACE_START/TRACE_STOP需配套使用，若Trace图上未显示打点，则说明两者没有配对。
不支持跨核使用，例如TRACE_START在AI Cube打点，则TRACE_STOP打点也需要在AI Cube上，不能在AI Vector上。

调用示例：

TRACE_START(0x2);
Add(zLocal, xLocal, yLocal, dataSize);
TRACE_STOP(0x2);

TRACE_STOP接口说明如下。

函数原型： #define TRACE_STOP(apid)

函数功能： 终止位置打点

参数(IN)： apid，取值需与TRACE_START接口参数取值保持一致，否则影响打点结果。

参数(OUT)： None

返回值： NA

使用约束：

TRACE_START/TRACE_STOP需配套使用，若Trace图上未显示打点，则说明两者没有配对。
不支持跨核使用，例如TRACE_START在AI Cube打点，则TRACE_STOP打点也需要在AI Cube上，不能在AI Vector上。

调用示例：

TRACE_START(0x2);
Add(zLocal, xLocal, yLocal, dataSize);
TRACE_STOP(0x2);
CPU孪生调试功能
更多功能
