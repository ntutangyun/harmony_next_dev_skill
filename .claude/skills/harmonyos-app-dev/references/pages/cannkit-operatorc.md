# operator[]

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorc_

const int64_t &operator[](size_t idx) const：dim值，在idx>=kMaxDimNum时，行为未定义。

int64_t &operator[](size_t idx)：dim值，在idx>=kMaxDimNum时，行为未定义。

约束说明

调用者需要保证index合法，即idx<kMaxDimNum。

调用示例
Shape shape0({3, 256, 256});
auto dim0 = shape0[0]; // 3
auto dim5 = shape0[5]; // 5
auto invalid_dim = shape0[kMaxDimNum]; // 行为未定义
operator!=
IsScalar
