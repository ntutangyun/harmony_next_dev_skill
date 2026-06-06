# GetInputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputdesc_

const CompileTimeTensorDesc *GetInputDesc(const size_t index) const
参数说明
参数	输入/输出	说明
index	输入	算子输入索引，从0开始计数。
返回值

输入TensorDesc的指针，当输入index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见CompileTimeTensorDesc。

约束说明

无

调用示例
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeInputNum(); ++idx) {
  auto input_td = extend_context->GetInputDesc(idx);
  // ...
}
ExtendedKernelContext
GetOutputDesc
