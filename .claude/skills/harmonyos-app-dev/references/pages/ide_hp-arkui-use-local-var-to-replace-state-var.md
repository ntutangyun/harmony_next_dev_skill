# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-local-var-to-replace-state-var_

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

@performance/hp-arkui-use-id-in-get-resource-sync-api
@performance/hp-arkui-use-onAnimationStart-for-swiper-preload
