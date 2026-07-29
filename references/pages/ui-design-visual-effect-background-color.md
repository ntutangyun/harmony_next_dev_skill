# 按压阴影

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-color_

场景介绍

从6.0.0(20)版本开始，新增支持按压阴影。

通过按压阴影接口可以设置组件的背景色变化效果，一般常用于组件按压交互时的背景色变化场景。

开发步骤

导入模块。

import { hdsEffect } from '@kit.UIDesignKit';

创建按压阴影效果。

@Entry
@Component
struct PressShadowExample {
  @State buttonBlendState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
  @State buttonGradientState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

  build() {
    NavDestination() {
      Column({ space: 50 }) {
        Button('BLEND_WHITE', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.buttonBlendState)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.buttonBlendState = hdsEffect.PressShadowType.BLEND_WHITE;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.buttonBlendState = hdsEffect.PressShadowType.NONE;
            }
          })

        Button('GRADIENT', { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.buttonGradientState)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.buttonGradientState = hdsEffect.PressShadowType.BLEND_GRADIENT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.buttonGradientState = hdsEffect.PressShadowType.NONE;
            }
          })
      }
      .height('70%')
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .height('100%')
    .title('Button example')
    .backgroundColor('#040404')
  }
}

## Code blocks

### Code block 1

```
import { hdsEffect } from '@kit.UIDesignKit';
```

### Code block 2

```
@Entry
@Component
struct PressShadowExample {
  @State buttonBlendState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;
  @State buttonGradientState: hdsEffect.PressShadowType = hdsEffect.PressShadowType.NONE;

  build() {
    NavDestination() {
      Column({ space: 50 }) {
        Button('BLEND_WHITE', { buttonStyle: ButtonStyleMode.EMPHASIZED, role: ButtonRole.ERROR, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.buttonBlendState)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.buttonBlendState = hdsEffect.PressShadowType.BLEND_WHITE;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.buttonBlendState = hdsEffect.PressShadowType.NONE;
            }
          })

        Button('GRADIENT', { buttonStyle: ButtonStyleMode.NORMAL, stateEffect: false })
          .visualEffect(new hdsEffect.HdsEffectBuilder()
            .pressShadow(this.buttonGradientState)
            .buildEffect())
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.buttonGradientState = hdsEffect.PressShadowType.BLEND_GRADIENT;
            } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
              this.buttonGradientState = hdsEffect.PressShadowType.NONE;
            }
          })
      }
      .height('70%')
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .height('100%')
    .title('Button example')
    .backgroundColor('#040404')
  }
}
```
