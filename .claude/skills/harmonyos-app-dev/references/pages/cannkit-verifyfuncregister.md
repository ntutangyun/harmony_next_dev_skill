# VerifyFuncRegister

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verifyfuncregister_

VerifyFuncRegister(const std::string &operator_type, const VerifyFunc &verify_func);
VerifyFuncRegister(const char_t *const operator_type, const VerifyFunc &verify_func);
~VerifyFuncRegister() = default;
参数说明
参数名	输入/输出	描述
operator_type	输入	算子类型。
verify_func	输入	算子verify函数。
返回值

VerifyFuncRegister构造函数返回VerifyFuncRegister类型的对象。

约束说明

算子verifyFunc函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。

GetDataTypeLength
ConvertToAscendString
