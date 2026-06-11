# @typescript-eslint/quotes

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_quotes_

强制使用一致的反引号、双引号或单引号风格。

说明

该规则默认检查字符串是否正确使用双引号。如需修改请参考选项。

该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用@hw-stylistic/quotes。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/quotes": "error"
  }
}

选项

详情请参考@typescript-eslint/quotes选项。

正例

export const double = "double";
export const foo = `back
tick`;  // backticks are allowed due to newline

反例

// 默认推荐使用双引号
export const single = 'single';
export const unescaped = 'a string containing "double" quotes';
export const backtick = `back\ntick`; // you can use \n in single or double quoted strings

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/quotes": "error"
  }
}
```

### Code block 2

```
export const double = "double";
export const foo = `back
tick`;  // backticks are allowed due to newline
```

### Code block 3

```
// 默认推荐使用双引号
export const single = 'single';
export const unescaped = 'a string containing "double" quotes';
export const backtick = `back\ntick`; // you can use \n in single or double quoted strings
```

### Code block 4

```
plugin:@typescript-eslint/all
```
