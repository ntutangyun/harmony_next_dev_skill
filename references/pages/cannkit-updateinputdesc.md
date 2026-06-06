# UpdateInputDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updateinputdesc_

graphStatus UpdateInputDesc(const std::string &name, const TensorDesc &tensor_desc);
graphStatus UpdateInputDesc(const char_t *name, const TensorDesc &tensor_desc);
参数说明
参数名	输入/输出	描述
name	输入	算子Input名称。
tensor_desc	输入	TensorDesc对象。
返回值
类型	描述
graphStatus	更新TensorDesc成功，返回GRAPH_SUCCESS， 否则，返回GRAPH_FAILED。
异常处理
异常场景	说明
无对应name输入	函数提前结束，返回GRAPH_FAILED。
约束说明

无

TryGetInputDesc
UpdateOutputDesc
