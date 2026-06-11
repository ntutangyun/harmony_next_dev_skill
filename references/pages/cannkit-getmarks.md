# GetMarks

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmarks_

函数功能

在资源类算子推理的上下文中，获取成对资源算子的标记。

函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

const std::vector<std::string> &GetMarks() const
void GetMarks(std::vector<AscendString> &marks) const

参数说明

无

返回值

类型	描述
const std::vector<std::string>	资源类算子的标记。

异常处理

无

约束说明

无

## Code blocks

### Code block 1

```
const std::vector<std::string> &GetMarks() const
void GetMarks(std::vector<AscendString> &marks) const
```
