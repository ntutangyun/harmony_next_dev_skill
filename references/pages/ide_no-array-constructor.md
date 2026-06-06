# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-array-constructor_

export const createArray = (array: string) => new Array(array.length);
反例
Array();


Array('0', '1', '2');


new Array('0', '1', '2');
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/naming-convention
@typescript-eslint/no-base-to-string
