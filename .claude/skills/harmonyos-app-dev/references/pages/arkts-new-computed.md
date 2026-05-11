# @Computed装饰器：计算属性

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed_

------Computed----------');
    return this.firstName + ' ' + this.lastName + this.age;
  }


  build() {
    Column() {
      Text(this.lastName + ' ' + this.firstName)
      Text(this.lastName + ' ' + this.firstName)
      Divider()
      Text(this.fullName)
      Text(this.fullName)
      Button('changed lastName')
        .onClick(() => {
          this.lastName += 'a';
        })


      Button('changed age')
        .onClick(() => {
          this.age++;  // 无法触发Computed
        })
    }
  }
}
CustomComponentUse.ets

计算属性本身会带来性能开销，在实际应用开发中需要注意：

对于简单的计算逻辑，可以不使用计算属性。
如果计算逻辑在视图中仅使用一次，则不使用计算属性，直接求解。

在@ObservedV2装饰的类中使用计算属性。

点击Button改变lastName，触发@Computed fullName重新计算，且只被计算一次。

import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';


@ObservedV2
class Name {
  @Trace public firstName: string = 'Hua';
  @Trace public lastName: string = 'Li';


  @Computed
  get fullName() {
    hilog.info(DOMAIN, TAG, BUNDLE + '---------Computed----------');
    return this.firstName + ' ' + this.lastName;
  }
}


const name: Name = new Name();


@Entry
@ComponentV2
struct ObservedV2ClassUser {
  name1: Name = name;


  build() {
    Column() {
      Text(this.name1.fullName)
      Text(this.name1.fullName)
      // 点击Button改变lastName，触发fullName重新计算，且只被计算一次
      Button('changed lastName').onClick(() => {
        this.name1.lastName += 'a';
      })
    }
  }
}
ObservedV2ClassUser.ets
@Computed装饰的属性可以被@Monitor监听变化

如何使用计算属性求解fahrenheit和kelvin。示例如下：

点击“-”，celsius-- -> fahrenheit -> kelvin --> kelvin变化时调用onKelvinMonitor。

点击“+”，celsius++ -> fahrenheit -> kelvin --> kelvin变化时调用onKelvinMonitor。

import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';


@Entry
@ComponentV2
struct ComputedPropertyResolution {
  @Local celsius: number = 20;


  @Computed
  get fahrenheit(): number {
    return this.celsius * 9 / 5 + 32; // C -> F
  }


  @Computed
  get kelvin(): number {
    return (this.fahrenheit - 32) * 5 / 9 + 273.15; // F -> K
  }


  @Monitor('kelvin')
  onKelvinMonitor(mon: IMonitor) {
    hilog.info(DOMAIN, TAG, BUNDLE + 'kelvin changed from' + mon.value()?.before + ' to ' + mon.value()?.now);
  }


  build() {
    Column({ space: 20 }) {
      Row({ space: 20 }) {
        Button('-')
          .onClick(() => {
            this.celsius--;
          })


        Text(`Celsius ${this.celsius.toFixed(1)}`).fontSize(40)


        Button('+')
          .onClick(() => {
            this.celsius++;
          })
      }


      Text(`Fahrenheit ${this.fahrenheit.toFixed(2)}`).fontSize(40)
      Text(`Kelvin ${this.kelvin.toFixed(2)}`).fontSize(40)
    }
    .width('100%')
  }
}
ComputingPropertyResolution.ets
@Computed装饰的属性可以初始化@Param

下面的例子使用@Computed初始化@Param。

点击Button('-')和Button('+')改变商品数量，quantity是被@Trace装饰的，其改变时可以被观察到的。

quantity的改变会触发total和qualifiesForDiscount重新计算，计算商品总价和是否可以享有优惠。

total和qualifiesForDiscount的改变会触发子组件Child对应Text组件刷新。

@ObservedV2
class Article {
  @Trace public quantity: number = 0;
  public unitPrice: number = 0;


  constructor(quantity: number, unitPrice: number) {
    this.quantity = quantity;
    this.unitPrice = unitPrice;
  }
}


@Entry
@ComponentV2
struct ComputingInitParam {
  @Local shoppingBasket: Article[] = [new Article(1, 20), new Article(5, 2)];


  @Computed
  get total(): number {
    return this.shoppingBasket.reduce((acc: number, item: Article) => acc + (item.quantity * item.unitPrice), 0);
  }


  @Computed
  get qualifiesForDiscount(): boolean {
    return this.total >= 100;
  }


  build() {
    Column() {
      Text(`Shopping List: `)
        .fontSize(30)
      ForEach(this.shoppingBasket, (item: Article) => {
        Row() {
          Text(`unitPrice: ${item.unitPrice}`)
          // 点击Button减少quantity，触发total和qualifiesForDiscount重新计算
          Button('-')
            .onClick(() => {
              if (item.quantity > 0) {
                item.quantity--;
              }
            })
          Text(`quantity: ${item.quantity}`)
          // 点击Button增加quantity，触发total和qualifiesForDiscount重新计算
          Button('+')
            .onClick(() => {
              item.quantity++;
            })
        }


        Divider()
      })
      Child({ total: this.total, qualifiesForDiscount: this.qualifiesForDiscount })
    }.alignItems(HorizontalAlign.Start)
  }
}


@ComponentV2
struct Child {
  @Param total: number = 0;
  @Param qualifiesForDiscount: boolean = false;


  build() {
    Row() {
      Text(`Total: ${this.total} `)
        .fontSize(30)
      Text(`Discount: ${this.qualifiesForDiscount} `)
        .fontSize(30)
    }
  }
}
ComputedInitParam.ets
@SyncMonitor装饰器：状态变量修改同步监听
@Type装饰器：标记类属性的类型
