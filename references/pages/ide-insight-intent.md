# 创建意图框架

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent_

DevEco Studio支持创建意图框架，帮助应用理解用户意图，并提供相应的服务和体验。

使用约束

支持API 11及以上工程创建意图框架；

仅支持在Stage工程的HAP模块中创建意图框架。

使用方式

Intent domain：意图垂域。

Source entry name：意图框架入口代码文件名。

PlayMusic：开启/关闭PlayMusic意图能力，实现播放歌曲（指定一首）。默认需要关联UIAbility，可在Ability name中下拉框选择需要关联的Ability能力。

PlayMusicList：开启/关闭PlayMusicList意图能力，实现播放歌单（指定一整个歌单）。默认需要关联UIAbility，可在Ability name下拉框中选择需要关联的Ability能力。

说明

PlayMusic和PlayMusicList不支持同时关闭，请至少开启一个意图。
