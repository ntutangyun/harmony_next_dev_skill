# GetInputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-getinputdesc_

当无此算子Input名称时，则返回TensorDesc默认构造的对象，其中，主要设置DataType为DT_FLOAT（表示float类型），Format为FORMAT_NCHW（表示NCHW）。


index	输入	

算子Input索引。

当无此算子Input索引时，则返回TensorDesc默认构造的对象，其中，主要设置DataType为DT_FLOAT（表示float类型），Format为FORMAT_NCHW（表示NCHW）。

返回值
类型	描述
TensorDesc	算子Input的TensorDesc。
异常处理

无

约束说明

无

GetInputsSize
GetName
