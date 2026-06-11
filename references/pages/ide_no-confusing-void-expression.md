# @typescript-eslint/no-confusing-void-expression

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-confusing-void-expression_

要求void类型的表达式出现在合适的位置。

void指要被忽略的函数返回，如果将void类型的表达式作为值使用，比如分配给变量、作为函数参数传递或者从函数中返回，容易产生误导。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-void-expression": "error"
  }
}

选项

详情请参考@typescript-eslint/no-confusing-void-expression选项。

正例

export function func(): void {
  console.info('no return');
}

反例

export function func(): void {
  return console.info('no return');
}

console.info(func());

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-confusing-void-expression": "error"
  }
}
```

### Code block 2

```
export function func(): void {
  console.info('no return');
}
```

### Code block 3

```
export function func(): void {
  return console.info('no return');
}

console.info(func());
```

### Code block 4

```
plugin:@typescript-eslint/all
```
