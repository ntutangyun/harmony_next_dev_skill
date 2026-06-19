# 空间照片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-spatial-image_

从26.0.0版本开始，新增支持空间照片功能。

简介

传统的2D照片虽然能记录瞬间，但缺乏立体感和沉浸感。用户查看照片时无法从不同角度观察场景中的物体，难以获得身临其境的体验。空间照片技术通过依托端侧AI模型，对单张2D图像进行深度估算，重建出可交互的3D立体模型，解决了该一问题，使开发者能够在应用中实现3D物体展示、空间导航、交互式场景浏览等沉浸式AR和VR体验。

基本概念

3D Gaussian模型（MODELTYPE_GS）：一种基于高斯椭球的3D表示方式，渲染质量高，适合对视觉效果要求较高的场景。

Mesh模型（MODELTYPE_MESH）：传统的三角网格模型，兼容性好、渲染效率高，适合对性能要求较高的场景。

模型文件：系统生成的文件涵盖3D几何数据、运动参数、单目深度三类数据，默认存储在应用沙箱路径，单文件容量为数十MB。相关文件的生命周期管理（存储、清理、备份等）均由开发者自行维护。

约束与限制

生成的模型文件可能较大（数十MB），需确保存储空间充足。

同一时间仅支持一个任务，需等待前一个任务完成后再发起新的任务。

前提条件

使用空间照片功能前需要申请下列权限：

传感器权限：用于SpatialImageController.calcRenderPos()获取陀螺仪数据。

网络权限：用于prepareEnv()下载AI模型。

存储权限：如需将模型文件保存到外部存储，需申请对应权限。

开发流程

空间照片的开发流程包含以下核心步骤：

检查兼容性：调用SpatialImageGenerator.isSupport()判断设备是否支持空间照片能力，并检查AI模型是否存在。

下载模型：若AI模型缺失，调用prepareEnv()下载模型，并通过回调监听下载进度。

异步生成3D模型：将PixelMap格式的2D图像、指定的模型类型和输出URI传入generate()，异步生成3D模型文件。

加载与渲染：使用SpatialImageController加载生成的模型文件，并配合陀螺仪数据实现动态视角交互。

接口说明

接口名	描述
isSupport(): SpatialImageStatus	检查设备是否支持空间照片，并判断所需AI模型是否存在。
prepareEnv(callback: ProgressCallback): Promise<SpatialImageStatus>	下载模型，并通过回调函数监听下载进度。使用Promise异步回调。
cancelPrepare(): Promise<SpatialImageStatus>	取消正在进行的AI模型下载。使用Promise异步回调。
generate(image: PixelMap, type: SpatialImageModelType, uri: string): Promise<SpatialImageStatus>	从2D图像生成3D模型、运动参数和单目深度图，并保存到指定路径。该操作耗时较长，同一时间仅允许一个生成任务执行。使用Promise异步回调。
cancelGenerate(): Promise<SpatialImageStatus>	取消正在进行的模型生成任务。使用Promise异步回调。
constructor(uri: string)	创建SpatialImageController实例，加载指定URI的模型文件。
calcRenderPos(response: GyroscopeResponse): CameraPose	根据陀螺仪传感器数据计算渲染相机的姿态（位置和旋转）。该方法需要高频调用，建议在每次陀螺仪数据回调或每帧渲染时调用。相机历史姿态状态在内部维护，首次调用时返回初始姿态。

开发步骤

[h2]场景1：生成与渲染空间照片

任务场景：用户在应用中选择一张本地2D照片，应用将其转换为3D模型，并允许用户通过转动设备从不同角度查看模型。

导入必要模块。

import { spatialImage } from '@kit.SpatialReconKit';
import { image } from '@kit.ImageKit';
import { sensor } from '@kit.SensorServiceKit';

调用isSupport，实现检查兼容性并准备环境的目的。

async function initSpatialImage(): Promise<boolean> {
  // 检查设备是否支持空间照片，并判断所需AI模型是否存在
  let supportStatus: spatialImage.SpatialImageStatus = spatialImage.SpatialImageGenerator.isSupport();
  if (supportStatus === spatialImage.SpatialImageStatus.STATUS_NOT_SUPPORT) {
    console.error('Device does not support spatial image');
    return false;
  }

  // 如果AI模型不存在
  if (supportStatus === spatialImage.SpatialImageStatus.STATUS_AIMODEL_NOT_EXIST) {
    // 下载AI模型
    let downloadPromise = this.generator.prepareEnv((progress: number) => {
      console.info(`Download progress: ${progress * 100}%`);
      // 更新UI进度条
    });
    let result = await downloadPromise;
    if (result !== spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
      console.error('Download AI models failed');
      return false;
    }
  }
  return true;
}

调用generate，实现从图库选择图像并生成3D模型的目的。

async function generate3DModel(pixelMap: image.PixelMap, uri: string): Promise<boolean> {
  // 使用Mesh模型类型，生成结果保存到uri指定路径
  let result = await this.generator.generate(
    pixelMap,
    spatialImage.SpatialImageModelType.MODELTYPE_MESH,
    uri
  );

  switch (result) {
    case spatialImage.SpatialImageStatus.STATUS_SUCCESS:
      console.info('Model generated successfully');
      return true;
    case spatialImage.SpatialImageStatus.STATUS_GENERATE_CANCELLED:
      console.info('Generation cancelled');
      return false;
    case spatialImage.SpatialImageStatus.STATUS_GENERATE_FAILED:
      console.error('Generation failed');
      return false;
    default:
      return false;
  }
}

调用calcRenderPos，实现加载模型并启动陀螺仪监听的目的。

// 创建控制器，加载指定URI的模型文件
let controller: spatialImage.SpatialImageController = new spatialImage.SpatialImageController(uri);

// 监听陀螺仪数据并更新相机姿态
sensor.on(sensor.SensorId.GYROSCOPE, (response: sensor.GyroscopeResponse) => {
  // 每帧或每次传感器事件调用
  if (controller != null) {
    let cameraPose = controller.calcRenderPos(response);
    // 将cameraPose.position和cameraPose.rotation传递给3D渲染引擎
  }
}, { interval: 2000000 });

实现效果：

用户转动设备时，3D模型会呈现相应的视角变化，如同透过一个窗口观察真实物体。模型具有立体感，表面细节和遮挡关系符合物理规律。

[h2]场景2：取消正在生成的任务

任务场景：在模型生成过程中，用户可能因等待时间过长希望取消当前任务。应用需要提供取消功能，并正确处理资源释放和UI状态重置。

维护生成任务的Promise引用。

private currentGeneratePromise: Promise<spatialImage.SpatialImageStatus> | null = null;

async startGeneration(pixelMap: image.PixelMap, uri: string) {
  if (this.currentGeneratePromise) {
    console.warn('Generation already in progress');
    return;
  }

  this.currentGeneratePromise = this.generator.generate(
    pixelMap,
    spatialImage.SpatialImageModelType.MODELTYPE_GS,
    uri
  );

  let result = await this.currentGeneratePromise;
  this.currentGeneratePromise = null;

  if (result === spatialImage.SpatialImageStatus.STATUS_GENERATE_CANCELLED) {
    // 更新UI：显示"已取消"
  } else if (result === spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
    // 更新UI：显示成功
  }
}

调用cancelGenerate，实现取消逻辑的目的。

async cancelGenerate(): Promise<void> {
  let cancelRet = await this.generator.cancelGenerate();
  if (cancelRet === spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
    console.info('Generate cancelled');
  }
}

实现效果：

在模型生成过程中，用户可能因等待时间过长而希望取消当前任务。应用需要提供取消按钮，并正确处理资源释放和UI状态重置。

## Code blocks

### Code block 1

```
import { spatialImage } from '@kit.SpatialReconKit';
import { image } from '@kit.ImageKit';
import { sensor } from '@kit.SensorServiceKit';
```

### Code block 2

```
async function initSpatialImage(): Promise<boolean> {
  // 检查设备是否支持空间照片，并判断所需AI模型是否存在
  let supportStatus: spatialImage.SpatialImageStatus = spatialImage.SpatialImageGenerator.isSupport();
  if (supportStatus === spatialImage.SpatialImageStatus.STATUS_NOT_SUPPORT) {
    console.error('Device does not support spatial image');
    return false;
  }

  // 如果AI模型不存在
  if (supportStatus === spatialImage.SpatialImageStatus.STATUS_AIMODEL_NOT_EXIST) {
    // 下载AI模型
    let downloadPromise = this.generator.prepareEnv((progress: number) => {
      console.info(`Download progress: ${progress * 100}%`);
      // 更新UI进度条
    });
    let result = await downloadPromise;
    if (result !== spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
      console.error('Download AI models failed');
      return false;
    }
  }
  return true;
}
```

### Code block 3

```
async function generate3DModel(pixelMap: image.PixelMap, uri: string): Promise<boolean> {
  // 使用Mesh模型类型，生成结果保存到uri指定路径
  let result = await this.generator.generate(
    pixelMap,
    spatialImage.SpatialImageModelType.MODELTYPE_MESH,
    uri
  );

  switch (result) {
    case spatialImage.SpatialImageStatus.STATUS_SUCCESS:
      console.info('Model generated successfully');
      return true;
    case spatialImage.SpatialImageStatus.STATUS_GENERATE_CANCELLED:
      console.info('Generation cancelled');
      return false;
    case spatialImage.SpatialImageStatus.STATUS_GENERATE_FAILED:
      console.error('Generation failed');
      return false;
    default:
      return false;
  }
}
```

### Code block 4

```
// 创建控制器，加载指定URI的模型文件
let controller: spatialImage.SpatialImageController = new spatialImage.SpatialImageController(uri);

// 监听陀螺仪数据并更新相机姿态
sensor.on(sensor.SensorId.GYROSCOPE, (response: sensor.GyroscopeResponse) => {
  // 每帧或每次传感器事件调用
  if (controller != null) {
    let cameraPose = controller.calcRenderPos(response);
    // 将cameraPose.position和cameraPose.rotation传递给3D渲染引擎
  }
}, { interval: 2000000 });
```

### Code block 5

```
private currentGeneratePromise: Promise<spatialImage.SpatialImageStatus> | null = null;

async startGeneration(pixelMap: image.PixelMap, uri: string) {
  if (this.currentGeneratePromise) {
    console.warn('Generation already in progress');
    return;
  }

  this.currentGeneratePromise = this.generator.generate(
    pixelMap,
    spatialImage.SpatialImageModelType.MODELTYPE_GS,
    uri
  );

  let result = await this.currentGeneratePromise;
  this.currentGeneratePromise = null;

  if (result === spatialImage.SpatialImageStatus.STATUS_GENERATE_CANCELLED) {
    // 更新UI：显示"已取消"
  } else if (result === spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
    // 更新UI：显示成功
  }
}
```

### Code block 6

```
async cancelGenerate(): Promise<void> {
  let cancelRet = await this.generator.cancelGenerate();
  if (cancelRet === spatialImage.SpatialImageStatus.STATUS_SUCCESS) {
    console.info('Generate cancelled');
  }
}
```
