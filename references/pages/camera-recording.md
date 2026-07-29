# 录像(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording_

在开发相机应用时，需要先申请相关权限。

相机应用可通过调用和控制相机设备，完成预览、拍照和录像等基础操作。

录像也是相机应用的最重要功能之一，录像是循环帧的捕获。对于录像的自定义配置，开发者可以参考拍照中的步骤4，设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

开发步骤

详细的API说明请参考@ohos.multimedia.camera (相机管理)。

导入media模块。

创建录像输出流的SurfaceId以及录像输出的数据，都需要用到系统提供的media接口@ohos.multimedia.media (媒体服务)能力，导入media接口的方法如下。

import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';
import { media } from '@kit.MediaKit';

创建Surface。

系统提供的media接口可以创建一个录像AVRecorder实例，通过该实例的getInputSurface方法获取SurfaceId，与录像输出流做关联，处理录像输出流输出的数据。

this.avRecorder = await this.createAVRecorder();
if (this.avRecorder === undefined) {
  Logger.error(TAG, 'Failed to create the avRecorder.');
  return;
}
await this.prepareAVRecorder();
let videoSurfaceId = await this.avRecorder.getInputSurface();

创建录像输出流。

通过CameraOutputCapability中的videoProfiles属性，可获取当前设备支持的录像输出流。然后，定义创建录像的参数，通过createVideoOutput方法创建录像输出流。

说明

1.预览流与录像输出流的分辨率的宽高比要保持一致，如示例代码中宽高比为640:480 = 4:3，则需要预览流中的分辨率的宽高比也为4:3，如分辨率选择640:480，或960:720，或1440:1080，以此类推。

2.在设置预览输出流的分辨率宽高前，需要先通过AVRecorderProfile查询视频帧支持可配置的宽高范围。

3.获取录像旋转角度的方法：通过VideoOutput中的getVideoRotation方法获取rotation实际的值。

4.录像输出流帧率通过CameraOutputCapability中的videoProfiles属性，选择VideoProfile中frameRateRange满足实际业务需求的录像输出流videoProfile。

createVideoOutputFn(cameraManager: camera.CameraManager, videoProfileObj: camera.VideoProfile,
  surfaceId: string): camera.VideoOutput | undefined {
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(videoProfileObj, surfaceId);
    Logger.info(TAG, `createVideoOutputFn success: ${videoOutput}`);
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `createVideoOutputFn failed: ${err.code}`);
  }
  return videoOutput;
}

开始录像。

说明

在设置预览流帧率时，需要先通过getActiveFrameRate查询当前录像流的帧率。

当录像流已设置过范围帧率时，预览流帧率必须设置与其相同的范围帧率。

当录像流已设置过固定帧率时，预览流帧率要设置成录像帧率的约数，且必须也为固定帧率。

部分设备前置镜头录像分辨率若选择3280*2160，录像模式下可能会出现视频倒置的情况，建议在commitConfig后设置视频防抖setVideoStabilizationMode，避免该问题发生。

先通过videoOutput的start方法启动录像输出流，再通过avRecorder的start方法开始录像。

async startVideo(): Promise<void> {
  Logger.info(TAG, 'startVideo is called');
  try {
    await this.videoOutput?.start();
    await this.avRecorder?.start();
    this.isRecording = true;
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `startVideo err: ${err.code}`);
  }
  Logger.info(TAG, 'startVideo End of call');
}

停止录像。

先通过avRecorder的stop方法停止录像，再通过videoOutput的stop方法停止录像输出流。

async stopVideo(): Promise<void> {
  Logger.info(TAG, 'stopVideo is called');
  if (!this.isRecording) {
    Logger.info(TAG, 'not in recording');
    return;
  }
  try {
    if (this.avRecorder) {
      await this.avRecorder.stop();
    }
    if (this.videoOutput) {
      await this.videoOutput.stop();
    }
    this.isRecording = false;
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `stopVideo err: ${err.code}`);
  }
  Logger.info(TAG, 'stopVideo End of call');
}

状态监听

在相机应用开发过程中，可以随时监听录像输出流状态，包括录像开始、录像结束、录像流输出的错误。

通过注册固定的frameStart回调函数获取监听录像开始结果，videoOutput创建成功时即可监听，录像第一次曝光时触发，有该事件返回结果则认为录像开始。

previewOutput.on('frameStart', (): void => {
  Logger.debug(TAG, 'Preview frame started');
  AppStorage.setOrCreate('frameStart', ++this.frameStartFlag);
});

通过注册固定的frameEnd回调函数获取监听录像结束结果，videoOutput创建成功时即可监听，录像完成最后一帧时触发，有该事件返回结果则认为录像流已结束。

previewOutput.on('frameEnd', (): void => {
  Logger.debug(TAG, 'Preview frame ended');
});

通过注册固定的error回调函数获取监听录像输出错误结果，callback返回预览输出接口使用错误时对应的错误码，错误码类型参见CameraErrorCode。

previewOutput.on('error', (previewOutputError: BusinessError): void => {
  Logger.info(TAG, `Preview output previewOutputError: ${JSON.stringify(previewOutputError)}`);
});

示例代码

基于CameraKit通过AVRecorder录像

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { camera } from '@kit.CameraKit';
import { media } from '@kit.MediaKit';
```

### Code block 2

```
this.avRecorder = await this.createAVRecorder();
if (this.avRecorder === undefined) {
  Logger.error(TAG, 'Failed to create the avRecorder.');
  return;
}
await this.prepareAVRecorder();
let videoSurfaceId = await this.avRecorder.getInputSurface();
```

### Code block 3

```
createVideoOutputFn(cameraManager: camera.CameraManager, videoProfileObj: camera.VideoProfile,
  surfaceId: string): camera.VideoOutput | undefined {
  let videoOutput: camera.VideoOutput | undefined = undefined;
  try {
    videoOutput = cameraManager.createVideoOutput(videoProfileObj, surfaceId);
    Logger.info(TAG, `createVideoOutputFn success: ${videoOutput}`);
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `createVideoOutputFn failed: ${err.code}`);
  }
  return videoOutput;
}
```

### Code block 4

```
async startVideo(): Promise<void> {
  Logger.info(TAG, 'startVideo is called');
  try {
    await this.videoOutput?.start();
    await this.avRecorder?.start();
    this.isRecording = true;
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `startVideo err: ${err.code}`);
  }
  Logger.info(TAG, 'startVideo End of call');
}
```

### Code block 5

```
async stopVideo(): Promise<void> {
  Logger.info(TAG, 'stopVideo is called');
  if (!this.isRecording) {
    Logger.info(TAG, 'not in recording');
    return;
  }
  try {
    if (this.avRecorder) {
      await this.avRecorder.stop();
    }
    if (this.videoOutput) {
      await this.videoOutput.stop();
    }
    this.isRecording = false;
  } catch (error) {
    let err = error as BusinessError;
    Logger.error(TAG, `stopVideo err: ${err.code}`);
  }
  Logger.info(TAG, 'stopVideo End of call');
}
```

### Code block 6

```
previewOutput.on('frameStart', (): void => {
  Logger.debug(TAG, 'Preview frame started');
  AppStorage.setOrCreate('frameStart', ++this.frameStartFlag);
});
```

### Code block 7

```
previewOutput.on('frameEnd', (): void => {
  Logger.debug(TAG, 'Preview frame ended');
});
```

### Code block 8

```
previewOutput.on('error', (previewOutputError: BusinessError): void => {
  Logger.info(TAG, `Preview output previewOutputError: ${JSON.stringify(previewOutputError)}`);
});
```
