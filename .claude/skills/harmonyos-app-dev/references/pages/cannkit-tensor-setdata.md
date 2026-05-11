# SetData

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdata_

graphStatus SetData(const std::vector<AscendString> &datas);
graphStatus SetData(uint8_t *data, size_t size, const Tensor::DeleteFunc &deleter_func);
参数说明
参数名	输入/输出	描述
data/datas	输入	需设置的数据。
size	输入	数据的长度，单位为字节。
deleter_func	输入	

用于释放data数据。

using DeleteFunc = std::function<void(uint8_t *)>;

返回值
类型	描述
graphStatus	设置成功返回GRAPH_SUCCESS，否则，返回GRAPH_FAILED。
异常处理

无

约束说明

无

GetTensorDesc
SetDataType
