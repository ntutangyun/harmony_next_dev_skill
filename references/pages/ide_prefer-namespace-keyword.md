# @typescript-eslint/prefer-namespace-keyword

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-namespace-keyword_

推荐使用“namespace”关键字而不是“module”关键字来声明一个自定义的 TypeScript 模块。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-namespace-keyword": "error"
  }
}

选项

该规则无需配置额外选项。

正例

export namespace Example {}

反例

export module Example {}

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-namespace-keyword": "error"
  }
}
```

### Code block 2

```
export namespace Example {}
```

### Code block 3

```
export module Example {}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
