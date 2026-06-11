# GetDimNum

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdimnum_

函数功能

获取dim_num。

函数原型

size_t GetDimNum() const

参数说明

无

返回值

获取dim_num，即Shape的长度。

约束说明

无

调用示例

Shape shape0({3, 256, 256});
auto dim_num = shape0.GetDimNum(); // 3

## Code blocks

### Code block 1

```
size_t GetDimNum() const
```

### Code block 2

```
Shape shape0({3, 256, 256});
auto dim_num = shape0.GetDimNum(); // 3
```
