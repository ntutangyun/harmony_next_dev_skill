# 管理麦克风静音状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mic-management_

因为在录制过程中需要使用麦克风录制相关音频数据，所以建议开发者在调用录制接口前查询麦克风状态，并在录制过程中监听麦克风的状态变化，避免影响录制效果。

在音频录制过程中，用户可以将麦克风静音，此时录音过程正常进行，录制生成的数据文件的大小随录制时长递增，但写入文件的数据均为0，即无声数据（空白数据）。

录音不支持音量调节。

开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取完整示例。

在AudioVolumeGroupManager中提供了管理麦克风状态的方法，接口的详细说明请参考音量API文档AudioVolumeGroupManager。

创建audioVolumeGroupManager对象。

import { audio } from '@kit.AudioKit';

let audioVolumeGroupManager: audio.AudioVolumeGroupManager;
// 创建audioVolumeGroupManager对象。
async function loadVolumeGroupManager(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
  const groupid = audio.DEFAULT_VOLUME_GROUP_ID;
  audioVolumeGroupManager = await audio.getAudioManager().getVolumeManager().getVolumeGroupManager(groupid);
  console.info('audioVolumeGroupManager create success.');
  // ...
}

调用on('micStateChange')监听麦克风状态变化，当麦克风静音状态发生变化时将通知应用。

目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅），因此推荐使用单一AudioManager实例进行开发。

// 监听麦克风状态变化。
async function on() {
  audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
    console.info(`Current microphone status is: ${micStateChange.mute} `);
  });
}

调用isMicrophoneMute查询麦克风当前静音状态，返回true为静音，false为非静音。

// 查询麦克风是否静音。
async function isMicrophoneMute(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
  await audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
    console.info(`isMicrophoneMute is: ${value}.`);
    // ...
  });
}

## Code blocks

### Code block 1

```
import { audio } from '@kit.AudioKit';

let audioVolumeGroupManager: audio.AudioVolumeGroupManager;
// 创建audioVolumeGroupManager对象。
async function loadVolumeGroupManager(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
  const groupid = audio.DEFAULT_VOLUME_GROUP_ID;
  audioVolumeGroupManager = await audio.getAudioManager().getVolumeManager().getVolumeGroupManager(groupid);
  console.info('audioVolumeGroupManager create success.');
  // ...
}
```

### Code block 2

```
// 监听麦克风状态变化。
async function on() {
  audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
    console.info(`Current microphone status is: ${micStateChange.mute} `);
  });
}
```

### Code block 3

```
// 查询麦克风是否静音。
async function isMicrophoneMute(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
  await audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
    console.info(`isMicrophoneMute is: ${value}.`);
    // ...
  });
}
```
