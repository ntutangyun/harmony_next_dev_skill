# GetComputeNodeOutputNum

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeoutputnum_

auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeOutputNum(); ++idx) {
  auto input_td = extend_context->GetOutputDesc(idx);
  // ...
}
GetComputeNodeInputNum
GetAttrs
