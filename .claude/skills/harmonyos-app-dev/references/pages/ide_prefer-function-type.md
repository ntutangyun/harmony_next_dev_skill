# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-function-type_

export function foo(example: GeneratedTypeLiteralInterface): number {
  return example();
}


export interface Foo {
  (bar: string): this;
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/prefer-for-of
@typescript-eslint/prefer-includes
