# INFER_FUNC_REG

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infer-func-reg_

该函数内部会自动调用INFER_VERIFY_FUNC(op_name, x)，INFER_VERIFY_FUNC函数中的op_name为算子的类型，x为指向INFER_FUNC_REG（op_name,x）中“x”的指针。

约束说明

无

参数说明
参数名	输入/输出	描述
op_name	输入	算子类型。
x	输入	InferShape函数名，和IMPLEMT_INFERFUNC的InferShape函数名保持一致。
返回值

无

INFER_FORMAT_FUNC_REG
原型定义接口（REG_OP）
