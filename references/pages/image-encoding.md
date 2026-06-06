# 使用ImagePacker完成图片编码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding_

从API version 18开始，支持使用PackToDataFromPixelmapSequence和PackToFileFromPixelmapSequence将多个PixelMap编码为GIF格式。

开发步骤

图片编码相关API的详细介绍请参见ImagePacker。

图片编码进文件流

导入相关模块包。

// 导入相关模块。
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { resourceManager } from '@kit.LocalizationKit';
EncodingPixelMap.ets

设置编码选项PackingOption。

2.1 这里以编码成jpeg图片为例。编码的目标格式format遵循MIME标准定义，因此PackingOption.format应设置为image/jpeg，编码后的文件扩展名可设为.jpg或.jpeg。

let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
CodecUtility.ets

2.2 当图片源是HDR，且希望编码为HDR图片文件时，需要额外配置desiredDynamicRange。

// 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
CodecUtility.ets

封装函数，传入imageSource或pixelMap，使用packToData接口编码到ArrayBuffer，或使用packToFile接口编码到文件。

说明

在进行编码前，需要先获取imageSource或pixelMap，可参考使用ImageSource完成图片解码。

定义copyData，获取编码后的文件流，方便后续保存为图片或者用于解码显示。

let copyData: ArrayBuffer = new ArrayBuffer(0);
CodecUtility.ets

pixelMap编码到ArrayBuffer。

async function packToDataFromPixelMap(pixelMap : image.PixelMap) {
  const imagePackerApi = image.createImagePacker();
  let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
  // 资源本身为hdr且设备支持HDR编码则会编码为hdr内容(需要资源本身为hdr且设备支持HDR编码，支持jpeg格式)。
  packOpts.desiredDynamicRange = image.PackingDynamicRange.AUTO;
  try{
    let data = await imagePackerApi.packToData(pixelMap, packOpts);
    // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
    copyData = new ArrayBuffer(0);
    copyData = data;
  } catch (error) {
    console.error('Failed to pack the pixelMap to data. And the error is: ' + error);
  }
}
CodecUtility.ets

imageSource编码到ArrayBuffer。

async function packToDataFromImageSource(imageSource : image.ImageSource) {
  const imagePackerApi = image.createImagePacker();
  let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
  try {
    let data = await imagePackerApi.packToData(imageSource, packOpts);
    // data 为编码获取到的文件流，写入文件保存即可得到一张图片。
    copyData = new ArrayBuffer(0);
    copyData = data;
  } catch (error) {
    console.error('Failed to pack the imageSource to data. And the error is: ' + error);
  }
}
CodecUtility.ets

pixelMap编码到文件。

async function packToFileFromPixelMap(context : Context, pixelMap : image.PixelMap) {
  const imagePackerApi = image.createImagePacker();
  let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
  const path : string = context.cacheDir + '/pixel_map.jpg';
  try {
    let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    await imagePackerApi.packToFile(pixelMap, file.fd, packOpts);
  } catch (error) {
    console.error('Failed to pack the pixelMap to file. And the error is: ' + error);
  }
}
CodecUtility.ets

imageSource编码到文件。

async function packToFileFromImageSource(context : Context, imageSource : image.ImageSource) {
  const imagePackerApi = image.createImagePacker();
  let packOpts : image.PackingOption = { format: 'image/jpeg', quality: 95 };
  const filePath : string = context.cacheDir + '/image_source.jpg';
  try {
    let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    await imagePackerApi.packToFile(imageSource, file.fd, packOpts);
  } catch (error) {
    console.error('Failed to pack the imageSource to file. And the error is: ' + error);
  }
}
CodecUtility.ets

将图片保存进图库。

将图片编码到ArrayBuffer或文件后，可使用Media Library Kit的相关接口保存媒体库资源保存进图库。

示例代码
图片压缩
图片编码
使用ImagePacker完成多图对象编码
