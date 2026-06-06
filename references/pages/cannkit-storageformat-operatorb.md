# operator!=

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatorb_

StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
bool is_diff_fmt = format != another_format; // true
operator==
StorageShape
