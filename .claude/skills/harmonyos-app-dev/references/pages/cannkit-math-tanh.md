# Tanh

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-math-tanh_

__aicore__ inline void Tanh(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const uint32_t calCount)
参数说明

表1 模板参数说明

参数名	描述
T	操作数的数据类型。支持的数据类型为：half/float。
isReuseSource	是否允许修改源操作数。该参数预留，传入默认值false即可。

表2 接口参数说明

参数名	输入/输出	描述
dstTensor	输出	

目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。


srcTensor	输入	

源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。


calCount	输入	实际计算数据元素个数。
返回值

无

支持的型号

Kirin9020系列处理器

KirinX90系列处理器

约束说明

操作数地址偏移对齐要求请参见通用约束。

输入输出操作数参与计算的数据长度要求32B对齐。

调用示例
AscendC::TPipe pipe;
// calCount为实际计算数据元素个数
// 其它处理省略
AscendC::Tanh<T, false>(yLocal, xLocal, calCount);
数学库
激活函数
