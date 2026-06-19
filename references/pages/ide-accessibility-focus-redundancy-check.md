# @correctness/accessibility-focus-redundancy-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-focus-redundancy-check_

在无障碍场景开发中，避免存在控件焦点冗余。

规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-focus-redundancy-check": "suggestion"
  }
}

选项

该规则无需配置额外选项。

正例

@Entry
@Component
struct FocusRedundancyPositive {
    build() {
        Column() {
            Column() {
                Button('提交')
                    .onClick(() => {})
            }
            .accessibilityGroup(true)
            .onClick(() => {})
        }
    }
}

反例

@Entry
@Component
struct FocusRedundancyNegative {
    build() {
        Column() {
            Column() {
                Button('按钮1')
                    .accessibilityText('操作')
                    .onClick(() => {})

                Text('文本')
                    .accessibilityText('说明文字')

                Image($r('app.media.icon'))
                    .accessibilityText('图标')
                    .onClick(() => {})
            }
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
    "@correctness/accessibility-focus-redundancy-check": "suggestion"
  }
}
```

### Code block 2

```
@Entry
@Component
struct FocusRedundancyPositive {
    build() {
        Column() {
            Column() {
                Button('提交')
                    .onClick(() => {})
            }
            .accessibilityGroup(true)
            .onClick(() => {})
        }
    }
}
```

### Code block 3

```
@Entry
@Component
struct FocusRedundancyNegative {
    build() {
        Column() {
            Column() {
                Button('按钮1')
                    .accessibilityText('操作')
                    .onClick(() => {})

                Text('文本')
                    .accessibilityText('说明文字')

                Image($r('app.media.icon'))
                    .accessibilityText('图标')
                    .onClick(() => {})
            }
            .onClick(() => {})
        }
    }
}
```

### Code block 4

```
plugin:@correctness/all
```
