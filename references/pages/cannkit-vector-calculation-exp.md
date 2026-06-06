# Exp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-vector-calculation-exp_

__aicore__ inline void Exp(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const int32_t& calCount)
参数说明

表1 模板参数说明

参数名	描述
T	操作数数据类型。

表2 参数说明

参数名	输入/输出	描述
dstLocal	输出	

目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

Kirin9020系列处理器，支持的数据类型为：half/float。

KirinX90系列处理器，支持的数据类型为：half/float。


srcLocal	输入	

源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

源操作数的数据类型需要与目的操作数保持一致。

Kirin9020系列处理器，支持的数据类型为：half/float。

KirinX90系列处理器，支持的数据类型为：half/float。


calCount	输入	输入数据元素个数。
返回值

无

支持的型号

Kirin9020系列处理器

KirinX90系列处理器

约束说明

操作数地址偏移对齐要求请参见通用约束。

调用示例

本样例中只展示Compute流程中的部分代码。本样例的srcLocal和dstLocal均为half类型，占16位bit。

如果开发者需要运行样例代码，请将该代码段拷贝并替换样例模板中Compute函数的部分代码即可。

tensor前n个数据计算接口样例：

AscendC::Exp(dstLocal, srcLocal, 512);

结果示例如下。

输入数据(srcLocal): [0.0 1.0 2.0 3.0 ...]
输出数据(dstLocal):
[1.0 2.719 7.391 20.08 ...]
单目指令
Ln
