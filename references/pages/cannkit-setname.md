# SetName

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setname_

函数功能

向TensorDesc中设置Tensor的名称。

函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

void SetName(const std::string &name);
void SetName(const char_t *name);

参数说明

参数名	输入/输出	描述
name	输入	需设置的Tensor的名称。

返回值

无

异常处理

无

约束说明

无

## Code blocks

### Code block 1

```
void SetName(const std::string &name);
void SetName(const char_t *name);
```
