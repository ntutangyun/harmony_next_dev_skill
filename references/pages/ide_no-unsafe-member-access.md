# @typescript-eslint/no-unsafe-member-access

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-member-access_

禁止成员访问“any”类型的值。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-unsafe-member-access": "error"
  }
}

选项

该规则无需配置额外选项。

正例

declare const properlyTyped: { prop: { a: string } };

export const v1 = properlyTyped.prop.a;

const key = 'a';
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];

反例

declare const properlyTyped: { prop: { a: any } };

export const v1 = properlyTyped.prop.a;

const key = 'a' as any;
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx: any = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];

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
    "@typescript-eslint/no-unsafe-member-access": "error"
  }
}
```

### Code block 2

```
declare const properlyTyped: { prop: { a: string } };

export const v1 = properlyTyped.prop.a;

const key = 'a';
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```

### Code block 3

```
declare const properlyTyped: { prop: { a: any } };

export const v1 = properlyTyped.prop.a;

const key = 'a' as any;
export const v2 = properlyTyped.prop[key];

const arr = ['1', '2', '3'];
let idx: any = 1;
export const v3 = arr[idx];
export const v4 = arr[idx++];
```

### Code block 4

```
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```
