# 代码分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-analyse_

CodeGenie支持在对话框中输入对代码段和代码文件分析要求，帮助开发者快速理解代码逻辑、代码功能、技术细节和潜在问题等，提升开发效率。

DevEco Studio 6.0.2 Beta1之前版本，分析代码文件时需要通过Files入口选中文件；分析代码片段时，选中代码段后需点击图标开启光标上下文功能。

在DevEco Studio 6.0.2 Beta1版本，分析代码文件时，支持在对话框输入要分析的代码文件或直接分析当前文件；分析代码片段时，选中代码段后直接分析，无需开启图标。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Ask智能体分析代码文件。

选择HarmonyOS Ask智能体，在对话框中输入“/”，点击Project。

在对话框输入@符号选择Files，或点击@Add Context > Files，或在对话框输入文件路径，指定需要分析的代码文件。未指定代码文件时，分析当前代码文件。

在对话框输入描述，点击发送后等待回复。
