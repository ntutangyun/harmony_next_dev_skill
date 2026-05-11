# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-word-break-in-space_

"@performance/hp-arkui-use-word-break-to-replace-zero-width-space": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
@Component
export struct MyComponent {
  private diskName: string = '';


  build() {
    Text(this.diskName)
      .textAlign(TextAlign.Start)
      .wordBreak(WordBreak.BREAK_ALL)
  }
}
反例
@Component
export struct MyComponent {
  private diskName: string = '';


  build() {
    Text(this.diskName.split("").join("\u200B"))
      .textAlign(TextAlign.Start)
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-use-transition-to-replace-animateto
@performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）
