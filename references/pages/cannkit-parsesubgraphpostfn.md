# ParseSubgraphPostFn

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parsesubgraphpostfn_

OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFunc &subgraph_post_fn)
OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFuncV2 &subgraph_post_fn);
参数说明
参数	输入/输出	说明
subgraph_post_fn	输入	

子图中输入输出节点跟算子的输入输出的对应关系函数对象。

详见回调函数ParseSubgraphFuncV2 。

约束说明

无

回调函数ParseSubgraphFuncV2

开发者自定义并实现ParseSubgraphFuncV2函数，完成解析子图中输入输出节点跟算子的输入输出的对应关系功能，回调函数原型定义如下。

Status ParseSubgraphFuncV2(const ge::AscendString &subgraph_name, const ge::Graph &graph)

表1 参数说明

参数	输入/输出	说明
subgraph_name	输入	子图名字。
graph	输出	构造的子图。
FusionParseParamsFn（Overload）
ParseOpToGraphFn
