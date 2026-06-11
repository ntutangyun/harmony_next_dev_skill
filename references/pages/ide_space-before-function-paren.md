# @typescript-eslint/space-before-function-paren

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_space-before-function-paren_

强制在函数名和括号之间保持一致的空格风格。

说明

该规则默认要求函数名和括号间有空格。如需修改请参考选项。

该规则建议在对.ts文件进行检查时使用。如需检查.ets文件，建议使用@hw-stylistic/space-before-function-paren。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-before-function-paren": "error"
  }
}

选项

详情请参考@typescript-eslint/space-before-function-paren选项。

正例

// 默认foo和(之间需要一个空格
export function foo () {
  // ...
}

反例

// 默认foo和(之间需要一个空格
export function foo() {
  // ...
}

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/space-before-function-paren": "error"
  }
}
```

### Code block 2

```
// 默认foo和(之间需要一个空格
export function foo () {
  // ...
}
```

### Code block 3

```
// 默认foo和(之间需要一个空格
export function foo() {
  // ...
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
