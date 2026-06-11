# 离线部署模拟器

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-no-network_

如果开发者所使用的电脑处于完全无网络的离线环境中，需要先在一台可访问网络的电脑上准备好DevEco Studio并下载模拟器镜像，将DevEco Studio和模拟器镜像文件拷贝到无网络电脑中。

有网络电脑：

在可访问网络的电脑上下载安装DevEco Studio，并下载所需的模拟器镜像，具体可参考创建模拟器。

例如在Windows电脑下载手机镜像，并指定镜像下载路径为D:\Sdk，实际完整的镜像路径是D:\Sdk\system-image\HarmonyOS-xxx\phone_all_x86。

说明

如未指定镜像下载路径，默认路径请参考创建模拟器。

无网络电脑：

拷贝镜像时，在无网络电脑新建存放镜像的目录，如D:\No-network\Sdk，在此目录下新建镜像子文件夹路径system-image\HarmonyOS-xxx\phone_all_x86，将有网络电脑phone_all_x86下的所有文件拷贝到该路径下。
