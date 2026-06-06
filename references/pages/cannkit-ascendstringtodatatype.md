# AscendStringToDataType

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtodatatype_

static DataType AscendStringToDataType(const AscendString &str);
参数说明
参数	输入/输出	说明
str	输入	待转换的DataType字符串形式，AscendString类型。
返回值

输入合法时，返回转换后的DataType enum值，枚举定义请参考DataType；输入不合法时，返回DT_UNDEFINED并打印报错日志。

约束说明

无

调用示例
ge::AscendString type_str("DT_UINT32");
auto data_type = AscendStringToDataType(type_str); // 8
DataTypeToAscendString
FormatToAscendString
