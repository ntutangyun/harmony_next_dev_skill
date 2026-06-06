# 媒体库资源访问工具

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mediatool_

- 1 user_data_rw user_data_rw 6107481 2025-05-28 20:34 IMG_1748435794_000.jpg
-rw-rw---- 1 user_data_rw user_data_rw 839323 2025-05-28 23:06 IMG_1748444892_016.jpg
-rw-rw---- 1 user_data_rw user_data_rw 9614937 2025-05-28 23:41 IMG_1748446677_032.jpg
-rw-rw---- 1 user_data_rw user_data_rw 3004885 2025-05-29 00:43 IMG_1748450699_048.jpg
-rw-rw---- 1 user_data_rw user_data_rw 1915961 2025-05-29 01:18 IMG_1748452814_064.jpg
-rw-rw---- 1 user_data_rw user_data_rw 13078 2025-05-29 02:41 IMG_1748457806_080.jpeg
> hdc shell mediatool recv /storage/media/local/files/Photo/16/IMG_1748435794_000.jpg /data/local/tmp/out.jpg
Table Name: Photos
/data/local/tmp/out.jpg
> hdc file recv /data/local/tmp/out.jpg .
FileTransfer finish, Size:10015455, File count = 1, time:679ms rate:14750.30kB/s
导出所有媒体库资产
> hdc shell mkdir /data/local/tmp/media
> hdc shell mediatool recv all /data/local/tmp/media
Table Name: Photos
/data/local/tmp/media/MyImage.jpg


Table Name: Audios
> hdc shell tar -cvf /data/local/tmp/media.tar /data/local/tmp/media/*
removing leading '/' from member names
data/local/tmp/media/MyImage.jpg
> hdc file recv /data/local/tmp/media.tar .
FileTransfer finish, Size:10017280, File count = 1, time:664ms rate:15086.27kB/s
删除特定媒体库资产

示例删除图库中名字叫MyImage的jpg图片：

> hdc shell mediatool query -u MyImage.jpg
find 1 result
uri
"file://media/Photo/1/IMG_1743078145_000/MyImage.jpg"
> hdc shell mediatool delete file://media/Photo/1/IMG_1743078145_000/MyImage.jpg
[SUCCESS] delete success.
彻底重置媒体库数据库
> hdc shell mediatool delete all
媒体库uri介绍/获取方式

uri是媒体库资产的唯一标识符。mediatool使用uri来判断需要操作的媒体资产对象。

可使用以下方式获取uri：

mediatool query 加上 -u 的选项可以返回对应媒体资产的uri。需要输入对应资产的显示名（在图库中展示的名字带后缀名）。

媒体库uri可以用于mediatool recv命令导出特定媒体库资产，也可以用于mediatool delete删除特定媒体库资产。

uri样例：file://media/Photo/1/IMG_1743078145_000/MyImage.jpg。

在mediatool操作中，需要使用以上uri时，无论使用file://media/Photo/1/IMG_1743078145_000/MyImage.jpg还是file://media/Photo/1都能够正确的定位到目标资产。

hdc命令

从API version 21开始，支持通过hdc命令可以访问媒体库文件路径。包含：/mnt/data/<uid>/media_fuse/Photo/目录及其子目录。<uid>为当前用户的id。

媒体库文件查询

支持查询指定路径下未被隐藏的图片和视频。

命令格式如下所示。

hdc shell ls -l DEST

使用示例：

$ hdc shell ls -l /mnt/data/100/media_fuse/Photo # 返回相册列表
drwxrwxrwx 2 user_data_rw user_data_rw 3440 1970-01-01 00:00 其它
drwxrwxrwx 2 user_data_rw user_data_rw 3440 1970-01-01 00:00 相机
$ hdc shell ls -l /mnt/data/100/media_fuse/Photo/相机 # 列出相机文件夹下所有未被隐藏的本地图片和视频
total 32813056
-rw-rw-rw- 1 user_data_rw user_data_rw 7085591 1970-01-01 00:00 1.jpg
-rw-rw-rw- 1 user_data_rw user_data_rw 6217442 1970-01-01 00:00 2.jpg
$ hdc shell ls -l /mnt/data/100/media_fuse/Photo/相机/1.jpg # 命令返回1.jpg的详细信息
-rw-rw-rw- 1 user_data_rw user_data_rw 7085591 1970-01-01 00:00 /mnt/data/100/media_fuse/Photo/相机/1.jpg
媒体库文件导出

支持导出指定路径下所有未被隐藏的本地文件和目录。

命令格式如下所示。

hdc file recv DEST SOURCE

使用示例：

$ hdc file recv /mnt/data/100/media_fuse/Photo/相机/文件A # 导出文件A
FileTransfer finish, Size:xxx, File...
$ hdc file recv /mnt/data/100/media_fuse/Photo/相机 # 导出相机目录及里面的文件
FileTransfer finish, Size:xxx, File...
$ hdc file recv /mnt/data/100/media_fuse/Photo/ # 导出Photo目录及其子文件
FileTransfer finish, Size:xxx, File...
媒体库文件导入

支持导入媒体文件（图片、视频等）及目录，但不支持创建目录。当目录名称相同时会将内容合并（保留所有不重名的文件）；当文件名称相同时会覆盖目标文件。

hdc file send SOURCE DEST

使用示例：

$ hdc file send D:\dest\相机 /mnt/data/100/media_fuse/Photo/ # 导入“D:\dest\相机”的所有文件到/mnt/data/100/media_fuse/Photo/相机/
FileTransfer finish, Size:xxx, File...
$ hdc file send D:\dest\新建目录 /mnt/data/100/media_fuse/Photo/相机/ # 不支持创建目录
[Fail][E005005] Error create directory: operation not permitted, path:/mnt/data/100/media_fuse/Photo/相机//新建目录
$ hdc file send D:\dest\相机\文件A /mnt/data/100/media_fuse/Photo/相机 # 导入文件A到/mnt/data/100/media_fuse/Photo/相机/
FileTransfer finish, Size:xxx, File...
媒体库文件删除

支持删除相册中的指定文件，但不支持删除目录。

hdc shell rm DEST

使用示例：

$ hdc shell rm /mnt/data/100/media_fuse/Photo/相机 # 返回失败
rm: /mnt/data/100/media_fuse/Photo/相机: Is a directory
$ hdc shell rm /mnt/data/100/media_fuse/Photo/相机/文件A # 无返回信息，删除成功
toybox
devicedebug工具
