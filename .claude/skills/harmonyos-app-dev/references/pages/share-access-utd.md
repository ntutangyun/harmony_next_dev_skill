# 宿主应用发起分享需使用精细化的utd类型

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-utd_

根据给定的文件后缀名和所归属的标准化数据类型查询标准化数据类型的ID。参见：uniformTypeDescriptor.getUniformDataTypeByFilenameExtension。

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare } from '@kit.ShareKit';


try {
  let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
  if (utdTypeId) {
    // 构造ShareData，需配置一条有效数据信息
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utdTypeId,
      uri: 'file://.../xxx.jpg'
    });
    // 构建ShareController
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    // 获取UIAbility上下文对象
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    // 进行分享面板显示
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DEFAULT,
      selectionMode: systemShare.SelectionMode.SINGLE
    });
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Failed to getUniformDataTypeByFilenameExtension. Code: ${error.code}, message: ${error.message} `);
}

根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型的ID。参见：uniformTypeDescriptor.getUniformDataTypeByMIMEType。

import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare } from '@kit.ShareKit';


try {
  let utdTypeId = utd.getUniformDataTypeByMIMEType('image/jpeg', utd.UniformDataType.IMAGE);
  if (utdTypeId) {
    // 构造ShareData，需配置一条有效数据信息
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utdTypeId,
      uri: 'file://.../xxx.jpg'
    });
    // 构建ShareController
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    // 获取UIAbility上下文对象
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    // 进行分享面板显示
    controller.show(context, {
      previewMode: systemShare.SharePreviewMode.DEFAULT,
      selectionMode: systemShare.SelectionMode.SINGLE
    });
  }
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`Failed to getUniformDataTypeByMIMEType. Code: ${error.code}, message: ${error.message} `);
}
Share Kit体验规范
目标设备接收分享数据一步直达体验
