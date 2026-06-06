# MutableTensorData

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutabletensordata_

t.MutableTensorData() = TensorData{reinterpret_cast<void *>(a.data()), nullptr}; // 设置新tensordata
auto td = t.GetTensorData(); // TensorData{a, nullptr}
GetTensorData
TilingContext
