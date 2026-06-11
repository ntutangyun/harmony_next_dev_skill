# 创建模拟器

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create_

有网络环境可参考以下步骤创建模拟器，如果是无网络环境，请查看离线部署模拟器。

说明

在macOS中，您可能在活动监视器中发现模拟器进程占用的内存超过设置的内存。实际上，活动监视器中的Memory并不代表模拟器进程实际使用的物理内存，更多详情请参考macOS上活动监视器中显示模拟器内存偏高。

使用预置的模拟器

从DevEco Studio 6.1.0 Beta2版本开始，如果本地没有模拟器，DevEco Studio会预置模拟器，开发者无需创建即可快速使用。

说明

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

在设备选择框中，选择预置的模拟器并点击运行按钮后，根据界面提示下载镜像，或点击菜单栏Tools > Device Manager >下载镜像后，即可快捷使用模拟器。

创建新的模拟器

在模拟器配置界面，可以选择一个默认的设备模板，首次使用时请点击设备右侧的下载模拟器镜像，您也可以在该界面更新或删除不同设备的模拟器镜像。

单击Edit可以设置镜像文件的存储路径。macOS默认存储在~/Library/Huawei/Sdk下，Windows默认存储在C:\Users\xxx\AppData\Local\Huawei\Sdk下。

说明

如果配置界面显示异常，例如设备列表为空等，可先关闭DevEco Studio，并进入~/Library/Huawei（Windows路径为C:\Users\xxx\AppData\Local\Huawei）目录，删除DevEcoStudiox.x文件夹（如DevEcoStudio6.0，具体文件夹名称和安装的DevEco Studio版本相关）以清理缓存。

Name：设置模拟器的名称。

Screen size：屏幕的对角线长度，单位为inch。

Resolution：分辨率，包括宽度和高度，单位为px。

DPI：像素密度，DPI 越高，UI组件占用的像素点越多，从而提供更精细的显示效果。

Cold boot：以开机启动的方式重新启动。

Quick boot：启动时加载上次关闭时保存的快照，启动后会恢复至上次关闭时的状态。

Memory：设置模拟器的内存。

Storage：设置模拟器的存储空间。

确认所有参数后，点击Finish创建模拟器。
