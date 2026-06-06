# ohpm

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-restore_

该命令会停止当前ohpm-repo服务，并用打包文件<file_path>中的内容替换ohpm-repo部署根目录<deploy_root>的相应文件，然后重启ohpm-repo服务。该命令执行前必须已执行过ohpm-repo实例启动命令ohpm-repo start。

说明
<file_path>：由ohpm-repo pack命令得到的打包产物。

支持相对和绝对路径配置，当配置为相对路径时，以当前命令行工作路径为根目录。

<deploy_root>：ohpm-repo部署根目录 执行install命令后，会创建一个名为OHPM_REPO_DEPLOY_ROOT的环境变量，记录的是ohpm-repo私仓部署目录。
参数
<file_path>
类型：String
必填参数

指定待解压的打包文件路径。

示例

执行以下命令：

ohpm-repo restore "D:\pack_1702625827995.zip"

结果示例：

ohpm-repo deploy
ohpm-repo mirror_storage
