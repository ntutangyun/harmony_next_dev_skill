# 批注

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-annotation_

enableAnnotation(annotationType: SupportedAnnotationType, color?: number): void	在常用操作之间切换并添加批注。
示例代码

先加载PDF文档。

调用PdfView预览组件，渲染显示。

调用enableAnnotation方法，进入批注模式。

import { pdfService, pdfViewManager, PdfView } from '@kit.PDFKit';


@Entry
@Component
struct PdfPage {
  private pdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;


  aboutToAppear(): void {
    // 确保沙箱目录有input.pdf文档
    let filePath = this.context.resourceDir + '/input.pdf';
    (async () => {
      let loadResult: pdfService.ParseResult = await this.pdfController.loadDocument(filePath);
      if (pdfService.ParseResult.PARSE_SUCCESS === loadResult) {
        // 添加删除线批注
        this.pdfController.enableAnnotation(pdfViewManager.SupportedAnnotationType.STRIKETHROUGH, 0xAAEEEEEE);
      }
    })()
  }


  build() {
    Column() {
      // 加载PdfView组件进行预览
      PdfView({
        controller: this.pdfController,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
  }
}
高亮显示PDF文档
PDF缩略图转换为图片
