# @security/no-commented-code

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-commented-code_

不使用的代码段建议直接删除，不允许通过注释的方式保留。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-commented-code": "warn"
  }
}

选项

该规则无需配置额外选项。

正例

// this is a comment

反例

// console.log('info')

规则集

plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@security/no-commented-code": "warn"
  }
}
```

### Code block 2

```
// this is a comment
```

### Code block 3

```
// console.log('info')
```

### Code block 4

```
plugin:@security/recommended
plugin:@security/all
```
