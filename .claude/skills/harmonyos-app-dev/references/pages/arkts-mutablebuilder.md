# mutableBuilder：实现全局@Builder动态更新

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mutablebuilder_

>buttonBuilder
        } else {
          this.message += 'T';
          this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder
        }
      })
    }.position({x: 120, y: 60})
  }
}

点击Button，可将textBuilder动态更改为buttonBuilder，如下图所示：

使用mutableBuilder显示弹出菜单

由于MutableBuilder继承自WrappedBuilder，故mutableBuilder对应的@Builder具有跟WrappedBuilder同等能力，如下示例，mutableBuilder对应的@Builder方法可作为bindMenu入参，支持点击弹出菜单。

@Builder
function overBuilder() {
  Row() {
    Text('全局 Builder')
      .fontSize(30)
      .fontWeight(FontWeight.Bold)
  }
}


@Entry
@Component
struct Index {
  @State arr: number[] = [1,2,3,4,5];


  mutableBuilderMenu: MutableBuilder<[]> = mutableBuilder<[]>(overBuilder);
  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(`${item}`)
            .width('100%')
              .height(100)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
          }
          // 使用mutableBuilder显示弹出菜单
          .bindMenu(this.mutableBuilderMenu.builder)
        }, (item: number) => JSON.stringify(item))
      }
    }
  }
}
观察mutableBuilder中@Builder的变化

mutableBuilder对应的@Builder函数中可使用MutableBinding进行包裹来观察状态变量的变化，同时可通过@Monitor或addMonitor监听mutableBuilder中@Builder的变化。

import { UIUtils, MutableBinding } from '@kit.ArkUI';


@Builder
function textBuilder(p: MutableBinding<string>) {
  Text(p.value)
    .margin(20)
    .onClick(() => {
      p.value += 't';
    })
}


@Builder
function buttonBuilder(p: MutableBinding<string>) {
  Button(p.value)
    .margin(20)
    .onClick(() => {
      p.value += 'b';
    })
}


let counter: number = 1;


@Entry
@ComponentV2
struct MyApp {
  @Local message: string = 'init';
  @Local switchingBuilder: MutableBuilder<[MutableBinding<string>]> = mutableBuilder(textBuilder);


  @Monitor('switchingBuilder') variableChange(m: IMonitor): void {
    console.info(`Builder changed. is buttonBuilder: ${m.value<MutableBuilder<[MutableBinding<string>]>>()?.now.builder === buttonBuilder}`);
  }


  build() {
    Column() {
      this.switchingBuilder.builder(UIUtils.makeBinding(()=> this.message, txt => this.message = txt))
      Button('Click to change')
        .onClick(() => {
          counter++;
          if(counter % 2 === 0) {
            this.message += 'B';
            this.switchingBuilder = mutableBuilder(buttonBuilder); // textBuilder--->buttonBuilder，@Monitor会触发回调
          } else {
            this.message += 'T';
            this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder，@Monitor会触发回调
          }
        })
    }.position({x: 120, y: 60})
  }
}

点击Click to change按钮，可将textBuilder动态切换为buttonBuilder，this.message将自动加B，界面会显示initB按钮。点击initB按钮，buttonBuilder中的p.value将自动加b，如下图所示：

点击Click to change按钮将textBuilder动态切换为buttonBuilder时，@Monitor将监听到全局@Builder的变化，并打印日志@Builder changed. is buttonBuilder: true。

wrapBuilder：封装全局@Builder
@Styles装饰器：定义组件重用样式
