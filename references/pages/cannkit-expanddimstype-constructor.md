# 构造函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expanddimstype-constructor_

为了简化，补维规则部分与字符串的顺序相反，例如字符串描述的补维规则为"1100"，那么对应的补维规则为"0011"，转换为数字为3。补维规则的概念和描述方法请参考简介。

表2 int64_t位域定义

字段	类型	含义
高8比特	uint8_t	补维规则长度。
低56比特	位域	使用0、1描述的补维规则。
返回值

返回一个ExpandDimsType对象，且该对象的补维规则（mask_）以及补维后的维度（size_）均根据入参expand_dims_type完成设置。

约束说明

无

调用示例
ExpandDimsType type("1001"); // 设置mask_为1001，size_为4
简介
operator==
