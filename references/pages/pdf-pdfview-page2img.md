# PDF缩略图转换为图片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-page2img_

场景介绍

调用getPagePixelMap方法，将指定PDF缩略图转化为图片。

接口说明

接口名	描述
getPagePixelMap(pageIndex: number, isSync?: boolean): Promise<image.PixelMap>	获取对应PDF页面的缩略图，使用Promise异步回调。

示例代码

调用loadDocument方法，加载PDF文档。

调用getPagePixelMap方法，获取image.PixelMap对象。

将image.PixelMap转化为二进制图片文件并保存。

import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  // 将 pixelMap 转成图片格式
  pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
      /**
       设置打包参数
       format：图片打包格式
       quality：JPEG 编码输出图片质量
       */
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 }
      // 创建ImagePacker实例
      const imagePackerApi = image.createImagePacker()
      imagePackerApi.packToData(pixelMap, packOpts).then((buffer: ArrayBuffer) => {
        resolve(buffer)
      }).catch((err: BusinessError) => {
        reject()
      })
    })
  }

  build() {
    Column() {
      // 转换为图片并保存到应用沙箱
      Button('getPagePixelMap').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
          let pixmap: image.PixelMap = await this.controller.getPagePixelMap(0, true);
          if (!pixmap) {
            return
          }
          const imgBuffer = await this.pixelMap2Buffer(pixmap)
          try {
            const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.png`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            await fileIo.write(file.fd, imgBuffer);
            // 关闭文件
            await fileIo.close(file.fd)
          } catch (e) {
            let error: BusinessError = e as BusinessError;
            hilog.error(0x0000, 'getPagePixelMap-', `Code: ${error.code}, message: ${error.message} `);
          }
        }
      })
    }
  }
}

## Code blocks

### Code block 1

```
import { pdfService, pdfViewManager } from '@kit.PDFKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里存在input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  // 将 pixelMap 转成图片格式
  pixelMap2Buffer(pixelMap: image.PixelMap): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {
      /**
       设置打包参数
       format：图片打包格式
       quality：JPEG 编码输出图片质量
       */
      let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 }
      // 创建ImagePacker实例
      const imagePackerApi = image.createImagePacker()
      imagePackerApi.packToData(pixelMap, packOpts).then((buffer: ArrayBuffer) => {
        resolve(buffer)
      }).catch((err: BusinessError) => {
        reject()
      })
    })
  }

  build() {
    Column() {
      // 转换为图片并保存到应用沙箱
      Button('getPagePixelMap').onClick(async () => {
        if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
          let pixmap: image.PixelMap = await this.controller.getPagePixelMap(0, true);
          if (!pixmap) {
            return
          }
          const imgBuffer = await this.pixelMap2Buffer(pixmap)
          try {
            const file =
                fileIo.openSync(this.context.filesDir + `/${Date.now()}.png`, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            await fileIo.write(file.fd, imgBuffer);
            // 关闭文件
            await fileIo.close(file.fd)
          } catch (e) {
            let error: BusinessError = e as BusinessError;
            hilog.error(0x0000, 'getPagePixelMap-', `Code: ${error.code}, message: ${error.message} `);
          }
        }
      })
    }
  }
}
```
