# 获取文件URI

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-get-file-url_

场景介绍

Enterprise Data Guard Kit为应用提供获取用户个人数据目录下文件路径信息的能力，该路径可被应用直接打开，从而辅助判断是否是KIA文件。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void	使用Callback方式获取文件路径信息。
getFileUri(path: string): Promise<FilePathInfo>	使用Promise方式获取文件路径信息。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口getFileUri，获取文件URI。

通过回调函数方式，获取文件URI。

const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

/**
 * 获取文件URI。使用callback异步回调。
 * @param accountId: 用户ID
 */
function getFileUriCallBack(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
    }
  });
}

通过Promise方式，获取文件URI。

const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件URI。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function getFileUriPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/bbb.txt`;
  guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
    hilog.info(DOMAIN, TAG,
      `Succeeded in getting the uri of file. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.`);
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
const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

/**
 * 获取文件URI。使用callback异步回调。
 * @param accountId: 用户ID
 */
function getFileUriCallBack(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
    }
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_FileUri';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件URI。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function getFileUriPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/bbb.txt`;
  guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
    hilog.info(DOMAIN, TAG,
      `Succeeded in getting the uri of file. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the uri of file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
