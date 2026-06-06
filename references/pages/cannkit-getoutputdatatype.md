# GetOutputDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputdatatype_

ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetOutputDataType(0);
  // ...
}
GetRequiredInputDataType
SetOutputDataType
