# COMMON_INFER_FUNC_REG

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-common-infer-func-reg_

与INFER_FUNC_REG的区别是，此函数注册的InferShape函数入参为operator基类而非子类，此接口支持多算子共用同一个InferShape函数。

函数原型
COMMON_INFER_FUNC_REG(op_name, x)

该函数内部会自动调用COMMON_INFER_VERIFY_FUNC(x)，COMMON_INFER_VERIFY_FUNC(x)函数中的x为指向COMMON_INFER_FUNC_REG(op_name, x)中“x”的指针。

约束说明

无

参数说明
参数名	输入/输出	描述
op_name	输入	算子类型。
x	输入	InferShape函数名，和IMPLEMT_COMMON_INFERFUNC的InferShape函数名保持一致。
返回值

无

BROADCAST_INFER
DECLARE_ERRORNO
