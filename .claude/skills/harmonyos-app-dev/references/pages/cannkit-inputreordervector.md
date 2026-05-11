# InputReorderVector

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inputreordervector_

OpRegistrationData &InputReorderVector(const std::vector<int32_t> &input_order)
参数说明
参数	输入/输出	说明
input_order	输入	算子输入的调整列表， 下标表示原输入索引，下标对应的值表示调整后新的输入索引。例如：第三方框架的算子A对应的AI处理器算子为AD，原输入0为in0， 原输入1为in1，原输入2为in2，插件调用接口传入input_order = {1, 0, 2}，那么解析后算子AD的输入0为in1， 输入1为in0，输入2为in2。
返回值

OpRegistrationData类的引用。

异常处理

无

约束说明

无

AutoMappingSubgraphIndex
Promote
