# AscendStringToFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtoformat_

static Format AscendStringToFormat(const AscendString &str);
参数说明
参数	输入/输出	说明
str	输入	待转换的Format字符串形式，AscendString类型。
返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考Format；输入不合法时，返回FORMAT_RESERVED，并打印报错信息。

约束说明

无

调用示例
ge::AscendString format_str("NHWC");
auto format = AscendStringToFormat(format_str); // 1
FormatToAscendString
DataTypeToSerialString
