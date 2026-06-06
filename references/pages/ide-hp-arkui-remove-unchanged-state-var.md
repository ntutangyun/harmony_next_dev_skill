# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-remove-unchanged-state-var_

"@performance/hp-arkui-remove-unchanged-state-var": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
class Translate {
  translateX: number = 20;
}


@Component
struct Title {
  build() {
    Row() {
      // 本地资源 icon.png
      Image($r('app.media.icon'))
        .width(50)
        .height(50)
      Text("Title")
        .fontSize(20)
    }
  }
}


@Entry
@Component
struct MyComponent {
  @State translateObj: Translate = new Translate();
  // 直接使用一般变量即可
  button_msg: string = "i am button";


  build() {
    Column() {
      Title()
      Stack() {
      }
      .backgroundColor("black")
      .width(200)
      .height(400)


      Button(this.button_msg)
        .onClick(() => {
          animateTo({
            duration: 50
          }, () => {
            this.translateObj.translateX = (this.translateObj.translateX + 50) % 150
          })
        })
    }
    .translate({
      x: this.translateObj.translateX
    })
  }
}
反例
@Observed
class Translate {
  translateX: number = 20;
}


@Component
struct Title {
  build() {
    Row() {
      // 本地资源 icon.png
      Image($r('app.media.icon'))
        .width(50)
        .height(50)
      Text("Title")
        .fontSize(20)
    }
  }
}


@Entry
@Component
struct MyComponent {
  @State translateObj: Translate = new Translate();
  @State button_msg: string = "i am button";


  build() {
    Column() {
      Title()
      Stack() {
      }
      .backgroundColor("black")
      .width(200)
      .height(400)


      // 这里只是用了状态变量button_msg的值，没有任何写的操作
      Button(this.button_msg)
        .onClick(() => {
          animateTo({
            duration: 50
          }, () => {
            this.translateObj.translateX = (this.translateObj.translateX + 50) % 150
          })
        })
    }
    .translate({
      x: this.translateObj.translateX
    })
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-remove-redundant-state-var
@performance/hp-arkui-set-cache-count-for-lazyforeach-grid
