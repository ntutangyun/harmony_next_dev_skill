# HasSubFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hassubformat_

format	输入	实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。
返回值

true：实际format中包含子format。

false：实际format中不包含子format。

异常处理

无

约束说明

无

HasC0Format
ge::graphStatus
