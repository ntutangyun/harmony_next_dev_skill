# 高精几何重建（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-volume-measurement_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从6.0.0(20)开始，高精几何重建能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持高精几何重建特性（ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE）。

接口说明

以下接口为AREngine高精几何重建相关接口，详细接口和说明，请参考AR Engine API参考。

接口名	描述
HMS_AREngine_ARFrame_AcquireSemanticDenseData	获取当前帧的高精几何重建对象数据。
HMS_AREngine_ARConfig_GetSemanticDenseMode	获取已设置的高精几何重建模式。
HMS_AREngine_ARConfig_SetSemanticDenseMode	设置当前所需的高精几何重建模式。
HMS_AREngine_ARSemanticDense_AcquireCubeData	获取识别到的高精几何重建对象数据中的立方体数据。
HMS_AREngine_ARSemanticDense_AcquireCubeDataSize	获取识别到的高精几何重建对象数据中的立方体数量。
HMS_AREngine_ARSemanticDense_Release	释放高精几何重建对象。

开发步骤

[h2]声明Native接口

开发者可参考AR物体摆放章节的声明Native接口。

[h2]创建UI界面

首先创建一个UI界面ARSemanticDense.ets，用于选择高精几何重建相关模式。

import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense();
}

@Component
struct ARSemanticDense {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {
    NavDestination() {
      Column() {
        Button($r('app.string.semantic_dense_normal'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 0).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 0. Code is ${err.code}, message is ${err.message}.`);
            });
          })

        Button($r('app.string.semantic_dense_cube_volume'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 1).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 1. Code is ${err.code}, message is ${err.message}.`);
            })
          })

        Button($r('app.string.semantic_dense_cube_space'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 2).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 2. Code is ${err.code}, message is ${err.message}.`);
            })
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

最后创建一个ARSemanticDenseRender.ets，使用XComponent组件用于加载相机预览画面，并定时触发每一帧绘制。

import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseRenderBuilder() {
  ARSemanticDenseRender();
}

@Component
struct ARSemanticDenseRender {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  private xComponentId: string = 'ARSemanticDense';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private interval: number = -1;
  private inputInterval: number = -1;
  private getCubeInfoInterval: number = -1;
  private isUpdate: boolean = false;
  private semanticDenseMode: number = 0;
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build(): void {
    NavDestination() {
      RelativeContainer() {

        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .opacity(0.2)
          .width('100%')
          .height('100%')
          .zIndex(0.1)
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
                if (this.semanticDenseMode != 0) {
                  this.volume = arEngineDemo.getVolume(this.idStr);
                }
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            if (this.interval !== -1) {
              clearInterval(this.interval);
              this.interval = -1;
            }

            if (this.inputInterval !== -1) {
              clearInterval(this.inputInterval);
              this.inputInterval = -1;
            }

            if (this.getCubeInfoInterval !== -1) {
              clearInterval(this.getCubeInfoInterval);
              this.getCubeInfoInterval = -1;
            }
          })

        Text(this.volume)
          .fontColor(Color.Red)
          .fontSize(14)
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation, 2, this.semanticDenseMode]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(async () => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.semanticDenseMode = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

[h2]引入AR Engine

开发者可参考AR物体摆放章节的引入AR Engine。

[h2]创建AR会话并配置高精几何重建相关模式

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
SetSemanticDenseMode(params.semanticDenseMode, mArSession, arConfig);
AREngine_ARSemanticDenseMode outSemanticDenseMode = ARENGINE_SEMANTIC_DENSE_MODE_DISABLED;
HMS_AREngine_ARConfig_GetSemanticDenseMode(mArSession, arConfig, &outSemanticDenseMode);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));

[h2]获取当前环境中的高精几何重建信息

创建一个帧对象，调用HMS_AREngine_ARFrame_AcquireSemanticDenseData函数，从当前帧中获取环境中的高精几何重建信息，其中包含了环境中的稠密点云信息和立方体信息。

AREngine_ARSemanticDenseData *arSemanticDense = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireSemanticDenseData(arSession, arFrame, &arSemanticDense);

[h2]获取高精几何重建信息中的立方体数据

调用HMS_AREngine_ARSemanticDense_AcquireCubeData函数，获取当前环境中的立方体数据，立方体的数据结构详情参考AREngine_ARSemanticDenseCubeData。

HMS_AREngine_ARSemanticDense_AcquireCubeData(arSession, arSemanticDense, &semanticDenseCubeData);

调用HMS_AREngine_ARSemanticDense_AcquireCubeDataSize函数，获取当前环境中的立方体数量，如果立方体数量大于0，即可从中获取单个立方体的数据进行绘制和体积计算。

HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(arSession, arSemanticDense, &cubeDataSize);

[h2]绘制相关几何信息

通过获取到的AREngine_ARSemanticDenseCubeData对象来绘制立方体。

if (semanticDenseCubeData != nullptr && cubeDataSize > 0) {
    mCubeRenderer.Draw(projectionMat, viewMat, semanticDenseCubeData);
}

## Code blocks

### Code block 1

```
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense();
}

@Component
struct ARSemanticDense {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {
    NavDestination() {
      Column() {
        Button($r('app.string.semantic_dense_normal'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 0).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 0. Code is ${err.code}, message is ${err.message}.`);
            });
          })

        Button($r('app.string.semantic_dense_cube_volume'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 1).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 1. Code is ${err.code}, message is ${err.message}.`);
            })
          })

        Button($r('app.string.semantic_dense_cube_space'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 2).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 2. Code is ${err.code}, message is ${err.message}.`);
            })
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### Code block 2

```
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseRenderBuilder() {
  ARSemanticDenseRender();
}

@Component
struct ARSemanticDenseRender {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  private xComponentId: string = 'ARSemanticDense';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private interval: number = -1;
  private inputInterval: number = -1;
  private getCubeInfoInterval: number = -1;
  private isUpdate: boolean = false;
  private semanticDenseMode: number = 0;
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build(): void {
    NavDestination() {
      RelativeContainer() {

        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .opacity(0.2)
          .width('100%')
          .height('100%')
          .zIndex(0.1)
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
                if (this.semanticDenseMode != 0) {
                  this.volume = arEngineDemo.getVolume(this.idStr);
                }
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            if (this.interval !== -1) {
              clearInterval(this.interval);
              this.interval = -1;
            }

            if (this.inputInterval !== -1) {
              clearInterval(this.inputInterval);
              this.inputInterval = -1;
            }

            if (this.getCubeInfoInterval !== -1) {
              clearInterval(this.getCubeInfoInterval);
              this.getCubeInfoInterval = -1;
            }
          })

        Text(this.volume)
          .fontColor(Color.Red)
          .fontSize(14)
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation, 2, this.semanticDenseMode]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(async () => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.semanticDenseMode = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### Code block 3

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
SetSemanticDenseMode(params.semanticDenseMode, mArSession, arConfig);
AREngine_ARSemanticDenseMode outSemanticDenseMode = ARENGINE_SEMANTIC_DENSE_MODE_DISABLED;
HMS_AREngine_ARConfig_GetSemanticDenseMode(mArSession, arConfig, &outSemanticDenseMode);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### Code block 4

```
AREngine_ARSemanticDenseData *arSemanticDense = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireSemanticDenseData(arSession, arFrame, &arSemanticDense);
```

### Code block 5

```
HMS_AREngine_ARSemanticDense_AcquireCubeData(arSession, arSemanticDense, &semanticDenseCubeData);
```

### Code block 6

```
HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(arSession, arSemanticDense, &cubeDataSize);
```

### Code block 7

```
if (semanticDenseCubeData != nullptr && cubeDataSize > 0) {
    mCubeRenderer.Draw(projectionMat, viewMat, semanticDenseCubeData);
}
```
