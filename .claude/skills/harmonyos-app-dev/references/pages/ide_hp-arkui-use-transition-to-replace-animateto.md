# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-transition-to-replace-animateto_

"@performance/hp-arkui-use-transition-to-replace-animateto": "warn",
  }
}
选项

该规则无需配置额外选项。

正例
@Entry
@Component
struct MyComponent {
  @State show: boolean = true;


  build() {
    Column() {
      Row() {
        if (this.show) {
          Text('value')
            // Set id to make transition interruptible
            .id('myText')
            .transition(TransitionEffect.OPACITY.animation({ duration: 1000 }))
        }
      }.width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)
      Text('toggle state')
        .onClick(() => {
          // Through transition, animates the appearance or disappearance of transparency.
          this.show = !this.show;
        })
    }
  }
}
反例
@Entry
@Component
struct MyComponent {
  @State mOpacity: number = 1;
  @State show: boolean = true;


  build() {
    Column() {
      Row() {
        if (this.show) {
          Text('value')
            .opacity(this.mOpacity)
        }
      }
      .width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)


      Text('toggle state')
        .onClick(() => {
          this.show = true;
          animateTo({
            duration: 1000, onFinish: () => {
              if (this.mOpacity === 0) {
                this.show = false;
              }
            }
          }, () => {
            this.mOpacity = this.mOpacity === 1 ? 0 : 1;
          })
        })
    }
  }
}
规则集
plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-use-taskpool-for-web-request
@performance/hp-arkui-use-word-break-to-replace-zero-width-space
