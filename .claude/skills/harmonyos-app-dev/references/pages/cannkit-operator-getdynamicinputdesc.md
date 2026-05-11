# GetDynamicInputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-getdynamicinputdesc_

TensorDesc GetDynamicInputDesc(const std::string &name, uint32_t index) const;
TensorDesc GetDynamicInputDesc(const char_t *name, uint32_t index) const;
参数说明
参数名	输入/输出	描述
name	输入	算子动态Input的名称。
index	输入	算子动态Input编号，编号从0开始。
返回值
类型	描述
TensorDesc	获取TensorDesc成功，则返回算子动态Input的TensorDesc；获取失败，则返回TensorDesc默认构造的对象，其中，主要设置DataType为DT_FLOAT（表示float类型），Format为FORMAT_NCHW（表示NCHW）。
异常处理

无

约束说明

无

GetDynamicInputNum
GetDynamicOutputNum
