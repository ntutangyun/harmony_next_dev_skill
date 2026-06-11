# @typescript-eslint/explicit-module-boundary-types

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-module-boundary-types_

导出到外部的函数和公共类方法，需要显式的定义返回类型和参数类型。

该规则仅支持对.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-module-boundary-types": "error"
  }
}

选项

详情请参考@typescript-eslint/explicit-module-boundary-types选项。

正例

// A function with no return value (void)
export function test1(): void {
  return;
}

// A return value of type string
export const arrowFn1 = (): string => 'test';

// All arguments should be typed
export const arrowFn2 = (arg: string): string => `test ${arg}`;

export class Test {
  // A class method with no return value (void)
  public method(): void {
    return;
  }
}

// The function does not apply because it is not an exported function.
function test2() {
  return;
}

test2();

反例

// Should indicate that no value is returned (void)
export function test() {
  return;
}

// Should indicate that a string is returned
export const arrowFn1 = () => 'test';

// All arguments should be typed
export const arrowFn2 = (arg): string => `test ${arg}`;
export const arrowFn3 = (arg: any): string => `test ${arg}`;

export class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}

规则集

plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/explicit-module-boundary-types": "error"
  }
}
```

### Code block 2

```
// A function with no return value (void)
export function test1(): void {
  return;
}

// A return value of type string
export const arrowFn1 = (): string => 'test';

// All arguments should be typed
export const arrowFn2 = (arg: string): string => `test ${arg}`;

export class Test {
  // A class method with no return value (void)
  public method(): void {
    return;
  }
}

// The function does not apply because it is not an exported function.
function test2() {
  return;
}

test2();
```

### Code block 3

```
// Should indicate that no value is returned (void)
export function test() {
  return;
}

// Should indicate that a string is returned
export const arrowFn1 = () => 'test';

// All arguments should be typed
export const arrowFn2 = (arg): string => `test ${arg}`;
export const arrowFn3 = (arg: any): string => `test ${arg}`;

export class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}
```

### Code block 4

```
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```
