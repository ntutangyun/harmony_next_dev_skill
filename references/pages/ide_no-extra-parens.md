# @typescript-eslint/no-extra-parens

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-extra-parens_

禁止使用不必要的括号。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-parens": "error"
  }
}

选项

详情请参考@typescript-eslint/no-extra-parens选项。

正例

// 默认不允许在任何表达式中使用不必要的括号
(0).toString();

const result = (() => {
  console.info('arrow function');
}) ? '1' : '2';

(/^a$/).test(result);

反例

// 默认不允许在任何表达式中使用不必要的括号
const b = 10;
const c = 20;
export const a = (b * c);

export const d = (a * b) + c;

export const myType = typeof (a);

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-extra-parens": "error"
  }
}
```

### Code block 2

```
// 默认不允许在任何表达式中使用不必要的括号
(0).toString();

const result = (() => {
  console.info('arrow function');
}) ? '1' : '2';

(/^a$/).test(result);
```

### Code block 3

```
// 默认不允许在任何表达式中使用不必要的括号
const b = 10;
const c = 20;
export const a = (b * c);

export const d = (a * b) + c;

export const myType = typeof (a);
```

### Code block 4

```
plugin:@typescript-eslint/all
```
