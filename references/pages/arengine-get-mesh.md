# 获取网格扫描信息（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-mesh_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.1.0(18)开始，获取网格扫描信息能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持环境Mesh识别特性（ARENGINE_FEATURE_TYPE_MESH）。

接口说明

网格扫描主要依赖ARSceneMesh，以下接口为AR网格扫描相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARSceneMesh.getVertices	获取场景网格中的顶点坐标数据。
ARSceneMesh.getVertexNormals	获取场景网格中的顶点法线坐标数据。
ARSceneMesh.getTriangleIndices	获取场景网格中的三角形索引数据。
ARSceneMesh.release	释放环境网格数据对象。
ARFrame.hitTest	根据相机投射光线，获取预览区域中的像素坐标（pixelX和pixelY）来确定射线方向，然后检测这个射线在平面或点云中是否有交点。
ARHitResult.getHitPose	获取交点位姿。
ARHitResult.getTrackable	获取被命中的可追踪对象。
ARHitResult.createAnchor	在交点（intersection）创建一个锚点。
ARHitResult.release	释放命中检测结果对象占用的内存。
ARPose.getMatrix	将位姿数据转换为一个4x4的矩阵。
ARPose.release	释放位姿对象占用的内存。

开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者XComponent绘制识别的平面。关于AGP的介绍可以查看ArkGraphics 3D简介和AGP引擎。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

[h2]导入模块

网格扫描能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CubeGeometry, CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node,
  PrimitiveTopology, Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import { arrayBufferFloat32ToNumber, arrayBufferInt32ToNumber, arrayToVec3, getStatusBarHeight } from '../utils/Utils';

[h2]定义变量

定义变量hitAnchorList存储放置物体处的锚点信息、hitPoseList存储放置物体处的位姿信息和statusBarHeight设备状态栏高度。

let frame: arEngine.ARFrame;
let hitAnchorList: arEngine.ARAnchor[] = [];
let hitPoseList: Vec3[] = [];

[h2]显示预览流

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

@Builder
export function ARMeshBuilder(): void {
  ARMesh();
}
// ...
@Component
struct ARMesh {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State statusBarHeight: number = 0;

  async aboutToAppear(): Promise<void> {
    this.statusBarHeight = await getStatusBarHeight(this.context);
  }

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
            .onClick((event) => {
              this.objectCollisionDetection(event);
            })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
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

  private objectCollisionDetection(event: ClickEvent): void {
    let x: number = this.getUIContext().vp2px(event.windowX);
    let y: number = this.getUIContext().vp2px(event.windowY) - this.statusBarHeight;
    logger.info(`Get onclick position, x: ${x} y: ${y}.`);

    try {
      let result: arEngine.ARHitResult[] = frame.hitTest(x, y);
      logger.info(`The hitresult size is: ${result.length}.`);
      if (!result) {
        return;
      }

      for (let i = 0; i < result.length; i++) {
        let hitResult: arEngine.ARHitResult = result[i];
        let distance: number = hitResult.distance;
        logger.info(`The hitresult distance is: ${distance}.`);

        if (distance <= 0) {
          continue;
        }

        let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
        let pos: Vec3 = hitAnchor.getPose().translation;

        hitPoseList.push(pos);
        hitAnchorList.push(hitAnchor);

        if (hitPoseList.length > 10) {
          hitPoseList.splice(0, 1);
          hitAnchorList.splice(0, 1);
        }
      }
      logger.info('Succeeded in getting hit result.');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get hitResults. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.ENABLE,
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        logger.info('Succeeded in initting ARView.');
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
      })
    })
  }

  private async stopARView(): Promise<void> {
    // ...
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }
}

[h2]获取mesh网格数据

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，获取mesh网格数据。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }

    let session: arEngine.ARSession | undefined = ctx.session;

    // The mesh color is controlled by the file mesh.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/mesh.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    try {
      frame = session.getFrame();
      let camera: arEngine.ARCamera = frame.getCamera();

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        planeVertices = arrayBufferFloat32ToNumber(frame.acquireSceneMesh().getVertices());
        triangleIndices = arrayBufferInt32ToNumber(frame.acquireSceneMesh().getTriangleIndices());
        vertexNormals = arrayBufferFloat32ToNumber(frame.acquireSceneMesh().getVertexNormals());
        isDisplayCube = true;
      } else {
        planeVertices = [];
        triangleIndices = [];
        vertexNormals = [];
        isDisplayCube = false;
      }
      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire depth information. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}

[h2]获取网格扫描信息的自定义方法

自定义数据转换方法arrayBufferFloat32ToNumber及arrayBufferInt32ToNumber可以参考数据类型转换说明。

## Code blocks

### Code block 1

```
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CubeGeometry, CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node,
  PrimitiveTopology, Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import { arrayBufferFloat32ToNumber, arrayBufferInt32ToNumber, arrayToVec3, getStatusBarHeight } from '../utils/Utils';
```

### Code block 2

```
let frame: arEngine.ARFrame;
let hitAnchorList: arEngine.ARAnchor[] = [];
let hitPoseList: Vec3[] = [];
```

### Code block 3

```
@Builder
export function ARMeshBuilder(): void {
  ARMesh();
}
// ...
@Component
struct ARMesh {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State statusBarHeight: number = 0;

  async aboutToAppear(): Promise<void> {
    this.statusBarHeight = await getStatusBarHeight(this.context);
  }

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
            .onClick((event) => {
              this.objectCollisionDetection(event);
            })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
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

  private objectCollisionDetection(event: ClickEvent): void {
    let x: number = this.getUIContext().vp2px(event.windowX);
    let y: number = this.getUIContext().vp2px(event.windowY) - this.statusBarHeight;
    logger.info(`Get onclick position, x: ${x} y: ${y}.`);

    try {
      let result: arEngine.ARHitResult[] = frame.hitTest(x, y);
      logger.info(`The hitresult size is: ${result.length}.`);
      if (!result) {
        return;
      }

      for (let i = 0; i < result.length; i++) {
        let hitResult: arEngine.ARHitResult = result[i];
        let distance: number = hitResult.distance;
        logger.info(`The hitresult distance is: ${distance}.`);

        if (distance <= 0) {
          continue;
        }

        let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
        let pos: Vec3 = hitAnchor.getPose().translation;

        hitPoseList.push(pos);
        hitAnchorList.push(hitAnchor);

        if (hitPoseList.length > 10) {
          hitPoseList.splice(0, 1);
          hitAnchorList.splice(0, 1);
        }
      }
      logger.info('Succeeded in getting hit result.');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get hitResults. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.ENABLE,
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        logger.info('Succeeded in initting ARView.');
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
      })
    })
  }

  private async stopARView(): Promise<void> {
    // ...
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }
}
```

### Code block 4

```
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }

    let session: arEngine.ARSession | undefined = ctx.session;

    // The mesh color is controlled by the file mesh.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/mesh.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    try {
      frame = session.getFrame();
      let camera: arEngine.ARCamera = frame.getCamera();

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        planeVertices = arrayBufferFloat32ToNumber(frame.acquireSceneMesh().getVertices());
        triangleIndices = arrayBufferInt32ToNumber(frame.acquireSceneMesh().getTriangleIndices());
        vertexNormals = arrayBufferFloat32ToNumber(frame.acquireSceneMesh().getVertexNormals());
        isDisplayCube = true;
      } else {
        planeVertices = [];
        triangleIndices = [];
        vertexNormals = [];
        isDisplayCube = false;
      }
      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire depth information. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```
