# 批注

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-annotation_

进入批注模式，目前支持高亮、下划线和删除线类型批注。

接口说明

接口名	描述
enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void	在常用操作之间切换并添加批注。

示例代码

先加载PDF文档。

调用PdfView预览组件，渲染显示。

调用enableAnnotation方法，进入批注模式。

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
// ...

@Entry
@Component
struct AnnotationPage {
  private pdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAFF0000);
      }
    })()
  }

  build() {
  // ...
      Column() {
        PdfView({
          controller: this.pdfController,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
  }
}

## Code blocks

### Code block 1

```
import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';
// ...

@Entry
@Component
struct AnnotationPage {
  private pdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;

  aboutToAppear(): void {
    // 确保在工程目录src/main/resources/resfile里有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAFF0000);
      }
    })()
  }

  build() {
  // ...
      Column() {
        PdfView({
          controller: this.pdfController,
          pageFit: pdfService.PageFit.FIT_WIDTH,
          showScroll: true
        })
          .id('pdfview_app_view')
          .layoutWeight(1);
      }
      // ...
  }
}
```
