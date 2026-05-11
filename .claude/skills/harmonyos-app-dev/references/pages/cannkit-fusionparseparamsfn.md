# FusionParseParamsFn

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-fusionparseparamsfn_

OpRegistrationData &FusionParseParamsFn(const FusionParseParamFunc &fusionParseParamFn)
参数说明
参数	输入/输出	说明
fusionParseParamFn	输入	解析融合算子属性的函数，请参见回调函数FusionParseParamFunc。
约束说明

对于融合算子插件，FusionParseParamsFn接口后续版本将会废弃，请使用FusionParseParamsFn（Overload）接口进行融合算子属性的解析。

回调函数FusionParseParamFunc

开发者自定义并实现FusionParseParamFunc类函数，完成原始模型中属性到适配AI处理器的模型中属性的映射，将结果填入Operator类中。

Status FusionParseParamFunc(const  vector<const google::protobuf::Message *> &v_op_origin, ge::Operator  &op_dest)

表1 参数说明

参数	输入/输出	说明
v_op_origin	输入	一组scope内的protobuf格式的数据结构（来源于原始模型的prototxt文件），包含算子属性信息。
op_dest	输出	

融合算子数据结构，保存融合算子信息。

关于Operator类，请参见Operator。

ParseParamsByOperatorFn
FusionParseParamsFn（Overload）
