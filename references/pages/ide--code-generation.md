# 代码生成

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide--code-generation_

CodeGenie具备自然语言代码生成能力，在对话框内输入代码需求描述，点击发送，将自动生成符合要求的代码段。

DevEco Studio 6.0.2 Beta1之前版本，生成的代码一键复制或一键插入至编辑区当前光标位置。

在DevEco Studio 6.0.2 Beta1版本，生成的代码直接应用到代码文件中；在Changed Files中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原；以及支持在问答区编译验证功能。

从DevEco Studio 6.0.2 Release版本开始，使用HarmonyOS Act智能体时，生成的代码直接应用到代码文件中；在Changed Files中可查看被修改的文件，修改前后内容对比，逐项接受或拒绝；代码还原，以及支持在问答区编译验证。

操作步骤

选择HarmonyOS Act智能体，在对话框输入功能描述，点击发送，等待生成。

在问答区域的Changed Files可以查看被修改的文件，点击文件对比修改前后差异；将鼠标悬浮在文件路径上，点击可接受或拒绝该文件的修改；点击Accept All/Reject All按钮，接受或拒绝所有文件的修改；在编辑器右键Local History > Show History，查看历史修改文件还原代码。

点击问答区中Run，可以编译验证；开启Auto Run开关，可以开启自动编译验证。Auto Run更多描述可参考Agent配置。

示例

在index页面中添加一个可以跳转至另外页面的按钮。
