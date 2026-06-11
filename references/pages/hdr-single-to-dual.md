# 单层HDR图片转换双层

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-single-to-dual_

调用者可以调用本模块提供的C API接口，实现Decompose单层HDR图片转双层HDR图片。

该能力常用于图片分享中，如下图所示：

规格说明

支持的数据输入格式：

使用图片单层HDR转双层HDR转换算法Decompose。

输入ColorSpaceName	输入HdrMetadataType	输入PIXEL_FORMAT	输出ColorSpaceName	输出 HdrMetadataType	输出PIXEL_FORMAT
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_BASE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	SRGB_LIMIT/SRGB	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_ALTERNATE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_HLG_LIMIT/BT2020_HLG	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888
BT2020_PQ_LIMIT/BT2020_PQ	HDR_METADATA_TYPE_NONE	YCBCR_P010, YCRCB_P010, RGBA_1010102	DISPLAY_P3_LIMIT/DISPLAY_P3	HDR_METADATA_TYPE_NONE	RGBA_8888/ BGRA_8888

分辨率规格：

最小分辨率（单位：像素）	最大分辨率（单位：像素）
32*32	8880*8880

内存规格：

处理的PixelMap对象需为DMA内存。

开发指导

具体实现可参考示例工程。

[h2]在 CMake 脚本中链接动态库

add_library(entry SHARED napi_init.cpp ImageProcessing/ImageProcessing.cpp)
target_link_libraries(entry PUBLIC ${BASE_LIBRARY})

[h2]ArkTS侧调用的开发步骤

通过解码器获取10 bit的PixelMap。

const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoViewPicker.select(photoSelectOptions)
  .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
    let fd = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
    const imageSource = image.createImageSource(fd.fd);
    let option: image.DecodingOptions = {};
    option.index = 0;
    option.desiredDynamicRange = image.DecodingDynamicRange.AUTO;
    this.pixelMapSrc = imageSource.createPixelMapSync(option);
    this.getColorSpace();
    this.hasPhoto = true;
  })

创建8 bit的PixelMap。

let dualPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);
let gainmapPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);

配置色彩框架和元数据信息。

let colorSpaceDISPLAY_P3 : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.DISPLAY_P3);
let colorSpaceBT2020_HLG : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
sdrpixelMap.setColorSpace(colorSpaceDISPLAY_P3);
sdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.BASE);
gainmappixelMap.setColorSpace(colorSpaceDISPLAY_P3);
gainmappixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.GAINMAP);
hdrpixelMap.setColorSpace(colorSpaceBT2020_HLG);
hdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.ALTERNATE);

[h2]Native侧调用的开发步骤

添加头文件。

#include <multimedia/image_framework/image_mdk_common.h>
#include <multimedia/image_framework/image_pixel_map_mdk.h>
#include <multimedia/image_framework/image/pixelmap_native.h>
#include <multimedia/video_processing_engine/image_processing.h>
#include <multimedia/video_processing_engine/image_processing_types.h>
#include <native_color_space_manager/native_color_space_manager.h>

（可选）初始化环境。

一般在进程内第一次使用时调用，可提前完成部分耗时操作。

ImageProcessing_ErrorCode ret =  OH_ImageProcessing_InitializeEnvironment();

（可选）查询能力支持。建议在使用对应能力前调用。

//输入格式
ImageProcessing_ColorSpaceInfo SRC_INFO;
ImageProcessing_ColorSpaceInfo DST_GAIN_INFO;
ImageProcessing_ColorSpaceInfo DST_INFO;
SRC_INFO.colorSpace = BT2020_HLG;
SRC_INFO.metadataType = HDR_METADATA_TYPE_ALTERNATE;
SRC_INFO.pixelFormat = PIXEL_FORMAT_RGBA_1010102;
DST_INFO.colorSpace = DISPLAY_P3;
DST_INFO.metadataType = HDR_METADATA_TYPE_BASE;
DST_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
DST_GAIN_INFO.colorSpace = DISPLAY_P3;
DST_GAIN_INFO.metadataType = HDR_METADATA_TYPE_GAINMAP;
DST_GAIN_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
//能力查询
bool flag = OH_ImageProcessing_IsDecompositionSupported(&SRC_INFO, &DST_INFO, &DST_GAIN_INFO);

创建8 bit的PixelMap。

napi_value ImageProcessing::CreatePixelMap(napi_env env, napi_callback_info info)
{
    napi_value udfVar = nullptr;
    napi_value pixelMap = nullptr;
    napi_value thisVar = nullptr;
    napi_value argValue[2] = {0};
    size_t argCount = 2;
    size_t count = 2;
    if (napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi_ok || argCount < count ||
        argValue[0] == nullptr || argValue[1] == nullptr) {
        return nullptr;
    }
    int32_t width = 0;
    int32_t height = 0;
    napi_get_value_int32(env, argValue[1], &width);
    napi_get_value_int32(env, argValue[0], &height);
    struct OhosPixelMapCreateOps createOps;
    createOps.width = width;
    createOps.height = height;
    int32_t rgba8888 = 3;
    createOps.pixelFormat = rgba8888;
    createOps.alphaType = 0;

    size_t bufferSize = createOps.width * createOps.height * 4;
    void *buff = malloc(bufferSize);
    int32_t res = OH_PixelMap_CreatePixelMapWithStride(env, createOps, (uint8_t *)buff, bufferSize, createOps.width * 4,
        &pixelMap);
    free(buff);
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "createPixelMap",
        "OH_PixelMap_CreatePixelMapWithStride %{public}d", res);
    if (res != IMAGE_RESULT_SUCCESS || pixelMap == nullptr) {
        return udfVar;
    }
    return pixelMap;
}

将ArkTS中的PixelMap转换为C++的PixelMap。

OH_PixelmapNative* sdr = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[0], &sdr);
OH_PixelmapNative* gainmap = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[1], &gainmap);
OH_PixelmapNative* hdr = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[2], &hdr);

创建图片HDR单层转双层模块。

应用可以通过图片处理引擎模块类型来创建图片HDR单层转双层模块。示例中的变量说明如下：

instance：图片处理模块实例。

IMAGE_PROCESSING_TYPE_DECOMPOSITION：图片HDR单层转双层。

预期返回值：IMAGE_PROCESSING_SUCCESS

OH_ImageProcessing* instance = nullptr;
ret = OH_ImageProcessing_Create(&instance, IMAGE_PROCESSING_TYPE_DECOMPOSITION);

执行算法。

ret = OH_ImageProcessing_Decompose(instance, hdr, sdr, gainmap);

释放实例资源。

ret = OH_ImageProcessing_Destroy(instance);
instance = nullptr;

释放初始化环境资源。

ret = OH_ImageProcessing_DeinitializeEnvironment();

完整示例代码

ArkTS示例代码：

decompose.ets示例代码

C++相关示例代码：

CMakeLists.txt示例代码

ImageProcessing.h示例代码

ImageProcessing.cpp示例代码

## Code blocks

### Code block 1

```
add_library(entry SHARED napi_init.cpp ImageProcessing/ImageProcessing.cpp)
target_link_libraries(entry PUBLIC ${BASE_LIBRARY})
```

### Code block 2

```
const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoViewPicker.select(photoSelectOptions)
  .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
    let fd = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
    const imageSource = image.createImageSource(fd.fd);
    let option: image.DecodingOptions = {};
    option.index = 0;
    option.desiredDynamicRange = image.DecodingDynamicRange.AUTO;
    this.pixelMapSrc = imageSource.createPixelMapSync(option);
    this.getColorSpace();
    this.hasPhoto = true;
  })
```

### Code block 3

```
let dualPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);
let gainmapPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);
```

### Code block 4

```
let colorSpaceDISPLAY_P3 : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.DISPLAY_P3);
let colorSpaceBT2020_HLG : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
sdrpixelMap.setColorSpace(colorSpaceDISPLAY_P3);
sdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.BASE);
gainmappixelMap.setColorSpace(colorSpaceDISPLAY_P3);
gainmappixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.GAINMAP);
hdrpixelMap.setColorSpace(colorSpaceBT2020_HLG);
hdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.ALTERNATE);
```

### Code block 5

```
#include <multimedia/image_framework/image_mdk_common.h>
#include <multimedia/image_framework/image_pixel_map_mdk.h>
#include <multimedia/image_framework/image/pixelmap_native.h>
#include <multimedia/video_processing_engine/image_processing.h>
#include <multimedia/video_processing_engine/image_processing_types.h>
#include <native_color_space_manager/native_color_space_manager.h>
```

### Code block 6

```
ImageProcessing_ErrorCode ret =  OH_ImageProcessing_InitializeEnvironment();
```

### Code block 7

```
//输入格式
ImageProcessing_ColorSpaceInfo SRC_INFO;
ImageProcessing_ColorSpaceInfo DST_GAIN_INFO;
ImageProcessing_ColorSpaceInfo DST_INFO;
SRC_INFO.colorSpace = BT2020_HLG;
SRC_INFO.metadataType = HDR_METADATA_TYPE_ALTERNATE;
SRC_INFO.pixelFormat = PIXEL_FORMAT_RGBA_1010102;
DST_INFO.colorSpace = DISPLAY_P3;
DST_INFO.metadataType = HDR_METADATA_TYPE_BASE;
DST_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
DST_GAIN_INFO.colorSpace = DISPLAY_P3;
DST_GAIN_INFO.metadataType = HDR_METADATA_TYPE_GAINMAP;
DST_GAIN_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
//能力查询
bool flag = OH_ImageProcessing_IsDecompositionSupported(&SRC_INFO, &DST_INFO, &DST_GAIN_INFO);
```

### Code block 8

```
napi_value ImageProcessing::CreatePixelMap(napi_env env, napi_callback_info info)
{
    napi_value udfVar = nullptr;
    napi_value pixelMap = nullptr;
    napi_value thisVar = nullptr;
    napi_value argValue[2] = {0};
    size_t argCount = 2;
    size_t count = 2;
    if (napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi_ok || argCount < count ||
        argValue[0] == nullptr || argValue[1] == nullptr) {
        return nullptr;
    }
    int32_t width = 0;
    int32_t height = 0;
    napi_get_value_int32(env, argValue[1], &width);
    napi_get_value_int32(env, argValue[0], &height);
    struct OhosPixelMapCreateOps createOps;
    createOps.width = width;
    createOps.height = height;
    int32_t rgba8888 = 3;
    createOps.pixelFormat = rgba8888;
    createOps.alphaType = 0;

    size_t bufferSize = createOps.width * createOps.height * 4;
    void *buff = malloc(bufferSize);
    int32_t res = OH_PixelMap_CreatePixelMapWithStride(env, createOps, (uint8_t *)buff, bufferSize, createOps.width * 4,
        &pixelMap);
    free(buff);
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "createPixelMap",
        "OH_PixelMap_CreatePixelMapWithStride %{public}d", res);
    if (res != IMAGE_RESULT_SUCCESS || pixelMap == nullptr) {
        return udfVar;
    }
    return pixelMap;
}
```

### Code block 9

```
OH_PixelmapNative* sdr = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[0], &sdr);
OH_PixelmapNative* gainmap = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[1], &gainmap);
OH_PixelmapNative* hdr = nullptr;
OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[2], &hdr);
```

### Code block 10

```
OH_ImageProcessing* instance = nullptr;
ret = OH_ImageProcessing_Create(&instance, IMAGE_PROCESSING_TYPE_DECOMPOSITION);
```

### Code block 11

```
ret = OH_ImageProcessing_Decompose(instance, hdr, sdr, gainmap);
```

### Code block 12

```
ret = OH_ImageProcessing_Destroy(instance);
instance = nullptr;
```

### Code block 13

```
ret = OH_ImageProcessing_DeinitializeEnvironment();
```
