# MutableExpandDimsType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableexpanddimstype_

StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
ExpandDimsType new_dim_type("1010");
format.SetExpandDimsType(new_dim_type);
auto &fmt_dim_type = format.MutableExpandDimsType();
SetExpandDimsType
operator==
