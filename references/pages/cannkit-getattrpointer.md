# GetAttrPointer

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattrpointer_

template<typename T>  const T *GetAttrPointer(size_t index) const
参数说明
参数	输入/输出	说明
T	指定的输出类型	属性类型。
index	输入	属性在IR原型定义中的索引。
返回值

指向属性的指针。

约束说明

无

调用示例
#include "register/op_def_registry.h"


namespace optiling {
static ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    const gert::RuntimeAttrs* runtime_attrs = context->GetAttrs();
    const gert::ContinuousVector attr0 = runtime_attrs->GetAttrPointer<gert::ContinuousVector>(0);
    return ge::GRAPH_SUCCESS;
}
}
构造函数
GetInt
