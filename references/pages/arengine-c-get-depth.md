# 获取深度图（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-depth_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.5(17)开始，获取深度估计信息能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持深度估计特性（ARENGINE_FEATURE_TYPE_DEPTH）。

接口说明

以下接口为AR深度估计相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
HMS_AREngine_ARSession_Create	创建一个新的AREngine_ARSession会话。
HMS_AREngine_ARSession_Update	更新AR Engine的计算结果。
HMS_AREngine_ARSession_Configure	配置AREngine_ARSession会话。
HMS_AREngine_ARFrame_Create	创建一个新的AREngine_ARFrame对象，将指针存储到*outFrame中。
HMS_AREngine_ARSession_SetDisplayGeometry	设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。
HMS_AREngine_ARSession_SetCameraGLTexture	设置可用于存储相机预览流数据的OpenGL纹理。
HMS_AREngine_ARSession_GetAllTrackables	获取所有指定类型的可跟踪对象集合。
HMS_AREngine_ARTrackableList_AcquireItem	从可跟踪列表中获取指定index的对象。
HMS_AREngine_ARPlane_GetCenterPose	获取从平面的局部坐标系到世界坐标系转换的位姿信息。
HMS_AREngine_ARFrame_AcquireCamera	获取当前帧的相机参数对象。
HMS_AREngine_ARPose_Create	分配并初始化一个新的位姿对象。
HMS_AREngine_ARCamera_GetPose	获取当前相机对象在AR世界空间中的位姿。
HMS_AREngine_ARConfig_SetDepthMode	设置深度模式。
HMS_AREngine_ARFrame_AcquireDepthImage16Bits	获取当前帧的深度图像。
HMS_AREngine_ARFrame_AcquireDepthConfidenceImage	获取当前帧的深度图像对应的置信度信息。

开发步骤

[h2]声明Native接口

开发者可参考AR物体摆放章节的声明Native接口。

[h2]创建UI界面

首先创建一个UI界面ARDepth.ets，用于选择是否开启深度图渲染模式。

// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepth.ets。
@Builder
export function ARDepthBuilder() {
  ARDepth();
}

@Component
struct ARDepth {
  pageInfo: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button('关闭深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 0); // 0表示关闭渲染
          })

        Button('开启深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 1); // 1表示打开渲染
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

最后创建一个ARDepthRender.ets，使用XComponent组件用于加载相机预览画面，并定时触发每一帧绘制。

// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepthRender.ets。
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARDepthRenderBuilder() {
  ARDepthRender();
}

@Component
struct ARDepthRender {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private isUpdate: boolean = true;
  private params: number = 0;
  private xComponentId = 'ARDepth';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State distance: string = '';
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // 每一帧通过调用AR Engine的Native API update来更新计算结果
                arEngineDemo.update(this.xComponentId);
                this.distance = arEngineDemo.getDistance(this.xComponentId);
              }
            }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })

        Text(this.distance)
          .fontColor(Color.Yellow)
          .fontSize(24)
          .textShadow({
            radius: 10,
            color: Color.Black,
            offsetX: 0,
            offsetY: 0
          })
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([0, this.params, 1, this.rotation]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.params = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

}

配置路由进行页面间跳转，页面路由配置详细可查看组件导航(Navigation) (推荐)。

[h2]引入AR Engine

开发者可参考AR物体摆放章节的引入AR Engine。

[h2]创建AR会话

创建AR会话并配置为开启深度模式。

AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置深度模式为开启状态。
HMS_AREngine_ARConfig_SetDepthMode(arSession, arConfig, ARENGINE_DEPTH_MODE_AUTOMATIC);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);

[h2]获取当前环境中的深度图

调用HMS_AREngine_ARFrame_AcquireDepthImage16Bits函数，获取当前环境中的深度信息，并将结果存放在depthImage中。

AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARImage *depthImage = nullptr;
// 获取深度图
HMS_AREngine_ARFrame_AcquireDepthImage16Bits(arSession, arFrame, &depthImage);

[h2]获取当前深度图对应的深度置信度图

调用HMS_AREngine_ARFrame_AcquireDepthConfidenceImage函数，获取当前深度图对应的置信度图。

AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARImage *depthConfidenceImage = nullptr;
// 获取深度置信度图
HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(arSession, arFrame, &depthConfidenceImage);

[h2]获取深度图和深度置信度图中的值

深度图和深度置信度图包装为AREngine_ARImage对象，可以通过此对象获取对应的深度图和深度置信度图。

AREngine_ARImageFormat format;
// 获取当前帧图像的数据格式
HMS_AREngine_ARImage_GetFormat(arSession, depthImage, &format);
int32_t depthWidth;
// 获取深度图的宽度
HMS_AREngine_ARImage_GetWidth(arSession, depthImage, &depthWidth);
int32_t depthHeight;
// 获取深度图的高度
HMS_AREngine_ARImage_GetHeight(arSession, depthImage, &depthHeight);
uint8_t *depthData = nullptr;
int32_t depthLength = 0;
// 获取深度图的数据
HMS_AREngine_ARImage_GetPlaneData(arSession, depthImage, 0, (const uint8_t **)&depthData, &depthLength);

[h2]使用完毕后，销毁深度图和深度置信度图

HMS_AREngine_ARImage_Release(depthImage);
HMS_AREngine_ARImage_Release(depthConfidenceImage);

## Code blocks

### Code block 1

```
// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepth.ets。
@Builder
export function ARDepthBuilder() {
  ARDepth();
}

@Component
struct ARDepth {
  pageInfo: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button('关闭深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 0); // 0表示关闭渲染
          })

        Button('开启深度图渲染模式', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 1); // 1表示打开渲染
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### Code block 2

```
// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARDepthRender.ets。
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARDepthRenderBuilder() {
  ARDepthRender();
}

@Component
struct ARDepthRender {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private isUpdate: boolean = true;
  private params: number = 0;
  private xComponentId = 'ARDepth';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State distance: string = '';
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // 每一帧通过调用AR Engine的Native API update来更新计算结果
                arEngineDemo.update(this.xComponentId);
                this.distance = arEngineDemo.getDistance(this.xComponentId);
              }
            }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })

        Text(this.distance)
          .fontColor(Color.Yellow)
          .fontSize(24)
          .textShadow({
            radius: 10,
            color: Color.Black,
            offsetX: 0,
            offsetY: 0
          })
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([0, this.params, 1, this.rotation]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.params = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

}
```

### Code block 3

```
AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置深度模式为开启状态。
HMS_AREngine_ARConfig_SetDepthMode(arSession, arConfig, ARENGINE_DEPTH_MODE_AUTOMATIC);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### Code block 4

```
AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARImage *depthImage = nullptr;
// 获取深度图
HMS_AREngine_ARFrame_AcquireDepthImage16Bits(arSession, arFrame, &depthImage);
```

### Code block 5

```
AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARImage *depthConfidenceImage = nullptr;
// 获取深度置信度图
HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(arSession, arFrame, &depthConfidenceImage);
```

### Code block 6

```
AREngine_ARImageFormat format;
// 获取当前帧图像的数据格式
HMS_AREngine_ARImage_GetFormat(arSession, depthImage, &format);
int32_t depthWidth;
// 获取深度图的宽度
HMS_AREngine_ARImage_GetWidth(arSession, depthImage, &depthWidth);
int32_t depthHeight;
// 获取深度图的高度
HMS_AREngine_ARImage_GetHeight(arSession, depthImage, &depthHeight);
uint8_t *depthData = nullptr;
int32_t depthLength = 0;
// 获取深度图的数据
HMS_AREngine_ARImage_GetPlaneData(arSession, depthImage, 0, (const uint8_t **)&depthData, &depthLength);
```

### Code block 7

```
HMS_AREngine_ARImage_Release(depthImage);
HMS_AREngine_ARImage_Release(depthConfidenceImage);
```
