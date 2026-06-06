# 判断应用是否被系统分享拉起

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-launch-param_

通过UIAbility处理分享内容时，可使用onCreate或onNewWant的LaunchParam.launchReasonMessage字段是否为'ReasonMessage_SystemShare'判断。

通过UIExtensionAbility处理分享内容时，可使用onCreate的LaunchParam.launchReasonMessage字段是否为'ReasonMessage_SystemShare'判断。

示例代码

通过UIAbility处理分享内容。

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';


export default class ShareUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
      // 识别为被系统分享拉起
      console.info('被拉起原因：系统分享');
    }
  }


  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
      // 识别为被系统分享拉起
      console.info('被拉起原因：系统分享');
    }
  }


  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/ShareUIPage'); // 此路径仅为示例 请替换实际路径
  }
}

通过UIExtensionAbility处理分享内容。

import { AbilityConstant, ShareExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';


export default class ShareExtAbility extends ShareExtensionAbility {
  onCreate(launchParam: AbilityConstant.LaunchParam): void {
    if (launchParam.launchReasonMessage === 'ReasonMessage_SystemShare') {
      // 识别为被系统分享拉起
      console.info('被拉起原因：系统分享');
    }
  }


  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    session.loadContent('pages/ShareExtDialog'); // 此路径仅为示例 请替换实际路径
  }
}
分享详情页关闭分享面板
共享联系人信息到分享推荐区
