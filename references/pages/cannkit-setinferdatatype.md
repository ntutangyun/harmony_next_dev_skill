# SetInferDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinferdatatype_

OpDef &SetInferDataType(gert::OpImplRegisterV2::InferDataTypeKernelFunc func);
参数说明
参数	输入/输出	说明
func	输入	

DataType推导函数。InferDataTypeKernelFunc类型定义如下。

using InferDataTypeKernelFunc = UINT32 (*)(InferDataTypeContext *);

返回值

OpDef算子定义。

约束说明

无

SetInferShape
AICore
