# SetData

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdata_

函数功能

设置Tensor的数据。

函数原型

void SetData(TensorData &&data)

参数说明

参数	输入/输出	说明
data	输入	需要设置的数据。 关于TensorData类型的定义，请参见TensorData。

返回值

无

约束说明

无

调用示例

Tensor t = {{}, {}, {}, {}, nullptr};
void *a = &t;
TensorData td(a, nullptr);
t.SetData(std::move(td));

## Code blocks

### Code block 1

```
void SetData(TensorData &&data)
```

### Code block 2

```
Tensor t = {{}, {}, {}, {}, nullptr};
void *a = &t;
TensorData td(a, nullptr);
t.SetData(std::move(td));
```
