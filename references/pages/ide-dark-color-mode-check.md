# @performance/dark-color-mode-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-dark-color-mode-check_

通过启用深色模式，可以进一步实现能耗的降低。应用需要根据当前设备状态来适配深色模式。

说明

在检查整个工程时，该规则才生效。

code-linter.json5配置文件中的overrides和ignore字段对该规则不生效。

若想关闭该规则检查，可将code-linter.json5配置文件中rules字段设置为off。

规则配置

// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}

选项

该规则无需配置额外选项。

正例

src
├── main
│   ├── ets
│   └── resources
│       └── dark
│           └── element
│               └── color.json
│
├── mock
│   └── mock-config.json5

反例

src
├── main
│   ├── ets
│   └── resources
│       └── dark
│           └── element
│
├── mock
│   └── mock-config.json5

规则集

plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@performance/dark-color-mode-check": "suggestion",
  }
}
```

### Code block 2

```
src
├── main
│   ├── ets
│   └── resources
│       └── dark
│           └── element
│               └── color.json
│
├── mock
│   └── mock-config.json5
```

### Code block 3

```
src
├── main
│   ├── ets
│   └── resources
│       └── dark
│           └── element
│
├── mock
│   └── mock-config.json5
```

### Code block 4

```
plugin:@performance/all
```
