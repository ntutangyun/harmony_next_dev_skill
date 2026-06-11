# 检测环境中的平面（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-plane_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.1.0(18)开始，检测环境平面能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SLAM）。

接口说明

检测平面通过ARPlane平面对象进行，以下接口为平面相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARTrackable.getPose	获取追踪目标的位姿信息。
ARTrackable.getAnchors	获取绑定到输入可跟踪对象的锚点对象。
ARPose.getMatrix	将位姿数据转换为一个4x4的矩阵。
ARPlane.getPolygonXZ	获取检测到的平面2D顶点数组。
ARPlane.getSubsumedBy	获取平面的父平面（当平面与另一个平面合并时会生成父平面）。
ARPlane.isPoseInExtents	检查给定位姿是否在平面的边界矩形内。
ARPlane.isPoseInPolygon	检查给定位姿是否在平面的边界多边形内。

开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者XComponent绘制识别的平面。关于AGP的介绍可以查看ArkGraphics 3D简介和AGP引擎。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

[h2]导入模块

平面检测能力所需的模块导入如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { Matrix4 } from '@kit.ArkUI';

[h2]显示预览流

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

@Builder
export function ARPlaneBuilder(): void {
  ARPlane();
}

@Component
struct ARPlane {
  @State arContext?: arViewController.ARViewContext = undefined;

  build(): void {
    // ...
  }

  private initARView(): void {
    // ...
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

[h2]检测环境平面

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，通过ARSession.getAllTrackables方法获取所有识别到的平面。

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
      let camera: arEngine.ARCamera = frame.getCamera();
      let trackable: arEngine.ARTrackable[] = [];

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
        console.info(`Succeeded in getting tracking plane, length is: ${trackable.length}`); // 打印当前识别到的平面数量
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}

[h2]检测平面的自定义方法

自定义方法获取顶点数据getVertices、创建索引generateMeshIndex、创建mesh数据generateMeshInput。

// 获取三维空间顶点坐标，第一个入参的位姿矩阵按垂直列排列，第二个坐标点为(x, 0, z, 1)，对应x-z平面。
export function getVertices(mat: Matrix4, point: number[]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < point.length; i += 2) {
    let single: Vec3 = {
      x: (mat[2] * point[i] + mat[6] * 0
        + mat[10] * point[i + 1] + mat[14] * 1.0),
      y: mat[1] * point[i] + mat[5] * 0
        + mat[9] * point[i + 1] + mat[13] * 1.0,
      z: -(mat[0] * point[i] + mat[4] * 0
        + mat[8] * point[i + 1] + mat[12] * 1.0),
    }
    result.push(single);
  }
  return result;
}
// 创建 ARWorld 的 mesh索引。由于平面是由三角形拼接而成的，因此每个平面上的每个三角形的首个顶点索引都是相同的。
export function generateMeshIndex(input: Vec3[][]): number[] {
  let result: number[] = [];
  let start: number = 0;

  for (let i = 0; i < input.length; i++) {
    let length: number = input[i].length;

    for (let j = start + 1; j < start + length - 1; j++) {
      result.push(start);
      result.push(j);
      result.push(j + 1);
    }
    start += length;
  }
  return result;
}

export function generateMeshInput(vex: Vec3[][]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < vex.length; i++) {
    let tmp: Vec3[] = vex[i];
    for (let j = 0; j < tmp.length; j++) {
      result.push(tmp[j]);
    }
  }
  return result;
}

## Code blocks

### Code block 1

```
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { Matrix4 } from '@kit.ArkUI';
```

### Code block 2

```
@Builder
export function ARPlaneBuilder(): void {
  ARPlane();
}

@Component
struct ARPlane {
  @State arContext?: arViewController.ARViewContext = undefined;

  build(): void {
    // ...
  }

  private initARView(): void {
    // ...
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
```

### Code block 3

```
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
      let camera: arEngine.ARCamera = frame.getCamera();
      let trackable: arEngine.ARTrackable[] = [];

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        trackable = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
        console.info(`Succeeded in getting tracking plane, length is: ${trackable.length}`); // 打印当前识别到的平面数量
      }

    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```

### Code block 4

```
// 获取三维空间顶点坐标，第一个入参的位姿矩阵按垂直列排列，第二个坐标点为(x, 0, z, 1)，对应x-z平面。
export function getVertices(mat: Matrix4, point: number[]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < point.length; i += 2) {
    let single: Vec3 = {
      x: (mat[2] * point[i] + mat[6] * 0
        + mat[10] * point[i + 1] + mat[14] * 1.0),
      y: mat[1] * point[i] + mat[5] * 0
        + mat[9] * point[i + 1] + mat[13] * 1.0,
      z: -(mat[0] * point[i] + mat[4] * 0
        + mat[8] * point[i + 1] + mat[12] * 1.0),
    }
    result.push(single);
  }
  return result;
}
// 创建 ARWorld 的 mesh索引。由于平面是由三角形拼接而成的，因此每个平面上的每个三角形的首个顶点索引都是相同的。
export function generateMeshIndex(input: Vec3[][]): number[] {
  let result: number[] = [];
  let start: number = 0;

  for (let i = 0; i < input.length; i++) {
    let length: number = input[i].length;

    for (let j = start + 1; j < start + length - 1; j++) {
      result.push(start);
      result.push(j);
      result.push(j + 1);
    }
    start += length;
  }
  return result;
}

export function generateMeshInput(vex: Vec3[][]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < vex.length; i++) {
    let tmp: Vec3[] = vex[i];
    for (let j = 0; j < tmp.length; j++) {
      result.push(tmp[j]);
    }
  }
  return result;
}
```
