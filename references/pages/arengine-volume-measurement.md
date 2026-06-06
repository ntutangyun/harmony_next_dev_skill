# 高精几何重建（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-volume-measurement_

高精几何重建能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE）。

接口说明

高精几何重建主要依赖ARSemanticDenseData，以下接口为高精几何重建的相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARSession.getFrame	获取AR Engine处理后的一帧数据。
ARFrame.acquireSemanticDense	返回当前帧的高精几何重建对象数据。
ARSemanticDenseData.acquireCubeData	返回一个高精几何重建对象的立方体数据信息的列表。
ARSemanticDenseData.release	释放高精几何重建对象数据。
开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

导入模块

高精几何重建能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
定义变量

定义变量cubeVertexData接收立方体顶点数据，定义变量cubeConfidence接收识别出立方体的置信度数据，定义变量cubeLabel接收立方体的语义信息。

let cubeVertexData: Array<number>;
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;
显示预览流

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

更改semanticDenseMode为ARSemanticDenseMode.CUBE_VOLUME，启用体积测量识别能力。

在设备界面上显示识别到的几何数据信息，使用重复调用函数方法在设备界面上实时更新识别到的几何数据信息。

@Builder
export function ARSemanticDenseBuilder(): void {
  ARSemanticDense();
}


@Component
struct ARSemanticDense {
  @State arContext?: arViewController.ARViewContext = undefined;


  build(): void {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
            .height('100%')
            .width('100%')
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
    })
    .onWillDisappear(() => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }


  private initARView(): void {
    Scene.load().then((scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticDenseMode: arEngine.ARSemanticDenseMode.CUBE_VOLUME, // 开启体积测量
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.DISABLED,
        meshMode: arEngine.ARMeshMode.DISABLED,
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        console.info('Succeeded in initializing ARView.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
      })
    })
  }


  private stopARView(): void {
    // ...
  }
  private resumeARView(): void {
    // ...
  }
  private pauseARView(): void {
    // ...
  }
}
获取立方体体积数据

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，通过ARSession.getFrame方法获取当前帧，通过ARFrame.acquireSemanticDense获得当前帧的高精几何重建对象数据，通过ARSemanticDenseData.acquireCubeData从高精几何重建对象数据中获取识别到的立方体体积数据，相关变量定义参考定义变量。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }


  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }


  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }


    let arSession: arEngine.ARSession = ctx.session;


    try {
      let frame: arEngine.ARFrame = arSession.getFrame();
      if (frame) {
        let semanticData: arEngine.ARSemanticDenseData = frame.acquireSemanticDense();
        if(semanticData){
          if(semanticData.cubeDataSize>0){
            // 获取第一个Cube的体积数据
            let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()[0];
            cubeVertexData = semanticCubeData.vertexData;
            cubeConfidence = semanticCubeData.confidence;
            cubeLabel = semanticCubeData.label;
          }
          await semanticData.release();
        }
      }
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
高精几何重建介绍
高精几何重建（C/C++）
