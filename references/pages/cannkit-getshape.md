# GetShape

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshape_

函数功能

获取Tensor的shape，包含运行时和原始shape。

函数原型

const StorageShape &GetShape() const
StorageShape &GetShape()

参数说明

无

返回值

const StorageShape &GetShape() const：返回只读的shape引用。

StorageShape &GetShape()：返回shape引用。

关于StorageShape类型的定义，请参见StorageShape。

约束说明

无

调用示例

StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.GetShape(); // sh

## Code blocks

### Code block 1

```
const StorageShape &GetShape() const
StorageShape &GetShape()
```

### Code block 2

```
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.GetShape(); // sh
```
