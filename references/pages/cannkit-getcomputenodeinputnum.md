# GetComputeNodeInputNum

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeinputnum_

auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeInputNum(); ++idx) {
  auto input_td = extend_context->GetInputDesc(idx);
  // ...
}
GetIrOutputInstanceInfo
GetComputeNodeOutputNum
