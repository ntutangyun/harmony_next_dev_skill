# GetListListInt

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getlistlistint_

函数功能

获取ContinuousVectorVector *类型的属性值，即二维数组且每个元素类型为int。

函数原型

const ContinuousVectorVector *GetListListInt(const size_t index) const

参数说明

参数	输入/输出	说明
index	输入	属性在IR原型定义中的索引。

返回值

指向属性值的指针。

关于ContinuousVectorVector类型的定义，请参见ContinuousVectorVector。

约束说明

无

调用示例

// 假设某算子的IR原型定义中，第一个属性的值是二维数组int类型
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
const ContinuousVectorVector *attr0 = runtime_attrs->GetListListInt(0);

## Code blocks

### Code block 1

```
const ContinuousVectorVector *GetListListInt(const size_t index) const
```

### Code block 2

```
// 假设某算子的IR原型定义中，第一个属性的值是二维数组int类型
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
const ContinuousVectorVector *attr0 = runtime_attrs->GetListListInt(0);
```
