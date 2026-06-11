# @performance/number-init-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-number-init-check_

该规则将检查number是否正确使用。

根据ArkTS高性能编程实践，建议修改。

规则配置

// code-linter.json5
{
  "rules": {
    "@performance/number-init-check": "suggestion",
  }
}

选项

该规则无需配置额外选项。

正例

let intNum = 1;
intNum = 2;
let floatNum = 1.3;
floatNum = 2.4;

反例

let intNum = 1;
// intNum is declared as int. Avoid changing it to float.
intNum = 1.1;
let floatNum = 1.3;
// floatNum is declared as float. Avoid changing it to int.
floatNum = 2;

规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@performance/number-init-check": "suggestion",
  }
}
```

### Code block 2

```
let intNum = 1;
intNum = 2;
let floatNum = 1.3;
floatNum = 2.4;
```

### Code block 3

```
let intNum = 1;
// intNum is declared as int. Avoid changing it to float.
intNum = 1.1;
let floatNum = 1.3;
// floatNum is declared as float. Avoid changing it to int.
floatNum = 2;
```

### Code block 4

```
plugin:@performance/all
```
