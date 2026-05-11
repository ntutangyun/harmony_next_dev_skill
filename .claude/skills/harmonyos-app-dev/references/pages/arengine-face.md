# 人脸跟踪（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-face_

人脸跟踪能力支持部分Phone、部分Tablet、TV设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_FACE）。

接口说明

人脸跟踪主要依赖ARFace，以下接口为人脸跟踪的相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARSession.getFrame	获取AR Engine处理后的一帧数据。
ARSession.getAllTrackables	获取当前session中包含的人脸对象。
ARFace.getGeometry	返回一个人脸几何对象。
ARFace.getBlendShapes	返回一个人脸微表情对象。
开发步骤

对于使用ArkTS的任何AR应用，首先需要参考AR特性检查接口检查当前设备是否支持该特性。若设备支持，创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

导入模块

人脸跟踪能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
定义变量

定义变量face接收人脸对象，定义变量faceGeometry接收人脸几何对象，定义变量faceBlendShapes接收人脸微表情对象。

let face: arEngine.ARFace;
let faceGeometry: arEngine.ARGeometry;
let faceBlendShapes: arEngine.ARBlendShapes;
显示预览流

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

更改type为ARType.FACE，更改cameraLensFacing为ARCameraLensFacing.FRONT，更改multiFaceMode为ARMultiFaceMode.MULTIFACE_DISABLE，启用前置相机的人脸跟踪能力。

@Builder
export function ARFaceBuilder(): void {
  ARFace();
}


@Component
struct ARFace {
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
        type: arEngine.ARType.FACE,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        semanticMode: arEngine.ARSemanticMode.NONE,
        meshMode: arEngine.ARMeshMode.DISABLED,
        focusMode: arEngine.ARFocusMode.AUTO,
        cameraLensFacing: arEngine.ARCameraLensFacing.FRONT,
        multiFaceMode: arEngine.ARMultiFaceMode.MULTIFACE_DISABLE
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
获取人脸几何数据和微表情数据

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，通过ARSession.getFrame方法获取当前帧，通过ARSession.getAllTrackables获得当前会话包含的人脸对象数据，通过ARFace.getGeometry和ARFace.getBlendShapes从人脸对象数据中获取识别到的几何信息和微表情信息，相关变量定义参考定义变量。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }


  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
    // ...
  }


  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    if (!ctx.session) {
      return;
    }


    let arSession: arEngine.ARSession = ctx.session;


    try {
      let frame: arEngine.ARFrame = arSession.getFrame();
      if (frame) {
        // 获取face信息
        let trackables: Array<arEngine.ARTrackable> = arSession.getAllTrackables(arEngine.ARTrackableType.FACE);
        for (let i = 0; i < trackables.length; ++i) {
          if (trackables[i].state !== arEngine.ARTrackingState.TRACKING) {
            console.error('Face not in tracking state');
            continue;
          }
          face = trackables[i] as arEngine.ARFace;
          faceGeometry = face.getGeometry();
          faceBlendShapes = face.getBlendShapes();
          if(faceGeometry){
            let tmpVert = faceGeometry.getVertices();
            let tmpIndices = faceGeometry.getIndices();
          }
          if(faceBlendShapes){
            let tmpData = faceBlendShapes.getData();
            let tmpTypes = faceBlendShapes.getTypes();
          }
          faceGeometry.release();
          faceBlendShapes.release();
        }
      }
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
人脸识别与跟踪介绍
人脸跟踪（C/C++）
