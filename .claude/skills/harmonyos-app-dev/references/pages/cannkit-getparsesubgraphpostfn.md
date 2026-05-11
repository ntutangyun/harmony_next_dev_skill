# GetParseSubgraphPostFn

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getparsesubgraphpostfn_

using ParseSubgraphFunc = std::function<Status(const std::string &subgraph_name, const ge::Graph &graph)>

Status GetParseSubgraphPostFn(ParseSubgraphFuncV2 &func) const

该函数会返回ParseSubgraphFuncV2类型的函数对象，ParseSubgraphFuncV2函数的声明如下。

using ParseSubgraphFuncV2 = std::function<Status(const ge::AscendString &subgraph_name, const ge::Graph &graph)>
参数说明

GetParseSubgraphPostFn()函数

无

GetParseSubgraphPostFn(ParseSubgraphFuncV2 &func)函数

参数	输入/输出	说明
func	输出	实现算子注册的子图中输入输出节点跟算子的输入输出对应关系的函数对象。
约束说明

无

GetFusionParseParamByOpFn
GetParseOpToGraphFn
