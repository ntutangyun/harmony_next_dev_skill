# GetOutputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputdesc_

const CompileTimeTensorDesc *GetOutputDesc(const size_t index) const
参数说明
参数	输入/输出	说明
index	输入	算子输出索引，从0开始计数。
返回值

输出TensorDesc的指针，当输入index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见CompileTimeTensorDesc。

约束说明

无

调用示例
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeInfo()->GetOutputsNum(); ++idx) {
  auto output_td = extend_context->GetOutputDesc(idx);
  // ...
}
GetInputDesc
GetOptionalInputDesc
