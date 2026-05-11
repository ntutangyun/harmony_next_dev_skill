# 获取并使用公共目录

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-dir-permission_

目录环境能力接口（ohos.file.environment）提供获取公共目录路径的能力，支持三方应用在公共文件用户目录下进行文件访问操作。

约束限制

使用此方式，需确认设备具有以下系统能力：SystemCapability.FileManagement.File.Environment.FolderObtain，当前仅支持2in1设备。
if (!canIUse('SystemCapability.FileManagement.File.Environment.FolderObtain')) {
    console.error('this api is not supported on this device');
    return;
}
公共目录获取接口仅用于获取公共目录路径，不对公共目录访问权限进行校验。若需访问公共目录需申请对应的公共目录访问权限。三方应用需要访问公共目录时，需通过弹窗授权向用户申请授予 Download 目录权限、Documents 目录权限或 Desktop 目录权限，具体参考访问控制-向用户申请授权。
   "requestPermissions" : [
       "ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY",
       "ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY",
   ]
示例

获取公共目录路径。

import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
function getUserDirExample() {
  try {
    const downloadPath = Environment.getUserDownloadDir();
    console.info(`Succeeded in getting user download dir: ${downloadPath}`);
    const documentsPath = Environment.getUserDocumentDir();
    console.info(`Succeeded in getting user document dir: ${documentsPath}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to get user dir. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets

以Download目录为例，访问Download目录下的文件。

import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
function readUserDownloadDirExample(context: common.UIAbilityContext) {
  try {
    // 获取 Download 目录
    const downloadPath = Environment.getUserDownloadDir();
    console.info(`Succeeded in getting user download dir: ${downloadPath}`);
    const dirPath = context.filesDir;
    // 查看 Download 目录下的文件并拷贝到沙箱目录中
    let fileList: string[] = fileIo.listFileSync(downloadPath);
    fileList.forEach((file, index) => {
      console.info(`${downloadPath} ${index}: ${file}`);
      if (fileIo.statSync(`${downloadPath}/${file}`).isFile()) {
        fileIo.copyFileSync(`${downloadPath}/${file}`, `${dirPath}/${file}`);
      }
    });
    // 查看沙箱目录下对应的文件
    fileList = fileIo.listFileSync(dirPath);
    fileList.forEach((file, index) => {
      console.info(`Succeeded in listing file, ${dirPath} ${index}: ${file}`);
    });
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to read user download dir. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets

以Download目录为例，保存文件到Download目录。

import { BusinessError } from '@kit.BasicServicesKit';
import { Environment } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
function writeUserDownloadDirExample() {
  // 检查是否具有 READ_WRITE_DOWNLOAD_DIRECTORY 权限，无权限则需要向用户申请授予权限。
  try {
    // 获取 Download 目录
    const downloadPath = Environment.getUserDownloadDir();
    console.info(`Succeeded in getting user download dir: ${downloadPath}`);
    // 保存 temp.txt 到 Download 目录下
    const file = fileIo.openSync(`${downloadPath}/temp.txt`, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
    fileIo.writeSync(file.fd, 'write a message');
    fileIo.closeSync(file);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed to write user download dir. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets
通过 C/C++ 接口获取并使用公共目录

除了通过ArkTS访问公共目录的方式，也可通过C/C++接口进行目录访问，具体可以参考 oh_environment.h。

约束限制

使用此接口，需确认设备具有以下系统能力：SystemCapability.FileManagement.File.Environment.FolderObtain。
三方应用需要访问公共目录时，需通过弹窗授权向用户申请授予Download目录权限、Documents目录权限或Desktop目录权限，具体参考访问控制-向用户申请授权。
接口说明

接口的详细说明，请参考oh_environment.h。

接口名称	描述
FileManagement_ErrCode OH_Environment_GetUserDownloadDir (char **result)	获取用户Download目录沙箱路径。只支持2in1设备
FileManagement_ErrCode OH_Environment_GetUserDesktopDir (char **result)	获取用户Desktop目录沙箱路径。只支持2in1设备
FileManagement_ErrCode OH_Environment_GetUserDocumentDir (char **result)	获取用户Document目录沙箱路径。只支持2in1设备
开发步骤

在CMake脚本中链接动态库

CMakeLists.txt中添加以下lib。

target_link_libraries(sample PUBLIC libohenvironment.so libhilog_ndk.z.so)

添加头文件

#include <filemanagement/environment/oh_environment.h>
#include <filemanagement/fileio/oh_fileio.h>
#include <hilog/log.h>

调用OH_Environment_GetUserDownloadDir接口获取用户Download目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

#include <cstdlib>
void GetUserDownloadDirExample()
{
    char *downloadPath = nullptr;
    FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
    if (ret == 0) {
        OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, download path=%{public}s", downloadPath);
        free(downloadPath);
    } else {
        OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
    }
}
napi_init.cpp

调用OH_Environment_GetUserDownloadDir接口获取用户Download目录沙箱路径，并查看Download目录下的文件。示例代码如下所示：

#include <cstdlib>
#include <dirent.h>
void ScanUserDownloadDirPathExample()
{
    // 获取 download 路径
    char *downloadPath = nullptr;
    FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
    if (ret == 0) {
        OH_LOG_INFO(LOG_APP, "Succeeded in scanning user download directory, path=%{public}s", downloadPath);
    } else {
        OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
        return;
    }
    // 查看文件夹下的文件
    struct dirent **namelist = nullptr;
    int num = scandir(downloadPath, &namelist, nullptr, nullptr);
    if (num < 0) {
        free(downloadPath);
        OH_LOG_ERROR(LOG_APP, "Failed to scan directory");
        return;
    }


    for (int i = 0; i < num; i++) {
        OH_LOG_INFO(LOG_APP, "Succeeded in scanning directory, file name is %{public}s", namelist[i]->d_name);
    }
    free(downloadPath);
    for (int i = 0; i < num; i++) {
        free(namelist[i]);
    }
    free(namelist);
}
napi_init.cpp

调用OH_Environment_GetUserDownloadDir接口获取用户Download目录沙箱路径，并保存temp.txt到Download目录下。示例代码如下所示：

#include <fstream>
void WriteUserDownloadDirPathExample()
{
    // 获取 download 路径
    char *downloadPath = nullptr;
    FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
    if (ret == 0) {
        OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, path=%{public}s", downloadPath);
    } else {
        OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
        return;
    }
    // 保存文件到 download 目录下
    std::string filePath = std::string(downloadPath) + "/temp.txt";
    free(downloadPath);


    std::ofstream outfile;
    outfile.open(filePath.c_str());
    if (!outfile) {
        OH_LOG_ERROR(LOG_APP, "Failed to open file");
        return;
    }
    std::string msg = "Write a message";
    outfile.write(msg.c_str(), msg.size());
    outfile.close();
}
napi_init.cpp
授权持久化(C/C++)
分布式文件系统
