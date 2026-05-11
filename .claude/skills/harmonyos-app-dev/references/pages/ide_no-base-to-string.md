# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-base-to-string_

// Passing an object or class instance to string concatenation:
const obj: MyType = {
  name: 'object'
};
export const v1 = '' + obj;


class MyClass {}
const value = new MyClass();
export const v2 = value + '';


// Interpolation and manual .toString() calls too:
export const v3 = `Value: ${value}`;
export const v4 = obj.toString();
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-array-constructor
@typescript-eslint/no-confusing-non-null-assertion
