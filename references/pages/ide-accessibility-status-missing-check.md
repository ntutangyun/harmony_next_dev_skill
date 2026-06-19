# @correctness/accessibility-status-missing-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-accessibility-status-missing-check_

在无障碍场景开发中，须通过accessibilityRole声明组件的类型标识，如“按钮”、“编辑框”。

规则配置

// code-linter.json5
{
  "rules": {
    "@correctness/accessibility-status-missing-check": "suggestion"
  }
}

选项

该规则无需配置额外选项。

正例

@Entry
@Component
struct AccessibilityStatusMissingPositive {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
                .accessibilityRole(AccessibilityRoleType.BUTTON)
                .onClick(() => {})
		}
	}
}

反例

@Entry
@Component
struct AccessibilityStatusMissingNegative {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
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
    "@correctness/accessibility-status-missing-check": "suggestion"
  }
}
```

### Code block 2

```
@Entry
@Component
struct AccessibilityStatusMissingPositive {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
                .accessibilityRole(AccessibilityRoleType.BUTTON)
                .onClick(() => {})
		}
	}
}
```

### Code block 3

```
@Entry
@Component
struct AccessibilityStatusMissingNegative {
    build() {
        Column() {
            Column()
                .width(100)
                .height(60)
                .backgroundColor(0xf0f0f0)
                .onClick(() => {})
        }
    }
}
```

### Code block 4

```
plugin:@correctness/all
```
