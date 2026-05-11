# InputsDataDependency

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inputsdatadependency_

OpImplRegisterV2 &InputsDataDependency(std::initializer_list<int32_t> inputs);
参数说明
参数	输入/输出	说明
inputs	输入	指定算子计算需要依赖的输入index列表。举例来说，inputs={0, 3}，说明该算子的计算需要依赖第0、3个输入的tensor值。
返回值

返回算子的OpImplRegisterV2 对象，该对象新增设置算子计算依赖第几个输入tensor的值。

约束说明

无

TilingParse
InferOutDataTypeSameWithFirstInput
