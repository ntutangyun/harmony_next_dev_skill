# GetInputConstData

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputconstdata_

graphStatus GetInputConstData(const std::string &dst_name, Tensor &data) const;
graphStatus GetInputConstData(const char_t *dst_name, Tensor &data) const;
参数说明
参数名	输入/输出	描述
dst_name	输入	输入名称。
data	输出	返回Const节点的数据Tensor。
返回值
类型	描述
graphStatus	如果指定算子Input对应的节点为Const节点且获取数据成功，返回GRAPH_SUCCESS，否则，返回GRAPH_FAILED。
异常处理

无

约束说明

无

GetInferenceContext
GetInputsSize
