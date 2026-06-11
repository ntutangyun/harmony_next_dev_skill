# 录屏

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-screen-recording_

在应用开发过程中，可以使用录屏功能录制应用的运行状态，并通过录屏文件向他人展示正在开发的应用的各种功能效果。

使用约束

如果设置了锁屏密码，录屏开始前请解锁设备屏幕，锁屏状态下录屏应用无法正常拉起。

如果设置了锁屏密码，录屏时请保持设备的屏幕解锁状态，若录屏过程中锁屏将导致录屏应用退出。

模拟器不支持录屏。

通过DevEco Studio录屏

连接真机设备，并在其中运行应用。

在DevEco Studio底部切换到Log页签。

设置录屏自定义路径

通过命令行方式录屏

hdc是可以用于调试的命令行工具，通过该工具可以实现录屏功能。更多关于命令行工具hdc的说明请参见hdc工具使用指导。

hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4

hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility

hdc shell mediatool query test.mp4 -u

需要再执行如下命令，指定该uri，将录屏文件复制到有下载权限的路径中（如/data/local/tmp）。

hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp

命令返回值第二行即为录屏文件路径{RecordFile}。

hdc file recv {RecordFile} d:\test.mp4

## Code blocks

### Code block 1

```
hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // 指定录屏文件名称为test.mp4
```

### Code block 2

```
hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility
```

### Code block 3

```
hdc shell mediatool query test.mp4 -u
```

### Code block 4

```
hdc shell mediatool recv "file://media/Photo/2/VID_1736853237_001/test.mp4" /data/local/tmp
```

### Code block 5

```
hdc file recv {RecordFile} d:\test.mp4
```
