# 编辑区对话

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-edit-area-code-generation_

CodeGenie提供Inline Edit能力，支持在ArkTS文件的编辑窗口中通过自然语言进行问答，基于上下文智能生成代码片段，提升代码可读性。

从DevEco Studio 6.0.2 Beta1开始，Inline Edit支持选择三方模型，根据指定的模型进行生成代码。

从DevEco Studio 6.1.0 Beta1开始，Inline Edit入口名称变更为Inline Chat。

当前有以下两种方式唤醒Inline Chat对话框：

若未选中代码片段，在代码编辑区域右键选择CodeGenie > Inline Chat（或使用快捷键Alt+I，macOS中为Command+I）。

若选中一段代码，点击Inline Chat（或使用快捷键Alt+I，macOS中为Command+I）浮框。

在DevEco Studio 6.1.0 Beta2之前版本，如未出现浮框，可在File > Settings > CodeGenie > Code Generation（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Generation）中取消勾选Hide Inline Chat Overlay选项。

从DevEco Studio 6.1.0 Beta2版本开始，如未出现浮框，可在File > Settings > CodeGenie > Code Completion & Inline Chat（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Completion & Inline Chat）中勾选Show Inline Chat tips启用浮窗。

从DevEco Studio 6.1.0 Release版本开始，如未出现浮框，可在File > Settings > CodeGenie > Code Suggestion & Inline Chat（macOS中为DevEco Studio > Preferences/Settings > CodeGenie > Code Suggestion & Inline Chat）中勾选Show inline chat floating hints启用浮窗。

选择在CodeGenie中已配置的三方模型，或者使用默认模型。三方模型配置具体请参考模型（Model）配置。

若选择默认模型，在对话框中输入所需要的代码功能描述，在键盘输入回车或点击发送，开始生成代码。点击Stop Generation，中断本轮代码生成过程。

若选择三方模型，支持分析当前代码文件和生成分析报告，以及进行参数校验（Parameter Validation）、代码注释（Code Explanation）、代码优化（Code Optimization），分析报告和参数校验等结果跟模型有关，具体操作如下：
未选中代码片段，在对话框中输入"/"，在键盘输入回车或点击发送，对当前代码文件开始分析。点击Stop Generation，中断本轮代码生成过程。

选中一段代码，在对话框中输入"/"，选择Parameter Validation/Code Explanation/Code Optimization，可输入或不输入所需的功能描述，在键盘输入回车或点击发送后开始生成。点击Stop Generation，中断本轮代码生成过程。

生成完毕将在编辑区展示本轮生成的代码内容，并通过不同颜色体现与当前代码的对比差异。

绿色区域：新生成的代码内容。
蓝色区域：对现有代码进行修改的内容。
红色区域：删除的代码内容。
点击Inline Chat对话框中Accept All（或使用快捷键Alt+Enter），接受当前生成的全部内容；
点击Inline Chat对话框中刷新按钮/Regenerate，将根据当前描述重新生成代码片段；
点击编辑区中Accept（或使用快捷键Shift+Ctrl+Y，macOS上为Shift+Command+Y），分段逐一接受并保留生成内容；
点击编辑区中Reject（或使用快捷键Shift+Ctrl+N，macOS上为Shift+Command+N），分段逐一拒绝并删除当前生成内容；
点击Further Edit（或使用快捷键Ctrl+K，macOS上为Command+K），重新进行输入，开始新一轮问答。

编辑区代码生成
代码续写
