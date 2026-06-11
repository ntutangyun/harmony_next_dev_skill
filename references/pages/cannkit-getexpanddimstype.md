# GetExpandDimsType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimstype_

函数功能

获取补维规则。

函数原型

ExpandDimsType GetExpandDimsType() const

参数说明

无

返回值

补维规则。

约束说明

无

调用示例

ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto fmt_dim_type = format.GetExpandDimsType();

## Code blocks

### Code block 1

```
ExpandDimsType GetExpandDimsType() const
```

### Code block 2

```
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto fmt_dim_type = format.GetExpandDimsType();
```
