# 判断PDF文档是否加密及删除加密

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-isencrypt-removesecurity_

private pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
  private context = this.getUIContext().getHostContext() as Context;


  build() {
    Column() {
      // 判断文档是否加密，并删除加密
      Button('isEncryptedAndRemoveSecurity').onClick(async () => {
        // 确保在工程目录src/main/resources/resfile里有input.pdf文档
        let filePath = this.context.resourceDir + '/input.pdf';
        let isEncrypt = this.pdfDocument.isEncrypted(filePath);
        if (isEncrypt) {
          let hasRemoveEncrypt = this.pdfDocument.removeSecurity();
          hilog.info(0x0000, 'PdfPage', 'isEncryptedAndRemoveSecurity %{public}s!',
            hasRemoveEncrypt ? 'success' : 'fail');
        }
      })
    }
  }
}
转换整个PDF文档为图片
添加、删除书签
