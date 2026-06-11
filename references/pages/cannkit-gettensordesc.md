# GetTensorDesc

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensordesc_

函数功能

获取Tensor的描述符。

函数原型

TensorDesc GetTensorDesc() const;

参数说明

无

返回值

类型	描述
TensorDesc	返回当前Tensor的描述符。

异常处理

无

约束说明

修改返回的TensorDesc信息，不影响Tensor对象中已有的TensorDesc信息。

## Code blocks

### Code block 1

```
TensorDesc GetTensorDesc() const;
```
