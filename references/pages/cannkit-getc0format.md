# GetC0Format

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getc0format_

------------------------------------------------

* | 4 bits | 4bits | 2 bytes | 1 byte |

* |------------|-------------|----------------|--------|

* | reserved | c0 -format | sub-format | format |

* ---------------------------------------------------

*/

函数原型
inline int32_t GetC0Format(int32_t format)
参数说明
参数	输入/输出	说明
format	输入	实际format（4字节大小，第1个字节的高四位为预留字段，低四位为c0 format段，第2-3字节为子format信息，第4字节为主format信息）。
返回值

如果包含c0 format，返回c0 format的值。

如果不包含c0 format，返回0。

异常处理

无

约束说明

无

ConvertToListAscendString
GetC0Value
