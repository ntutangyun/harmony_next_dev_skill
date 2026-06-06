# 添加和删除模块

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-new-module_

模块（Module）是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件。一个应用/元服务通常会包含一个或多个模块，因此，可以在工程中创建多个模块。模块支持entry、feature（仅应用工程支持创建）、har、shared四种类型，具体请参考module.json5配置文件。

从DevEco Studio 6.0.1 Beta1开始，创建Native C++模块或Library模板时支持选择C++版本。

创建新的模块
通过如下三种方法，在工程中添加新的模块。

方法1：鼠标移到工程目录顶部，单击鼠标右键，选择New > Module...，开始创建新的Module，此时该模块将创建在工程根目录下。
方法2：选中工程目录中任意文件，然后在菜单栏选择File > New > Module...，开始创建新的Module，此时该模块将创建在工程根目录下。
方法3：在工程根目录下创建一个新的Directory，可在该目录下单击鼠标右键，选择New > Module...，创建新的模块，此时模块将创建在该文件目录下，方便开发者对模块进行分类管理。
说明

当前暂不支持在AppScope、hvigor、oh_modules、build、以点开头的目录（如：.hvigor、.idea）下通过单击鼠标右键创建模块。

在New Project Module界面中，选择需要创建的模板，单击Next。

在模块配置页面，设置新增模块的基本信息，然后单击Next。

Module name：新增模块的名称，Module name不可与工程名称/工程中其他模块名称相同。
Module type：仅在Ability模板存在该字段，可以选择Feature和Entry类型。
说明
同一工程通过新增模块仅支持创建一个entry模块。如需构建entry类型模块，可在module.json5文件中修改相应module下的type字段。
如果同一类型的设备已经存在entry模块，出现新的entry模块后，还需要配置分发策略。
Device type：选择模块的设备类型，如果新建模块的Module type为feature，则只能选择该工程原有的设备类型；如果Module type为entry，可以选择该模块支持的其他设备类型。
Enable native：仅Library模板存在，将创建一个可以调用C/C++的共享包。
C++ Standard：C++标准库，取值包括：Toolchain Default、C++11、C++14。从DevEco Studio 6.0.1 Beta1开始支持。

若该模块的模板类型为Ability，还需要设置新增Ability的Ability name和Exported参数，Exported参数表示该Ability是否可以被其它应用/元服务所调用（FA模型下为Visible参数)。

勾选（true）：可以被其它应用/元服务调用。
不勾选（false）：不能被其它应用/元服务调用。

单击Finish，等待创建完成后，可以在工程目录中查看和编辑新增的模块。工程中所包含模块的信息可以在build-profile.json5中modules字段进行配置。
删除模块

在工程目录中选中要删除的模块，单击鼠标右键，选中Delete，并在弹出的对话框中单击Delete。

模块管理
导入和引用模块
