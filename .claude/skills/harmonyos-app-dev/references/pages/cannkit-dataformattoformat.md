# DataFormatToFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dataformattoformat_

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用入参为AscendString类型的接口。

返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考Format，仅支持部分格式，详见约束说明；输入不合法时，返回FORMAT_RESERVED，并打印报错信息。

约束说明

只支持以下几种格式：

"NCHW"：FORMAT_NCHW

"NHWC"：FORMAT_NHWC

"NDHWC"：FORMAT_NDHWC

"NCDHW"：FORMAT_NCDHW

"ND"：FORMAT_ND

调用示例
// 如果使用的是AscendString入参的接口(建议使用)
ge::AscendString format_str = "NHWC";
auto format = DataFormatToFormat(format_str); // 1
 
// 如果使用的是std::string入参的接口(不建议使用)
std::string format_str = "NHWC";
auto format = DataFormatToFormat(format_str); // 1
SerialStringToFormat
GetDataTypeLength
