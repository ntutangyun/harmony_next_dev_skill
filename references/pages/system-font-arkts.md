# 系统字体的信息获取和使用（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-font-arkts_

--------' + String(fontConfig.fontDir.length));
for (let i = 0; i < fontConfig.fontDir.length; i++) {
  console.info(fontConfig.fontDir[i]);
}
console.info('sysFontMfg::generic-------------' + String(fontConfig.generic.length));
for (let i = 0; i < fontConfig.generic.length; i++) {
  console.info('sysFontMfg::family:' + fontConfig.generic[i].family);
  for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
    console.info(fontConfig.generic[i].alias[j].name + ' ' + fontConfig.generic[i].alias[j].weight);
  }
}
console.info('sysFontMfg::fallback------------' + String(fontConfig.fallbackGroups.length));
for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
  console.info('sysFontMfg::fontSetName:' + fontConfig.fallbackGroups[i].fontSetName);
  for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
    console.info('sysFontMfg::language:' + fontConfig.fallbackGroups[i].fallback[j].language + ' family:' +
      fontConfig.fallbackGroups[i].fallback[j].family);
  }
}
Index.ets

以下打印的示例为应用设备系统对应的部分系统字体配置信息情况，不同设备系统配置信息可能不同，此处仅示意。

使用或切换系统字体

系统字体可以有多种，可以先获取系统字体配置信息，再根据其中的字体家族名（即TextStyle中的fontFamilies）来进行系统字体的切换和使用。

如果不指定使用任何字体时，会使用系统默认字体“HarmonyOS Sans”显示文本。

导入依赖的相关模块。

import { text } from '@kit.ArkGraphics2D';

创建textStyle1，指定fontFamilies为“HarmonyOS Sans SC”，默认中文字体为“HarmonyOS Sans SC”。

let textStyle1: text.TextStyle = {
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  fontSize: 100,
  fontFamilies: ['HarmonyOS Sans SC']
};
Index.ets

创建textStyle2，指定fontFamilies为“HarmonyOS Sans TC”（该两种字体易于观察同一文字字型差异）。

let textStyle2: text.TextStyle = {
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  fontSize: 100,
  fontFamilies: ['HarmonyOS Sans TC']
};
Index.ets

创建段落生成器。

// 创建一个段落样式对象，以设置排版风格
let myParagraphStyle: text.ParagraphStyle = {
  textStyle: textStyle1,
  align: 3,
  wordBreak: text.WordBreak.NORMAL
};
// 获取全局字体集实例
let fontCollection = text.FontCollection.getGlobalInstance(); //获取Arkui全局FC
// 创建一个段落生成器
let ParagraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
Index.ets

先后将textStyle1和textStyle2添加到段落样式中并添加文字。

let str:string = '模块描述\n';
// 添加第一种文本样式和对应文本内容
ParagraphGraphBuilder.pushStyle(textStyle1);
ParagraphGraphBuilder.addText(str);
// 添加第二种文本样式和对应文本内容
ParagraphGraphBuilder.pushStyle(textStyle2);
ParagraphGraphBuilder.addText(str);
Index.ets

生成段落，用于后续绘制使用。

let paragraph = ParagraphGraphBuilder.build();
Index.ets

效果展示如下：

自定义字体的注册和使用（ArkTS）
使用主题字体（C/C++）
