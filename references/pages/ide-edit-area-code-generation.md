# 编辑区对话

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation_

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型进行生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

从26.0.0 Beta1版本开始，如未出现浮框，可在File > Settings > CodeGenie >Inline Chat（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Inline Chat）中勾选Show inline chat floating hints启用浮窗。

从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在File > Settings > CodeGenie > Code Suggestion & Inline Chat（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Suggestion & Inline Chat）中勾选Show inline chat floating hints启用浮窗。

从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在File > Settings > CodeGenie > Code Completion & Inline Chat（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Completion & Inline Chat）中勾选Show Inline Chat tips启用浮窗。

在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在File > Settings > CodeGenie > Code Generation（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Generation）中取消勾选Hide Inline Chat Overlay选项。

绿色区域：新生成的代码内容。

蓝色区域：对现有代码进行修改的内容。

红色区域：删除的代码内容。

点击Inline Chat对话框中Accept All（或使用快捷键Alt+Enter），接受当前生成的全部内容；

点击Inline Chat对话框中刷新按钮/Regenerate，将根据当前描述重新生成代码片段；

点击编辑区中Accept（或使用快捷键Shift+Ctrl+Y，macOS上为Shift+Command+Y），分段逐一接受并保留生成内容；

点击编辑区中Reject（或使用快捷键Shift+Ctrl+N，macOS上为Shift+Command+N），分段逐一拒绝并删除当前生成内容；

点击Further Edit（或使用快捷键Ctrl+K，macOS上为Command+K），重新进行输入，开始新一轮问答。
