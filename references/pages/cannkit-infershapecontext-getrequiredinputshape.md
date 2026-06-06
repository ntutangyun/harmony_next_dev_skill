# GetRequiredInputShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getrequiredinputshape_

const Shape *GetRequiredInputShape(const size_t ir_index) const;
参数说明
参数	输入/输出	说明
ir_index	输入	必选输入在算子IR原型定义中的索引，从0开始计数。
返回值

返回指定输入的shape指针，若输入的ir_index非法，返回空指针。

关于Shape类型的定义，请参见Shape。

约束说明

无

调用示例
ge::graphStatus InferShapeForXXX(InferShapeContext *context) {
  auto in_shape = context->GetRequiredInputShape(2);
  // ...
}
GetRequiredInputTensor
GetOutputShape
