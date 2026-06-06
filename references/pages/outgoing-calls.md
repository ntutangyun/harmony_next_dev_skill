# 去电场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/outgoing-calls_

on(type: 'voipCallUiEvent', callback: Callback<VoipCallUiEventInfo>): void	订阅voipCallUiEvent事件。
off(type: 'voipCallUiEvent', callback?: Callback<VoipCallUiEventInfo>): void	取消订阅voipCallUiEvent事件。
reportOutgoingCall(voipCallAttribute: VoipCallAttribute): Promise<ErrorReason>	上报去电。
reportCallAudioEventChange(callId: string, callAudioEvent: CallAudioEvent): Promise<void>	上报音频事件。
reportCallStateChange(callId: string, callState: VoipCallState): Promise<void>	上报通话状态改变。
reportCallStateChange(callId: string, callState: VoipCallState, callType: VoipCallType): Promise<void>	上报通话状态改变，并指定通话类型。
开发步骤

去电场景的开发步骤与来电场景相似。

导入相关依赖。

import { voipCall } from '@kit.CallServiceKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

为了感知到用户在实况窗上做的静音与解除静音、挂断通话等操作，应用需要注册voipCallUiEvent事件。建议在上报去电之前注册。

示例代码如下：

// 注册voipCallUiEvent事件
voipCall.on('voipCallUiEvent', callback => {
  hilog.info(0x0000, 'CallDemo', 'Succeeded in registering voipCallUiEvent');
});

应用内部建立通话连接之后，需要向Call Service Kit上报去电，并携带通话信息，详见VoipCallAttribute。

系统会在屏幕左上角，展示通话胶囊。

以语音去电为例，示例代码如下：

// 构建上报去电的参数
let voipCallAttribute: voipCall.VoipCallAttribute = {
  callId: '1234567890',
  voipCallType: voipCall.VoipCallType.VOIP_CALL_VOICE,
  userName: 'Jack',
  userProfile: image.createPixelMapSync(new ArrayBuffer(100), { size: { width: 90, height: 90 } }),
  abilityName: 'VoipCallAbility',
  voipCallState: voipCall.VoipCallState.VOIP_CALL_STATE_DIALING,  // 去电的状态必须是DIALING
  showBannerForIncomingCall: true
};


// 向Call Service Kit上报去电
voipCall.reportOutgoingCall(voipCallAttribute).then(errorReason => {
  if (errorReason == voipCall.ErrorReason.ERROR_NONE) {
    hilog.info(0x0000, 'CallDemo', 'Succeeded in reporting the outgoing call');
  } else {
    hilog.error(0x0000, 'CallDemo', 'Failed to report the outgoing call: %{public}d', errorReason);
  }
});
注意

上报去电时，通话状态必须是VOIP_CALL_STATE_DIALING，否则Call Service Kit会认为参数不合法而返回1007200001错误码。

如果对端接听，应用需要向Call Service Kit上报通话状态VOIP_CALL_STATE_ACTIVE。系统会更新通话胶囊，开始展示通话计时。

示例代码如下：

// ...应用服务器收到对端接听的消息
let answeredCallId = '123456'; //与reportOutgoingCall携带callId一致，应用内通话唯一ID。


// 向Call Service Kit上报通话状态
voipCall.reportCallStateChange(answeredCallId, voipCall.VoipCallState.VOIP_CALL_STATE_ACTIVE);

去电场景，用户也可以拉起通知中心面板，在实况窗通知上执行静音或解除静音。

开发方法与来电场景相同，详见来电场景：静音与解除静音。

去电场景，用户也可以拉起通知中心面板，在实况窗通知上点击挂断。

开发方式与来电场景相同，详见来电场景：用户点击挂断。

通话结束后，可以解除voipCallUiEvent事件。

示例代码如下：

// 解除voipCallUiEvent事件
voipCall.off('voipCallUiEvent', callback => {
  hilog.info(0x0000, 'CallDemo', `Succeeded in unRegistering voipCallUiEvent, callId: ${callback.callId}`);
});
来电场景
企业联系人信息来去电页面显示
