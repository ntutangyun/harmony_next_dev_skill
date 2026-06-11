# Free

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-free_

函数功能

释放tensor。

函数原型

ge::graphStatus Free()

参数说明

无

返回值

成功时返回：ge::GRAPH_SUCCESS。

失败时返回manager函数返回的状态码。

关于ge::graphStatus类型的定义，请参见ge::graphStatus。

约束说明

无

调用示例

std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, nullptr);
td.Free();

## Code blocks

### Code block 1

```
ge::graphStatus Free()
```

### Code block 2

```
std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, nullptr);
td.Free();
```
