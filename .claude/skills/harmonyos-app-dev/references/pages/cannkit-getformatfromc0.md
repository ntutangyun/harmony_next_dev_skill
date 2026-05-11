# GetFormatFromC0

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getformatfromc0_

------------------------------------------------

* | 4 bits | 4bits | 2 bytes | 1 byte |

* |------------|-------------|----------------|--------|

* | reserved | c0 -format | sub-format | format |

* ---------------------------------------------------

*/

函数原型
inline int32_t GetFormatFromC0(int32_t format, int32_t c0_format)
参数说明
参数	输入/输出	说明
format	输入	sub-format与主format信息，值不超过0xffffffU。
c0_format	输入	c0_format信息，值不超过0xfU。
返回值

指定的format和c0_format对应的实际format。

异常处理

无

约束说明

无

GetC0Value
GetFormatFromSub
