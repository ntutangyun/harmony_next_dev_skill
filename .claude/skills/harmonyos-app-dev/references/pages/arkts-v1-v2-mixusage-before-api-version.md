# 状态管理V1和V2混用指导（API version 19前）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage-before-api-version_

--------- V1桥接组件 ------------
      V1BridgeComponent()


      // ....


    }
  }
}


// V1桥接组件
@Component
struct V1BridgeComponent {
  @State @Watch('onDirectionChange') viewModel: ViewModelV1 = new ViewModelV1(20);


  onDirectionChange() {
    // 将V1的数据转成V2的数据
    ViewModelV2.instance().fontSize = this.viewModel.fontSize;
  }


  build() {
    Column() {
      Text(`V1组件原始数据fontSize-${this.viewModel.fontSize}`)
        .fontSize(this.viewModel.fontSize)


      Button('V1组件修改字体大小').onClick(() => {
        this.viewModel.updateFontSize(10); // V1 V2组件刷新
      })


      // ------------ V2业务组件 ------------
      V2Comp()
    }
  }
}


@ObservedV2
class ViewModelV2 {
  // 单例实例
  private static singleton_: ViewModelV2;
  @Trace public fontSize: number = 40;


  // 私有构造函数（禁止外部new）
  private constructor() {
  }


  static instance(): ViewModelV2 {
    if (!ViewModelV2.singleton_) {
      ViewModelV2.singleton_ = new ViewModelV2();
    }
    return ViewModelV2.singleton_;
  }
}


// 新增V2业务组件
@ComponentV2
struct V2Comp {
  // 获取V2单例实例（组件内可直接访问）
  private v2Model = ViewModelV2.instance();


  build() {
    Column() {
      Text(`V2组件fontSize-${this.v2Model.fontSize}`)
        .fontSize(this.v2Model.fontSize)


      Button('V2组件修改字体大小')
        .onClick(() => {
          this.v2Model.fontSize = 60; // V2组件刷新
        })
    }
  }
}
V1ToV2_ObservedClass.ets

@ObservedV2装饰的class

@ObservedV2+@Trace的观测能力在V1和V2版本中均受支持，但在V1中不支持将V1装饰器与@ObservedV2装饰的实例对象共同使用。以下示例代码中，若info对象被@State修饰，则会导致编译错误，需移除V1的装饰器。

@ObservedV2
class InfoTen {
  @Trace public myId: number;
  public name: string;


  constructor(myId?: number, name?: string) {
    this.myId = myId || 0;
    this.name = name || 'aaa';
  }
}


@ComponentV2
struct ChildTen {
  // V2对数据输入有严格的管理，从父组件传入数据时，必须使用@Param装饰器进行数据接收
  @Param info: InfoTen = new InfoTen();


  build() {
    Column() {
      Text(`Child-V2 info id:${this.info.myId}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.info.myId++; // 刷新
        })
    }
  }
}


@Entry
@Component
struct IndexTen {
  // @State info: InfoTen = new InfoTen(); // 错误写法。Class类型，不支持传递，编译器报错；消除编译错误请去掉@State
  info: InfoTen = new InfoTen(); // 正确写法


  build() {
    Column() {
      Text(`Parent-V1 info id:${this.info.myId}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.info.myId++; // 刷新
        })


      ChildTen({
        info: this.info,
      })
    }
    .height('100%')
    .width('100%')
  }
}
V1ToV2_ObservedV2AndTrace.ets
传递嵌套对象

V1装饰器的观测能力是对数据本身做代理，因此当数据存在嵌套时，V1只能通过@Observed+@ObjectLink的方式拆分子组件，观测深层次数据。但V2无法接收@Observed装饰的对象，@ObjectLink也无法在V2中使用。@Observed并没有@ObservedV2+@Trace那样强大的深层次观测能力，这里不再对@Observed的深层次嵌套进行讨论，只讨论@ObservedV2在V1的使用场景。

@Observed装饰的class嵌套@ObservedV2装饰的class

@ObservedV2和@Observed嵌套使用时，类对象能否被V1的装饰器装饰取决于最外层class使用的装饰器。如果最外层是@Observed修饰的类，可以和V2装饰器一起使用，比如@State。@State仅能观察第一层的变化，如果要深度观察，需要传递给@ObjectLink。

以下示例代码中：

最外层MessageInfoNested1类被@Observed修饰，在V1组件IndexOne中可以被@State修饰。数据源@State的第二层的改变（info和messageId属性），虽不能触发本层的刷新，但会被@ObjectLink和@Param观察到，并触发它们关联组件的刷新。
messageInfo属性传递给V1组件，V1组件ChildOne要用@ObjectLink接收，而传递给V2组件GrandSon1的info属性的class类用@ObservedV2修饰。
@Track防止MessageInfo1类中的info因messageId改变而连带刷新，开发者去掉@Track可观测到，当messageId改变时，info的连带刷新，但这并非@ObjectLink的观测能力。
@ObservedV2
class InfoOne {
  @Trace public myId: number;
  public name: string;


  constructor(myId?: number, name?: string) {
    this.myId = myId || 0;
    this.name = name || 'aaa';
  }
}


@Observed
class MessageInfo1 { // 一层嵌套
  @Track public info: InfoOne; // 防止messageId改变导致info的连带刷新
  @Track public messageId: number; // 防止messageId改变导致info的连带刷新


  constructor(info?: InfoOne, messageId?: number) {
    this.info = info || new InfoOne();
    this.messageId = messageId || 0;
  }
}


@Observed
class MessageInfoNested1 { // 二层嵌套
  public messageInfo: MessageInfo1;


  constructor(messageInfo?: MessageInfo1) {
    this.messageInfo = messageInfo || new MessageInfo1();
  }
}


@ComponentV2
struct GrandSon1 {
  @Param info: InfoOne = new InfoOne();


  build() {
    Column() {
      Text(`ObjectLink info info.myId:${this.info.myId}`) // myId属性被@Trace装饰，可以观测变化
        .fontSize(30)
        .onClick(() => {
          this.info.myId++; // 当前组件和父组件ChildOne都刷新
        })
    }
  }
}


@Component
struct ChildOne {
  @ObjectLink messageInfo: MessageInfo1;


  build() {
    Column() {
      Text(`ObjectLink MessageInfo messageId:${this.messageInfo.messageId}`) // 经过@ObjectLink拆解之后，可以观测一层类属性变化
        .fontSize(30)
        .onClick(() => {
          this.messageInfo.messageId++; // 当前组件UI刷新
        })
      Divider()
        .color(Color.Blue)
      Text(`ObjectLink MessageInfo info.myId:${this.messageInfo.info.myId}`) // myId属性被@Trace装饰，可以观测变化
        .fontSize(30)
        .onClick(() => {
          this.messageInfo.info.myId++; // 当前组件和GrandSon1子组件的UI都刷新
        })
      GrandSon1({ info: this.messageInfo.info }); // 继续拆解一层子组件
    }
  }
}


@Entry
@Component
struct IndexOne {
  @State messageInfoNested: MessageInfoNested1 = new MessageInfoNested1(); // 三层嵌套的数据，如何观测内部。


  build() {
    Column() {
      // 观察messageInfoNested，@State只有一层观测能力，无法观察到变化
      Text(`messageInfoNested messageId:${this.messageInfoNested.messageInfo.messageId}`)
        .fontSize(30)
        .onClick(() => {
          this.messageInfoNested.messageInfo.messageId++; // 当前组件不刷新，子组件ChildOne的UI刷新
        })
      Divider()
        .color(Color.Blue)
      // 通过@ObjectLink嵌套观察 messageInfoId
      ChildOne({ messageInfo: this.messageInfoNested.messageInfo }) // 经过拆分后，使用@ObjectLink拆分可以观察到深一层的变化
      Divider()
        .color(Color.Blue)
    }
    .height('100%')
    .width('100%')
    .margin(10)
  }
}
ObserveNestedClasses_ObservedAndObjectLink.ets

@ObservedV2+@Trace观察class嵌套类

@ObservedV2+@Trace将观测能力实现在类属性上，所以当类属性被@Trace标记时，无论嵌套多少层，均能观测到变化。以下示例代码中，MessageInfoNested对象及其属性均被@ObservedV2修饰，在V1组件Index中使用时，不能和V1装饰器一起使用。将messageInfo属性从V1组件传递给V2组件，V2组件Child通过@Param接收，且修改能被观测。

@ObservedV2
class Info {
  @Trace public myId: number;
  public name: string;


  constructor(myId?: number, name?: string) {
    this.myId = myId || 0;
    this.name = name || 'aaa';
  }
}


@ObservedV2
class MessageInfo { // 一层嵌套
  @Trace public info: Info; // 防止messageId改变导致info的连带刷新
  @Trace public messageId: number; // 防止info改变导致messageId的连带刷新


  constructor(info?: Info, messageId?: number) {
    this.info = info || new Info(); // 使用传入的info或创建一个新的Info
    this.messageId = messageId || 0;
  }
}


@ObservedV2
class MessageInfoNested { // 二层嵌套，MessageInfoNested如果是被@ObservedV2装饰，则不可以被V1的状态变量更新相关的装饰器装饰，如@State
  public messageInfo: MessageInfo;


  constructor(messageInfo?: MessageInfo) {
    this.messageInfo = messageInfo || new MessageInfo();
  }
}


@ComponentV2
struct Child {
  @Param messageInfo: MessageInfo =  new MessageInfo();


  build() {
    Column() {
      Text(`Child MessageInfo messageId:${this.messageInfo.messageId}`)
        .fontSize(30)
        .onClick(() => {
          this.messageInfo.messageId++; // 刷新
        })
    }
  }
}


@Entry
@Component
struct Index {
  messageInfoNested: MessageInfoNested = new MessageInfoNested(); // 三层嵌套的数据，如何观测内部。


  build() {
    Column() {
      Text(`messageInfoNested messageId:${this.messageInfoNested.messageInfo.messageId}`)
        .fontSize(30)
        .onClick(() => {
          this.messageInfoNested.messageInfo.messageId++;
        })
      Divider()
        .color(Color.Blue)
      Text(`messageInfoNested name:${this.messageInfoNested.messageInfo.info.name}`) // 未被@Trace修饰，无法观测
        .fontSize(30)
        .onClick(() => {
          this.messageInfoNested.messageInfo.info.name += 'a';
        })
      Divider()
        .color(Color.Blue)
      Text(`messageInfoNested myId:${this.messageInfoNested.messageInfo.info.myId}`) // 被@Trace修饰，无论嵌套多少层都能观测
        .fontSize(30)
        .onClick(() => {
          this.messageInfoNested.messageInfo.info.myId++;
        })
      Divider()
        .color(Color.Blue)
      // 通过@ObservedV2和@Trace观察messageInfo
      Child({messageInfo: this.messageInfoNested.messageInfo})
    }
    .height('100%')
    .width('100%')
    .margin(10)
  }
}
ObserveNestedClasses_ObsevedV2AndTrace.ets
V2组件使用V1组件

V2的状态变量传递给V1的自定义组件，存在以下限制：

V1可以不使用装饰器接收数据。V1自定义组件中，不使用装饰器接收的变量被视为普通变量。

V1使用装饰器接收数据时，仅可通过@State、@Prop、@Provide接收。

V1使用装饰器接收数据时，不支持内置类型的数据，否则编译报错。

传递简单类型状态变量

V2向V1自定义组件传递简单类型状态变量时，V1仅能通过@State、@Prop、@Provide装饰器接收数据。以下示例代码中，ThirdPartyComp组件模拟第三方库，接收来自V2组件的布尔值。

// 模拟三方库导入的V1组件
@Component
struct ThirdPartyComp {
  // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
  @State prop: boolean = true; // 可以观测到变化


  build() {
    Column() {
      Text(`ThirdPartyComp：${this.prop}`)
    }
  }
}


@Entry
@ComponentV2
struct V2Comp2 {
  @Local param: boolean = false;


  build() {
    Column() {
      Text(`V2Comp2：${this.param}`)


      // V2组件向V1的三方库传递简单状态变量
      ThirdPartyComp({ prop: this.param })
    }
  }
}
V2ToV1_SimpleData.ets
传递class类型

定义普通class

V2向V1自定义组件传递数据时，支持普通class类。在以下示例代码中，InfoFive类未被@ObservedV2修饰，传递给V1组件ChildFive时，可以使用@State接收。修改V1组件中的info变量，依赖@State的观测能力刷新UI。

class InfoFive {
  public myId: number;
  public name: string;


  constructor(myId?: number, name?: string) {
    this.myId = myId || 0;
    this.name = name || 'aaa';
  }
}


@Component
struct ChildFive {
  // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
  @State info: InfoFive = new InfoFive(); // 可以观测一层类属性变化


  build() {
    Column() {
      Text(`info id:${this.info.myId}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.info.myId++; // 当前组件UI刷新
        })
    }
  }
}


@Entry
@ComponentV2
struct IndexFive {
  @Provider() info: InfoFive = new InfoFive(); // Class类型，支持传递


  build() {
    Column() {
      ChildFive({
        info: this.info,
      })
    }
    .height('100%')
    .width('100%')
  }
}
V2CommonVariablesToV1CustomComponent.ets

定义@ObserveV2修饰的class

V1装饰器不能和@ObservedV2一起使用。在以下示例代码中，InfoNine类被@observedV2装饰，V1组件接收变量时，info变量不能被V1装饰器修饰，但通过修改可以刷新UI，依赖的是@ObservedV2+@Trace的观测能力。

@ObservedV2
class InfoNine {
  @Trace public myId: number;
  public name: string;


  constructor(myId?: number, name?: string) {
    this.myId = myId || 0;
    this.name = name || 'aaa';
  }
}


@Component
struct ChildNine {
  info: InfoNine = new InfoNine(); // V1装饰器不能和@ObservedV2一起使用


  build() {
    Column() {
      Text(`info id:${this.info.myId}`) // 显示info.myId变量
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.info.myId++; // 当前组件UI刷新,依赖@ObservedV2+@Trace的能力
        })
    }
  }
}


@Entry
@ComponentV2
struct IndexNine {
  @Provider() info: InfoNine = new InfoNine();


  build() {
    Column() {
      ChildNine({
        info: this.info,
      })
    }
    .height('100%')
    .width('100%')
  }
}
V2ToV1_ObservedV2AndTrace.ets
传递普通内置类型

V2->V1传递内置类型，V2定义内置类型的装饰器和V1接收内置类型的装饰器是互斥的。

V1使用装饰器接收数据时，内置类型不支持在V2中用装饰器修饰。
V1可以不使用装饰器接收数据，接收过来的变量在V1定义组件内也会是普通变量，在V2中可以用装饰器修饰。

在以下示例代码中，V2向V1自定义组件传递set变量，V1组件使用@Provide接收。因此，在V2组件IndexEight中定义set变量时，为避免编译错误，set变量不能用@Local修饰。

@Component
struct ChildEight {
  // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
  @Provide set: Set<number> = new Set();


  build() {
    Column() {
      ForEach(Array.from(this.set.values()), (item: number) => { // 显示set变量
        Text(`${item}`)
          .fontSize(30)
      })
    }
  }
}


@Entry
@ComponentV2
struct IndexEight {
  // @Local set: Set<number> = new Set([10, 20]); // 错误写法。内置类型状态变量，不支持传递；消除编译错误请去掉@Local
  set: Set<number> = new Set([10, 20]); // 正确写法。


  build() {
    Column() {
      ChildEight({
        set: this.set
      })
    }
    .height('100%')
    .width('100%')
  }
}
V2ToV1_CommonBuildInClass.ets
混用场景总结

对V1和V2混用场景进行梳理后，可以总结出：

当V1中混用V2自定义组件时（即V1的组件或者类数据向V2传递），大部分V1的能力在V2都是被禁止的。

当V2中混用V1自定义组件时（即V2的组件或者类数据向V1传递），做了部分功能开放。例如：@ObservedV2和@Trace，这也是对V1嵌套类数据的观测能提供的最大的帮助。

所以在代码开发过程中，不建议开发者混用V1和V2版本。然而，在代码迁移方面，V1的开发者可以逐步将代码迁移到V2，以稳步替换V1的功能代码。同时，不建议在V2的代码架构中混用V1的代码。

状态管理V1和V2混用场景
状态管理V1和V2混用指导（API version 19及之后）
