# @typescript-eslint/comma-dangle

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-dangle_

允许或禁止使用尾随逗号。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-dangle": "error"
  }
}

选项

详情请参考@typescript-eslint/comma-dangle选项。

正例

// 默认不允许尾随逗号
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux'
};

const arr = ['1', '2'];

export { foo, arr };

反例

interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux',
};

const arr = ['1', '2',];

export { foo, arr, };

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-dangle": "error"
  }
}
```

### Code block 2

```
// 默认不允许尾随逗号
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux'
};

const arr = ['1', '2'];

export { foo, arr };
```

### Code block 3

```
interface MyType {
  bar: string;
  qux: string;
}

const foo: MyType = {
  bar: 'baz',
  qux: 'qux',
};

const arr = ['1', '2',];

export { foo, arr, };
```

### Code block 4

```
plugin:@typescript-eslint/all
```
