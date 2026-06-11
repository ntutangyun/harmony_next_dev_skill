# @typescript-eslint/no-unnecessary-type-constraint

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-type-constraint_

不允许在泛型中使用不必要的约束条件。

泛型参数（<T>）如果不包含“extends”关键字，默认约束条件是“unknown”（即<T extends unknown>），所以“<T extends any>“、“<T extends unknown>“的写法是多余的。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unnecessary-type-constraint": "error"
  }
}

选项

该规则无需配置额外选项。

正例

export interface Foo<T> {
  foo: T;
}

export const bar = <T>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T>(param: T): void {
  console.info(`${param as string}`);
}

反例

// extends any或者extends unknown的写法是多余的
export interface Foo<T extends any> {
  foo: T;
}

export const bar = <T extends unknown>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T extends any>(param: T): void {
  console.info(`${param as string}`);
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
    "@typescript-eslint/no-unnecessary-type-constraint": "error"
  }
}
```

### Code block 2

```
export interface Foo<T> {
  foo: T;
}

export const bar = <T>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T>(param: T): void {
  console.info(`${param as string}`);
}
```

### Code block 3

```
// extends any或者extends unknown的写法是多余的
export interface Foo<T extends any> {
  foo: T;
}

export const bar = <T extends unknown>(param: T): void => {
  console.info(`${param as string}`);
};

export function foo<T extends any>(param: T): void {
  console.info(`${param as string}`);
}
```

### Code block 4

```
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```
