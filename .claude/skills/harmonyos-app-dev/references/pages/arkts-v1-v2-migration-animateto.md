# AnimateTo使用迁移

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-animateto_

由于当前animateTo与V2的刷新机制不兼容，执行动画前的额外修改未生效，实际显示的动画效果如下图所示：绿色矩形从长宽50变为200，字符串从Hello变为Hello ArkUI。

迁移方案
API version 22之前的迁移方案

从API version 22之前，可以使用一个duration为0的animateToImmediately将额外的修改先刷新，再执行原来的动画达成预期的效果。

完整代码如下：

@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';


  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          this.w = 100;
          this.h = 100;
          this.message = 'Hello World';
          animateToImmediately({
            duration: 0
          }, () => {
          })
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
LocalQuestionAnimateToImmediately.ets
API version 22及以后的迁移方案

从API version 22开始，可以使用applySync接口实现预期的显示效果。

原理为使用applySync接口同步刷新闭包函数内的状态变量变化，再执行原来的动画达成预期的效果。

import { UIUtils } from '@kit.ArkUI';


@Entry
@ComponentV2
struct Index {
  @Local w: number = 50; // 宽度
  @Local h: number = 50; // 高度
  @Local message: string = 'Hello';


  build() {
    Column() {
      Button('change size')
        .margin(20)
        .onClick(() => {
          // 在执行动画前，存在额外的修改
          UIUtils.applySync(() => {
            this.w = 100;
            this.h = 100;
            this.message = 'Hello World';
          })
          this.getUIContext().animateTo({
            duration: 1000
          }, () => {
            this.w = 200;
            this.h = 200;
            this.message = 'Hello ArkUI';
          })
        })
      Column() {
        Text(`${this.message}`)
      }
      .backgroundColor('#ff17a98d')
      .width(this.w)
      .height(this.h)
    }
  }
}
LocalQuestionExpectedEffect.ets
内置对象的迁移
状态管理V1和V2混用场景
