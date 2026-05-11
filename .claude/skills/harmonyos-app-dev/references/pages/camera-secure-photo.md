# 安全相机(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-secure-photo_

通过Device Security Kit来创建证明密钥（安全摄像头序列号会作为入参）、初始化证明会话。Device Security Kit初始化证明会话完成后会返回给应用匿名证书链。
通过Camera Kit配置安全相机输入输出流，重点是配置安全数据流，注册安全数据流每帧安全图像回调监听。
解析安全数据流每帧安全图像，在服务器侧完成安全图像的签名验证。
说明

当前文档主要说明通过Camera Kit完成的步骤，证明会话相关步骤需通过Device Security Kit完成，具体可参考可信应用服务-安全摄像头。

开发步骤

详细的API说明请参考Camera API参考。

导入依赖，需要导入相机框架相关领域依赖。

import { camera } from '@kit.CameraKit';
import { image } from '@kit.ImageKit';

选择支持安全相机的设备。

通过CameraManager中的getSupportedSceneModes方法，可以获取当前设备支持的所有模式，如果当前设备支持安全相机模式，即可使用该设备做后续安全相机操作。

当前安全相机仅支持手机前置镜头。

function isSecureCamera(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice): boolean {
  let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
  const secureMode = sceneModes.find(mode => mode === camera.SceneMode.SECURE_PHOTO);
  if (secureMode) {
    console.info('current device support secure camera!');
    return true;
  } else {
    console.info('current device not support secure camera!');
    return false;
  }
}


let secureCamera: camera.CameraDevice;


function getSecureCamera(cameraManager: camera.CameraManager): void {
  let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
  for (let index = 0; index < cameraArray.length; index++) {
    if (isSecureCamera(cameraManager, cameraArray[index])) {
      secureCamera = cameraArray[index];
    }
  }
}

查询相机设备在安全模式下支持的输出能力。

通过CameraManager的getSupportedOutputCapability方法，可获取设备在安全模式下支持的输出能力。

当前安全相机仅支持输出预览流，推荐预览流使用640 * 480分辨率。

function getSupportedOutputCapability(cameraManager: camera.CameraManager, secureCamera: camera.CameraDevice): void {
  let outputCap: camera.CameraOutputCapability =
    cameraManager.getSupportedOutputCapability(secureCamera, camera.SceneMode.SECURE_PHOTO);
  let previewProfilesArray: Array<camera.Profile> = outputCap.previewProfiles;
}

创建设备输入输出。

安全相机需要创建两路输出流：

一路是普通的预览流，用于界面显示，普通预览流的创建流程请参考预览开发指导。

一路是安全数据流，用于安全服务校验，安全数据流需要通过image.createImageReceiver创建图像接收类ImageReceiver，再通过其getReceivingSurfaceId方法获取surfaceId。

说明

安全数据流没有单独的数据类型，同属于预览流，输出能力与预览流保持一致，创建ImageReceiver仅支持JPEG格式。

async function createInputAndOutputs(cameraManager: camera.CameraManager,
                                     secureCamera: camera.CameraDevice,
                                     previewProfile: camera.Profile,
                                     previewSurfaceId: string): Promise<void> {
  // 创建输入流
  let cameraInput: camera.CameraInput = cameraManager.createCameraInput(secureCamera);
  // 创建普通预览输出流
  let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, previewSurfaceId);
  // 创建安全数据输出流
  const receiver: image.ImageReceiver =
    image.createImageReceiver({ width: previewProfile.size.width, height: previewProfile.size.height },
                              image.ImageFormat.JPEG, 8);
  const secureSurfaceId: string = await receiver.getReceivingSurfaceId();
  let secureOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, secureSurfaceId);
}

打开安全设备。

CameraInput提供了open(isSecureEnabled)方法用于打开安全相机并返回安全摄像头序列号，该序列号是安全模块创建证明会话的必需参数。

仅当isSecureEnabled为true时，才会打开安全相机，并有安全序列号返回。

async function openCamera(cameraInput: camera.CameraInput) {
  const seqId: bigint = await cameraInput.open(true);
}

使用Device Security Kit的能力，创建证明密钥、打开证明会话。请参考Device Security Kit（设备安全服务）的开发指导：可信应用服务-安全摄像头。

创建安全相机会话，配流启流。

创建安全相机模式的会话，将输入流、输出流加入会话，需要将安全数据流通过SecureSession的addSecureOutput方法标记成安全输出。

async function openSession(cameraManager: camera.CameraManager,
                           cameraInput: camera.CameraInput,
                           previewOutput: camera.PreviewOutput,
                           secureOutput: camera.PreviewOutput): Promise<void> {
  try {
    let secureSession: camera.SecureSession = cameraManager.createSession(camera.SceneMode.SECURE_PHOTO);
    if (secureSession === undefined) {
      console.error('create secureSession failed!');
    }
    secureSession.beginConfig();
    secureSession.addInput(cameraInput);
    secureSession.addOutput(previewOutput);
    secureSession.addOutput(secureOutput);
    secureSession.addSecureOutput(secureOutput); // 把secureOutput标记成安全输出
    await secureSession.commitConfig();
    await secureSession.start();
  } catch (err) {
    console.error('openSession failed!');
  }
}

安全模式会话正常启动后，预览流和安全数据流数据逐帧上报，安全数据流每帧数据可以通过ImageReceiver注册imageArrival回调获取。

function onBuffer(receiver: image.ImageReceiver): void {
  receiver.on('imageArrival', () => {
    // 从ImageReceiver读取下一张图片
    receiver.readNextImage().then((img: image.Image) => {
      // 从图像中获取组件缓存
      img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
        // 安全数据流内容，应用通过解析该buffer内容完成签名认证
        const buffer = component.byteBuffer;
        console.info('Succeeded in getting component byteBuffer.');
      })
    })
  })
}

解析安全数据流每帧安全图像，在服务器侧完成安全图像的签名验证。

如果有在端侧验证图像数据或地理位置数据签名的需求，可参考验证签名中与安全图像相关的部分。

释放安全相机，使用Session的release方法。

相机旋转角度的术语
动态调整预览帧率(ArkTS)
