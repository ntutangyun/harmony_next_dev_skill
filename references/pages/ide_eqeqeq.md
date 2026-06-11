# eqeqeq

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_eqeqeq_

要求使用===和!==。

规则配置

// code-linter.json5
{
  "rules": {
    "eqeqeq": "error"
  }
}

选项

详情请参考eslint/eqeqeq选项。

正例

export function test(a: string, b: string) {
  return a === b;
}

反例

export function test(a: string, b: string) {
  // Expected '===' and instead saw '=='.
  return a == b;
}

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "eqeqeq": "error"
  }
}
```

### Code block 2

```
export function test(a: string, b: string) {
  return a === b;
}
```

### Code block 3

```
export function test(a: string, b: string) {
  // Expected '===' and instead saw '=='.
  return a == b;
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
