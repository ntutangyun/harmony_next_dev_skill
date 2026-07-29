# 删除指定路径下的文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-delete-file_

场景介绍

Enterprise Data Guard Kit为应用提供对用户个人数据目录下指定路径文件的删除能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
deleteFile(path: string, callback: AsyncCallback<void>): void	使用Callback方式删除指定路径下的文件。
deleteFile(path: string): Promise<void>	使用Promise方式删除指定路径下的文件。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口deleteFile，删除指定路径下的文件。

通过回调函数方式，删除指定路径下的文件。

const TAG: string = 'FileGuard_DeleteFile';
const DOMAIN: number = 0x0000;

/**
 * 删除指定路径下的文件。使用callback异步回调。
 * @param accountId: 用户ID
 */
function deleteFileCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ccc.txt`;
  guard.deleteFile(path, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
    }
  });
}

通过Promise方式，删除指定路径下的文件。

const TAG: string = 'FileGuard_DeleteFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除指定路径下的文件。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function deleteFilePromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ddd.txt`;
  guard.deleteFile(path).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
  });
}

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'FileGuard_DeleteFile';
const DOMAIN: number = 0x0000;

/**
 * 删除指定路径下的文件。使用callback异步回调。
 * @param accountId: 用户ID
 */
function deleteFileCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ccc.txt`;
  guard.deleteFile(path, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
    }
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_DeleteFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除指定路径下的文件。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function deleteFilePromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/ddd.txt`;
  guard.deleteFile(path).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in deleting file.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
