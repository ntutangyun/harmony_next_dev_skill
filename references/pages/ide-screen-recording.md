# 录屏

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording_

点击DevEco Studio底部Log页签，选择HiLog > Settings > Record Screen选项。

在弹出的界面选择自定义路径，当设置好路径并勾选“Use the selected path and auto-generated file name as defaults and don't ask again”选项后，录屏时将自动使用此时设置的路径以及以录屏时的时间戳构造的文件名作为录屏文件的保存地址及文件名。

通过命令行方式录屏

hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见hdc工具使用指导。

启动录屏。

hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4

停止录屏。

hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility

获取录屏文件位置，记录为{RecordFile}。

hdc shell mediatool query test.mp4 -u
如果查询的结果中包含uri字段，则返回值第三行对应的录屏文件路径不允许直接下载。

需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp

命令返回值第二行即为录屏文件路径{RecordFile}。

如果查询结果不包含uri字段，则返回值第二行即为录屏文件路径{RecordFile}。

指定上一个步骤中获取到的录屏文件路径{RecordFile}，下载录屏文件到本地。

hdc file recv {RecordFile} d:\test.mp4

截屏
调试错误码
