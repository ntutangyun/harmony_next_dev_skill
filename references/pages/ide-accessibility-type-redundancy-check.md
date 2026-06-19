# @correctness/accessibility-type-redundancy-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-type-redundancy-check_

在无障碍场景开发中，避免存在冗余的button、radio等组件类型，否则可能导致冗余播放等问题。

规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-type-redundancy-check": "suggestion"
  }
}

选项

该规则无需配置额外选项。

正例

@Entry
@Component
struct AccessibilityTypeRedundancyPositive {
    build() {
        Column() {
            Button('提交')
                .accessibilityText('提交表单')
                .onClick(() => {})
        }
    }
}

反例

@Entry
@Component
struct AccessibilityTypeRedundancyNegative {
    build() {
        Column() {
            Button()
                .accessibilityText('提交按钮')
                .onClick(() => {})
        }
    }
}

规则集

plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-type-redundancy-check": "suggestion"
  }
}
```

### Code block 2

```
@Entry
@Component
struct AccessibilityTypeRedundancyPositive {
    build() {
        Column() {
            Button('提交')
                .accessibilityText('提交表单')
                .onClick(() => {})
        }
    }
}
```

### Code block 3

```
@Entry
@Component
struct AccessibilityTypeRedundancyNegative {
    build() {
        Column() {
            Button()
                .accessibilityText('提交按钮')
                .onClick(() => {})
        }
    }
}
```

### Code block 4

```
plugin:@correctness/all
```
