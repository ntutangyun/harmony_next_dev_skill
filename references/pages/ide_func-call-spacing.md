# @typescript-eslint/func-call-spacing

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_func-call-spacing_

禁止或者要求函数名与函数名后面的括号之间加空格。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/func-call-spacing": "error"
  }
}

选项

详情请参考@typescript-eslint/func-call-spacing选项。

正例

function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn();

反例

function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn ();

fn
();

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/func-call-spacing": "error"
  }
}
```

### Code block 2

```
function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn();
```

### Code block 3

```
function fn() {
  console.log('hello');
}

// 默认不允许函数名称和左括号之间有空格。
fn ();

fn
();
```

### Code block 4

```
plugin:@typescript-eslint/all
```
