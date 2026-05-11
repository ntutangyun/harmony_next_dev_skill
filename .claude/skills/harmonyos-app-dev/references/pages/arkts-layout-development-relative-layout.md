# 相对布局 (RelativeContainer)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-relative-layout_

> 组件B --> 锚点2，即A具有left锚点，B具有right锚点，同时A的right锚点与B的HorizontalAlign.Start对齐，B的left锚点与A的HorizontalAlign.End对齐。

链的方向和格式在链头组件的chainMode接口中声明；链内元素的bias属性全部失效，链头元素的bias属性作为整个链的bias生效。链头是指在满足成链规则时链的第一个组件（在水平方向上，从左边开始，镜像语言中从右边开始；在垂直方向上，从上边开始）。
如果链内所有元素的size超出链的锚点约束，超出部分将被均匀分配到链的两侧。在PACKED链中，可以通过Bias设置超出部分的分布。

在以下示例代码中，通过alignRules和chainMode将九个在容器内的Row组件分为三组水平链式排列。组件row1、组件row2和组件row3顶部对齐，水平方向成SPREAD链，链内组件在锚点间均匀分布。组件row4、组件row5、组件row6垂直方向基于容器居中，水平方向成SPREAD_INSIDE链，链内除首尾2个组件对齐锚点外，其他组件在链中均匀分布。组件row7、组件row8、组件row9底部对齐，水平方向组成PACKED链，链内组件无间隙。

@Entry
@Component
struct RelativeChainModeExample {
  build() {
    Row() {
      RelativeContainer() {
        Row() {
          Text('row1')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row2', align: HorizontalAlign.Start },
          top: { anchor: '__container__', align: VerticalAlign.Top }
        })
        .id('row1')
        .chainMode(Axis.Horizontal, ChainStyle.SPREAD)


        Row() {
          Text('row2')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row1', align: HorizontalAlign.End },
          right: { anchor: 'row3', align: HorizontalAlign.Start },
          top: { anchor: 'row1', align: VerticalAlign.Top }
        })
        .id('row2')


        Row() {
          Text('row3')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row2', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row1', align: VerticalAlign.Top }
        })
        .id('row3')


        Row() {
          Text('row4')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row5', align: HorizontalAlign.Start },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })
        .id('row4')
        .chainMode(Axis.Horizontal, ChainStyle.SPREAD_INSIDE)


        Row() {
          Text('row5')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row4', align: HorizontalAlign.End },
          right: { anchor: 'row6', align: HorizontalAlign.Start },
          top: { anchor: 'row4', align: VerticalAlign.Top }
        })
        .id('row5')


        Row() {
          Text('row6')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row5', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row4', align: VerticalAlign.Top }
        })
        .id('row6')


        Row() {
          Text('row7')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#a3cf62')
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          right: { anchor: 'row8', align: HorizontalAlign.Start },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        })
        .id('row7')
        .chainMode(Axis.Horizontal, ChainStyle.PACKED)


        Row() {
          Text('row8')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#00ae9d')
        .alignRules({
          left: { anchor: 'row7', align: HorizontalAlign.End },
          right: { anchor: 'row9', align: HorizontalAlign.Start },
          top: { anchor: 'row7', align: VerticalAlign.Top }
        })
        .id('row8')


        Row() {
          Text('row9')
        }
        .justifyContent(FlexAlign.Center)
        .width(80)
        .height(80)
        .backgroundColor('#0a59f7')
        .alignRules({
          left: { anchor: 'row8', align: HorizontalAlign.End },
          right: { anchor: '__container__', align: HorizontalAlign.End },
          top: { anchor: 'row7', align: VerticalAlign.Top }
        })
        .id('row9')
      }
      .width(300).height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%')
  }
}
RelativeContainerMultipleComponentsChainMode.ets

使用辅助线辅助定位子组件

辅助线（guideLine）是在容器内虚拟出的额外水平或垂直锚点，便于统一对齐到特定偏移位置，从而避免为每个组件单独编写重复的偏移设置。

辅助线分为垂直（Vertical）和水平（Horizontal）两种：垂直辅助线通过start和end属性指定其距离容器左侧和右侧的距离；水平辅助线通过start和end属性指定其距离容器顶部和底部的距离。

如果同时设置了start和end，当两者规则冲突时，仅start属性生效。
若容器在某个方向的尺寸被声明为"auto"，则该方向上的guideLine位置只能使用start属性声明（不允许使用百分比）。

在以下示例代码中，定义了一条垂直辅助线guideline1，距离容器左侧50vp，以及另一条水平辅助线guideline2，距离容器顶部50vp。组件row1通过这两条辅助线来定位自身位置，无需设置bias。

@Entry
@Component
struct RelativeGuideLineExample {
  build() {
    Row() {
      RelativeContainer() {
        Row()
          .width(100)
          .height(100)
          .backgroundColor('#a3cf62')
          .alignRules({
            left: { anchor: 'guideline1', align: HorizontalAlign.End },
            top: { anchor: 'guideline2', align: VerticalAlign.Top }
          })
          .id('row1')
      }
      .width(300)
      .height(300)
      .margin({ left: 50 })
      .border({ width: 2, color: '#6699FF' })
      .guideLine([{ id: 'guideline1', direction: Axis.Vertical, position: { start: 50 } },
        { id: 'guideline2', direction: Axis.Horizontal, position: { start: 50 } }])
    }
    .height('100%')
  }
}
RelativeContainerComponentGuideLine.ets

多个组件的屏障

屏障（barrier）是容器的一种动态参考边界，它基于一组指定组件的实际位置，计算出它们在特定方向上的公共最远边界。当需要让某个组件参照多个组件的集体边界时使用，例如实现“位于这些组件右侧”或“不与其他任何组件重叠”等效果。

屏障可以有上下左右四个方向。垂直方向（TOP，BOTTOM）的屏障仅能作为组件的水平方向锚点，用作垂直方向锚点时值为0；水平方向（LEFT，RIGHT）的屏障仅能作为组件的垂直方向锚点，用作水平方向锚点时值为0。

与静态的guideline不同，barrier会随参照组件位置变化而自动更新，只需定义实际需要的方向即可。

在下列示例代码中，item1，item2，item3三个组件可以视为由一个隐形的矩形区域包围着，outer1基于这个“隐形区域”的底部边界进行布局，位于该区域的下方；outer2基于这个“隐形区域”的右侧边界进行布局，位于该区域的右侧。

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('item 1')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item1')
        .alignRules({
          top: {
            anchor: '__container__',
            align: VerticalAlign.Top
          },
          left: {
            anchor: '__container__',
            align: HorizontalAlign.Start
          }
        })
      Text('item 2')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item2')
        .alignRules({
          top: {
            anchor: 'item1',
            align: VerticalAlign.Bottom
          },
          left: {
            anchor: 'item1',
            align: HorizontalAlign.End
          }
        })
      Text('item 3')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#a3cf62')
        .id('item3')
        .alignRules({
          bottom: {
            anchor: 'item2',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'item2',
            align: HorizontalAlign.End
          }
        })
      Text('outer 1')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#00ae9d')
        // 定义其位置
        .alignRules({
          top: {
            anchor: 'barrier_bottom',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'barrier_left',
            align: HorizontalAlign.Start
          }
        })


      Text('outer 2')
        .width(80)
        .height(80)
        .textAlign(TextAlign.Center)
        .backgroundColor('#00ae9d')
        // 定义其位置
        .alignRules({
          top: {
            anchor: 'barrier_top',
            align: VerticalAlign.Top
          },
          left: {
            anchor: 'barrier_right',
            align: HorizontalAlign.Start
          }
        })
    }
    .width('100%')
    .padding(10)
    .barrier([
      {
        id: 'barrier_left',
        direction: BarrierDirection.LEFT,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_right',
        direction: BarrierDirection.RIGHT,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_top',
        direction: BarrierDirection.TOP,
        referencedId: ['item1', 'item2', 'item3']
      },
      {
        id: 'barrier_bottom',
        direction: BarrierDirection.BOTTOM,
        referencedId: ['item1', 'item2', 'item3']
      },
    ])
  }
}
RelativeContainerComponentBarrier.ets

弹性布局 (Flex)
栅格布局 (GridRow/GridCol)
