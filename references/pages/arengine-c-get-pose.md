# 获取设备位姿（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-pose_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.0(12)开始，获取设备位姿能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SLAM）。

创建ARSession

开发者可以参考管理AR会话创建ARSession。

获取设备当前位姿

创建一个空位姿变量cameraPose。

AREngine_ARPose *cameraPose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &cameraPose);

获取当前时刻相机位姿信息，并存储在cameraPose变量中。

// 创建一个新的AREngine_ARFrame对象。
AREngine_ARFrame *arFrame = nullptr;
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
// 更新当前帧的结果到arFrame。
HMS_AREngine_ARSession_Update(arSession, arFrame);
// 获取当前帧的相机参数对象。
AREngine_ARCamera *arCamera = nullptr;
HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera);
// 获取当前时刻相机位姿信息。
HMS_AREngine_ARCamera_GetPose(arSession, arCamera, cameraPose);

从cameraPose中获取相机位姿的不同分量，包括平移分量和旋转分量。

float poseRaw[7] = { 0.0f };
HMS_AREngine_ARPose_GetPoseRaw(arSession, cameraPose, poseRaw, 7);

## Code blocks

### Code block 1

```
AREngine_ARPose *cameraPose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &cameraPose);
```

### Code block 2

```
// 创建一个新的AREngine_ARFrame对象。
AREngine_ARFrame *arFrame = nullptr;
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
// 更新当前帧的结果到arFrame。
HMS_AREngine_ARSession_Update(arSession, arFrame);
// 获取当前帧的相机参数对象。
AREngine_ARCamera *arCamera = nullptr;
HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera);
// 获取当前时刻相机位姿信息。
HMS_AREngine_ARCamera_GetPose(arSession, arCamera, cameraPose);
```

### Code block 3

```
float poseRaw[7] = { 0.0f };
HMS_AREngine_ARPose_GetPoseRaw(arSession, cameraPose, poseRaw, 7);
```
