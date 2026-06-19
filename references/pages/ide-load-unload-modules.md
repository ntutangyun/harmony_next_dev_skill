# 卸载和加载模块

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-load-unload-modules_

功能介绍

在大工程开发过程中，模块较多时会导致内存占用高和代码索引较慢，影响开发效率。从26.0.0 Beta1版本开始，DevEco Studio提供加载/卸载模块（Load/Unload Modules）的功能，开发者可以按照需求加载模块，从而降低对内存资源占用和提升代码索引效率。但是，加载/卸载模块功能可能会影响代码编辑能力，具体请参考下面表格。

加载/卸载模块功能	代码编辑能力	是否可用
加载模块	代码高亮	可用
语法、语义检查	可用
代码联想	可用
代码跳转	可用
引用查找	可用（无法查找到卸载模块的引用）
代码搜索（双击Shift键打开）	可用
代码重构	可用（重构时不修改卸载模块的代码）
模块编译	可用
卸载模块	代码高亮	可用
语法、语义检查	不可用
代码联想	不可用
代码跳转	部分可用（加载模块直接或间接引用链上的文件，可正常跳转至定义处）
引用查找	不可用
代码搜索（双击Shift键打开）	可用
代码重构	不可用
模块编译	可用

操作步骤

在工程根目录或模块根目录单击鼠标右键，选择Load/Unload Modules...，会弹出加载/卸载模块的可视化操作界面。

在Loaded Modules窗口勾选模块后点击Unload，可将模块添加到卸载模块；在Unloaded Modules窗口勾选模块后点击Load，可将模块添加到加载模块。

点击Unload All可将加载的模块全部添加到卸载模块中，点击Load All可将卸载的模块全部添加到加载模块中。

说明

开发者可以在[projectPath]/.idea/.deveco/unload/unload.modules.json文件中查看卸载模块信息。
