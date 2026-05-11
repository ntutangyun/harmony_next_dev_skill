# Init

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-init_

size_t total_size = capacity * sizeof(int64_t) + sizeof(ContinuousVector);
auto holder = std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[total_size]);
reinterpret_cast<ContinuousVector *>(holder.get())->Init(capacity); // 100U
Create
GetSize
