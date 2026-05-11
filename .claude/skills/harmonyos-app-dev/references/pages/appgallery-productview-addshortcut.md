# 添加桌面快捷方式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-productview-addshortcut_

应用内快捷方式为用户提供了一种快速访问应用功能和内容的便捷方式。通过静态资源和自定义资源方式创建桌面快捷方式，并向用户展示确认弹窗。用户确认后，快捷方式将添加至桌面。静态快捷方式适用于常用功能，如创建新播放列表，而自定义快捷方式适用于特定的、临时内容，如添加最新的新闻文章。

说明

单个应用最多可添加2个快捷方式。

业务流程

应用预先调用checkPinShortcutPermitted接口检查是否允许快捷方式加桌。

AppGallery Kit获取应用传入的快捷方式信息并生成检查结果。

AppGallery Kit返回应用检查结果和有效时间给应用。

检查通过后应用给用户展示添加快捷方式入口。

用户点击“添加”快捷方式。

调用requestNewPinShortcut接口请求创建快捷方式。

AppGallery Kit加载快捷方式信息并弹出用户确认框。

用户确认是否同意加桌。

用户同意后，AppGallery Kit处理加桌请求。

AppGallery Kit返回加桌结果给应用。

约束与限制

应用市场推荐服务不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。

应用市场推荐服务支持Phone、Tablet、PC/2in1设备。并且从6.0.2(22)版本开始，新增支持TV设备。

接口说明

详细接口说明可参考接口文档。

接口名	描述
checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, labelResName: string, iconResName: string): Promise<CheckShortcutResult>	以静态资源方式校验桌面快捷方式。
checkPinShortcutPermitted(context: common.UIAbilityContext, shortcutId: string, want: Want, label: string, foregroundIcon: string, backgroundIcon: string): Promise<CheckShortcutResult>	以自定义资源方式校验桌面快捷方式。
requestNewPinShortcut(context: common.UIAbilityContext, tid: string): Promise<void>	创建桌面快捷方式。
开发步骤
以静态资源方式创建桌面快捷方式

导入productViewManager模块及相关公共模块。

import { productViewManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

构造调用checkPinShortcutPermitted接口校验桌面快捷方式的参数。

const uiContext =this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前Page页面的上下文信息
const shortcutId = "id_test1"; // 对应shortcuts标签中配置的shortcutId, 例如: "shortcutId": "id_test1"
const labelResName = "shortcut"; // 对应shortcuts标签中配置的label资源索引名称, 例如: "label": "$string:shortcut"
const iconResName = "aa_icon"; // 对应shortcuts标签中配置的icon资源索引名称, 例如: "icon": "$media:aa_icon"
const want: Want = {            // 对应shortcuts标签中配置的want
  bundleName: "com.example.appgallery.kit.demo",
  moduleName: "entry",
  abilityName: "EntryAbility",
  parameters: {
    testKey: "testValue"
  }
};
说明

需提前创建应用静态快捷方式，且shortcutId、labelResName、iconResName、want参数需要与shortcuts标签中的配置保持一致。

若校验参数发生变化，则每次覆盖生成新的tid，否则返回历史tid以及剩余过期时间expired。

调用checkPinShortcutPermitted接口，将步骤2中的全部参数依次传入接口中，并保存异步返回的结果CheckShortcutResult。

try {
  let checkShortcutResult: productViewManager.CheckShortcutResult;
  productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, labelResName, iconResName)
    .then((result: productViewManager.CheckShortcutResult) => {
      hilog.info(0x0001, 'TAG', `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`);
      checkShortcutResult = result;
    }).catch((error: BusinessError) => {
    hilog.error(0x0001, 'TAG',
      `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
  })
} catch (err) {
  hilog.error(0x0001, 'TAG', `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
}

构造调用requestNewPinShortcut接口创建桌面快捷方式的参数。

const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前Page页面的上下文信息
const tid = checkShortcutResult.tid;

将步骤4中的uiContext、tid参数依次传入requestNewPinShortcut接口中。

try {
  productViewManager.requestNewPinShortcut(uiContext, tid)
    .then(() => {
      hilog.info(0x0001, 'TAG', `requestNewPinShortcut success.`);
    }).catch((error: BusinessError) => {
    hilog.error(0x0001, 'TAG', `requestNewPinShortcut error. code is ${error.code}, message is ${error.message}`);
  })
} catch (err) {
  hilog.error(0x0001, 'TAG', `requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}`);
}
说明

快捷方式加桌成功后，原校验结果tid会失效，再次加桌需重新校验生成新的tid。

推荐预先调用checkPinShortcutPermitted接口，确保用户有权限在桌面上创建快捷方式，避免无效操作，当用户点击加桌后，再调用requestNewPinShortcut接口执行加桌请求。

为了减少权限检查时间和提高加桌操作流畅性，不建议在用户点击加桌后再连续调用这两个接口执行加桌。

以自定义资源方式创建桌面快捷方式

导入productViewManager模块及相关公共模块。

import { productViewManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

构造调用checkPinShortcutPermitted接口构造校验桌面快捷方式的参数。

const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // 当前Page页面的上下文信息
const shortcutId = `${Date.now()}`; // 快捷方式ID
  // 点击快捷方式后被拉起的目标应用的bundleName、moduleName、abilityName
const want: Want = {
  bundleName: "com.example.appgallery.kit.demo",
  moduleName: "entry",
  abilityName: "EntryAbility",
  parameters: {
    testKey: "testValue"
  }
 }
 const label = "shortcut"; // 显示在桌面名称的文本内容
 // 显示在桌面图标的应用沙箱地址，图标最大不超过100KB，格式为png和webp
 const foregroundIcon = uiContext.filesDir + "/icon.png";
 const backgroundIcon = "";
说明

当前不支持背景层图标，参数backgroundIcon传空字符串。

若校验参数发生变化，则每次覆盖生成新的tid，否则返回历史tid以及剩余过期时间expired。

调用checkPinShortcutPermitted接口，将步骤2中的全部参数依次传入接口中，并保存异步返回的结果CheckShortcutResult。

try {
  let checkShortcutResult: productViewManager.CheckShortcutResult;
  productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, label, foregroundIcon, backgroundIcon)
    .then((result: productViewManager.CheckShortcutResult) => {
      hilog.info(0x0001, 'TAG', `checkPinShortcutPermitted success result is ${JSON.stringify(result)}`)
      checkShortcutResult = result;
    }).catch((error: BusinessError) => {
    hilog.error(0x0001, 'TAG',
      `checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}`);
  })
} catch (err) {
  hilog.error(0x0001, 'TAG', `checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}`);
}

构造调用requestNewPinShortcut接口创建桌面快捷方式的参数。

const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前Page页面的上下文信息
// checkPinShortcutPermitted接口返回的属性tid值。
const tid = checkShortcutResult.tid;

调用requestNewPinShortcut接口，将步骤4中的参数依次传入接口中。

try {
  productViewManager.requestNewPinShortcut(uiContext, tid)
    .then(() => {
      hilog.info(0x0001, 'TAG', `requestNewPinShortcut success.`);
    }).catch((error: BusinessError) => {
    hilog.error(0x0001, 'TAG', `requestNewPinShortcut error. code is ${error.code}, message is ${error.message}`);
  })
} catch (err) {
  hilog.error(0x0001, 'TAG', `requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}`);
}
说明

快捷方式加桌成功后，原校验结果tid会失效，再次加桌需重新校验生成新的tid。

为了提升用户体验，推荐预先调用checkPinShortcutPermitted接口，当用户点击加桌后，再调用requestNewPinShortcut接口执行加桌请求。

不建议在用户点击加桌后再连续调用这两个接口执行加桌。

应用内快捷方式
查询应用内快捷方式
