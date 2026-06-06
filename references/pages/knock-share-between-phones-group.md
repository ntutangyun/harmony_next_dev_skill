# 邀请组队

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-group_

针对以上场景，Share Kit提供单向仅发送能力。参考：SendCapabilityRegistry的sendOnly属性。

若碰一碰的双方都设置单向仅发送，则终止本次分享并提示用户"请任意一方退出当前应用后再试"；反之，均可分享成功。

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';


@Component
export default struct Index {
  aboutToAppear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
      sendOnly: true, // 声明仅支持单向发送 若对端也同样声明仅支持单向发送 则双向分享时会失败
    }
    harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
      let uiContext: UIContext = this.getUIContext();
      let contextFaker: Context = uiContext.getHostContext() as Context;
      let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // 仅为示例 请替换正确的文件路径
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.HYPERLINK,
        content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
        // 根据title,description,thumbnailUri会生成不同的卡片模板。
        thumbnailUri: fileUri.getUriFromPath(filePath),
        title: '碰一碰分享卡片标题',
        description: '碰一碰分享卡片描述'
      });
      sharableTarget.share(shareData);
    });
  }


  aboutToDisappear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
    }
    // 解除碰一碰分享'knockShare'监听事件
    harmonyShare.off('knockShare', capabilityRegistry);
  }


  build() {
  }
}
设置组队邀请预览

预览图设置参考：设置分享预览。

处理组队链接

当目标应用被分享拉起时，可以通过onCreate或onNewWant回调中获取传入的want参数。其中want.uri字段为邀请组队的链接，通过链接上携带的参数信息，处理组队邀请的业务逻辑。

示例代码：

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';


export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    try {
      windowStage.loadContent('pages/Index');
    } catch (error) {
      console.error(`onWindowStageCreate error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }


  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info('EntryAbility onCreate invoked. uri: ', want.uri);
    // to do things.
  }


  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info('EntryAbility onNewWant invoked. uri: ', want.uri);
    // to do things.
  }
}
异常场景终止分享

当碰一碰分享回调触发时，发生异常场景导致无法继续分享，可终止本次分享。

参考：异常场景终止分享。

内容分享
手机与PC/2in1碰一碰分享
