# 构造函数和析构函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-construction-and-destructor_

函数功能

Allocator构造函数和析构函数。

函数原型

Allocator() = default;
virtual ~Allocator() = default;
Allocator(const Allocator &) = delete;
Allocator &operator=(const Allocator &) = delete;

参数说明

无

返回值

无

异常处理

无

约束说明

虚基类需要开发者派生。

## Code blocks

### Code block 1

```
Allocator() = default;
virtual ~Allocator() = default;
Allocator(const Allocator &) = delete;
Allocator &operator=(const Allocator &) = delete;
```
