# 分布式媒体会话常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-faq-distributed_

本文汇总音视频应用在分布式媒体会话（投播）接入AVSession Kit过程中遇到的典型问题及其定位与解决方法。开发者可结合媒体会话管理错误码和HiLog日志进一步定位问题。

无法正确获取投播视频总时长

问题现象

发起投播后，无法正确获取投播视频总时长（duration）。

可能原因

投播场景下，视频总时长需要通过AVCastController（投播控制器）获取。如果AVCastController对象未正确创建，或媒体尚未在远端开始播放（时长由远端解析媒体后上报），则无法获取到总时长。

解决措施

通过以下任一方式获取投播总时长：

方式一：注册on('playbackStateChange')事件，回调返回的AVPlaybackState中的extras字段携带duration媒体播放总时长。

// 注册播放状态变化监听，从extras中获取投播总时长。
avCastController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  if (playbackState.extras?.duration !== undefined) {
    let duration = playbackState.extras.duration as number;
    console.info(`Cast duration: ${duration} ms`);
  }
});

方式二：注册on('mediaItemChange')事件，回调返回的AVQueueItem中，其description（AVMediaDescription）的duration字段即为媒体播放总时长。

// 注册投播媒体内容变化监听，从AVQueueItem中获取投播总时长。
avCastController.on('mediaItemChange', (item: avSession.AVQueueItem) => {
  let duration = item.description?.duration;
  console.info(`Cast duration: ${duration} ms`);
});

方式三：通过getCurrentItem获取当前投播的资源信息，返回的AVQueueItem中description的duration字段即为媒体播放总时长。

// 获取当前投播资源信息，从AVQueueItem中获取投播总时长。
let item: avSession.AVQueueItem = await avCastController.getCurrentItem();
let duration = item.description?.duration;
console.info(`Cast duration: ${duration} ms`);

若上述方式均获取不到时长，请确认投播控制器AVCastController对象已正确创建，且媒体已在远端开始播放。AVCastController对象需在投播连接成功后才能获取，请在投播连接成功后再进行时长获取相关操作。

投播控制命令失效

问题现象

手机投播到支持标准DLNA协议的电视设备后，发送的控制命令失效，如快进、快退、seek等命令无响应或on('seekDone')等回调未触发。

可能原因

应用侧控制命令回调未正确注册，或控制命令未正确发送。

对端设备不支持相应的控制能力，或本端与对端设备存在兼容性问题。

本端发送的控制命令参数有误。

解决措施

确认问题是否为应用独有。若只有当前应用出现该问题，先排查应用侧控制命令回调是否正确注册（如通过sendControlCommand发送命令、注册对应监听）；若其他应用投播同一设备同样异常，则继续向下排查。

确认是否与对端设备有关。尝试更换对端设备验证，例如投播到HarmonyOS 5.0.0及以上版本的PC/2in1设备、HarmonyOS 3.1及以上的TV设备，或其他支持标准DLNA协议的设备。若更换设备后问题消失，说明问题在远端设备；若问题依旧，说明问题在本端设备。

检查是否有投播错误回调。若注册了on('error')或投播控制错误回调（如on('castControlGenericError')）并收到错误，可通过抓包工具，观察报文中的错误码，进一步确认是本端命令参数问题还是对端能力不支持。

投播歌词不显示

问题现象

投播到远端设备后，远端设备不显示歌词内容。

可能原因

歌词内容超出长度限制。投播场景下，歌词通过AVQueueItem中AVMediaDescription的lyricContent字段传递，字符串长度需小于40960字节，超出限制将导致歌词不显示。

对端设备不支持歌词展示。部分对端设备可能不支持歌词展示能力。

解决措施

确保歌词内容不超过40960字节的长度限制。

尝试更换对端设备验证。建议投播到HarmonyOS 5.0.0及以上版本的PC/2in1设备、HarmonyOS 3.1及以上的TV设备等支持完整投播能力的设备进行对比。

投播到PC/2in1设备时鼠标悬停歌词停止滚动

问题现象

投播到PC/2in1设备上时，会在PC/2in1播放器进行播放。鼠标悬停到歌词区域时，歌词停止滚动；移开鼠标后，歌词恢复到正确的播放位置继续滚动。

可能原因

此为PC/2in1播放器的设计行为。鼠标悬停在歌词区域时，PC/2in1播放器会暂停歌词自动滚动，方便用户查看和浏览歌词内容；鼠标移开后，歌词自动回到与当前播放进度匹配的位置并恢复滚动。

解决措施

该现象为PC/2in1播放器的正常设计规格，无需应用侧处理。

控制远端设备音量不一致

问题现象

投播后在本端调节音量，远端设备实际音量变化与本端显示不一致，或调节音量无响应。

可能原因

可投播的南向设备存在硬件差异，不同远端设备的最大音量不一致（例如TV设备为100，PC/2in1为20或15），直接按本端音量值下发会导致与远端实际音量不匹配。

解决措施

可参考如下方案实现音量的归一化处理与下发：

通过监听AVCastController的on('playbackStateChange')回调，从AVPlaybackState的extras字段获取当前对端设备的最大音量格子数（maxCastVolume），计算音量变化步长，并将远端上报的volume换算为本端音量值。

import { avSession } from '@kit.AVSessionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'CastVolume';
// 本端最大音量基准值。
const MAX_VOLUME_VALUE = 100;
// 远端设备的最大音量格子数（TV设备：100，PC/2in1：20或15等，由远端上报）。
private maxCastVolume: number = MAX_VOLUME_VALUE;
// 每次按下系统音量键远端音量变化的步长值（不同远端设备步长可能不同）。
private changeVolumeStepSize: number = 1;
// 当前本端维护的音量值。
private currentVolume: number = 0;

listenPlaybackStateChange() {
  // 创建avCastController，并监听播放状态变化，关注volume字段。
  avCastController.on('playbackStateChange', ['volume'], (playbackState: avSession.AVPlaybackState) => {
    if (playbackState) {
      this.volumeChangeHandle(playbackState);
    }
  });
}

volumeChangeHandle(avState: avSession.AVPlaybackState) {
  // 从 extras 中获取远端最大音量格子数，换算步长。
  if (avState.extras?.maxCastVolume !== undefined && typeof avState.extras?.maxCastVolume === 'number') {
    this.maxCastVolume = avState.extras?.maxCastVolume as number ?? MAX_VOLUME_VALUE;
    this.changeVolumeStepSize = Math.round(MAX_VOLUME_VALUE / this.maxCastVolume) || 1;
    hilog.info(0x0000, TAG, `volumeChangeHandle, changeVolumeStepSize: ${this.changeVolumeStepSize}, maxCastVolume: ${this.maxCastVolume}`);
  }
  // 将远端上报的音量值换算为本端步长值的整数倍。
  if (avState.volume !== undefined && avState.volume >= 0) {
    let currentVolumeStep = Math.round(avState.volume * this.maxCastVolume / MAX_VOLUME_VALUE);
    this.currentVolume = currentVolumeStep * this.changeVolumeStepSize;
  }
}

注册inputConsumer.on('keyPressed')拦截物理音量键事件，按计算出的步长累加/递减音量后，通过sendControlCommand下发setVolume命令（命令类型见AVCastControlCommandType）。

说明

inputConsumer.on('keyPressed') 从API版本16开始支持。订阅成功后，该按键的系统默认行为（如系统级音量调节）将被屏蔽，需在不再需要时调用inputConsumer.off('keyPressed')取消订阅以恢复系统响应。

设备行为差异：API版本23之前，该接口在Phone和Tablet设备上可正常调用，其他设备返回801错误码；从API版本23开始，增加支持PC/2in1和TV设备。

import { avSession } from '@kit.AVSessionKit';
import { inputConsumer, KeyCode, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'CastVolume';
const MAX_VOLUME_VALUE = 100;

// 封装投播音量设置接口。
public async setAVCastVolume(volume: number): Promise<void> {
  let avCommand: avSession.AVCastControlCommand = { command: 'setVolume', parameter: volume };
  try {
    await this.avCastController.sendControlCommand(avCommand);
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `setAVCastVolume failed, code: ${err.code}, message: ${err.message}`);
  }
}

// 拦截音量增事件。
public interceptIncrease() {
  let upOptions: inputConsumer.KeyPressedConfig = { key: KeyCode.KEYCODE_VOLUME_UP, action: 1, isRepeat: true };
  try {
    inputConsumer.on('keyPressed', upOptions, async (event: KeyEvent) => {
      let remoteVolume = this.currentVolume + this.changeVolumeStepSize;
      this.currentVolume = remoteVolume > MAX_VOLUME_VALUE ? MAX_VOLUME_VALUE : remoteVolume;
      await this.setAVCastVolume(this.currentVolume);
    });
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `register volume up failed, code: ${err.code}, message: ${err.message}`);
  }
}

// 拦截音量减事件。
public interceptDecrease() {
  let downOptions: inputConsumer.KeyPressedConfig = { key: KeyCode.KEYCODE_VOLUME_DOWN, action: 1, isRepeat: true };
  try {
    inputConsumer.on('keyPressed', downOptions, async (event: KeyEvent) => {
      let remoteVolume = this.currentVolume - this.changeVolumeStepSize;
      this.currentVolume = remoteVolume < 0 ? 0 : remoteVolume;
      await this.setAVCastVolume(this.currentVolume);
    });
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `register volume down failed, code: ${err.code}, message: ${err.message}`);
  }
}

投播发现不了设备

问题现象

发起投播时，搜索不到可投播的目标远端设备。

可能原因

会话filter协议设置为0。AVMetadata的filter字段表示当前会话支持的投播协议（取值见ProtocolType），默认为TYPE_CAST_PLUS_STREAM。若误设为0（TYPE_LOCAL，仅本地设备），系统将不会为其发现远端投播设备。

未通过setExtras声明投播能力。应用需通过setExtras向系统声明支持URL投播，入参形如{[ExtraKey.REQUIRE_ABILITY_LIST]: [ExtraKey.SUPPORT_URL_CASTING]}（见ExtraKey）。若未传入SUPPORT_URL_CASTING（'url-cast'），系统不会将该应用识别为可投播应用，导致发现不到设备。

解决措施

检查AVMetadata的filter字段，按需设置为TYPE_CAST_PLUS_STREAM、TYPE_DLNA等远端协议。

通过setExtras声明支持URL投播，入参传入SUPPORT_URL_CASTING（'url-cast'）。

## Code blocks

### Code block 1

```
// 注册播放状态变化监听，从extras中获取投播总时长。
avCastController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  if (playbackState.extras?.duration !== undefined) {
    let duration = playbackState.extras.duration as number;
    console.info(`Cast duration: ${duration} ms`);
  }
});
```

### Code block 2

```
// 注册投播媒体内容变化监听，从AVQueueItem中获取投播总时长。
avCastController.on('mediaItemChange', (item: avSession.AVQueueItem) => {
  let duration = item.description?.duration;
  console.info(`Cast duration: ${duration} ms`);
});
```

### Code block 3

```
// 获取当前投播资源信息，从AVQueueItem中获取投播总时长。
let item: avSession.AVQueueItem = await avCastController.getCurrentItem();
let duration = item.description?.duration;
console.info(`Cast duration: ${duration} ms`);
```

### Code block 4

```
import { avSession } from '@kit.AVSessionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'CastVolume';
// 本端最大音量基准值。
const MAX_VOLUME_VALUE = 100;
// 远端设备的最大音量格子数（TV设备：100，PC/2in1：20或15等，由远端上报）。
private maxCastVolume: number = MAX_VOLUME_VALUE;
// 每次按下系统音量键远端音量变化的步长值（不同远端设备步长可能不同）。
private changeVolumeStepSize: number = 1;
// 当前本端维护的音量值。
private currentVolume: number = 0;

listenPlaybackStateChange() {
  // 创建avCastController，并监听播放状态变化，关注volume字段。
  avCastController.on('playbackStateChange', ['volume'], (playbackState: avSession.AVPlaybackState) => {
    if (playbackState) {
      this.volumeChangeHandle(playbackState);
    }
  });
}

volumeChangeHandle(avState: avSession.AVPlaybackState) {
  // 从 extras 中获取远端最大音量格子数，换算步长。
  if (avState.extras?.maxCastVolume !== undefined && typeof avState.extras?.maxCastVolume === 'number') {
    this.maxCastVolume = avState.extras?.maxCastVolume as number ?? MAX_VOLUME_VALUE;
    this.changeVolumeStepSize = Math.round(MAX_VOLUME_VALUE / this.maxCastVolume) || 1;
    hilog.info(0x0000, TAG, `volumeChangeHandle, changeVolumeStepSize: ${this.changeVolumeStepSize}, maxCastVolume: ${this.maxCastVolume}`);
  }
  // 将远端上报的音量值换算为本端步长值的整数倍。
  if (avState.volume !== undefined && avState.volume >= 0) {
    let currentVolumeStep = Math.round(avState.volume * this.maxCastVolume / MAX_VOLUME_VALUE);
    this.currentVolume = currentVolumeStep * this.changeVolumeStepSize;
  }
}
```

### Code block 5

```
import { avSession } from '@kit.AVSessionKit';
import { inputConsumer, KeyCode, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'CastVolume';
const MAX_VOLUME_VALUE = 100;

// 封装投播音量设置接口。
public async setAVCastVolume(volume: number): Promise<void> {
  let avCommand: avSession.AVCastControlCommand = { command: 'setVolume', parameter: volume };
  try {
    await this.avCastController.sendControlCommand(avCommand);
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `setAVCastVolume failed, code: ${err.code}, message: ${err.message}`);
  }
}

// 拦截音量增事件。
public interceptIncrease() {
  let upOptions: inputConsumer.KeyPressedConfig = { key: KeyCode.KEYCODE_VOLUME_UP, action: 1, isRepeat: true };
  try {
    inputConsumer.on('keyPressed', upOptions, async (event: KeyEvent) => {
      let remoteVolume = this.currentVolume + this.changeVolumeStepSize;
      this.currentVolume = remoteVolume > MAX_VOLUME_VALUE ? MAX_VOLUME_VALUE : remoteVolume;
      await this.setAVCastVolume(this.currentVolume);
    });
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `register volume up failed, code: ${err.code}, message: ${err.message}`);
  }
}

// 拦截音量减事件。
public interceptDecrease() {
  let downOptions: inputConsumer.KeyPressedConfig = { key: KeyCode.KEYCODE_VOLUME_DOWN, action: 1, isRepeat: true };
  try {
    inputConsumer.on('keyPressed', downOptions, async (event: KeyEvent) => {
      let remoteVolume = this.currentVolume - this.changeVolumeStepSize;
      this.currentVolume = remoteVolume < 0 ? 0 : remoteVolume;
      await this.setAVCastVolume(this.currentVolume);
    });
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `register volume down failed, code: ${err.code}, message: ${err.message}`);
  }
}
```
