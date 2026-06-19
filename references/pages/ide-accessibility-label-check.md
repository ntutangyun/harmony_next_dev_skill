# @correctness/accessibility-label-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-label-check_

在无障碍场景中，建议通过accessibilityText为控件添加无障碍文本信息。

规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-label-check": "suggestion"
  }
}

选项

该规则无需配置额外选项。

正例

@Entry
@Component
struct AccessibilityLabelPositive {
    build() {
        Column() {
            Text('文本')
                .width(60)
                .height(60)
                .accessibilityText('返回')
                .onClick(() => {})
        }
    }
}

反例

@Entry
@Component
struct AccessibilityLabelNegative {
    build() {
        Column() {
            Text()
                .width(60)
                .height(60)
                .backgroundColor(0xeaeaea)
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
    "@correctness/accessibility-label-check": "suggestion"
  }
}
```

### Code block 2

```
@Entry
@Component
struct AccessibilityLabelPositive {
    build() {
        Column() {
            Text('文本')
                .width(60)
                .height(60)
                .accessibilityText('返回')
                .onClick(() => {})
        }
    }
}
```

### Code block 3

```
@Entry
@Component
struct AccessibilityLabelNegative {
    build() {
        Column() {
            Text()
                .width(60)
                .height(60)
                .backgroundColor(0xeaeaea)
                .onClick(() => {})
        }
    }
}
```

### Code block 4

```
plugin:@correctness/all
```
