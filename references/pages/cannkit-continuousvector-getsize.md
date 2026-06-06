# GetSize

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-getsize_

auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto size = cv->GetSize(); // 0U
Init
SetSize
