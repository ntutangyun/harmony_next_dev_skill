# 图像跟踪（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-image-track_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.1.0(18)开始，图像跟踪能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持图像跟踪特性（ARENGINE_FEATURE_TYPE_IMAGE）。

接口说明

以下接口为AR图像跟踪相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
HMS_AREngine_ARSession_Create	创建一个新的AREngine_ARSession会话。
HMS_AREngine_ARSession_Update	更新AR Engine的计算结果。
HMS_AREngine_ARSession_Configure	配置AREngine_ARSession会话。
HMS_AREngine_ARFrame_Create	创建一个新的AREngine_ARFrame对象，将指针存储到中*outFrame。
HMS_AREngine_ARSession_SetDisplayGeometry	设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。
HMS_AREngine_ARSession_SetCameraGLTexture	设置可用于存储相机预览流数据的openGL纹理。
HMS_AREngine_ARSession_GetAllTrackables	获取所有指定类型的可跟踪对象集合。
HMS_AREngine_ARTrackableList_AcquireItem	从可跟踪列表中获取指定index的对象。
HMS_AREngine_ARPlane_GetCenterPose	获取从平面的局部坐标系到世界坐标系转换的位姿信息。
HMS_AREngine_ARFrame_AcquireCamera	获取当前帧的相机参数对象。
HMS_AREngine_ARPose_Create	分配并初始化一个新的位姿对象。
HMS_AREngine_ARCamera_GetPose	获取当前相机对象在AR世界空间中的位姿。
HMS_AREngine_ARAugmentedImageDatabase_Create	创建一个空的跟踪图像数据。
HMS_AREngine_ARAugmentedImageDatabase_AddImage	将图像添加到图像数据库并输出对应图像的索引。
HMS_AREngine_ARTrackableList_GetSize	获取此列表中的可跟踪对象的数量。
HMS_AREngine_ARAugmentedImage_GetCenterPose	获取跟踪图像中心点在世界坐标系中的位姿信息。
HMS_AREngine_ARAugmentedImage_GetExtendX	以图像的中心点为坐标原点，获取在X轴上的宽度值。单位：米。
HMS_AREngine_ARAugmentedImage_GetExtendZ	以图像的中心点为坐标原点，获取在Z轴上的高度值。单位：米。
HMS_AREngine_ARAugmentedImageDatabase_Serialize	序列化特征数据库，在添加完图片后，可以将特征库序列化为buffer，用户可以保存此buffer以供下次使用。
HMS_AREngine_ARAugmentedImageDatabase_Deserialize	反序列化特征数据库，用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。

开发步骤

[h2]声明Native接口

开发者可参考AR物体摆放章节的声明Native接口。

[h2]创建UI界面

首先创建一个起始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。配置路由进行页面间跳转，页面路由配置详细可查看组件导航(Navigation) (推荐)。

import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder() {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();
  private imagePathArray: string[] = [];

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {

            try {
              let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
              photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
              photoOption.maxSelectNumber = 50;
              photoOption.isEditSupported = false;
              let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

              let photoResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoOption);
              if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
                this.imagePathArray = photoResult.photoUris;
                this.pageInfos.pushDestinationByName('ARImageByAdd', this.imagePathArray);
              }
            } catch (error) {
              const err: BusinessError = error as BusinessError;
              logger.error(`Failed to select by photoPicker. Code: ${err.code}, message is ${err.message}.`);
            }
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
              logger.error(
                `ARImageByDatabase Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
            })
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
}

创建一个ARImageByAdd.ets，用于选择图片，使用XComponent组件加载相机预览画面，并定时触发每一帧绘制。

import { taskpool } from '@kit.ArkTS';
import { display } from '@kit.ArkUI';
import { BusinessError, emitter, systemDateTime } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByAddBuilder() {
  ARImageByAdd();
}

@Component
struct ARImageByAdd {
  pageInfos: NavPathStack = new NavPathStack();
  @State addImageLog: string = '';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State imageTotalNumbers: number = 0;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private imageAddFailedNumbers: number = 0;
  private imageAddNumbers: number = 0;
  private imagePathList: string[] = [];
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State private isImageAddComplete: boolean = false;
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (!this.isUpdate || !this.isImageAddComplete || this.imageAddNumbers === 0) {
                return;
              }
              arEngineDemo.update(this.idStr);
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })

        Text(this.context.resourceManager.getStringByNameSync('add_image_msg_count') +
          this.imageTotalNumbers.toString() + '/' + this.imagePathList.length.toString() + '\n ' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_success') +
          this.imageAddNumbers + ' \n' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_fail') +
          this.imageAddFailedNumbers + '\n' + this.addImageLog)
          .width(300)
          .textAlign(TextAlign.Center)
          .fontColor(Color.Red)
          .visibility(!this.isImageAddComplete ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onBackPressed(() => {
      logger.error('Failed to onBackPressed.');
      return false;
    })
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      try {
        logger.info(`Image path length: ${this.imagePathList.length}.`);
        this.RegisterAddImageCallback();
        taskpool.execute(addImage, this.idStr, this.imagePathList, errcode).then(() => {
          logger.info('Add image task complete.');
          emitter.emit('checkAddImageResult');
        }).catch((err: BusinessError) => {
          logger.error(`Failed to execute taskpool. Code: ${err.code}, message is ${err.message}.`);
        })
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(`Failed to promise options error. Code: ${err.code}, message is ${err.message}.`);
      }
    })
    .onWillDisappear(() => {
      if (this.imageAddNumbers > 0) {
        arEngineDemo.saveImageDataBaseToLocal(this.idStr, this.context.filesDir);
      }
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.imagePathList = context.pathInfo.param as string[];
    })
    .hideTitleBar(true)
    .hideBackButton(false)
    .hideToolBar(true)
  }
  // ...
}

let errcode: Map<number, string> = new Map<number, string>([[0, 'success'], [1, 'size not match'],
  [2, 'too bright or too dark'], [3, 'image color is relatively single'], [4, 'other error']]);

// Asynchronously execute the task of adding pictures
@Concurrent
async function addImage(componentId: string, imagePathList: string[],
  errcode: Map<number, string>): Promise<void> {
  // ...
  }
}

创建一个ARImageByDatabase.ets，用于加载本地数据库，加载相机预览画面，并定时触发每一帧绘制。

import { display } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByDatabaseBuilder() {
  ARImageByDatabase();
}

@Component
struct ARImageByDatabase {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      arEngineDemo.setPath(this.idStr, this.context.filesDir);

      let imageCountInDatabase: number = arEngineDemo.getImageCount(this.idStr);
      logger.info(`ImageCountInDatabase: ${imageCountInDatabase}.`);
      if (imageCountInDatabase <= 0) {
        try {
          this.showDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to showDialog. Code is ${err.code}, message is ${err.message}`);
        }
      }
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  showDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked.');
          this.pageInfos.pop();
        }
      }]
    })
  }
}

配置路由进行页面间跳转，页面路由配置详细可查看组件导航(Navigation) (推荐)。

[h2]引入AR Engine

开发者可参考AR物体摆放章节的引入AR Engine。

[h2]创建AR会话

创建AR会话并配置ARType为图像跟踪。

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// Set AR type to ARENGINE_TYPE_IMAGE
CHECK(HMS_AREngine_ARConfig_SetARType(mArSession, arConfig, ARENGINE_TYPE_IMAGE));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));

[h2]创建跟踪图像数据库并添加图像

1.调用HMS_AREngine_ARAugmentedImageDatabase_Create函数，创建跟踪图像数据库。

CHECK(HMS_AREngine_ARAugmentedImageDatabase_Create(&mDataBase));

2.调用HMS_AREngine_ARAugmentedImageDatabase_AddImage函数，添加图像到数据库，将添加失败的结果保存在reason中。

AREngine_ARAugmentedImageSource image;
 // ...
uint32_t outputIndex = 0;
AREngine_ARAddAugmentedImageReason reason = ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE;
auto addRet = HMS_AREngine_ARAugmentedImageDatabase_AddImage(dataBase, &image, &outputIndex, &reason);

[h2]识别环境中的可跟踪图像

调用HMS_AREngine_ARSession_GetAllTrackables函数，检测当前环境中的所有跟踪图像，并将结果存放在augmentList中。

AREngine_ARTrackableList *augmentList = nullptr;
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &augmentList));
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_AUGMENTED_IMAGE, augmentList));

[h2]获取环境中的可跟踪图像数量

调用HMS_AREngine_ARTrackableList_GetSize函数获取平面数量，结果存放在augmentSize中。

int32_t augmentSize = 0;
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, augmentList, &augmentSize));

应用环境中，可能存在0个、1个或多个可跟踪图像。

当augmentSize等于0时，表示当前环境中不存在可跟踪图像。

当augmentSize等于1时，表示当前环境中仅存在1个可跟踪图像。

当augmentSize大于1时，表示当前环境中存在多个可跟踪图像。

[h2]获取跟踪图像示例

当存在1个或多个跟踪图像时，可以依次遍历augmentList获取所有跟踪图像。

for (int i = 0; i < augmentSize; ++i) {
    // 遍历所有可跟踪对象，根据应用进行处理。
}

对于第i个跟踪图像，创建并获取跟踪对象，并将其转化为跟踪图像对象AREngine_ARAugmentedImage。

AREngine_ARTrackable *augment = nullptr;
CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, augmentList, i, &augment));
AREngine_ARAugmentedImage *arImage = reinterpret_cast<AREngine_ARAugmentedImage*>(augment);

[h2]获取跟踪图像中心点在世界坐标系中的位姿信息

调用HMS_AREngine_ARAugmentedImage_GetCenterPose函数，获取跟踪图像中心点的位姿信息，位姿信息可参考获取设备位姿。

AREngine_ARPose *imagePose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &imagePose);
auto getPoseResult = HMS_AREngine_ARAugmentedImage_GetCenterPose(arSession, image, imagePose);

[h2]获取跟踪图像的宽度

调用HMS_AREngine_ARAugmentedImage_GetExtendX函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到X轴上的估计值。

float extent_x;
HMS_AREngine_ARAugmentedImage_GetExtendX(arSession, image, &extent_x);

调用HMS_AREngine_ARAugmentedImage_GetExtendZ函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到Z轴上的估计值。

float extent_z;
HMS_AREngine_ARAugmentedImage_GetExtendZ(arSession, image, &extent_z);

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder() {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();
  private imagePathArray: string[] = [];

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {

            try {
              let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
              photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
              photoOption.maxSelectNumber = 50;
              photoOption.isEditSupported = false;
              let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

              let photoResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoOption);
              if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
                this.imagePathArray = photoResult.photoUris;
                this.pageInfos.pushDestinationByName('ARImageByAdd', this.imagePathArray);
              }
            } catch (error) {
              const err: BusinessError = error as BusinessError;
              logger.error(`Failed to select by photoPicker. Code: ${err.code}, message is ${err.message}.`);
            }
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
              logger.error(
                `ARImageByDatabase Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
            })
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
}
```

### Code block 2

```
import { taskpool } from '@kit.ArkTS';
import { display } from '@kit.ArkUI';
import { BusinessError, emitter, systemDateTime } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByAddBuilder() {
  ARImageByAdd();
}

@Component
struct ARImageByAdd {
  pageInfos: NavPathStack = new NavPathStack();
  @State addImageLog: string = '';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State imageTotalNumbers: number = 0;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private imageAddFailedNumbers: number = 0;
  private imageAddNumbers: number = 0;
  private imagePathList: string[] = [];
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State private isImageAddComplete: boolean = false;
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (!this.isUpdate || !this.isImageAddComplete || this.imageAddNumbers === 0) {
                return;
              }
              arEngineDemo.update(this.idStr);
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })

        Text(this.context.resourceManager.getStringByNameSync('add_image_msg_count') +
          this.imageTotalNumbers.toString() + '/' + this.imagePathList.length.toString() + '\n ' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_success') +
          this.imageAddNumbers + ' \n' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_fail') +
          this.imageAddFailedNumbers + '\n' + this.addImageLog)
          .width(300)
          .textAlign(TextAlign.Center)
          .fontColor(Color.Red)
          .visibility(!this.isImageAddComplete ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onBackPressed(() => {
      logger.error('Failed to onBackPressed.');
      return false;
    })
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      try {
        logger.info(`Image path length: ${this.imagePathList.length}.`);
        this.RegisterAddImageCallback();
        taskpool.execute(addImage, this.idStr, this.imagePathList, errcode).then(() => {
          logger.info('Add image task complete.');
          emitter.emit('checkAddImageResult');
        }).catch((err: BusinessError) => {
          logger.error(`Failed to execute taskpool. Code: ${err.code}, message is ${err.message}.`);
        })
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(`Failed to promise options error. Code: ${err.code}, message is ${err.message}.`);
      }
    })
    .onWillDisappear(() => {
      if (this.imageAddNumbers > 0) {
        arEngineDemo.saveImageDataBaseToLocal(this.idStr, this.context.filesDir);
      }
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.imagePathList = context.pathInfo.param as string[];
    })
    .hideTitleBar(true)
    .hideBackButton(false)
    .hideToolBar(true)
  }
  // ...
}

let errcode: Map<number, string> = new Map<number, string>([[0, 'success'], [1, 'size not match'],
  [2, 'too bright or too dark'], [3, 'image color is relatively single'], [4, 'other error']]);

// Asynchronously execute the task of adding pictures
@Concurrent
async function addImage(componentId: string, imagePathList: string[],
  errcode: Map<number, string>): Promise<void> {
  // ...
  }
}
```

### Code block 3

```
import { display } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByDatabaseBuilder() {
  ARImageByDatabase();
}

@Component
struct ARImageByDatabase {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      arEngineDemo.setPath(this.idStr, this.context.filesDir);

      let imageCountInDatabase: number = arEngineDemo.getImageCount(this.idStr);
      logger.info(`ImageCountInDatabase: ${imageCountInDatabase}.`);
      if (imageCountInDatabase <= 0) {
        try {
          this.showDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to showDialog. Code is ${err.code}, message is ${err.message}`);
        }
      }
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  showDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked.');
          this.pageInfos.pop();
        }
      }]
    })
  }
}
```

### Code block 4

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// Set AR type to ARENGINE_TYPE_IMAGE
CHECK(HMS_AREngine_ARConfig_SetARType(mArSession, arConfig, ARENGINE_TYPE_IMAGE));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### Code block 5

```
CHECK(HMS_AREngine_ARAugmentedImageDatabase_Create(&mDataBase));
```

### Code block 6

```
AREngine_ARAugmentedImageSource image;
 // ...
uint32_t outputIndex = 0;
AREngine_ARAddAugmentedImageReason reason = ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE;
auto addRet = HMS_AREngine_ARAugmentedImageDatabase_AddImage(dataBase, &image, &outputIndex, &reason);
```

### Code block 7

```
AREngine_ARTrackableList *augmentList = nullptr;
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &augmentList));
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_AUGMENTED_IMAGE, augmentList));
```

### Code block 8

```
int32_t augmentSize = 0;
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, augmentList, &augmentSize));
```

### Code block 9

```
for (int i = 0; i < augmentSize; ++i) {
    // 遍历所有可跟踪对象，根据应用进行处理。
}
```

### Code block 10

```
AREngine_ARTrackable *augment = nullptr;
CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, augmentList, i, &augment));
AREngine_ARAugmentedImage *arImage = reinterpret_cast<AREngine_ARAugmentedImage*>(augment);
```

### Code block 11

```
AREngine_ARPose *imagePose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &imagePose);
auto getPoseResult = HMS_AREngine_ARAugmentedImage_GetCenterPose(arSession, image, imagePose);
```

### Code block 12

```
float extent_x;
HMS_AREngine_ARAugmentedImage_GetExtendX(arSession, image, &extent_x);
```

### Code block 13

```
float extent_z;
HMS_AREngine_ARAugmentedImage_GetExtendZ(arSession, image, &extent_z);
```
