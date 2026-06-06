# 获取分享结果

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-share-completed_

import { uniformTypeDescriptor as utd } from '@kit.ArkData';

构造分享数据。

// 构造ShareData，需配置一条有效数据信息
let data: systemShare.SharedData = new systemShare.SharedData({
  utd: utd.UniformDataType.PLAIN_TEXT,
  content: 'Hello HarmonyOS'
});

注册分享结果监听事件，并启动分享面板。

// 构建ShareController
let controller: systemShare.ShareController = new systemShare.ShareController(data);
// 获取UIAbility上下文对象
let uiContext: UIContext = this.getUIContext();
let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
// 注册分享结果事件监听
controller.on('shareCompleted', (result: systemShare.ShareOperationResult) => {
  console.info('shareCompleted name:', result.targetAbilityInfo.name);
  // 可根据分享渠道进行数据统计等操作
});


// 进行分享面板显示
controller.show(context, {
  previewMode: systemShare.SharePreviewMode.DEFAULT,
  selectionMode: systemShare.SelectionMode.SINGLE
});
自定义配置操作区
目标应用处理分享内容
