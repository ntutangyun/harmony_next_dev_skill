# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-type-assertions_

// 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = <Type>value;
export const y = x as object;
反例
interface MyType {
  name: string;
}
export const x: MyType = {
  name: 'hello'
};
// 默认推荐使用 value as Type：始终优先选择const x = value as Type; 而不是const x = <Type>value;
export const y = <object>x;
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/consistent-indexed-object-style
@typescript-eslint/consistent-type-definitions
