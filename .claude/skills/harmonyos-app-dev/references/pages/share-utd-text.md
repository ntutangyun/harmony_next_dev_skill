# 分享文本

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-utd-text_

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

构造分享数据。

// 构造ShareData，需配置一条有效数据信息
let shareData: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.TEXT,
  content: '这是一段文本内容',
  title: '文本内容', // 不传title字段时,显示content
  description: '文本描述',
  // thumbnail: new Uint8Array() // 推荐传入适合的缩略图 不传则显示默认text图标
});

额外增加一条数据。

shareData.addRecord({
  utd: utd.UniformDataType.TEXT,
  content: '这是一段文本内容',
  title: '文本内容', // 不传title字段时,显示content
  description: '文本描述',
});

启动分享面板。

// 进行分享面板显示
let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
let uiContext: UIContext = this.getUIContext();
let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
controller.show(context, {
  selectionMode: systemShare.SelectionMode.SINGLE,
  previewMode: systemShare.SharePreviewMode.DETAIL,
}).then(() => {
  console.info('ShareController show success.');
}).catch((error: BusinessError) => {
  console.error(`ShareController show error. code: ${error.code}, message: ${error.message}`);
});

完整示例代码请参见：samplecode-分享文本。

分享视频
碰一碰分享
