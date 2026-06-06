# GetInputShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputshape_

const StorageShape *GetInputShape(const size_t index) const;
参数说明
参数	输入/输出	说明
index	输入	算子输入索引，从0开始计数。
返回值

指定的输入shape指针，输入shape中包含了原始shape与运行时shape信息。关于StorageShape类型的定义，请参见StorageShape。

当输入index非法时返回空指针。

约束说明

无

调用示例
ge::graphStatus TilingForMul(TilingContext *context) {
  auto input_shape_0 = *context->GetInputShape(0);
  auto input_shape_1 = *context->GetInputShape(1);
  auto output_shape = context->GetOutputShape(0);
  // ...
}
TilingContext
GetInputTensor
