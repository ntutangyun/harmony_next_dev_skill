# 创建意图框架

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent_

PlayMusic：开启/关闭PlayMusic意图能力，实现播放歌曲（指定一首）。默认需要关联UIAbility，可在Ability name中下拉框选择需要关联的Ability能力。
PlayMusicList：开启/关闭PlayMusicList意图能力，实现播放歌单（指定一整个歌单）。默认需要关联UIAbility，可在Ability name下拉框中选择需要关联的Ability能力。
说明

PlayMusic和PlayMusicList不支持同时关闭，请至少开启一个意图。

点击Finish，完成意图框架创建。此时将在entry > src > main > ets > insightintents目录下生成入口代码文件；在entry > src > main > resource > base > profile中，生成insight_intent.json文件，可在该文件查看当前意图框架配置的相关信息。

创建服务卡片
端云一体化开发
