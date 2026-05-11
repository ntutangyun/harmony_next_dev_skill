# 打包工具

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/packing-tool_

打包工具用于在程序编译完成后，对编译出的文件等进行打包，以供安装发布。开发者可以使用DevEco Studio进行打包，也可使用打包工具的JAR包进行打包，JAR包通常存放在SDK路径下的toolchains目录中。

打包工具支持生成：Ability类型的模块包（HAP）、动态共享包（HSP）、应用程序包（App）、快速修复模块包（HQF）、快速修复包（APPQF）。

打包指令中的文件来源于DevEco Studio编译构建产物，文件路径查看操作如下。

在DevEco Studio工程根目录下的/hvigor/hvigor-config.json5文件中，修改"logging"下的"level"字段为"debug"。

在DevEco Studio菜单栏，依次选择"构建 -> 清理项目"。

在DevEco Studio菜单栏，依次选择"构建 -> 构建APP(s)"。

在DevEco Studio底部"构建"窗口，搜索"app_packing_tool.jar"，确认打包参数中文件的路径。

打包工具会对module.json文件属性进行合法性校验。module.json文件是编译构建产物，其属性值在编译构建时自动生成，与配置文件中配置项对应关系如下。

表1 module.json与配置文件属性的对照表

module.json属性	含义	module.json5配置项	app.json5配置项	工程级build-profile.json5配置项
bundleName	应用的Bundle名称。	-	bundleName	-
bundleType	应用的Bundle类型。	-	bundleType	-
versionCode	应用的版本号。	-	versionCode	-
debug	应用是否可调试。	-	debug	-
module/name	当前Module的名称。	module/name	-	-
minCompatibleVersionCode	应用能够兼容的最低历史版本号。	-	minCompatibleVersionCode	-
minAPIVersion	应用运行所需的最小API版本。	-	minAPIVersion	compatibleSdkVersion
targetAPIVersion	应用运行需要的API目标版本。	-	targetAPIVersion	

targetSdkVersion/compileSdkVersion

说明：targetSdkVersion存在时，targetAPIVersion由targetSdkVersion决定；

否则，targetAPIVersion由compileSdkVersion决定。


querySchemes	允许应用进行跳转查询的URL schemes。	querySchemes	-	-
generateBuildHash	标识当前HAP或HSP是否由打包工具生成哈希值。	generateBuildHash	generateBuildHash	-
buildVersion	应用的构建版本号。	-	buildVersion	-
打包拆包工具
拆包工具
