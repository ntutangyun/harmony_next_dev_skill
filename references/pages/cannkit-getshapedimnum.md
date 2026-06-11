# GetShapeDimNum

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapedimnum_

函数功能

获取shape的维度大小，即rank大小。

函数原型

size_t GetShapeDimNum() const;

参数说明

无

返回值

类型	描述
size_t	返回shape的维度大小，即shape的rank，如果是unknown的rank，返回0。

异常处理

无

约束说明

无

## Code blocks

### Code block 1

```
size_t GetShapeDimNum() const;
```
