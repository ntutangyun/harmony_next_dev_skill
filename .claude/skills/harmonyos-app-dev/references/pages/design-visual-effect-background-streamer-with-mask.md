# 自带背景的双边流光

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/design-visual-effect-background-streamer-with-mask_

通过通用视效组件HdsVisualComponent提供的自带背景的双边流光效果场景接口，支持设置两条边缘流光的起始、终止位置、边缘颜色效果以及与流光相叠加的背景板颜色，用于胶囊组件、屏幕边缘发光等。

开发步骤

导入模块。

// 从6.0.2(22)版本开始，无需手动导入HdsVisualComponentAttribute。具体请参考HdsVisualComponent的导入模块说明。
import {
  HdsVisualComponent,
  HdsVisualComponentAttribute,
  HdsSceneController,
  HdsSceneType
} from '@kit.UIDesignKit';

使用HdsVisualComponent组件，指定场景类型为DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK，并且设置场景参数。

@Entry
@Component
struct EdgeFlowLightVisualComponent {
  @State sceneController: HdsSceneController = new HdsSceneController()
    .setSceneParams({
      backgroundMaskColors: [Color.Green, Color.Red],
      firstEdgeFlowLight: {
        startPos: 0,
        endPos: 0.5,
        color: Color.Red
      },
      secondEdgeFlowLight: {
        startPos: 0,
        endPos: -0.5,
        color: Color.Green
      }
    })


  build() {
    Stack() {
      HdsVisualComponent()
        .scene(HdsSceneType.DUAL_EDGE_FLOW_LIGHT_WITH_BACKGROUND_MASK, this.sceneController, () => {
          console.info('Succeeded in finishing');
        })
        .width('100%')
        .height('50%')
    }
  }
}

背景流光
应用内多窗
