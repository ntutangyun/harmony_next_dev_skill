# GetOutputsNum

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputsnum_

函数功能

获取算子在网络中的实际输出个数。

函数原型

size_t GetOutputsNum() const

参数说明

无

返回值

算子的实际输出个数。

约束说明

无

调用示例

size_t index = compute_node_info->GetOutputsNum();

## Code blocks

### Code block 1

```
size_t GetOutputsNum() const
```

### Code block 2

```
size_t index = compute_node_info->GetOutputsNum();
```
