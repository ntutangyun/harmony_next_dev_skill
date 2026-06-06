# GetCapacity

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-getcapacity_

auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto cap = cv->GetCapacity(); // 100U
SetSize
GetData
