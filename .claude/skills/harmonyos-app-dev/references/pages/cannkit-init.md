# Init

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-init_

auto td_buf = std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[total_size]());
auto td = reinterpret_cast<TilingData *>(td_buf.get());
td->Init(cap_size, td_buf.get() + sizeof(TilingData)); // 内存平铺
CalcTotalSize
operator
