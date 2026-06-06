# 分享视频

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-video_

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

生成视频封面图（推荐）。

// 生成视频封面图
let uiContext: UIContext = this.getUIContext();
let contextFaker: Context = uiContext.getHostContext() as Context;
let thumbnailPath = contextFaker.filesDir + '/exampleImage.jpg'; // 仅为示例 请替换正确的文件路径
let imageSource: image.ImageSource = image.createImageSource(thumbnailPath);
let imagePacker: image.ImagePacker = image.createImagePacker();
let buffer: ArrayBuffer = await imagePacker.packToData(imageSource, {
  // 当前只支持'image/jpeg','image/webp'和'image/png'类型图片.
  format: 'image/jpeg',
  // JPEG编码中设定输出图片质量的参数,取值范围为0-100.
  // 建议适当压缩,图片过大无法拉起分享.
  quality: 30
});

构造分享数据。

// 构造ShareData，需配置一条有效数据信息
let filePath = contextFaker.filesDir + '/exampleVideo.mp4'; // 仅为示例 请替换正确的文件路径
// 获取精准的utd类型
let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.mp4', utd.UniformDataType.VIDEO);
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utdTypeId,
  uri: fileUri.getUriFromPath(filePath),
  title: '视频标题', // 不传title字段时,显示视频文件名
  description: '视频描述', // 不传description字段时,显示视频大小
  thumbnail: new Uint8Array(buffer), // 优先使用传递的缩略图做预览 不传则默认使用视频第一帧画面做预览图
});
说明

沙箱路径可通过fileUri.getUriFromPath方法获取文件URI。

额外增加一条数据

shareData.addRecord({
  utd: utdTypeId,
  uri: fileUri.getUriFromPath(filePath),
  title: '视频标题', // 不传title字段时,显示视频文件名
  description: '视频描述', // 不传description字段时,显示视频大小
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

完整示例代码请参见：samplecode-分享视频。

分享图片
分享文本
