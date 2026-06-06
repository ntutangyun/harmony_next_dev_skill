# @Once：初始化同步一次

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once_

@Local @Once onceLocal: string = 'onceLocal'; // 错误用法，@Once不能与@Local一起使用
// ···
}
@Component
struct Index {
  @Once @Param onceParam: string = 'onceParam'; // 错误用法
}
MyComponent.ets

@Once与@Param的先后顺序无关，可以写成@Param @Once也可以写成@Once @Param。

@ComponentV2
struct MyComponent {
// ···
  @Param @Once param1: number = 0;
  @Once @Param param2: number = 0;
// ···
}
MyComponent.ets
使用场景
变量仅初始化同步一次

@Once用于期望变量仅初始化同步数据源一次，之后不再继续同步变化的场景。

@ComponentV2
struct ChildComponent {
  // @Once装饰的onceParam仅初始化同步一次
  @Param @Once onceParam: string = '';


  build() {
    Column() {
      Text(`onceParam: ${this.onceParam}`)
    }
  }
}


@Entry
@ComponentV2
struct MyComponent {
  // ...
  @Local message: string = 'Hello World';


  build() {
    Column() {
      Text(`Parent message: ${this.message}`)
      Button('change message')
        .onClick(() => {
          this.message = 'Hello Tomorrow';
        })
      ChildComponent({ onceParam: this.message })
    }
  }
}
MyComponent.ets
本地修改@Param变量

当@Once与@Param结合使用时，可以解除@Param无法在本地修改的限制，并能够触发UI刷新。此时，使用@Param和@Once的效果类似于@Local，但@Param和@Once还能接收外部传入的初始值。

@ObservedV2
class Info {
  @Trace name: string;
  constructor(name: string) {
    this.name = name;
  }
}
@ComponentV2
struct Child {
  // @Once与@Param结合使用时，可以在本地修改，并能够触发UI刷新
  @Param @Once onceParamNum: number = 0;
  @Param @Once @Require onceParamInfo: Info;


  build() {
    Column() {
      Text(`Child onceParamNum: ${this.onceParamNum}`)
      Text(`Child onceParamInfo: ${this.onceParamInfo.name}`)
      Button('changeOnceParamNum')
        .onClick(() => {
          this.onceParamNum++;
        })
      Button('changeParamInfo')
        .onClick(() => {
          this.onceParamInfo = new Info('Cindy');
        })
    }
  }
}
@Entry
@ComponentV2
struct Index {
  @Local localNum: number = 10;
  @Local localInfo: Info = new Info('Tom');


  build() {
    Column() {
      Text(`Parent localNum: ${this.localNum}`)
      Text(`Parent localInfo: ${this.localInfo.name}`)
      Button('changeLocalNum')
        .onClick(() => {
          this.localNum++;
        })
      Button('changeLocalInfo')
        .onClick(() => {
          this.localInfo = new Info('Cindy');
        })
      Child({
        onceParamNum: this.localNum,
        onceParamInfo: this.localInfo
      })
    }
  }
}
Index.ets
@Param：组件外部输入
@Event装饰器：规范组件输出
