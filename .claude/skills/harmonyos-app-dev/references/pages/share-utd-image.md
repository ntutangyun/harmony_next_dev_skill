# 分享图片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-image_

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

构造分享数据。

// 构造ShareData，需配置一条有效数据信息
let uiContext: UIContext = this.getUIContext();
let contextFaker: Context = uiContext.getHostContext() as Context;
let filePath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
// 获取精准的utd类型
let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utdTypeId,
  uri: fileUri.getUriFromPath(filePath),
  title: '图片标题', // 不传title字段时,显示图片文件名
  description: '图片描述', // 不传description字段时,显示图片大小
  // thumbnail: new Uint8Array() // 优先使用传递的缩略图预览  不传则默认使用原图做预览图
});
说明

沙箱路径可通过fileUri.getUriFromPath方法获取文件URI。

额外增加一条数据。

shareData.addRecord({
  utd: utdTypeId,
  uri: fileUri.getUriFromPath(filePath),
  title: '图片标题', // 不传title字段时,显示图片文件名
  description: '图片描述', // 不传description字段时,显示图片大小
});

启动分享面板。

// 进行分享面板显示
let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
controller.show(context, {
  selectionMode: systemShare.SelectionMode.SINGLE,
  previewMode: systemShare.SharePreviewMode.DETAIL,
}).then(() => {
  console.info('ShareController show success.');
}).catch((error: BusinessError) => {
  console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
});

完整示例代码请参见：samplecode-分享图片。

分享链接
分享视频
