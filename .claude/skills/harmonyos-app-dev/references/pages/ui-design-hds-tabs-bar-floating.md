# 设置页签栏的悬浮样式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-tabs-bar-floating_

布局位置：设置barPosition为BarPosition.End且vertical为false，使页签栏置于容器底部。
层级叠加：设置barOverlap为true，使TabBar悬浮于TabContent。
样式限制，当前仅支持以下样式配置：
BottomTabBarStyle（底部标签栏样式）
CustomBuilder（自定义构建器）
开发步骤
导入相关模块。
 // 从6.0.2(22)版本开始，无需手动导入HdsTabsAttribute。具体请参考HdsTabs的导入模块说明。
 import { HdsTabs, HdsTabsAttribute, HdsTabsController, hdsMaterial } from '@kit.UIDesignKit';
创建Hds一级容器组件，设置HdsTabs组件的barFloatingStyle样式，并设置barOverlap为true，vertical为false，barPosition为BarPosition.End，可实现页签栏的悬浮样式。若在barFloatingStyle中设置miniBar，则可实现迷你栏。
@Entry
@Component
struct Index {
  // 初始化HdsTabs控制器。
  private controller: HdsTabsController = new HdsTabsController();


  @Builder
  miniBarBuilder() {
    Row() {
      Column() {
        Image($r('app.media.alarm_stop'))
          .width(40)
          .height(40)
          .borderRadius(40)
      }.width(48).height(48).justifyContent(FlexAlign.Center).margin({left: 4, right: 4})


      Text('Hello')


      Column() {
        Image($r('sys.media.ohos_ic_public_pause'))
          .width(40)
          .height(40)
          .borderRadius(40)
      }.width(48).height(48).justifyContent(FlexAlign.Center)
    }
  }


  build() {
    Column() {
      HdsTabs({ controller: this.controller }) {
        TabContent() {
          Scroll() {
            Column(){
              Image($r('app.media.ocean'))
              Image($r('app.media.desert'))
              Image($r('app.media.mountain'))
              Image($r('app.media.sunset'))
            }
          }
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Green'))


        TabContent() {
          Image($r('app.media.ocean'))
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.wifi_router_fill'), 'Blue'))


        TabContent() {
          Image($r('app.media.ocean'))
        }
        .tabBar(new BottomTabBarStyle($r('sys.media.ohos_ic_public_clock'), 'Yellow'))
      }
      // 设置barOverlap为true，vertical为false，barPosition为BarPosition.End
      .barOverlap(true)
      .barPosition(BarPosition.End)
      .vertical(false)
      // 设置页签栏悬浮样式。
      .barFloatingStyle({
        barWidth: { smallWidth: 200, mediumWidth: 300, largeWidth: 400 },
        barBottomMargin: 28,
        gradientMask: { maskColor: '#66F1F3F5', maskHeight: 92 },
        systemMaterialEffect: {
          materialType: hdsMaterial.MaterialType.IMMERSIVE,
          materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
        },
        // 设置迷你栏，若不设置，则仅有页签栏。
        miniBar: {
          miniBarBuilder: () => this.miniBarBuilder()
        }
      })
    }
  }
}
设置侧边栏半屏居中对齐样式
即时操作
