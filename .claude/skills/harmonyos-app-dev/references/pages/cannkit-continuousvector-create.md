# Create

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-create_

template<typename T>  static std::unique_ptr<uint8_t[]> Create(size_t capacity, size_t &total_size)
template<typename T>  static std::unique_ptr<uint8_t[]> Create(const size_t capacity)
参数说明
参数	输入/输出	说明
T	输入	实例中包含的元素类型。
capacity	输入	实例的最大容量。
total_size	输出	本实例的总长度。
返回值

指向本实例的指针。

约束说明

无

调用示例
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity); // 创建了一个可以存放100个int64_t数据的内存。
简介
Init
