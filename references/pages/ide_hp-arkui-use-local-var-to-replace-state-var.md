# @performance/hp-arkui-use-local-var-to-replace-state-var

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-local-var-to-replace-state-var_

建议使用临时变量替换状态变量。

通用丢帧场景下，建议优先修改。

规则配置

// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-local-var-to-replace-state-var": "warn",
  }
}

选项

该规则无需配置额外选项。

正例

@Entry
@Component
struct MyComponent {
  @State message: string = '';
  appendMsg(newMsg: string) {
      let message = this.message;
      message += newMsg;
      message += ";";
      message += "<br/>";
      this.message = message;
  }
  build() {
    // 业务代码...
  }
}

反例

@Entry
@Component
struct MyComponent {
  @State message: string = '';
  appendMsg(newMsg: string) {
      this.message += newMsg;
      this.message += ";";
      this.message += "<br/>";
  }
  build() {
    // 业务代码...
  }
}

规则集

plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@performance/hp-arkui-use-local-var-to-replace-state-var": "warn",
  }
}
```

### Code block 2

```
@Entry
@Component
struct MyComponent {
  @State message: string = '';
  appendMsg(newMsg: string) {
      let message = this.message;
      message += newMsg;
      message += ";";
      message += "<br/>";
      this.message = message;
  }
  build() {
    // 业务代码...
  }
}
```

### Code block 3

```
@Entry
@Component
struct MyComponent {
  @State message: string = '';
  appendMsg(newMsg: string) {
      this.message += newMsg;
      this.message += ";";
      this.message += "<br/>";
  }
  build() {
    // 业务代码...
  }
}
```

### Code block 4

```
plugin:@performance/recommended
plugin:@performance/all
```
