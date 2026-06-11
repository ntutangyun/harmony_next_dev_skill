# MutableTensorData

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutabletensordata_

函数功能

获取tensor中的数据。

函数原型

TensorData &MutableTensorData()

参数说明

无

返回值

可写的tensor data引用。

关于TensorData类型的定义，请参见TensorData。

约束说明

无

调用示例

Tensor t = {{}, {}, {}, {}, nullptr};
const Tensor &ct = t;
std::vector<int> a = {10};
t.MutableTensorData() = TensorData{reinterpret_cast<void *>(a.data()), nullptr}; // 设置新tensordata
auto td = t.GetTensorData(); // TensorData{a, nullptr}

## Code blocks

### Code block 1

```
TensorData &MutableTensorData()
```

### Code block 2

```
Tensor t = {{}, {}, {}, {}, nullptr};
const Tensor &ct = t;
std::vector<int> a = {10};
t.MutableTensorData() = TensorData{reinterpret_cast<void *>(a.data()), nullptr}; // 设置新tensordata
auto td = t.GetTensorData(); // TensorData{a, nullptr}
```
