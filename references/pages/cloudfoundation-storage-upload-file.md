# 上传指定文件至云侧

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-upload-file_

开发者可以快速将本地设备上的文件上传至云侧，上传完后，可以前往AppGallery Connect的“云存储”页面，查看上传的文档内容。

说明

上传的单个文件大小不得超过1GB。

约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

前提条件

已初始化存储实例。

操作步骤

导入相关模块。

import { cloudStorage } from '@kit.CloudFoundationKit';
// ...
import { request } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { GlobalContext } from '../common/GlobalContext';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

上传文件。

选择待上传的文件，下方示例代码中使用photoAccessHelper.PhotoViewPicker指定需要上传的文件。

将待上传的文件复制到context.cacheDir目录下。

说明

由于StorageBucket.uploadFile接口传入参数localPath只能设置为context.cacheDir目录下的文件路径，所以上传前需要先将文件复制到context.cacheDir目录下。

调用StorageBucket.uploadFile接口创建上传任务，监听上传任务的progress、completed、failed等事件。

启动上传任务。

完整的示例代码如下：

hilog.info(0x0000, 'Storage', `upload file with api`);
let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.maxSelectNumber = 1;
let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
  let fileUri = photoSelectResult.photoUris[0];
  hilog.info(0x0000, 'Storage', `pick file ${fileUri}`);
  let fileName = fileUri.split('/').pop() as string;
  UI.uploadFileName = fileName;
  hilog.info(0x0000, 'Storage', `file name ${fileName}`);
  let cacheFile = `${Date.now()}_${fileName}`;
  hilog.info(0x0000, 'Storage', `cacheFile ${cacheFile}`);
  let cacheFilePath = GlobalContext.getContext().cacheDir + '/' + cacheFile;

  try {
    let srcFile = fileIo.openSync(fileUri);
    let dstFile = fileIo.openSync(cacheFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    fileIo.copyFileSync(srcFile.fd, dstFile.fd);
    fileIo.closeSync(srcFile);
    fileIo.closeSync(dstFile);

    cloudStorage.bucket().uploadFile(GlobalContext.getContext(), {
      localPath: cacheFile,
      cloudPath: UI.uploadFileName,
      mode: request.agent.Mode.BACKGROUND
    })
      .then((task: request.agent.Task) => {
        task.on('progress', (progress) => {
          hilog.info(0x0000, 'Storage', `on progress ${JSON.stringify(progress)}`);
        });
        task.on('completed', (progress) => {
          hilog.info(0x0000, 'Storage', `on completed ${JSON.stringify(progress)}`);
          fileIo.unlink(cacheFilePath).catch((err: BusinessError) => {
            hilog.error(0x0000, 'Storage', `Failed to unlink file, code: ${err.code}, message: ${err.message}`);
          });
          hilog.info(0x0000, 'Storage', `delete cache file ${cacheFilePath}`);
        });
        task.on('failed', (progress) => {
          hilog.info(0x0000, 'Storage', `on failed ${JSON.stringify(progress)}`);
          fileIo.unlink(cacheFilePath).catch((err: BusinessError) => {
            hilog.error(0x0000, 'Storage', `Failed to unlink file, code: ${err.code}, message: ${err.message}`);
          });
          hilog.info(0x0000, 'Storage', `delete cache file ${cacheFilePath}`);
        });
        task.start((err: BusinessError) => {
          if (err) {
            hilog.error(0x0000, 'Storage',
              `Failed to start the uploadFileWithTask task, code: ${err.code}, message: ${err.message}`);
          } else {
            hilog.info(0x0000, 'Storage', `Succeeded in starting a uploadFileWithTask task.`);
          }
        });
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0000, 'Storage', `Failed to upLoadFile:  code: ${error.code}, message: ${error.message}`);
      });
  } catch (e) {
    hilog.info(0x0000, 'Storage', `uploadFile failed ${e.message}`);
  }
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to pick photo view, code: ${err.code}, message: ${err.message}`);
})

说明

上传完成，可以登录AppGallery Connect，选择项目，进入“云存储”界面查看文件列表。

## Code blocks

### Code block 1

```
import { cloudStorage } from '@kit.CloudFoundationKit';
// ...
import { request } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { GlobalContext } from '../common/GlobalContext';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

### Code block 2

```
hilog.info(0x0000, 'Storage', `upload file with api`);
let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.maxSelectNumber = 1;
let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
photoViewPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
  let fileUri = photoSelectResult.photoUris[0];
  hilog.info(0x0000, 'Storage', `pick file ${fileUri}`);
  let fileName = fileUri.split('/').pop() as string;
  UI.uploadFileName = fileName;
  hilog.info(0x0000, 'Storage', `file name ${fileName}`);
  let cacheFile = `${Date.now()}_${fileName}`;
  hilog.info(0x0000, 'Storage', `cacheFile ${cacheFile}`);
  let cacheFilePath = GlobalContext.getContext().cacheDir + '/' + cacheFile;

  try {
    let srcFile = fileIo.openSync(fileUri);
    let dstFile = fileIo.openSync(cacheFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    fileIo.copyFileSync(srcFile.fd, dstFile.fd);
    fileIo.closeSync(srcFile);
    fileIo.closeSync(dstFile);

    cloudStorage.bucket().uploadFile(GlobalContext.getContext(), {
      localPath: cacheFile,
      cloudPath: UI.uploadFileName,
      mode: request.agent.Mode.BACKGROUND
    })
      .then((task: request.agent.Task) => {
        task.on('progress', (progress) => {
          hilog.info(0x0000, 'Storage', `on progress ${JSON.stringify(progress)}`);
        });
        task.on('completed', (progress) => {
          hilog.info(0x0000, 'Storage', `on completed ${JSON.stringify(progress)}`);
          fileIo.unlink(cacheFilePath).catch((err: BusinessError) => {
            hilog.error(0x0000, 'Storage', `Failed to unlink file, code: ${err.code}, message: ${err.message}`);
          });
          hilog.info(0x0000, 'Storage', `delete cache file ${cacheFilePath}`);
        });
        task.on('failed', (progress) => {
          hilog.info(0x0000, 'Storage', `on failed ${JSON.stringify(progress)}`);
          fileIo.unlink(cacheFilePath).catch((err: BusinessError) => {
            hilog.error(0x0000, 'Storage', `Failed to unlink file, code: ${err.code}, message: ${err.message}`);
          });
          hilog.info(0x0000, 'Storage', `delete cache file ${cacheFilePath}`);
        });
        task.start((err: BusinessError) => {
          if (err) {
            hilog.error(0x0000, 'Storage',
              `Failed to start the uploadFileWithTask task, code: ${err.code}, message: ${err.message}`);
          } else {
            hilog.info(0x0000, 'Storage', `Succeeded in starting a uploadFileWithTask task.`);
          }
        });
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0000, 'Storage', `Failed to upLoadFile:  code: ${error.code}, message: ${error.message}`);
      });
  } catch (e) {
    hilog.info(0x0000, 'Storage', `uploadFile failed ${e.message}`);
  }
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'Storage', `Failed to pick photo view, code: ${err.code}, message: ${err.message}`);
})
```
