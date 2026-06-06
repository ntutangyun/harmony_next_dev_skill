# 使用SoundPlayer开发系统音效播放功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundplayer-for-playback_

支持的音效类型SystemSoundType信息如下表所示。可通过systemSoundManager.SystemSoundType.PHOTO_SHUTTER等具体类型，作为load、play或unload方法的入参。

播放音效类型	值	说明
PHOTO_SHUTTER	0	拍照音效。
VIDEO_RECORDING_BEGIN	1	视频录制开始音效。
VIDEO_RECORDING_END	2	视频录制结束音效。
开发步骤

以下各步骤示例为片段代码，可通过点击示例代码右下方的链接获取完整示例。

在调用SystemSoundPlayer的接口前，需要先通过createSystemSoundPlayer创建实例。

import { systemSoundManager } from '@kit.AudioKit';
// ...


// SystemSoundPlayer对象。
let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;


// ...
  systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
    console.info('Succeeded in creating the system sound player.');
    systemSoundPlayer = systemSoundPlayerInstance;
  }).catch((err: BusinessError) => {
    console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
  });
SoundPlayer.ets

调用load接口，加载指定类型音效资源。

import { systemSoundManager } from '@kit.AudioKit';
// ...


// 音效类型。
let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;


// ...
  systemSoundPlayer?.load(systemSoundType).then(() => {
    console.info('Succeeded in calling the load method.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to call the load method. Code: ${err.code}, message: ${err.message}`);
  });
SoundPlayer.ets

调用play接口，播放已加载的音效资源。

import { systemSoundManager } from '@kit.AudioKit';
// ...


// 音效类型。
let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;


// ...
  systemSoundPlayer?.play(systemSoundType).then(() => {
    console.info('Succeeded in calling the play method.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to call the play method. Code: ${err.code}, message: ${err.message}`);
  });
SoundPlayer.ets

调用unload接口，卸载之前已加载的音效资源。

import { systemSoundManager } from '@kit.AudioKit';
// ...


// 音效类型。
let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;


// ...
  systemSoundPlayer?.unload(systemSoundType).then(() => {
    console.info('Succeeded in calling the unload method.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to call the unload method. Code: ${err.code}, message: ${err.message}`);
  });
SoundPlayer.ets

调用release接口，释放系统音效播放器。

systemSoundPlayer?.release().then(() => {
  console.info('Succeeded in calling the release method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the release method. Code: ${err.code}, message: ${err.message}`);
});
SoundPlayer.ets
使用AudioHaptic开发音振协同播放功能(ArkTs)
播放音量管理
