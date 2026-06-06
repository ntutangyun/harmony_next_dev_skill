# 获取设备位姿（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose_

获取设备位姿支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SLAM）。

接口说明

获取设备位姿可以通过ARCamera相机对象获取，以下接口为获取设备位姿接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
ARCamera.getPose	获取摄像机在世界空间中的位姿信息。
开发步骤
导入模块

获取设备位姿能力需要依赖以下模块。

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';

Vec3是一个三维向量，用于存储设备的位姿信息。

定义变量

定义两个变量pose和stateReason，用于接收pose位姿信息和追踪失败原因。

let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;
显示预览流及设备位姿信息

首先初始化AR会话和AR场景，可以参考初始化AR会话和AR场景章节。

在设备界面上显示设备位姿信息及追踪失败原因，使用重复调用函数方法在设备界面上实时更新位姿和追踪失败原因的信息。

@Builder
export function ARPoseBuilder(): void {
  ARPose();
}


@Component
struct ARPose {
  @State arContext?: arViewController.ARViewContext = undefined;
  private intervalId: number = -1;
  // 重复调用函数时间间隔为33ms，即设定为30fps
  private delayInterval: number = 33;
  // 位姿的信息参数
  @State translation: Vec3 = {
    x: 0,
    y: 0,
    z: 0
  }
  // 追踪失败的原因
  @State reason: arEngine.ARTrackingStateReason = stateReason;


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


          // 在屏幕上显示设备位姿信息
          Column() {
            Text(`x: ${this.translation.x.toFixed(4)}`)
              .infoStyles()
            Text(`y: ${this.translation.y.toFixed(4)}`)
              .infoStyles()
            Text(`z: ${this.translation.z.toFixed(4)}`)
              .infoStyles()
            Text(`reason: ${this.reason}`)
              .infoStyles()
          }
          .alignItems(HorizontalAlign.Start)
          .margin({ left: 28, top: 28 })
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      // 设定在30fps下更新位姿和追踪失败原因的信息
      this.intervalId = setInterval(() => {
        if (pose !== undefined) {
          this.translation = pose.translation;
          this.reason = stateReason;
        }
      }, this.delayInterval);
    })
    .onWillDisappear(() => {
      // 退出setInterval函数
      clearInterval(this.intervalId);
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


// 界面显示文本样式
@Extend(Text)
function infoStyles() {
  .fontColor(Color.Yellow)
  .fontSize(24)
  .textShadow({
    radius: 10,
    color: Color.Black,
    offsetX: 0,
    offsetY: 0
  })
  .textAlign(TextAlign.Start)
}
获取设备位姿信息

调用ARViewCallback，使用其中的onFrameUpdate方法获取AR会话对象arSession，之后通过AR会话对象arSession获取每一帧对应的设备位姿信息。

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


    let arSession: arEngine.ARSession = ctx.session; // 获取AR会话


    try {
      // 获取每一帧的设备位姿信息及追踪失败的原因
      let frame: arEngine.ARFrame = arSession.getFrame();
      pose = frame.getCamera().getPose();
      stateReason = frame.getCamera().stateReason;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}`);
    }
  }
}
运动跟踪介绍
获取设备位姿（C/C++）
