# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-redundant-state-var_

"@performance/hp-arkui-remove-redundant-state-var": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
@Entry
@Component
struct MyComponent {
  @State message: string = "";


  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }


  build() {
    Column() {
      Stack() {
        Text(this.message)
      }
      .backgroundColor("black")
      .width(200)
      .height(400)


      Button("move")
    }
  }
}
反例
@Entry
@Component
struct MyComponent {
  @State message: string = "";


  appendMsg(newMsg: string): string {
    this.message += newMsg;
    return this.message;
  }


  build() {
    Column() {
      Stack() {
      }
      .backgroundColor("black")
      .width(200)
      .height(400)


      Button("move")
    }
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-remove-redundant-nest-container
@performance/hp-arkui-remove-unchanged-state-var
