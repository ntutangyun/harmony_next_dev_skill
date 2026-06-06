# MutableAttrs

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableattrs_

所有IR原型定义过的属性值以及通过IMPL_OP宏注册的属性值，属性值按照IR原型定义的顺序依次保存。返回对象为非const。

约束说明

无

调用示例
auto ret = bg::CreateComputeNodeInfo(node, buffer_pool);
ASSERT_NE(ret, nullptr);
auto compute_node_info = reinterpret_cast<ComputeNodeInfo *>(ret.get());
auto attrs = compute_node_info->MutableAttrs();
MutableOutputTdInfo
SetNodeType
