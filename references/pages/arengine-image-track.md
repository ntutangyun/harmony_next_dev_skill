# 图像跟踪（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-image-track_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.1.0(18)开始，图像跟踪能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持图像跟踪特性（ARENGINE_FEATURE_TYPE_IMAGE）。

接口说明

图像识别主要依赖ARAugmentedImageDatabase、ARImage，以下接口为图像识别相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
arEngine.createARAugmentedImageDatabase	创建一个增强型图像数据库。
ARAugmentedImageDatabase.deserialize	将增强图像数据库数据反序列化为一个新的增强图像数据库对象。
ARAugmentedImageDatabase.serialize	将增强图像数据库序列化为一个缓冲区。
ARAugmentedImageDatabase.addImage	将图像添加到图像数据库，并输出对应图像的索引。
ARAugmentedImageDatabase.getImageCount	获取图像数据库中图像的数量。
ARAugmentedImageDatabase.getCapacity	可以添加的最大图像数量。
ARAugmentedImageDatabase.getImageAddMode	获取图片添加模式。
ARAugmentedImageDatabase.setImageAddMode	设置图片添加模式。
ARAugmentedImageDatabase.release	释放增强图像数据库对象ARAugmentedImageDatabase占用的内存。
ARImage.release	释放相机视频流帧对象ARImage占用的内存。
ARAugmentedImage	表示可被追踪的增强图像对象。

开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者XComponent绘制识别的平面。关于AGP的介绍可以查看ArkGraphics 3D简介和AGP引擎。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话ARViewContext，用于管理AR Engine的系统状态。AR会话ARViewContext的创建可以参考管理AR会话章节。

[h2]创建UI页面

首先创建一个初始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。并配置路由进行页面间跳转，页面路由配置详细可查看组件导航(Navigation) (推荐)。

[h2]ARImage页面

import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder(): void {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.chooseImageToTrack();
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.loadDatabaseToTrack();
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private chooseImageToTrack(): void {
    try {
      let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      photoOption.maxSelectNumber = 50; // Default
      photoOption.isEditSupported = false;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

      photoPicker.select(photoOption).then((photoResult) => {
        if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
          this.pageInfos.pushDestinationByName('ARImageByAdd', photoResult.photoUris).catch((err: BusinessError) => {
            logger.error(`Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
          });
        }
      }).catch((err: BusinessError) => {
        logger.warn(`Failed to select photos. Code is ${err.code}, message is ${err.message}.`);
      })
    } catch (error) {
      logger.error(`Failed to select by photoPicker. Code: ${error.code}.`);
    }
  }

  private loadDatabaseToTrack(): void {
    this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
      logger.error(`ARImageByDatabase failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
    })
  }
}

[h2]ARImageByAdd页面

加载本地图片模式。

选择本地图片进行图像识别能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {
  CustomGeometry,
  Geometry,
  Image,
  Material,
  MaterialType,
  MeshResource,
  Node,
  PrimitiveTopology,
  Scene,
  SceneResourceFactory,
  Shader,
  ShaderMaterial,
  Vec3
} from '@kit.ArkGraphics3D';
import { collections } from '@kit.ArkTS';
import { Matrix4 } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { logger } from '../utils/Logger';
import { calculatePoint, createImageIndex, getImageVertices, getResourceString } from '../utils/Utils';

配置页面路由信息，定义数据库dataBase。

@Builder
export function ARImageByAddBuilder(): void {
  ARImageByAdd();
}

let dataBase: arEngine.ARAugmentedImageDatabase;

在设备界面上显示图片添加情况，无可用图片则弹窗提示，加载AR场景。

@Component
struct ARImageByAdd {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State addFailedImageCounts: number = 0;
  @State succeedImageCounts: number = 0;
  @State addFailedMessage: string[] = [];
  private imagePathArray: string[] = [];
  @State totalImageCounts: number = this.imagePathArray.length;
  // When destroy is set to true, the addImage function is used to determine whether to continue adding images.
  private isProgramExits: boolean = false;
  private isSaveDatabase: boolean = false;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        Column() {
          Text(`${getResourceString(this.context, 'add_image_msg_count')} ${this.succeedImageCounts +
            this.addFailedImageCounts} / ${this.totalImageCounts}`)
          Text(`${getResourceString(this.context, 'add_image_msg_success') + this.succeedImageCounts}`)
          Text(`${getResourceString(this.context, 'add_image_msg_fail') + this.addFailedImageCounts}`)

          if (this.addFailedMessage) {
            ForEach(this.addFailedMessage, (item: string) => {
              Text(`${item}`)
                .fontColor(Color.Red)
            }, (item: string) => item)
          }
        }
        .visibility(this.addFailedImageCounts + this.succeedImageCounts < this.totalImageCounts ? Visibility.Visible :
          Visibility.None)
        .foregroundColor(Color.Red)
        .zIndex(1)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

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
      arEngine.createARAugmentedImageDatabase()
        .then((arDataBase) => {
          dataBase = arDataBase;

          this.addImage(dataBase).then(() => {
            if (this.addFailedImageCounts === this.totalImageCounts) {
              this.ShowDialog(getResourceString(this.context, 'invalid_image_added'));
            }
            if (this.totalImageCounts === this.succeedImageCounts + this.addFailedImageCounts) {
              this.initARView();
              this.isSaveDatabase = true;
            }
          })
        }).catch((err: BusinessError) => {
        logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
      })
    })
    .onWillDisappear(async () => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.imagePathArray = context.pathInfo.param as string[];
      this.totalImageCounts = this.imagePathArray.length;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  // Asynchronously execute the task of adding pictures
  async addImage(dataBase: arEngine.ARAugmentedImageDatabase): Promise<void> {
    // ...
  }

  private initARView(): void {
    // ...
  }

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      this.isProgramExits = true;
      if (this.isSaveDatabase) {
        saveBufferToLocal(dataBase, this.context);
      }

      await dataBase.release();
      await this.arContext?.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }

  private ShowDialog(msg: string): void {
    // ...
  }
}

退出应用时，缓存图片特征到本地。

// Save the file locally
async function saveBufferToLocal(dataBase: arEngine.ARAugmentedImageDatabase, context: Context): Promise<void> {
  let filesDir: string = context.filesDir;
  let file: fileIo.File;
  try {
    file = fileIo.openSync(filesDir + '/test.bin',
      fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to open database. Code is ${err.code}, message is ${err.message}.`);
    return;
  }
  let buf: ArrayBuffer;
  try {
    buf = await dataBase.serialize();
    try {
      let writeLen: number = fileIo.writeSync(file.fd, buf);
      logger.info(`The length of buffer is: ${writeLen}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to write database. Code is ${err.code}, message is ${err.message}.`);
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to serialize database. Code is ${err.code}, message is ${err.message}.`);
  }

  try {
    fileIo.closeSync(file);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
  }
}

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，识别到目标图像则打印日志。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session || !dataBase) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    this.scene = ctx.scene;

    try {
      let imageNumber: number = dataBase.getImageCount();
      logger.info(`The number of images in the database is ${imageNumber}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get image count. Code is ${err.code}, message is ${err.message}`);
    }

    try {
      let imageCapacity: number = dataBase.getCapacity();
      logger.info(`The dataBase image capacity is: ${imageCapacity}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
    }


    let trackables: arEngine.ARTrackable[];
    try {
      trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
      return;
    }

    // The target image color is controlled by the file plane.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    logger.info(`The image trackable size: ${trackables.length}.`);
    let validImage: number = 0;
    for (let i = 0; i < trackables.length; ++i) {
      if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
        let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
        if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
          continue;
        }
        validImage += 1;
        let centerPose: arEngine.ARPose;
        try {
          centerPose = arImage.getPose();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        // ...
      }
    }
    // ...
  }
}

const errcode: collections.Map<number, string> = new collections.Map<number, string>([
  [0, 'success'],
  [1, 'size not match'],
  [2, 'too bright or too dark'],
  [3, 'image color is relatively single'],
  [4, 'other error']
])

[h2]ARImageByDatabase页面

加载本地数据库模式。

选择本地数据库进行图像识别能力所需要导入的模块如下：

import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {
  CustomGeometry,
  Geometry,
  Image,
  Material,
  MaterialType,
  MeshResource,
  Node,
  PrimitiveTopology,
  Scene,
  SceneResourceFactory,
  Shader,
  ShaderMaterial,
  Vec3
} from '@kit.ArkGraphics3D';
import { Matrix4 } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { logger } from '../utils/Logger';
import { calculatePoint, createImageIndex, getImageVertices } from '../utils/Utils';

配置页面路由信息，定义数据库dataBase。

@Builder
export function ARImageByDatabaseBuilder(): void {
  ARImageByDatabase();
}

let dataBase: arEngine.ARAugmentedImageDatabase;

加载AR场景，加载图像数据库，无可用数据库则弹窗提示。

@Component
struct ARImageByDatabase {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;

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
    .onAppear(() => {
      arEngine.createARAugmentedImageDatabase()
        .then((arDataBase) => {
          dataBase = arDataBase;

          try {
            let databaseBuffer: ArrayBuffer = readBuffer(this.context);
            dataBase.deserialize(databaseBuffer).then(() => {
              this.initARView();
            })
              .catch((err: BusinessError) => {
                logger.error(`Failed to deserialize database. Code is ${err.code}, message is ${err.message}.`);
              })
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}.`);
            this.ShowDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
          }
        })
        .catch((err: BusinessError) => {
          logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
        })
    })
    .onWillDisappear(async () => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  ShowDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
        .animation({ duration: 1000, curve: Curve.Sharp })
        .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 })
          .animation({ duration: 1000, curve: Curve.Sharp })),
        TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
          .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
            .animation({ duration: 100, curve: Curve.Smooth }))),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked.');
          this.pageInfos.pop();
          return;
        }
      }]
    })
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.IMAGE,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.DISABLED,
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
    if (!this.arContext) {
      return;
    }
    try {
      await dataBase.release();
      await this.arContext?.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }
}

读取本地数据库缓存文件的方法。

// Read local files into buffer
function readBuffer(context: Context): ArrayBuffer {
  let filesDir: string = context.filesDir;
  let srcFile: fileIo.File;
  try {
    srcFile = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to open file. Code is ${err.code}, message is ${err.message}.`);
    return new ArrayBuffer(0);
  }
  let fileStat: fileIo.Stat;
  let buf: ArrayBuffer;
  try {
    fileStat = fileIo.statSync(srcFile.fd);
    // Read the contents of the source file and write it to the destination file
    let readSize: number = 0;
    buf = new ArrayBuffer(fileStat.size);
    let readOptions: ReadOptions = {
      offset: readSize,
      length: fileStat.size
    }
    try {
      fileIo.readSync(srcFile.fd, buf, readOptions);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to read buffer. Code is ${err.code}, message is ${err.message}.`);
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to get file stat. Code is ${err.code}, message is ${err.message}.`);
    return new ArrayBuffer(0);
  }


  try {
    fileIo.closeSync(srcFile);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
  }
  return buf;
}

调用ARViewCallback，使用其中的onFrameUpdate方法进行帧数据更新，识别到目标图像则打印日志。

class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session || !dataBase) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    this.scene = ctx.scene;

    try {
      let imageNumber: number = dataBase.getImageCount();
      logger.info(`The number of images in the database is ${imageNumber}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to got image count. Code is ${err.code}, message is ${err.message}.`);
    }

    try {
      let imageCapacity: number = dataBase.getCapacity();
      logger.info(`The dataBase image capacity = ${imageCapacity}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to getCapacity. Code is ${err.code}, message is ${err.message}`);
    }

    let trackables: arEngine.ARTrackable[] = [];
    try {
      trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get all trackables. Code is ${err.code}, message is ${err.message}`);
    }

    // The target image color is controlled by the file plane.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    logger.info(`The image trackable size: ${trackables.length}.`);
    let validImage: number = 0;
    for (let i = 0; i < trackables.length; ++i) {
      if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
        let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
        if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
          continue;
        }
        validImage++;
        let centerPose: arEngine.ARPose;
        try {
          centerPose = arImage.getPose();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        // ...
      }
    }
    // ...
  }
}

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder(): void {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.chooseImageToTrack();
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.loadDatabaseToTrack();
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private chooseImageToTrack(): void {
    try {
      let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      photoOption.maxSelectNumber = 50; // Default
      photoOption.isEditSupported = false;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

      photoPicker.select(photoOption).then((photoResult) => {
        if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
          this.pageInfos.pushDestinationByName('ARImageByAdd', photoResult.photoUris).catch((err: BusinessError) => {
            logger.error(`Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
          });
        }
      }).catch((err: BusinessError) => {
        logger.warn(`Failed to select photos. Code is ${err.code}, message is ${err.message}.`);
      })
    } catch (error) {
      logger.error(`Failed to select by photoPicker. Code: ${error.code}.`);
    }
  }

  private loadDatabaseToTrack(): void {
    this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
      logger.error(`ARImageByDatabase failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
    })
  }
}
```

### Code block 2

```
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {
  CustomGeometry,
  Geometry,
  Image,
  Material,
  MaterialType,
  MeshResource,
  Node,
  PrimitiveTopology,
  Scene,
  SceneResourceFactory,
  Shader,
  ShaderMaterial,
  Vec3
} from '@kit.ArkGraphics3D';
import { collections } from '@kit.ArkTS';
import { Matrix4 } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { logger } from '../utils/Logger';
import { calculatePoint, createImageIndex, getImageVertices, getResourceString } from '../utils/Utils';
```

### Code block 3

```
@Builder
export function ARImageByAddBuilder(): void {
  ARImageByAdd();
}

let dataBase: arEngine.ARAugmentedImageDatabase;
```

### Code block 4

```
@Component
struct ARImageByAdd {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State addFailedImageCounts: number = 0;
  @State succeedImageCounts: number = 0;
  @State addFailedMessage: string[] = [];
  private imagePathArray: string[] = [];
  @State totalImageCounts: number = this.imagePathArray.length;
  // When destroy is set to true, the addImage function is used to determine whether to continue adding images.
  private isProgramExits: boolean = false;
  private isSaveDatabase: boolean = false;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        Column() {
          Text(`${getResourceString(this.context, 'add_image_msg_count')} ${this.succeedImageCounts +
            this.addFailedImageCounts} / ${this.totalImageCounts}`)
          Text(`${getResourceString(this.context, 'add_image_msg_success') + this.succeedImageCounts}`)
          Text(`${getResourceString(this.context, 'add_image_msg_fail') + this.addFailedImageCounts}`)

          if (this.addFailedMessage) {
            ForEach(this.addFailedMessage, (item: string) => {
              Text(`${item}`)
                .fontColor(Color.Red)
            }, (item: string) => item)
          }
        }
        .visibility(this.addFailedImageCounts + this.succeedImageCounts < this.totalImageCounts ? Visibility.Visible :
          Visibility.None)
        .foregroundColor(Color.Red)
        .zIndex(1)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

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
      arEngine.createARAugmentedImageDatabase()
        .then((arDataBase) => {
          dataBase = arDataBase;

          this.addImage(dataBase).then(() => {
            if (this.addFailedImageCounts === this.totalImageCounts) {
              this.ShowDialog(getResourceString(this.context, 'invalid_image_added'));
            }
            if (this.totalImageCounts === this.succeedImageCounts + this.addFailedImageCounts) {
              this.initARView();
              this.isSaveDatabase = true;
            }
          })
        }).catch((err: BusinessError) => {
        logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
      })
    })
    .onWillDisappear(async () => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.imagePathArray = context.pathInfo.param as string[];
      this.totalImageCounts = this.imagePathArray.length;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  // Asynchronously execute the task of adding pictures
  async addImage(dataBase: arEngine.ARAugmentedImageDatabase): Promise<void> {
    // ...
  }

  private initARView(): void {
    // ...
  }

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      this.isProgramExits = true;
      if (this.isSaveDatabase) {
        saveBufferToLocal(dataBase, this.context);
      }

      await dataBase.release();
      await this.arContext?.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }

  private ShowDialog(msg: string): void {
    // ...
  }
}
```

### Code block 5

```
// Save the file locally
async function saveBufferToLocal(dataBase: arEngine.ARAugmentedImageDatabase, context: Context): Promise<void> {
  let filesDir: string = context.filesDir;
  let file: fileIo.File;
  try {
    file = fileIo.openSync(filesDir + '/test.bin',
      fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to open database. Code is ${err.code}, message is ${err.message}.`);
    return;
  }
  let buf: ArrayBuffer;
  try {
    buf = await dataBase.serialize();
    try {
      let writeLen: number = fileIo.writeSync(file.fd, buf);
      logger.info(`The length of buffer is: ${writeLen}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to write database. Code is ${err.code}, message is ${err.message}.`);
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to serialize database. Code is ${err.code}, message is ${err.message}.`);
  }

  try {
    fileIo.closeSync(file);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
  }
}
```

### Code block 6

```
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session || !dataBase) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    this.scene = ctx.scene;

    try {
      let imageNumber: number = dataBase.getImageCount();
      logger.info(`The number of images in the database is ${imageNumber}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get image count. Code is ${err.code}, message is ${err.message}`);
    }

    try {
      let imageCapacity: number = dataBase.getCapacity();
      logger.info(`The dataBase image capacity is: ${imageCapacity}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
    }


    let trackables: arEngine.ARTrackable[];
    try {
      trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
      return;
    }

    // The target image color is controlled by the file plane.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    logger.info(`The image trackable size: ${trackables.length}.`);
    let validImage: number = 0;
    for (let i = 0; i < trackables.length; ++i) {
      if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
        let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
        if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
          continue;
        }
        validImage += 1;
        let centerPose: arEngine.ARPose;
        try {
          centerPose = arImage.getPose();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        // ...
      }
    }
    // ...
  }
}

const errcode: collections.Map<number, string> = new collections.Map<number, string>([
  [0, 'success'],
  [1, 'size not match'],
  [2, 'too bright or too dark'],
  [3, 'image color is relatively single'],
  [4, 'other error']
])
```

### Code block 7

```
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {
  CustomGeometry,
  Geometry,
  Image,
  Material,
  MaterialType,
  MeshResource,
  Node,
  PrimitiveTopology,
  Scene,
  SceneResourceFactory,
  Shader,
  ShaderMaterial,
  Vec3
} from '@kit.ArkGraphics3D';
import { Matrix4 } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { logger } from '../utils/Logger';
import { calculatePoint, createImageIndex, getImageVertices } from '../utils/Utils';
```

### Code block 8

```
@Builder
export function ARImageByDatabaseBuilder(): void {
  ARImageByDatabase();
}

let dataBase: arEngine.ARAugmentedImageDatabase;
```

### Code block 9

```
@Component
struct ARImageByDatabase {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;

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
    .onAppear(() => {
      arEngine.createARAugmentedImageDatabase()
        .then((arDataBase) => {
          dataBase = arDataBase;

          try {
            let databaseBuffer: ArrayBuffer = readBuffer(this.context);
            dataBase.deserialize(databaseBuffer).then(() => {
              this.initARView();
            })
              .catch((err: BusinessError) => {
                logger.error(`Failed to deserialize database. Code is ${err.code}, message is ${err.message}.`);
              })
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}.`);
            this.ShowDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
          }
        })
        .catch((err: BusinessError) => {
          logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
        })
    })
    .onWillDisappear(async () => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  ShowDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
        .animation({ duration: 1000, curve: Curve.Sharp })
        .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 })
          .animation({ duration: 1000, curve: Curve.Sharp })),
        TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
          .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
            .animation({ duration: 100, curve: Curve.Smooth }))),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked.');
          this.pageInfos.pop();
          return;
        }
      }]
    })
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.IMAGE,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.DISABLED,
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
    if (!this.arContext) {
      return;
    }
    try {
      await dataBase.release();
      await this.arContext?.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }
}
```

### Code block 10

```
// Read local files into buffer
function readBuffer(context: Context): ArrayBuffer {
  let filesDir: string = context.filesDir;
  let srcFile: fileIo.File;
  try {
    srcFile = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to open file. Code is ${err.code}, message is ${err.message}.`);
    return new ArrayBuffer(0);
  }
  let fileStat: fileIo.Stat;
  let buf: ArrayBuffer;
  try {
    fileStat = fileIo.statSync(srcFile.fd);
    // Read the contents of the source file and write it to the destination file
    let readSize: number = 0;
    buf = new ArrayBuffer(fileStat.size);
    let readOptions: ReadOptions = {
      offset: readSize,
      length: fileStat.size
    }
    try {
      fileIo.readSync(srcFile.fd, buf, readOptions);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to read buffer. Code is ${err.code}, message is ${err.message}.`);
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to get file stat. Code is ${err.code}, message is ${err.message}.`);
    return new ArrayBuffer(0);
  }


  try {
    fileIo.closeSync(srcFile);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
  }
  return buf;
}
```

### Code block 11

```
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session || !dataBase) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    this.scene = ctx.scene;

    try {
      let imageNumber: number = dataBase.getImageCount();
      logger.info(`The number of images in the database is ${imageNumber}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to got image count. Code is ${err.code}, message is ${err.message}.`);
    }

    try {
      let imageCapacity: number = dataBase.getCapacity();
      logger.info(`The dataBase image capacity = ${imageCapacity}.`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to getCapacity. Code is ${err.code}, message is ${err.message}`);
    }

    let trackables: arEngine.ARTrackable[] = [];
    try {
      trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get all trackables. Code is ${err.code}, message is ${err.message}`);
    }

    // The target image color is controlled by the file plane.shader
    let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
    this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
    this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
    this.material.colorShader = this.shader;
    (this.material as CustomerMaterial).blend = { enabled: true };

    logger.info(`The image trackable size: ${trackables.length}.`);
    let validImage: number = 0;
    for (let i = 0; i < trackables.length; ++i) {
      if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
        let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
        if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
          continue;
        }
        validImage++;
        let centerPose: arEngine.ARPose;
        try {
          centerPose = arImage.getPose();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        // ...
      }
    }
    // ...
  }
}
```
