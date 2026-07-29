# 打开文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-openfile_

场景介绍

普通应用无法直接访问公共路径下的文件，Enterprise Data Guard Kit为应用提供相关接口以获取文件描述符（fd）。

接口说明

详细接口说明可参考接口文档。

接口名	描述
openFile(path: string, callback: AsyncCallback<number>): void	通过Callback方式打开指定路径下的文件，获取文件描述符（fd）。
openFile(path: string): Promise<number>	使用Promise方式打开指定路径下的文件，获取文件描述符（fd）。
openFileWrite(path: string, callback: AsyncCallback<number>): void	在只写模式下，通过Callback方式打开用户个人数据目录下的文件，获取文件描述符（fd）。
openFileWrite(path: string): Promise<number>	在只写模式下，使用Promise方式打开用户个人数据目录下的文件，获取文件描述符（fd）。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口openFile，并且可选择以下一种方式打开文件，获取指定目录文件fd。

通过回调函数方式，打开指定路径下的文件，获取文件fd。

const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

/**
 * 打开文件。使用callback异步回调。
 */
function openFileCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  guard.openFile(path, (err: BusinessError, fd: number) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
  });
}

通过Promise方式，打开指定路径下的文件，获取文件fd。

const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 打开文件。使用Promise异步回调。
 */
function openFilePromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  guard.openFile(path).then((fd: number) => {
    hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
  });
}

只写模式下，打开用户个人数据目录下的文件，获取文件描述符。初始化FileGuard对象guard，调用接口openFileWrite，并且可选择以下一种方式获取指定目录文件fd。

通过回调函数方式，打开用户个人数据目录下的文件，获取文件fd。

const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 只写模式打开文件。使用callback异步回调。
 * @param accountId: 用户ID
 */
function openFileWriteCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.openFileWrite(path, (err: BusinessError, fd: number) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
  });
}

通过Promise方式，打开用户个人数据目录下的文件，获取文件fd。

const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 只写模式打开文件。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function openFileWritePromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.openFileWrite(path).then((fd: number) => {
    hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
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
const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

/**
 * 打开文件。使用callback异步回调。
 */
function openFileCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  guard.openFile(path, (err: BusinessError, fd: number) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 打开文件。使用Promise异步回调。
 */
function openFilePromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  guard.openFile(path).then((fd: number) => {
    hilog.info(DOMAIN, TAG, `Succeeded in opening file. path: ${path}, fd: ${fd}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to open file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 4

```
const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 只写模式打开文件。使用callback异步回调。
 * @param accountId: 用户ID
 */
function openFileWriteCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.openFileWrite(path, (err: BusinessError, fd: number) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
  });
}
```

### Code block 5

```
const TAG: string = 'FileGuard_OpenFile';
const DOMAIN: number = 0x0000;

// ...
/**
 * 只写模式打开文件。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function openFileWritePromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/aaa.txt`;
  guard.openFileWrite(path).then((fd: number) => {
    hilog.info(DOMAIN, TAG, `Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
