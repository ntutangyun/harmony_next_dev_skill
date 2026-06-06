# GetOptionalInputDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoptionalinputdatatype_

ge::DataType GetOptionalInputDataType(const size_t ir_index) const;
参数说明
参数	输入/输出	说明
ir_index	输入	可选输入在算子IR原型定义中的索引，从0开始计数。
返回值

返回指定输入的数据类型，若输入的ir_index非法或该输入没有实例化，返回DT_UNDEFINED。

约束说明

无

调用示例
ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetOptionalInputDataType(1);
  // ...
}
GetInputDataType
GetRequiredInputDataType
