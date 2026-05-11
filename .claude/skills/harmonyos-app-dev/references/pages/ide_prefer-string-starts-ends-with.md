# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-string-starts-ends-with_

"@typescript-eslint/prefer-string-starts-ends-with": "error"
  }
}
选项

该规则无需配置额外选项。

正例
declare const foo: string;


// starts with
foo.startsWith('bar');


// ends with
foo.endsWith('bar');
反例
declare const foo: string;
declare const index: number;
// starts with
foo[index] === 'b';
foo.charAt(index) === 'b';
foo.indexOf('bar') === index;
foo.slice(index) === 'bar';
foo.substring(index) === 'bar';
foo.match(/^bar/) !== null;
/^bar/.test(foo);


// ends with
foo[foo.length - index] === 'b';
foo.charAt(foo.length - index) === 'b';
foo.lastIndexOf('bar') === foo.length - index;
foo.slice(-index) === 'bar';
foo.substring(foo.length - index) === 'bar';
foo.match(/bar$/) !== null;
/bar$/.test(foo);
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/prefer-regexp-exec
@typescript-eslint/prefer-ts-expect-error
