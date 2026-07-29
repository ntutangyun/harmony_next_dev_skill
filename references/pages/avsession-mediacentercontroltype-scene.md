# 自定义播控中心控制按钮显示布局

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-mediacentercontroltype-scene_

从API版本26.0.0开始，系统支持自定义播控中心的控制按钮显示布局。本文档将介绍应用如何自定义播控中心显示的控制类型。

基本概念

播控中心常见的控制按钮类型包括：播放、暂停、上一首、下一首、快进、快退、收藏、循环模式、倍速，共九种。

应用通过avSession.createAVSession接口的入参AVSessionType设置会话类型。播控中心根据该类型显示对应的控制按钮组合，详见创建不同类型的会话。例如，audio类型会话在播控中心二级界面显示的按钮（从左至右）为：收藏、上一首、播放/暂停、下一首、循环模式。

播控中心的控制按钮布局分为三元组和五元组两种模式：

三元组：显示三个控制按钮，如播控中心一级界面

五元组：显示五个控制按钮，如播控中心二级界面

按钮位置编号规则（从左至右）：

五元组：四号位、二号位、一号位、三号位、五号位

三元组：二号位、一号位、三号位

本文后续描述均遵循此编号规则。

接入方案

系统提供setMediaCenterControlType接口，允许应用设置希望在播控中心优先显示的控制类型列表。播控中心根据该列表定制各界面的控制按钮布局。

可设置的控制类型详见AVMediaCenterControlType，其中不包含播放/暂停命令，因为播放/暂停的控制按钮在播控中心界面固定显示于一号位。

对于循环模式和倍速这类具有可选范围的控制类型，系统提供了专门的接口：

循环模式：使用setSupportedLoopModes设置支持的循环模式列表，播控中心据此显示对应的循环模式图标。可设置的模式请参考LoopMode。

倍速：使用setSupportedPlaySpeeds设置支持的倍速列表，播控中心据此显示对应的倍速图标。

[h2]按钮排布规则

播控中心会解析通过setMediaCenterControlType接口设置的控制类型列表，并按特定规则将控制按钮排布在三元组/五元组中。这个排布规则与传入的控制类型列表中元素的顺序无关，而是与控制类型是否在列表中存在有关。针对循环模式与倍速按钮的显示，还与应用设置的可选范围有关。

具体的排布规则如下：

一号位固定为播放/暂停按钮。

二号位优先显示下一首按钮。若列表不含下一首，则按序选择：快退 → 循环模式 → 收藏。

三号位优先显示上一首按钮。若列表不含上一首，则按序选择：快进 → 收藏 → 倍速。

四号位优先显示快退按钮。若列表不含快退，则按序选择：循环模式 → 收藏。

五号位优先显示快进按钮。若列表不含快进，则按序选择：收藏 → 倍速。

上一首与下一首成对出现，快进与快退成对出现。若列表仅包含其一，系统默认支持另一个。

如果列表包含循环模式，且满足以下任一条件，循环模式按钮才可显示：注册on('setLoopMode')监听；或注册on('setTargetLoopMode')监听并通过setSupportedLoopModes设置了长度大于1的循环模式列表。循环模式按钮仅显示于二号位或四号位（播放/暂停按钮左侧）。

如果列表包含倍速，且通过setSupportedPlaySpeeds设置了长度大于1的倍速列表，倍速按钮才可显示。倍速按钮仅显示于三号位或五号位（播放/暂停按钮右侧）。

当三元组/五元组同时支持循环模式和收藏时，收藏按钮显示于循环模式按钮右侧。

当三元组/五元组同时支持倍速和收藏时，收藏按钮显示于倍速按钮左侧。

当三元组/五元组支持收藏，但不支持循环模式和倍速时，收藏按钮优先显示于三号位或五号位（播放/暂停按钮右侧）。

支持的控制按钮优先填充二号位和三号位，其次填充四号位和五号位，剩余控制按钮显示在更多入口小窗中。

注意

本方案仅涉及按钮显示布局，按钮置灰逻辑仍遵循处理不支持的控制命令。

参考案例

说明

以下示例代码展示了应用如何在播控中心五元组上从左到右依次显示循环模式、上一首、播放/暂停、下一首、倍速。

import { avSession as AVSessionManager } from '@kit.AVSessionKit';

// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as Context;
            // 假设已经创建了一个session，如何创建session可以参考之前的案例。
            let type: AVSessionManager.AVSessionType = 'audio';
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
            // 设置必要的媒体信息和监听。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0',
              title: 'TITLE',
            };
            await session.setAVMetadata(metadata);
            session.on('play', () => {
              console.info(`onPlay`);
            });
            // 调用接口设置支持的控制命令类型列表
            session.setMediaCenterControlType(['playNext', 'setLoopMode', 'setSpeed']);
            // 注册'setTargetLoopMode'监听并设置支持的循环模式范围，以支持播控中心显示循环模式按钮
            session.on('setTargetLoopMode', (loopMode: AVSessionManager.LoopMode) => {
              console.info(`targetLoopMode change: ${loopMode}`);
            });
            session.setSupportedLoopModes(
              [AVSessionManager.LoopMode.LOOP_MODE_SINGLE, AVSessionManager.LoopMode.LOOP_MODE_LIST,
                AVSessionManager.LoopMode.LOOP_MODE_SHUFFLE]);
            // 设置支持的倍速范围，以支持播控中心显示倍速按钮
            session.setSupportedPlaySpeeds([0.5, 1.0, 2]);
            // 设置完成后，播控中心三元组会显示上一首、播放/暂停、下一首；五元组会显示循环模式、上一首、播放/暂停、下一首、倍速
            // ...
          } catch (err) {
            console.error(`Failed to setMediaCenterControlType. Code: ${err.code}, message: ${err.message}`);
          }

        })
    }
    .width('100%')
    .height('100%')
  }
}

## Code blocks

### Code block 1

```
import { avSession as AVSessionManager } from '@kit.AVSessionKit';

// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as Context;
            // 假设已经创建了一个session，如何创建session可以参考之前的案例。
            let type: AVSessionManager.AVSessionType = 'audio';
            let session = await AVSessionManager.createAVSession(context, 'SESSION_NAME', type);
            // 设置必要的媒体信息和监听。
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0',
              title: 'TITLE',
            };
            await session.setAVMetadata(metadata);
            session.on('play', () => {
              console.info(`onPlay`);
            });
            // 调用接口设置支持的控制命令类型列表
            session.setMediaCenterControlType(['playNext', 'setLoopMode', 'setSpeed']);
            // 注册'setTargetLoopMode'监听并设置支持的循环模式范围，以支持播控中心显示循环模式按钮
            session.on('setTargetLoopMode', (loopMode: AVSessionManager.LoopMode) => {
              console.info(`targetLoopMode change: ${loopMode}`);
            });
            session.setSupportedLoopModes(
              [AVSessionManager.LoopMode.LOOP_MODE_SINGLE, AVSessionManager.LoopMode.LOOP_MODE_LIST,
                AVSessionManager.LoopMode.LOOP_MODE_SHUFFLE]);
            // 设置支持的倍速范围，以支持播控中心显示倍速按钮
            session.setSupportedPlaySpeeds([0.5, 1.0, 2]);
            // 设置完成后，播控中心三元组会显示上一首、播放/暂停、下一首；五元组会显示循环模式、上一首、播放/暂停、下一首、倍速
            // ...
          } catch (err) {
            console.error(`Failed to setMediaCenterControlType. Code: ${err.code}, message: ${err.message}`);
          }

        })
    }
    .width('100%')
    .height('100%')
  }
}
```
