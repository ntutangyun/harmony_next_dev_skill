# makeObserved接口：将非观察数据变为可观察数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved_

------Computed----------');
    return this.message.id + ' ' + this.message.age;
  }


  build() {
    Column() {
      Text(`id: ${this.message.id}`)
        .id('textIdMessage')
        .fontSize(30)
        .margin(5)
        .onClick(() => {
          this.message.id++;
        })
      Text(`age: ${this.message.age}`)
        .id('textAgeMessageAge')
        .fontSize(30)
        .margin(5)
        .onClick(() => {
          this.message.age++;
        })
      Text(`Computed age + id: ${this.ageId}`)
        .fontSize(30)
        .margin(5)
      Button('change Info')
        .id('buttonChangeInfo')
        .fontSize(30)
        .margin(5)
        .onClick(() => {
          // 返回类实例本身，并赋值给message，触发@Computed和@Monitor
          this.message = UIUtils.makeObserved(new Info(200));
        })
      Child({ message: this.message })
    }
    .height('100%')
    .width('100%')
  }
}


@ComponentV2
struct Child {
  @Param @Require message: Info;


  build() {
    Text(`Child id: ${this.message.id}`)
      .fontSize(30)
      .margin(5)
  }
}
Page8.ets

makeObserved在@Component内使用

makeObserved不能和V1的状态变量装饰器一起使用，但可以在@Component装饰的自定义组件里使用。

import { UIUtils } from '@kit.ArkUI';
class Info {
  public id: number = 0;


  constructor(id: number) {
    this.id = id;
  }
}




@Entry
@Component
struct Page9 {
  // 如果和@State一起使用会抛出运行时异常
  message: Info = UIUtils.makeObserved(new Info(20));


  build() {
    RelativeContainer() {
      Text(`${this.message.id}`)
        .id('textNumber')
        .onClick(() => {
          this.message.id++;
        })
    }
    .height('100%')
    .width('100%')
  }
}
Page9.ets
常见问题
getTarget后的数据可以正常赋值，但是无法触发UI刷新

getTarget可以获取状态管理框架代理前的原始对象。

makeObserved封装的观察对象，可以通过getTarget获取到其原始对象，对原始对象的赋值不会触发UI刷新。

如下面例子：

先点击第一个Text组件，通过getTarget获取其原始对象，此时修改原始对象的属性不会触发UI刷新，但数据会正常赋值。
再点击第二个Text组件，此时修改this.observedObj的属性会触发UI刷新，Text显示21。
import { UIUtils } from '@kit.ArkUI';
class Info {
  public id: number = 0;
}


@Entry
@Component
struct Page10 {
  observedObj: Info = UIUtils.makeObserved(new Info());
  build() {
    Column() {
      Text(`${this.observedObj.id}`)
        .id('textobservedObj1')
        .fontSize(50)
        .onClick(() => {
          // 通过getTarget获取其原始对象，将this.observedObj赋值为不可观察的数据
          let rawObj: Info= UIUtils.getTarget(this.observedObj);
          // 不会触发UI刷新，但数据会正常赋值
          rawObj.id = 20;
        })


      Text(`${this.observedObj.id}`)
        .id('textobservedObj2')
        .fontSize(50)
        .onClick(() => {
          // 触发UI刷新，Text显示21
          this.observedObj.id++;
        })
    }
  }
}
getTarget接口：获取状态管理框架代理前的原始对象
canBeObserved接口：判断对象是否可被观察
