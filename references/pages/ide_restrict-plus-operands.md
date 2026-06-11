# @typescript-eslint/restrict-plus-operands

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-plus-operands_

要求加法的两个操作数都是相同的类型，并且是“bigint”、“number”或“string”。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-plus-operands": "error"
  }
}

选项

详情请参考@typescript-eslint/restrict-plus-operands选项。

正例

const num = 10;
const bigIntNum = 1n;
export const foo1 = parseInt('5.5', num) + num;
export const foo2 = bigIntNum + bigIntNum;

反例

const num = 10;
const bigIntNum = 1n;
export const foo2 = bigIntNum + num;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-plus-operands": "error"
  }
}
```

### Code block 2

```
const num = 10;
const bigIntNum = 1n;
export const foo1 = parseInt('5.5', num) + num;
export const foo2 = bigIntNum + bigIntNum;
```

### Code block 3

```
const num = 10;
const bigIntNum = 1n;
export const foo2 = bigIntNum + num;
```

### Code block 4

```
plugin:@typescript-eslint/all
```
