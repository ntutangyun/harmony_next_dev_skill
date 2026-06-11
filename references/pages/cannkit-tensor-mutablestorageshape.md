# MutableStorageShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-mutablestorageshape_

函数功能

获取运行时Tensor的shape，此shape对象是可变的。

函数原型

Shape &MutableStorageShape()

参数说明

无

返回值

运行时shape的引用。

约束说明

无

调用示例

StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableStorageShape(); // 2,1,3

## Code blocks

### Code block 1

```
Shape &MutableStorageShape()
```

### Code block 2

```
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableStorageShape(); // 2,1,3
```
