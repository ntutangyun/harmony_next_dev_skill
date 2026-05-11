# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-non-null-assertion_

"@typescript-eslint/no-confusing-non-null-assertion": "error"
  }
}
选项

该规则无需配置额外选项。

正例
interface Foo {
  bar?: string;
  num?: number;
}


function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
export const isEqualsBar = foo.bar === 'hello';
const num = 2;
export const isEqualsNum = num + (foo.num!) === num;
反例
interface Foo {
  bar?: string;
  num?: number;
}


function getFoo(): Foo {
  return {
    bar: 'bar',
    num: Number.MAX_VALUE
  };
}
const foo: Foo = getFoo();
// 可能会产生混淆，误以为是不等于
export const isEqualsBar = foo.bar! === 'hello';
// 可能会产生混淆，误以为是不等于
const num = 2;
export const isEqualsNum = num + foo.num! === num;
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-base-to-string
@typescript-eslint/no-confusing-void-expression
