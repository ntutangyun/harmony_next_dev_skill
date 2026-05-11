# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-implicit-any-catch_

该规则默认不允许使用隐式any类型。但是可以接受{"allowExplicitAny": true}对象作为规则参数，以允许使用显式的any类型。

示例：

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-implicit-any-catch": ["error", {"allowExplicitAny": true}]
  }
}

在配置{"allowExplicitAny": true}的条件下，以下代码不会产生告警：

try {
  // ...
} catch (e: any) {
  // ...
}
正例
try {
  // ...
} catch (e: unknown) {
  // ...
}
反例
try {
  // ...
// 默认不允许使用隐式any类型
} catch (e) {
  // ...
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-for-in-array
@typescript-eslint/no-implied-eval
