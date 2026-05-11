# 构造函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-range-constructor_

Range(T *min, T* max) : min_(min), max_(max) // 开发者指定上界max，下界min
Range(T *same_ele) : min_(same_ele), max_(same_ele) // 上下界均为same_ele
参数说明
参数	输入/输出	说明
min	输入	下界的指针，类型为T*。
max	输入	上界的指针，类型为T*。
same_ele	输入	构造相同上下界range实例时使用，上下界均使用same_ele赋值，类型为T*。
返回值

返回开发者指定构造的range对象。

约束说明

无

调用示例
// 1. 默认构造
Range<int> range1; // 上下界均为nullptr
// 2. 开发者指定上下界
int min = 0;
int max = 1024;
Range<int> range2(&min, &max); // 上界为1024Bytes，下界为0
// 3. 构造上下界相同的range
Range<int> range3(&min); // 上下界均为0
简介
operator==
