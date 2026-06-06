# 媒体开发概览

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multimedia-development-overview_

HarmonyOS提供丰富的一站式媒体业务开放能力，开发者能够在系统上快速开发主流的媒体业务，满足常规高频使用场景，并提供优秀的性能表现。

媒体系统架构

媒体系统架构提供用户视觉、听觉信息的处理能力，例如音视频信息的采集、编码存储、解码播放等。操作系统实现中，根据不同的媒体信息处理内容，将媒体划分为不同的模块，包括音频、视频、图片等。

媒体系统面向应用开发提供音视频应用、图库应用、相机应用的编程框架接口；面向设备开发提供对接不同硬件芯片的适配加速功能；中间以服务形式提供媒体核心功能和管理机制。

音频服务（Audio Kit）：提供场景化音频播放和录制接口，助力开发者快速构建音频高清采集及沉浸式播放能力。

音视频编解码服务（AVCodec Kit）：提供音视频编解码、媒体文件解析、封装及媒体数据输入等原子能力。

音视频播控服务（AVSession Kit）：提供系统级音视频管控服务，统一管理系统中所有音视频行为。

相机服务（Camera Kit）：提供场景化相机控制管理接口，实现预览图像显示、拍照图片保存及视频录制功能。

数字版权保护服务（DRM Kit）：提供DRM加密音视频解密，支持设备DRM证书管理、许可证管理及内容解密功能。

图片处理服务（Image Kit）：提供全面图片处理能力，帮助开发者实现图片的解码、编码、编辑、元数据处理和图片接收等功能。

媒体服务（Media Kit）：提供端到端播放原始媒体资源，音视频录制与屏幕录制，获取媒体资源元数据、缩略图，视频转码等功能。

媒体文件管理服务（Media Library Kit）：提供管理相册和媒体文件的能力，包括照片和视频。

铃声服务（Ringtone Kit）：提供铃声设置功能，为用户提供简单一致、安全高品质的铃声设置体验。

统一扫码服务（Scan Kit）：提供系统级的扫码服务。

媒体应用开发综述
相机预览

相机预览是启动相机后实时的图像显示，通常在拍照和录像前执行。

指南

预览(ArkTS)

双路预览(ArkTS)

动态调整预览帧率(ArkTS)

适配相机旋转角度(ArkTS)

预览(C/C++)

预览流二次处理(C/C++)

动态调整预览帧率(C/C++)

适配相机旋转角度(C/C++)

API参考

ArkTS API：camera

C API：OH_Camera

最佳实践

相机预览花屏解决方案
相机拍照

拍照是相机的最重要功能之一，Camera Kit提供多种拍照方式，开发者可以直接拉起系统相机拍照、采用系统预配置简化应用开发流程，或是根据开放接口开发一个专业的相机应用。

指南

通过系统相机拍照和录像(CameraPicker)

拍照(ArkTS)

分段式拍照(ArkTS)

动态照片拍摄(ArkTS)

使用相机预配置(ArkTS)

HDR Vivid相机拍照(ArkTS)

适配相机旋转角度(ArkTS)

拍照(C/C++)

分段式拍照(C/C++)

使用相机预配置(C/C++)

适配相机旋转角度(C/C++)

API参考

ArkTS API：camera

ArkTS组件：cameraPicker

C API：OH_Camera

最佳实践

相机分段式拍照性能优化实践

示例代码

基于系统相机实现拍照功能

实现相机数据采集保存功能

实现相机数据采集保存功能（C++）

视频播放

AVPlayer提供功能齐全的一体化播放能力，支持多种音视频格式和流媒体协议。应用使用AVPlayer不仅可以实现基础的播放控制，还可以通过外挂字幕、画中画、自定义UI控件、内容版权保护等功能，为用户提供优良的影音体验。

指南

AVPlayer简介（含支持的格式与协议）

使用AVPlayer播放视频(ArkTS)

使用AVPlayer设置播放URL(ArkTS)

使用AVPlayer播放流媒体(ArkTS)

使用AVPlayer添加视频外挂字幕(ArkTS)

使用AVPlayer播放视频(C/C++)

HDR Vivid视频播放

接入Background Tasks Kit长时任务实现后台播放

应用接入AVSession

应用接入播控自检

基于AVPlayer播放DRM节目(ArkTS)

视频转码(ArkTS)

在应用程序中使用画中画功能

API参考

ArkTS API：AVPlayer

C API：AVPlayer

最佳实践

在线视频播放卡顿优化实践

音画同步最佳实践

基于系统能力获取视频缩略图

示例代码

实现视频播放功能

实现视频边缓存边播放功能

实现视频流畅播放且支持后台与焦点打断功能

基于系统能力获取视频缩略图

实现流畅切换短视频

实现音画同步播放效果

设计体验

播控中心

画中画

视频录制

AVRecorder提供音视频录制的能力，AVScreenCapture提供屏幕录制的能力，支持多源输入，可灵活配置录制参数，帮助开发者轻松实现音视频录制功能。

指南

AVRecorder简介（含支持的格式）

使用AVRecorder录制视频(ArkTS)

AVScreenCapture简介（含支持的格式）

使用AVScreenCaptureRecorder录屏写文件(ArkTS)

使用AVScreenCapture录屏取码流(C/C++)

使用AVScreenCapture录屏写文件(C/C++)

HDR Vivid相机录像

HDR Vivid视频录制

使用Camera Kit录像(ArkTS)

API参考

ArkTS API：AVRecorder

C API：AVRecorder

ArkTS API：AVScreenCaptureRecorder

C API：AVScreenCapture

示例代码

基于CameraKit通过AVRecorder录像
视频投播

使用媒体播控，可以简单高效地将音视频投放到其他HarmonyOS设备上播放，如在手机上播放的音视频，可以投到2in1设备上继续播放。

指南

使用通话设备切换组件

投播组件开发指导

扩展屏投播开发指导

API参考

ArkTS API：avsession

ArkTS组件：AVCastPicker

示例代码

实现视频投播功能
音频播放

开发者可以使用AVPlayer播放媒体资源，如mp4/mp3/mkv/mpeg-ts等，也可以使用AudioRenderer播放PCM音频数据。

AVPlayer指南

使用AVPlayer播放音频(ArkTS)

使用AVPlayer设置播放URL(ArkTS)

使用AVPlayer播放流媒体(ArkTS)

使用SoundPool播放短音频(ArkTS)

使用AVPlayer播放音频(C/C++)

AVPlayer API参考

ArkTS API：AVPlayer

C API：AVPlayer

AudioRenderer指南

使用AudioRenderer开发音频播放功能

响应音频流输出设备变更

使用OHAudio开发音频播放功能(C/C++)

使用AudioHaptic开发音振协同播放功能

AudioRenderer API参考

ArkTS API：AudioRenderer

ArkTS API：audioHaptic

C API：OHAudio

通用指南

接入Background Tasks Kit长时任务实现后台播放

应用接入AVSession

应用接入播控自检

使用合适的音频流类型

音频焦点和音频会话介绍

使用AudioSession管理应用音频焦点(ArkTS)

使用AudioSession管理应用音频焦点(C/C++)

最佳实践

音频焦点管理解决方案

音乐服务卡片

示例代码

实现音频应用作为媒体会话提供方接入媒体会话

实现音频低时延录制与播放

基于AudioRenderer的音频播控和多场景交互

设计体验

播控中心
音频采集

AudioCapture提供了音频采集能力，为开发者提供PCM原始数据。

指南

使用AudioCapturer开发音频录制功能

使用OHAudio开发音频录制功能(C/C++)

API参考

ArkTS API：AudioCapturer

C API：OHAudio

示例代码

实现音频低时延录制与播放

基于AudioRenderer的音频播控和多场景交互

音频录制

AVRecorder提供音频录制的能力，帮助开发者录制纯音频文件。

指南

使用AVRecorder录制音频(ArkTS)

API参考

ArkTS API：AVRecorder

C API：AVRecorder

媒体资源的选择和保存

指南

使用Picker选择媒体库资源

使用PhotoPicker组件访问图片/视频

保存媒体库资源

API参考

ArkTS API：photoAccessHelper

ArkTS组件：AlbumPickerComponent

ArkTS组件：PhotoPickerComponent

ArkTS组件：RecentPhotoComponent

最佳实践

图片获取与保存实践

示例代码

实现图片获取与保存功能

基于PhotoPicker实现图片推荐功能

隐私安全

在进行媒体应用开发过程中，应用需要访问个人数据（如用户照片、视频、音频文件等）和设备数据（如相机、麦克风等）。这些资源受系统保护，使用时需通过Picker或申请相关权限。

访问个人数据

使用Picker选择媒体库资源

保存资源到媒体库

选择音频类文件

保存音频类文件

应用需要克隆、备份或同步图片/视频类文件时，可申请受限权限读写媒体库。

访问设备数据

麦克风权限ohos.permission.MICROPHONE、相机权限ohos.permission.CAMERA、媒体地理位置信息权限ohos.permission.MEDIA_LOCATION，均为用户授权权限，申请方式见向用户申请授权。

更多资源

Audio Kit

分类	资源链接
音频焦点	

- 开发指南：使用合适的音频流类型

- 开发指南：音频焦点和音频会话

- ArkTS API参考：AudioSession

- ArkTS API参考：StreamUsage


音频通话	

- 开发指南：使用AudioRenderer播放对端的通话声音

- 开发指南：使用AudioCapturer录制本端的通话声音


更多	

Audio Kit开发指南

Audio Kit API参考

AVCodec Kit

分类	资源链接
音频编解码	

- 开发指南：音频编码

- 开发指南：音频解码

- 示例代码：AudioEncoder（音频编码）

- 示例代码：AudioDecoder（音频解码）

- C API参考：AudioCodec（音频编解码）


视频编解码	

- 开发指南：视频编码

- 示例代码：VideoEncoder（视频编码）

- C API参考：VideoEncoder（视频编码）

- 开发指南：视频解码

- 示例代码：VideoDecoder（视频解码）

- C API参考：VideoDecoder（视频解码）


更多	

AVCodec Kit开发指南

AVCodec Kit API参考

AVSession Kit

分类	资源链接
本地媒体会话	

- ArkTS API参考：媒体会话管理

- 开发指南：应用接入AVSession场景介绍

- 示例代码：基于AVPlayer实现播放接入

- 示例代码：基于AudioRenderer实现播放接入


更多	

AVSession Kit开发指南

AVSession Kit API参考

Camera Kit

分类	资源链接
视频录制	

- ArkTS API参考：Camera API(相机管理)

- 开发指南：录像(ArkTS)

- 开发指南：录像(C/C++)

- 示例实现：录像实践(ArkTS)


安全相机	

- ArkTS API参考：SecureSession

- 开发指南：安全相机(ArkTS)


更多	

Camera Kit开发指南

Camera Kit API参考

DRM Kit

分类	资源链接
AVPlayer播放DRM节目	

- ArkTS API参考：DRM

- 开发指南：数字版权保护(ArkTS)

- 示例实现：基于AVPlayer播放DRM节目(ArkTS)


AVCodec播放DRM节目	

- C API参考：数字版权保护API(C/C++)

- 开发指南：数字版权保护(C/C++)

- 示例实现：基于AVCodec播放DRM节目(C/C++)


更多	

DRM Kit开发指南

DRM Kit API参考

Image Kit

分类	资源链接
图片解码	

支持HEIF、JPEG、PNG、WebP、GIF、BMP、SVG、ICO、DNG格式图片的解码。

- ArkTS指南：使用ImageSource完成图片解码

- C/C++指南：使用Image_NativeModule完成图片解码

支持自定义申请内存类型，优化解码效率。

- ArkTS指南：申请图片解码内存(ArkTS)

- C/C++指南：申请图片解码内存(C/C++)


图片编码	

支持编码为HEIF、JPEG、PNG、WebP、GIF格式图片。

- ArkTS指南：使用ImagePacker完成图片编码

- C/C++指南：使用Image_NativeModule完成图片编码


图片接收	

支持作为消费者接收和处理图片。

- ArkTS指南：使用ImageReceiver完成图片接收

- C/C++指南：使用Image_NativeModule完成图片接收


图片编辑和处理	

支持裁剪、缩放、偏移、旋转、翻转、设置透明度等图像变换，以及对图片部分区域做像素数据写入的位图操作。

- ArkTS指南：使用PixelMap完成图像变换

- ArkTS指南：使用PixelMap完成位图操作

- C/C++指南：使用Image_NativeModule完成位图操作

支持读取和编辑图片的EXIF信息。

- ArkTS指南：编辑图片EXIF信息

- C/C++指南：使用Image_NativeModule编辑图片EXIF信息

支持为图片添加个性化的滤镜效果。

- C/C++指南：使用ImageEffect编辑图片

支持对图片做清晰度增强、色彩空间转换、HDR效果转换。

- C/C++指南：图片缩放

- C/C++指南：图片色彩空间转换

- C/C++指南：图片动态元数据生成

- C/C++指南：单层HDR图片转换双层

- C/C++指南：双层HDR图片转换单层


更多	

Image Kit开发指南

Image Kit API参考

Media Kit

分类	资源链接
视频转码	

- ArkTS API参考：AVTranscoder

- 开发指南：使用AVTranscoder实现视频转码(ArkTS)

- 开发指南：创建异步线程执行AVTranscoder视频转码(ArkTS)


元数据	

- ArkTS API参考：AVMetadataExtractor

- C API参考：AVMetadataExtractor

- 开发指南：使用AVMetadataExtractor提取音视频元数据信息(ArkTS)

- 开发指南：使用AVMetadataExtractor获取元数据(C/C++)


缩略图	

- ArkTS API参考：AVImageGenerator

- C API参考：AVImageGenerator

- 开发指南：使用AVImageGenerator提取视频指定时间图像(ArkTS)

- 开发指南：使用AVImageGenerator获取视频帧(C/C++)

- 最佳实践：基于系统能力获取视频缩略图


更多	

Media Kit开发指南

Media Kit API参考

Media Library Kit

分类	资源链接
管理动态照片	

- 指南：访问和管理动态照片资源

- 指南：使用MovingPhotoView播放动态照片


更多	

Media Library Kit开发指南

Media Library Kit API参考

Ringtone Kit

分类	资源链接
铃声设置服务	

- ArkTS API参考：铃声服务

- 指南：设置铃声

Scan Kit

分类	资源链接
默认界面扫码	

- ArkTS API参考：默认界面扫码

- 指南：默认界面扫码


自定义界面扫码	

- ArkTS API参考：自定义界面扫码

- 指南：自定义界面扫码


图像识码	

- ArkTS API参考：图像识码

- 指南：识别本地图片

- 指南：识别图像数据


码图生成	

- ArkTS API参考：码图生成

- 指南：通过文本生成码图

- 指南：通过字节数组生成码图

使用HDR Vivid特性开发媒体应用
