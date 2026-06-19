# 工程问答

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask_

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

调用MCP工具

点击界面右上方按钮，或者点击界面右上方Settings按钮，选择MCP > MCP Market。

添加和开启所需的MCP工具。

返回到CodeGenie首页，在对话区域输入“/”，在弹出的菜单中选择“Project ”，输入所需的描述，点击发送后等待回复。

示例：

调用LSP工具

在对话区域输入“/”，在弹出的菜单中选择“Project ”，输入所需的描述，点击发送后等待回复。

示例：

语义检索

在菜单栏点击File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General，勾选Project Semantic Index下的Enable选项。

点击Apply或点击OK，开启语义检索功能。

在对话区域输入“/”，在弹出的菜单中选择“Project ”，输入所需的描述，点击发送后等待回复。

示例：
