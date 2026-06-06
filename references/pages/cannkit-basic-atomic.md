# 原子操作

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-atomic_

SetAtomicAdd、SetAtomicType、SetAtomicNone、SetAtomicMax、SetAtomicMin、SetStoreAtomicConfig、GetStoreAtomicConfig	

不支持。

KirinX90/Kirin9030处理器不支持开发者在GM完成Atomic操作。开发者需要在NPU片上的Buffer完成计算后，再使用基础API DataCopy将计算结果从NPU片上的Buffer搬到GM。

数据类型
同步控制
