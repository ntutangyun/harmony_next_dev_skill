# 使用本地真机运行应用

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device_

在真机设备上查看设置 > 系统中开发者选项是否存在，如果不存在，可在设置 > 具体的设备名称中，连续七次单击软件版本，直到提示“开启开发者选项”，点击确认开启后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
在设备运行应用/元服务需要根据配置调试签名章节，提前对应用/元服务进行签名。
使用USB连接方式
使用USB方式，将真机设备与PC端进行连接。
在设置 > 系统 > 开发者选项中，打开USB调试开关（确保设备已连接USB）。
在真机设备中会弹出“允许USB调试”的弹框，单击允许。

在菜单栏中，单击Run>Run'模块名称'或，或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。

DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。
使用设备连接助手排查问题

从DevEco Studio 5.1.1 Beta1版本开始，设备连接后，如果DevEco Studio无法识别到设备，显示“No Devices”，可使用设备连接助手来排查问题。点击设备下拉框，并点击Troubleshoot Device Connections打开该功能，分为三个步骤，每个步骤排查完后点击Next排查下一个。

通过USB连接设备：根据界面提示，使用USB连接设备后，点击Rescan Devices按钮，扫描已连接的设备，确保扫描结果中包含待调试的设备。
启用USB调试：根据界面提示，确保设备系统版本正确，并且启用开发者选项和USB调试。
重启HDC服务：如果DevEco Studio仍然无法识别设备，点击Restart hdc Service按钮重启HDC服务，重启后HDC会重新识别设备。如果重启后仍识别不到设备，请参考设备连接后，无法识别设备的处理指导或如何解决设备无法识别问题。
使用无线连接方式
将真机设备和PC连接到同一WLAN网络。
在设置 > 系统 > 开发者选项中，打开无线调试或通过WLAN调试（Wearable设备）开关，并获取设备端的IP地址和端口号。

连接设备，有两种方式。

在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。

执行hdc命令，关于hdc工具的使用指导请参考hdc。
hdc tconn 设备IP地址:端口号

在菜单栏中，单击Run>Run'模块名称'或，或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。

DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

配置调试签名
使用仿真器运行轻量级穿戴应用

## Code blocks

### Code block 1

```
hdc tconn 设备IP地址:端口号
```
