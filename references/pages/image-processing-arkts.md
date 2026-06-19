# 使用VideoProcessingEngine实现图片超分辨率

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-processing-arkts_

本模块提供图片细节增强的ArkTS接口，支持对图片内容进行清晰度增强和缩放处理。通过调用本模块，应用可以对低分辨率、细节不足或需要放大显示的图片进行超分处理，提升图片的视觉清晰度，处理后的图片数据可用于送显或输出。

超分，即超分辨率重建，是指在放大图片尺寸的同时，尽可能恢复和增强图片中的纹理、边缘等细节信息，减少普通插值缩放带来的模糊、锯齿或细节丢失问题。该能力适用于图片来源分辨率较低、图片需要放大显示、缩略图需要高清展示等场景。如需获得更明显的图片细节增强和超分效果，建议使用HIGH档。

约束与限制

当前仅支持处理同时满足以下条件的图片：

图片为SDR（Standard dynamic range）图片。

图片的像素格式为RGBA、BGRA、NV12、NV21，输出格式与输入格式一致。

处理的PixelMap对象需为DMA内存。

本模块提供4个质量档位的算法，处理效果逐渐变优，但性能也会逐渐下降。

质量档位	输入分辨率要求 （单位：像素）	输出分辨率要求 （单位：像素）	说明
NONE	宽：[32,3000] 高：[32,3000]	宽：[32,3000] 高：[32,3000]	仅适用于缩放场景，支持改变宽高比例，无清晰度增强效果。
LOW	宽：[32,3000] 高：[32,3000]	宽：[32,3000] 高：[32,3000]	仅适用于缩放场景，支持改变宽高比例。 缩放时会对图片进行低质量的清晰度增强，处理效率较高。 此质量档位为默认设置。
MEDIUM	宽：[32,3000] 高：[32,3000]	宽：[32,3000] 高：[32,3000]	仅适用于缩放场景，支持改变宽高比例。 缩放时会对图片进行中等质量的清晰度增强，处理效率适中。
HIGH	宽：[512,2000] 高：[512,2000]	宽：[512,2000] 高：[512,2000]	适用于缩放及清晰度增强场景，支持改变宽高比例。 缩放时会对图片进行高质量的清晰度增强，处理效率相对较低。

开发步骤

添加引用文件。

import { image, videoProcessingEngine } from '@kit.ImageKit';

初始化环境。

let promise: Promise<void> = videoProcessingEngine.initializeEnvironment();

（可选）配置输入。

let scale: number = 0.5;
let width: number = 512; // 示例代码，配置宽为512。
let height: number = 512;// 示例代码，配置高为512。
const color: ArrayBuffer = new ArrayBuffer(width * height * 4); // width * height * 4为需要创建的像素buffer大小。
let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height, width } }
let sourceImage : image.PixelMap = image.createPixelMapSync(color, opts);
let level : videoProcessingEngine.QualityLevel = videoProcessingEngine.QualityLevel.LOW;

创建图片处理模块。

预期返回值：videoProcessingEngine.ImageProcessor，图片处理模块实例。

// 创建图片细节增强模块实例
let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;

启动细节增强处理。当输入图片srcImage和输出图片dstImage分辨率不一致时，进行缩放。

示例中的变量说明如下：

sourceImage：PixelMap类型的输入图片，必填。

width：目标宽度（单位px），当没有配置目标缩放比例时必填。

height：目标高度（单位px），当没有配置目标缩放比例时必填。

scale：目标缩放比例，当没有配置目标分辨率时必填。目标分辨率即宽*高。

level：质量算法档位，默认为LOW。

方式一：指定原图、目标分辨率。

// 同步方法
let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
sourceImage, width, height, level);

// 异步方法
let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(sourceImage, width, height, level);

方式二：指定原图、缩放比例。

// 同步方法
let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
sourceImage, scale, level);

// 异步方法
let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(
sourceImage, scale, level);

释放处理资源。

videoProcessingEngine.deinitializeEnvironment();

示例代码

图片超分示例代码

## Code blocks

### Code block 1

```
import { image, videoProcessingEngine } from '@kit.ImageKit';
```

### Code block 2

```
let promise: Promise<void> = videoProcessingEngine.initializeEnvironment();
```

### Code block 3

```
let scale: number = 0.5;
let width: number = 512; // 示例代码，配置宽为512。
let height: number = 512;// 示例代码，配置高为512。
const color: ArrayBuffer = new ArrayBuffer(width * height * 4); // width * height * 4为需要创建的像素buffer大小。
let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height, width } }
let sourceImage : image.PixelMap = image.createPixelMapSync(color, opts);
let level : videoProcessingEngine.QualityLevel = videoProcessingEngine.QualityLevel.LOW;
```

### Code block 4

```
// 创建图片细节增强模块实例
let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
```

### Code block 5

```
// 同步方法
let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
sourceImage, width, height, level);
```

### Code block 6

```
// 异步方法
let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(sourceImage, width, height, level);
```

### Code block 7

```
// 同步方法
let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
sourceImage, scale, level);
```

### Code block 8

```
// 异步方法
let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(
sourceImage, scale, level);
```

### Code block 9

```
videoProcessingEngine.deinitializeEnvironment();
```
