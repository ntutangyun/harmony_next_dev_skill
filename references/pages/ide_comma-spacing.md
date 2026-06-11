# @typescript-eslint/comma-spacing

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_comma-spacing_

强制逗号前后的空格风格保持一致。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-spacing": "error"
  }
}

选项

详情请参考@typescript-eslint/comma-spacing选项。

正例

// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr1 = ['1', '2'];
export const arr2 = ['1',, '3'];

function qur(a: string, b: string) {
  return `${a}${b}`;
}
qur('1', '2');

反例

// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr = ['1' , '2'];

function qur(a: string ,b: string) {
  return `${a}${b}`;
}
qur('1' ,'2');

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/comma-spacing": "error"
  }
}
```

### Code block 2

```
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr1 = ['1', '2'];
export const arr2 = ['1',, '3'];

function qur(a: string, b: string) {
  return `${a}${b}`;
}
qur('1', '2');
```

### Code block 3

```
// 默认不允许逗号前有空格，逗号后需要一个或多个空格
export const arr = ['1' , '2'];

function qur(a: string ,b: string) {
  return `${a}${b}`;
}
qur('1' ,'2');
```

### Code block 4

```
plugin:@typescript-eslint/all
```
