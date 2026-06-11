# 应用UI生成

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator_

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

启用插件

单击OK并关闭设置窗口，插件启用成功。

开始使用

在DevEco Studio菜单栏点击Tools > Generate Project From...打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。

待配置项	说明
Installation package path	待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。
SDK path	等于或高于编译应用包所使用版本的SDK路径。
Git Bash path	Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。

待配置项	说明
Destination Path	生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改）
Compatible SDK	生成的新工程所使用的SDK版本

生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。

更多操作指导，请参考视频课程：毕方HarmonyOS UI代码生成工具。
