# Clang-Tidy代码检查

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-clang-tidy_

DevEco Studio支持通过内置的Clang-Tidy和自定义的Clang-Tidy对C/C++代码进行静态检查，以及支持配置检查规则，帮助开发者快速发现C++编码的问题。

检查规则配置

当前支持通过三种方式配置检查规则。

[h2]方式一：在Clang-Tidy Checks中配置

添加检查规则时，可点击按钮展开规则填写框，在不同行添加规则。添加完成后点击按钮，多条规则会自动用英文逗号隔开。

[h2]方式二：在 .clang-tidy文件中配置

在工程根目录中或在编辑器中搜索找到并打开 .clang-tidy文件。

[h2]方式三：在Inspection-checks中配置

在工程目录顶部或工程目录中任意文件，单击鼠标右键选择Inspect Code...。

在菜单栏点击Code > Inspect Code...。

添加检查规则时，可点击按钮展开规则填写框，在不同行添加规则。添加完成后点击按钮，多条规则会自动用英文逗号隔开。

通过内置Clang-Tidy检查代码

使用内置Clang-Tidy进行代码自动实时检查和手动检查。

[h2]自动实时检查

生效规则

若勾选了live update（show in “Current File”），自动实时检查时，Clang-Tidy Checks、.clang-tidy文件和Inspection-checks中配置的规则均生效；若不勾选live update（show in “Current File”），自动实时检查时，Clang-Tidy Checks和 .clang-tidy文件中配置的规则生效。

操作步骤

代码编辑时，工具自动提示语法错误等，将鼠标放置在错误代码处会显示详细的错误信息。

[h2]手动检查

生效规则

手动检查时，仅Inspection-checks中配置的规则生效。

操作步骤

在工程目录顶部或工程目录中任意文件，单击鼠标右键选择Inspect Code...。

在菜单栏点击Code > Inspect Code...。

通过自定义Clang-Tidy检查代码

从26.0.0 Beta1版本开始，支持使用自定义Clang-Tidy进行代码自动实时检查和手动检查。

生效规则

勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，.clang-tidy文件中配置的规则生效。

不勾选Prefer .clang-tidy files over IDE settings时，自动实时检查和手动检查时，Inspection-checks中配置的规则生效。

操作步骤

说明

clang-tidy.exe可从DevEco Studio安装目录中获取。

进入clang-tidy界面，若勾选Prefer .clang-tidy files over IDE settings， .clang-tidy文件中配置的规则生效；若不勾选Prefer .clang-tidy files over IDE settings，Inspection-checks中配置的规则生效。

若勾选live update（show in “Current File”），会开启自动实时检查；若不勾选，需要手动检查，手动检查操作具体请参考内置Clang-Tidy的手动检查。
