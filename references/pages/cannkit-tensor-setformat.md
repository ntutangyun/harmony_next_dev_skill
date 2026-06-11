# SetFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setformat_

函数功能

设置Tensor的Format。

函数原型

graphStatus SetFormat(const ge::Format &format);

参数说明

参数名	输入/输出	描述
format	输入	需设置的Format值。 关于Format类型，请参见Format。

返回值

类型	描述
graphStatus	设置成功返回GRAPH_SUCCESS，否则，返回GRAPH_FAILED。

异常处理

无

约束说明

无

## Code blocks

### Code block 1

```
graphStatus SetFormat(const ge::Format &format);
```
