# SetInstanceStart

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstancestart_

const auto &ir_inputs = node->GetOpDesc()->GetIrInputs();  // 算子IR定义的所有输入
for (size_t i = 0; i < ir_inputs.size(); ++i) {
  auto ins_info = compute_node_info.MutableInputInstanceInfo(i);  // 获取第i个IR输入对应的AnchorInstanceInfo对象
  GE_ASSERT_NOTNULL(ins_info);
  size_t input_index = ir_index_to_instance_index_pair_map[i].first; // 获取统计后的算子IR输入对应的实际输入index
  ins_info->SetInstanceStart(input_index); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
}
GetInstanceStart
SetInstantiationNum
