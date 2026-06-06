# 应用文件访问(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fileio-guidelines_

FileManagement_ErrCode OH_FileIO_GetFileLocation(char *uri, int uriLength, FileIO_FileLocation *location)	获取文件存储位置。
enum FileIO_FileLocation FileIO_FileLocation	文件存储位置枚举值。
enum FileManagement_ErrCode FileManagement_ErrCode	文件管理模块错误码。
开发步骤

在CMake脚本中链接动态库

CMakeLists.txt中添加以下lib。

target_link_libraries(sample PUBLIC libohfileio.so)

添加头文件

#include <cstdio>
#include <cstring>
#include <filemanagement/fileio/oh_fileio.h>

调用OH_FileIO_GetFileLocation接口获取文件存储位置。示例代码如下所示：

void GetFileLocationExample(char *uri)
{
    FileIO_FileLocation location;
    FileManagement_ErrCode ret = OH_FileIO_GetFileLocation(uri, strlen(uri), &location);
    if (ret == 0) {
        if (location == FileIO_FileLocation::LOCAL) {
            printf("Succeeded in getting file location, this file is on local.");
        } else if (location == FileIO_FileLocation::CLOUD) {
            printf("Succeeded in getting file location, this file is on cloud.");
        } else if (location == FileIO_FileLocation::LOCAL_AND_CLOUD) {
            printf("Succeeded in getting file location, this file is on  local and cloud.");
        }
    } else {
        printf("Failed to get file location, error code is %d", ret);
    }
}
napi_init.cpp
应用文件访问(ArkTS)
应用及文件系统空间统计
