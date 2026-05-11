# GetOutputShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getoutputshape_

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
GetRequiredInputShape
InferShapeRangeContext
