# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-assertion_

export const includesBaz = example.property?.includes('baz') ?? false;
反例
interface Example {
  property?: string;
}


declare const example: Example;
// 禁止使用"example.property!"的方式来进行非空断言
export const includesBaz = example.property!.includes('baz');
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-non-null-asserted-optional-chain
@typescript-eslint/no-parameter-properties
