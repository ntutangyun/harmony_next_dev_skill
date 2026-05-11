# 使用MovingPhotoView播放动态照片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/movingphotoview-guidelines_

MovingPhotoViewAttribute是用于配置MovingPhotoView组件属性的关键接口。API version 21及之前版本，导入MovingPhotoView组件后需要开发者手动导入MovingPhotoViewAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入MovingPhotoView组件后，会自动导入MovingPhotoViewAttribute，无需开发者手动导入。
MovingPhotoViewAttribute导入后，DevEco Studio会将其显示置灰，不影响开发者使用。

API version 21及之前版本：

import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';

API version 22及之后版本：

import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

获取动态照片对象（MovingPhoto）。

MovingPhoto对象需要通过photoAccessHelper接口创建或获取，MovingPhotoView只接收构造完成的MovingPhoto对象。

创建、获取的方式可参考访问和管理动态照片资源。

src: photoAccessHelper.MovingPhoto | undefined = undefined;

创建动态照片控制器（MovingPhotoViewController），用于控制动态照片的播放状态（如播放、停止）。

controller: MovingPhotoViewController = new MovingPhotoViewController();

创建动态照片组件。

以下参数取值仅为举例，具体每个属性的取值范围，可参考API文档：@ohos.multimedia.movingphotoview。

 // API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
 // API version 22及之后版本导入方式如下：
 import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';


 @Entry
 @Component
 struct Index {
   @State src: photoAccessHelper.MovingPhoto | undefined = undefined
   @State isMuted: boolean = false
   controller: MovingPhotoViewController = new MovingPhotoViewController();
   build() {
     Column() {
       MovingPhotoView({
         movingPhoto: this.src,
         controller: this.controller
       })
         // 是否静音播放，此处由按钮控制，默认值为false非静音播放。
         .muted(this.isMuted)
         // 视频显示模式，默认值为Cover。
         .objectFit(ImageFit.Cover)
         // 播放时触发。
         .onStart(() => {
           console.info('onStart');
         })
         // 播放结束触发。
         .onFinish(() => {
           console.info('onFinish');
         })
         // 播放停止触发。
         .onStop(() => {
           console.info('onStop')
         })
         // 出现错误触发。
         .onError(() => {
           console.error('onError');
         })
 
       Row() {
         // 按钮：开始播放。
         Button('start')
           .onClick(() => {
             this.controller.startPlayback()
           })
           .margin(5)
         // 按钮：停止播放。
         Button('stop')
           .onClick(() => {
             this.controller.stopPlayback()
           })
           .margin(5)
       }
       .alignItems(VerticalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .height('15%')
     }
   }
 }
效果展示

访问和管理动态照片资源
设备升级继承媒体文件访问权限
