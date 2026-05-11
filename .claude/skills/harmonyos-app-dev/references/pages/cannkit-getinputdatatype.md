# GetInputDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputdatatype_

ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetInputDataType(0);
  // ...
}
InferDataTypeContext
GetOptionalInputDataType
