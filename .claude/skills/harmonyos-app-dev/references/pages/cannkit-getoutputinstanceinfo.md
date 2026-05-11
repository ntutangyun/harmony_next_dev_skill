# GetOutputInstanceInfo

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputinstanceinfo_

const AnchorInstanceInfo *GetOutputInstanceInfo(const size_t ir_index) const
参数说明
参数	输入/输出	说明
ir_index	输入	算子IR原型定义中的输出索引，从0开始计数。
返回值

返回const类型的实例化对象的地址。

约束说明

无

调用示例
for (size_t i = 0; i < ir_outputs.size(); ++i) {
  auto ins_info = compute_node_info.GetOutputInstanceInfo(i);
  // ...
}
GetInputInstanceInfo
GetInputTdInfo
