# 构造函数和析构函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-construction-and-destructor_

Operator(const AscendString &name, const AscendString &type);
Operator(const char_t *name, const char_t *type);
virtual ~Operator() = default;
参数说明
参数名	输入/输出	描述
type	输入	算子类型。
name	输入	算子名称。
返回值

Operator构造函数返回Operator类型的对象。

异常处理

无

约束说明

无

Operator
AddControlInput
