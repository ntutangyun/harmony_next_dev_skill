# 构造函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-constructor_

StorageFormat(const ge::Format origin_format, const ge::Format storage_format, const ExpandDimsType &expand_dims_type)
参数说明
参数	输入/输出	说明
origin_format	输入	原始格式。
storage_format	输入	运行时格式。
expand_dims_type	输入	补维规则。
返回值

返回一个指定了origin_format、storage_format和expand_dims_type的StorageFormat对象 。

约束说明

无

调用示例
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
StorageFormat
GetOriginFormat
