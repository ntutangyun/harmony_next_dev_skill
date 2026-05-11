# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-tslint-comment_

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

@typescript-eslint/ban-ts-comment
@typescript-eslint/ban-types
