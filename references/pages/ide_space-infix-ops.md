# @typescript-eslint/space-infix-ops

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-infix-ops_

运算符前后要求有空格。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-infix-ops": "error"
  }
}

选项

详情请参考@typescript-eslint/space-infix-ops选项。

正例

declare const a: number;
declare const b: number;
export const c = a + b;

反例

declare const a: number;
declare const b: number;
export const c = a+b;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-infix-ops": "error"
  }
}
```

### Code block 2

```
declare const a: number;
declare const b: number;
export const c = a + b;
```

### Code block 3

```
declare const a: number;
declare const b: number;
export const c = a+b;
```

### Code block 4

```
plugin:@typescript-eslint/all
```
