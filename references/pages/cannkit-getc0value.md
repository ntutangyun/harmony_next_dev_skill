# GetC0Value

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getc0value_

format	输入	实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format，第2-3字节为子format信息，第4字节为主format信息）。
返回值

如果包含c0 format，返回实际format中包含的c0 format。

如果不包含c0 format，返回-1。

异常处理

无

约束说明

设置实际format格式时，第一个字节低四位的c0 format的范围只支持x=(0001~1111)，实际获取的c0 value为2^x-1。

GetC0Format
GetFormatFromC0
