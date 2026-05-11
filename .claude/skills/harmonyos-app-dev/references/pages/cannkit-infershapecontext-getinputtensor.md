# GetInputTensor

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getinputtensor_

如果输入没有被设置为数据依赖，调用此接口获取tensor时，只能在tensor中获取到正确的shape、format、datatype信息。无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

调用示例
ge::graphStatus InferShapeForReshape(InferShapeContext *context) {
  const gert::Shape *x_shape = context->GetInputShape(0);        // 获取第0个输入的shape
  const gert::Tensor *shape_tensor = context->GetInputTensor(1); // 获取第1个输入的tensor  数据依赖
  gert::Shape *output_shape = context->GetOutputShape(0);
  if (x_shape == nullptr || shape_tensor == nullptr || output_shape == nullptr) {
    // 防御式编程，不应该出现的场景，打印错误并返回失败
    return ge::GRAPH_FAILED;
  }
  // ...
}
GetInputShape
GetOptionalInputShape
