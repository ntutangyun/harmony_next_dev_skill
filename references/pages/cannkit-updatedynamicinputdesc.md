# UpdateDynamicInputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updatedynamicinputdesc_

graphStatus UpdateDynamicInputDesc(const std::string &name, uint32_t index, const TensorDesc &tensor_desc);
graphStatus UpdateDynamicInputDesc(const char_t *name, uint32_t index, const TensorDesc &tensor_desc);
参数说明
参数名	输入/输出	描述
name	输入	算子动态Input的名称。
index	输入	算子动态Input编号，编号起始值从1开始。
tensor_desc	输入	TensorDesc对象。
返回值
类型	描述
graphStatus	更新动态Input成功，返回GRAPH_SUCCESS， 否则，返回GRAPH_FAILED。
异常处理

无

约束说明

无

UpdateOutputDesc
UpdateDynamicOutputDesc
