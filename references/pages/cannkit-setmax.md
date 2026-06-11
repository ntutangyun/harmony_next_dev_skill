# SetMax

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmax_

函数功能

设置最大的T对象指针。

函数原型

void SetMax(T *max)

参数说明

参数	输入/输出	说明
max	输入	最大的T对象指针。

返回值

无

约束说明

无

调用示例

Range<int> range;
int max = 1024;
range.SetMax(&max);

## Code blocks

### Code block 1

```
void SetMax(T *max)
```

### Code block 2

```
Range<int> range;
int max = 1024;
range.SetMax(&max);
```
