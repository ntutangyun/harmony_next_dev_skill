# SetSize

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-setsize_

auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto ret = cv->SetSize(10U); // ge::GRAPH_SUCCESS
ret = cv->GetSize(101U); // ge::GRAPH_FAILED
GetSize
GetCapacity
