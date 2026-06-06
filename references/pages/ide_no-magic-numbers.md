# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-magic-numbers_

export const finalPrice = dutyFreePrice + dutyFreePrice * TAX;
反例
export const finalPrice = 100 + 100 * 0.25;


const data = ['foo', 'bar', 'baz'];
export const dataLast = data[2];
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-loss-of-precision
@typescript-eslint/no-misused-new
