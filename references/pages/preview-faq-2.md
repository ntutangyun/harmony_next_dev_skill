# 使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-faq-2_

DocumentViewPicker拿到的文件uri应用仅有临时权限，该权限无法分享给预览，导致预览失败。可先对uri持久化权限，然后再采用openPreview打开文件；或者可以先将文件拷贝至应用沙箱内，再预览沙箱内文件。

openPreview打开显示预览失败
Push Kit（推送服务）
