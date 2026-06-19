# FAST Kit术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-glossary_

C

[h2]Concurrent HashMap；并发哈希表

一种专为高并发场景设计的键值对数据结构，支持多线程环境下的安全存储、快速访问与高效更新，适用于对并发吞吐量和数据一致性要求较高的增删改查场景。

D

[h2]Direct Form II Transposed Structure；直接II型转置结构

二阶IIR滤波器的一种实现结构，具有延迟单元最少、数值稳定性好的特点。FAST Kit中的IIR滤波器支持多通道和多节级联配置。

O

[h2]Opaque Configuration；不透明配置

一种ABI稳定的配置抽象机制，库以不完整类型前向声明配置对象，外部代码仅通过指针句柄进行传递与操作，实现细节完全由库内部定义，保证后续版本可在不破坏二进制兼容性的前提下变更存储格式与语义。

R

[h2]Rectangular Partition Problem；矩形划分问题

给定N个彼此不相交的矩形，求M个彼此不相交且并集与输入完全相同的矩形，并使M尽可能少的优化问题。

S

[h2]Segment Map；线段表

一种用于高效处理数据序列区间段信息的数据结构，支持单点修改、区间修改、区间查询等操作，能将区间操作的时间复杂度从O(N)优化至O(logN)。典型实现为线段树（Segment Tree）。

[h2]Split Complex Format；分离复数格式

一种复数数组存储格式，将实部和虚部分别存储在独立的数组中，而非交错存储（real0, imag0, real1, imag1, ...）。FAST Kit提供交错格式与分离格式之间的相互转换接口。

[h2]Sweep Line Algorithm；扫描线算法

一种二维线性扫描算法，可用于高效解决矩形划分问题，通过扫描线沿坐标轴方向扫描，动态维护当前活跃的矩形集合，从而快速合并相邻矩形，输出数量尽可能少的不相交矩形集合。
