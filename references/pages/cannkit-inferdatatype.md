# InferDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferdatatype_

using InferDataTypeKernelFunc = UINT32 (*)(InferDataTypeContext *);
函数原型
OpImplRegisterV2 &InferDataType(InferDataTypeKernelFunc infer_datatype_func);
参数说明
参数	输入/输出	说明
infer_datatype_func	输入	要注册的自定义InferDataType函数，类型为InferDataTypeKernelFunc。
返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了InferDataType函数infer_datatype_func。

约束说明

无

InferShapeRange
Tiling
