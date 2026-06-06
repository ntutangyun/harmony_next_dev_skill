# GetAllAttrNamesAndTypes

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getallattrnamesandtypes_

const std::map<std::string, std::string> GetAllAttrNamesAndTypes() const;
graphStatus GetAllAttrNamesAndTypes(std::map<AscendString, AscendString> &attr_name_types) const;
参数说明
参数名	输入/输出	描述
attr_name_types	输出	所有的属性名称和属性类型。
返回值
类型	描述
graphStatus	

GRAPH_FAILED：失败。

GRAPH_SUCCESS：成功。

异常处理

无

约束说明

无

GetAttr
GetAllIrAttrNamesAndTypes
