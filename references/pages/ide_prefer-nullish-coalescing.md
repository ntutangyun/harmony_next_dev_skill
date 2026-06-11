# @typescript-eslint/prefer-nullish-coalescing

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-nullish-coalescing_

强制使用空值合并运算符（??）而不是逻辑运算符。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-nullish-coalescing": "error"
  }
}

选项

详情请参考@typescript-eslint/prefer-nullish-coalescing选项。

正例

function getText1(): string | undefined {
  return 'bar';
}

function getText2(): string | null {
  return 'bar';
}

const foo1: string | undefined = getText1();
export const v1 = foo1 ?? 'a string';

const foo2: string | null = getText2();
export const v2 = foo2 ?? 'a string';

反例

declare const a: string | null;
declare const b: string | null;

export const c = a || b;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-nullish-coalescing": "error"
  }
}
```

### Code block 2

```
function getText1(): string | undefined {
  return 'bar';
}

function getText2(): string | null {
  return 'bar';
}

const foo1: string | undefined = getText1();
export const v1 = foo1 ?? 'a string';

const foo2: string | null = getText2();
export const v2 = foo2 ?? 'a string';
```

### Code block 3

```
declare const a: string | null;
declare const b: string | null;

export const c = a || b;
```

### Code block 4

```
plugin:@typescript-eslint/all
```
