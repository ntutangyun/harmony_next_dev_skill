# MutableStorageShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutablestorageshape_

函数功能

获取可写的运行时shape。

函数原型

Shape &MutableStorageShape()

参数说明

无

返回值

可写的运行时shape。

约束说明

无

调用示例

StorageShape shape({3, 256, 256}, {256, 256, 3});
auto storage_shape = shape.MutableStorageShape(); // 256,256,3

## Code blocks

### Code block 1

```
Shape &MutableStorageShape()
```

### Code block 2

```
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto storage_shape = shape.MutableStorageShape(); // 256,256,3
```
