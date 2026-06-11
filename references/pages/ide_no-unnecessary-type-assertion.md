# @typescript-eslint/no-unnecessary-type-assertion

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-assertion_

禁止不必要的类型断言。

如果类型断言没有更改表达式的类型，也就没有必要使用。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-assertion": "error"
  }
}

选项

详情请参考@typescript-eslint/no-unnecessary-type-assertion选项。

正例

const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;

反例

const num = 3;
export const foo = num;
export const bar = foo!;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-assertion": "error"
  }
}
```

### Code block 2

```
const num = 3;
export const foo2 = num as number;
export const foo3 = 'foo' as string;
```

### Code block 3

```
const num = 3;
export const foo = num;
export const bar = foo!;
```

### Code block 4

```
plugin:@typescript-eslint/all
```
