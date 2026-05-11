# GetFormatFromSub

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getformatfromsub_

------------------------------------------------

* | 4 bits | 4bits | 2 bytes | 1 byte |

* |------------|-------------|----------------|--------|

* | reserved | c0 -format | sub-format | format |

* ---------------------------------------------------

*/

函数原型
inline int32_t GetFormatFromSub(int32_t primary_format, int32_t sub_format)
参数说明
参数	输入/输出	说明
primary_format	输入	主format信息，值不超过0xffU。
sub_format	输入	子format信息，值不超过0xffffU。
返回值

指定的主format和子format对应的实际format。

异常处理

无

约束说明

无

GetFormatFromC0
GetFormatFromSubAndC0
