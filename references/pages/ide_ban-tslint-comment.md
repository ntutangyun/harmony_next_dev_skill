# @typescript-eslint/ban-tslint-comment

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-tslint-comment_

不允许使用`//tslint:<rule-flag>`格式的注释。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-tslint-comment": "error"
  }
}

选项

该规则无需配置额外选项。

正例

// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
console.log('hello'); // This is a comment that just happens to mention tslint

反例

/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
console.log('hello'); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-tslint-comment": "error"
  }
}
```

### Code block 2

```
// This is a comment that just happens to mention tslint
/* This is a multiline comment that just happens to mention tslint */
console.log('hello'); // This is a comment that just happens to mention tslint
```

### Code block 3

```
/* tslint:disable */
/* tslint:enable */
/* tslint:disable:rule1 rule2 rule3... */
/* tslint:enable:rule1 rule2 rule3... */
// tslint:disable-next-line
console.log('hello'); // tslint:disable-line
// tslint:disable-next-line:rule1 rule2 rule3...
```

### Code block 4

```
plugin:@typescript-eslint/all
```
