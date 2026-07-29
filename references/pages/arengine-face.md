# 人脸跟踪（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-face_

约束与限制

从6.1.0(23)开始，人脸跟踪能力支持部分Phone、部分Tablet、TV设备。请参考硬件要求判断设备是否支持人脸识别与跟踪特性（ARENGINE_FEATURE_TYPE_FACE）。

接口说明

人脸跟踪主要依赖ARFace，以下接口为人脸跟踪的相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARSession.getFrame	获取AR Engine处理后的一帧数据。
ARSession.getAllTrackables	获取当前session中包含的人脸对象。
ARFace.getGeometry	返回一个人脸几何对象。
ARFace.getBlendShapes	返回一个人脸微表情对象。

开发步骤

对于使用ArkTS的任何AR应用，首先需要参考AR特性检查接口检查当前设备是否支持该特性。若设备支持，创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

[h2]导入模块

人脸跟踪能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node, PrimitiveTopology,
  Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import {arrayBufferFloat32ToNumber, arrayBufferInt32ToNumber, generateFaceMeshIndex,
  generateMeshInput, getFaceFrontVertices} from '../utils/Utils';

[h2]定义变量

定义变量face接收人脸对象，定义变量faceGeometry接收人脸几何对象，定义变量faceBlendShapes接收人脸微表情对象。

let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
// ...
// Data Process
let faceGeometry: arEngine.ARGeometry = face.getGeometry();
let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();

[h2]显示预览流

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

更改type为ARType.FACE，更改cameraLensFacing为ARCameraLensFacing.FRONT，更改multiFaceMode为ARMultiFaceMode.MULTIFACE_ENABLE，启用前置相机的人脸跟踪能力。

@Builder
export function ARFaceBuilder() {
  ARFace();
}
// ...
@Component
export struct ARFace {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State arContext?: arViewController.ARViewContext = undefined;

  build() {
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
    .onAppear(async () => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
      this.clearGlobalVariables();
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

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      await this.arContext.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private pauseARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.pause();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.resume();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private initARView(): void {
    Scene.load().then(async (result: Scene) => {
      try {
        let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
        logger.info(`ARFace isARTypeSupported is ${ret}`);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(
          `Failed to get whether the device is support ARFace. Code is ${err.code}, message is ${err.message}`);
      }

      let context = new arViewController.ARViewContext();
      context.scene = result;
      context.callback = new ARViewCallbackImpl();
      context.config = {
        type: arEngine.ARType.FACE,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: arEngine.ARPowerMode.NORMAL,
        focusMode: arEngine.ARFocusMode.AUTO,
        cameraLensFacing: arEngine.ARCameraLensFacing.FRONT,
        multiFaceMode: arEngine.ARMultiFaceMode.MULTIFACE_ENABLE,
      };
      context.init().then(() => {
        this.arContext = context;
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}`);
      });
    })
  }
  // ...
}

[h2]获取人脸几何数据和微表情数据

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，通过ARSession.getFrame方法获取当前帧，通过ARSession.getAllTrackables获得当前会话包含的人脸对象数据，通过ARFace.getGeometry和ARFace.getBlendShapes从人脸对象数据中获取识别到的几何信息和微表情信息，相关变量定义参考定义变量。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      logger.error('arSession is undefined');
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    // ...
    try {
      let mesh = new CustomGeometry();
      let geometry: Geometry | null = null;
      if (session == null) {
        logger.error('session is null');
      }

      let vertexArray: Vec3[][] = [];
      let indexArray: Map<number, number[]> = new Map;

      // Acquire face data
      let trackables: arEngine.ARTrackable[] = session.getAllTrackables(arEngine.ARTrackableType.FACE);
      logger.debug(`the faceList length is ${trackables.length}`);
      for (let i = 0; i < trackables.length; ++i) {
        let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
        let centerPose = face.getPose();
        let viewMatrix = centerPose.getMatrix();

        if (trackables[i].state !== arEngine.ARTrackingState.TRACKING) {
          logger.error(`Face not in tracking state`);
          continue;
        }
        // Data Process
        let faceGeometry: arEngine.ARGeometry = face.getGeometry();
        let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
        let tmpVert = faceGeometry.getVertices();
        let tmpIndices = faceGeometry.getIndices();
        faceVertices = arrayBufferFloat32ToNumber(tmpVert);
        let faceIndices: number[] = arrayBufferInt32ToNumber(tmpIndices);
        vertexArray.push(getFaceFrontVertices(viewMatrix, faceVertices));
        indexArray.set(i, faceIndices);

        // BlendShapes Print
        logger.info('the count of blendShapes is' + faceBlendShapes.count);
        logger.info('the data of blendShapes is' + arrayBufferFloat32ToNumber(faceBlendShapes.getData()));
        logger.info('the types of blendShapes is' + faceBlendShapes.getTypes());
      }

      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire face information. Code is ${err.code}, message is ${err.message}`)
    }
  }
}

## Code blocks

### Code block 1

```
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node, PrimitiveTopology,
  Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import {arrayBufferFloat32ToNumber, arrayBufferInt32ToNumber, generateFaceMeshIndex,
  generateMeshInput, getFaceFrontVertices} from '../utils/Utils';
```

### Code block 2

```
let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
// ...
// Data Process
let faceGeometry: arEngine.ARGeometry = face.getGeometry();
let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
```

### Code block 3

```
@Builder
export function ARFaceBuilder() {
  ARFace();
}
// ...
@Component
export struct ARFace {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State arContext?: arViewController.ARViewContext = undefined;

  build() {
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
    .onAppear(async () => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
      this.clearGlobalVariables();
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

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      await this.arContext.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private pauseARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.pause();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.resume();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private initARView(): void {
    Scene.load().then(async (result: Scene) => {
      try {
        let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
        logger.info(`ARFace isARTypeSupported is ${ret}`);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(
          `Failed to get whether the device is support ARFace. Code is ${err.code}, message is ${err.message}`);
      }

      let context = new arViewController.ARViewContext();
      context.scene = result;
      context.callback = new ARViewCallbackImpl();
      context.config = {
        type: arEngine.ARType.FACE,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: arEngine.ARPowerMode.NORMAL,
        focusMode: arEngine.ARFocusMode.AUTO,
        cameraLensFacing: arEngine.ARCameraLensFacing.FRONT,
        multiFaceMode: arEngine.ARMultiFaceMode.MULTIFACE_ENABLE,
      };
      context.init().then(() => {
        this.arContext = context;
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}`);
      });
    })
  }
  // ...
}
```

### Code block 4

```
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      logger.error('arSession is undefined');
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    // ...
    try {
      let mesh = new CustomGeometry();
      let geometry: Geometry | null = null;
      if (session == null) {
        logger.error('session is null');
      }

      let vertexArray: Vec3[][] = [];
      let indexArray: Map<number, number[]> = new Map;

      // Acquire face data
      let trackables: arEngine.ARTrackable[] = session.getAllTrackables(arEngine.ARTrackableType.FACE);
      logger.debug(`the faceList length is ${trackables.length}`);
      for (let i = 0; i < trackables.length; ++i) {
        let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
        let centerPose = face.getPose();
        let viewMatrix = centerPose.getMatrix();

        if (trackables[i].state !== arEngine.ARTrackingState.TRACKING) {
          logger.error(`Face not in tracking state`);
          continue;
        }
        // Data Process
        let faceGeometry: arEngine.ARGeometry = face.getGeometry();
        let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
        let tmpVert = faceGeometry.getVertices();
        let tmpIndices = faceGeometry.getIndices();
        faceVertices = arrayBufferFloat32ToNumber(tmpVert);
        let faceIndices: number[] = arrayBufferInt32ToNumber(tmpIndices);
        vertexArray.push(getFaceFrontVertices(viewMatrix, faceVertices));
        indexArray.set(i, faceIndices);

        // BlendShapes Print
        logger.info('the count of blendShapes is' + faceBlendShapes.count);
        logger.info('the data of blendShapes is' + arrayBufferFloat32ToNumber(faceBlendShapes.getData()));
        logger.info('the types of blendShapes is' + faceBlendShapes.getTypes());
      }

      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire face information. Code is ${err.code}, message is ${err.message}`)
    }
  }
}
```
