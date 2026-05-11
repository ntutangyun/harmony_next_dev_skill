# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-limit-refresh-scope_

Text().width('100%').height('70%').backgroundColor(0xd2cab3)
          .align(Alignment.Center).textAlign(TextAlign.Center);
        // 此处省略100个相同的背景Text组件
        Stack() {
          if (this.isVisible) {
            Text('New Page').height("70%").backgroundColor(0xd2cab3)
              .align(Alignment.Center).textAlign(TextAlign.Center);
          }
        }.width('100%').height('70%')
      }
      Button("press").onClick(() => {
        this.isVisible = !(this.isVisible);
      })
    }
  }
}
反例
@Entry
@Component
struct StackExample5 {
  @State isVisible : boolean = false;
  build() {
    Column() {
      Stack({alignContent: Alignment.Top}) {
        Text().width('100%').height('70%').backgroundColor(0xd2cab3)
          .align(Alignment.Center).textAlign(TextAlign.Center);
        // 此处省略100个相同的背景Text组件
        if (this.isVisible) {
          Text('New Page').height("70%").backgroundColor(0xd2cab3)
            .align(Alignment.Center).textAlign(TextAlign.Center);
        }
      }
      Button("press").onClick(() => {
        this.isVisible = !(this.isVisible);
      })
    }
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-load-on-demand
@performance/hp-arkui-no-func-as-arg-for-reusable-component
