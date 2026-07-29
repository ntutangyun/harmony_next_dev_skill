# 设置文件属性标签

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-tags_

场景介绍

Enterprise Data Guard Kit为应用提供对文件设置属性标签的能力，方便应用对管控文件进行标识、分类。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void	使用Callback方式设置文件属性标签。
setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>	使用Promise方式设置文件属性标签。
setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void	使用Callback方式设置文件自定义属性标签。
setFileCustomTag(path: string, tagList: Array<string>): Promise<void>	使用Promise方式设置文件自定义属性标签。
unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void	使用Callback方式取消设置文件自定义属性标签。
unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>	使用Promise方式取消设置文件自定义属性标签。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口setFileTag，设置文件属性标签。

通过回调函数方式，设置文件属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

/**
 * 设置文件属性标签。使用callback异步回调。
 */
function setFileTagCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  let tag: string = 'test1';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
  });
}

通过Promise方式，设置文件属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件属性标签。使用Promise异步回调。
 */
function setFileTagPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  let tag: string = 'test2';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口setFileCustomTag，设置文件自定义属性标签。

通过回调函数方式，设置文件自定义属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件自定义属性标签。使用callback异步回调。
 * @param accountId: 用户ID
 */
function setFileCustomTagCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
    }
  });
}

通过Promise方式，设置文件自定义属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件自定义属性标签。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function setFileCustomTagPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.setFileCustomTag(path, tagList).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口unsetFileCustomTag，取消文件自定义属性标签。

通过回调函数方式，取消文件自定义属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消文件自定义属性标签。使用callback异步回调。
 * @param accountId: 用户ID
 */
function unsetFileCustomTagCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
    }
  });
}

通过Promise方式，取消文件自定义属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消文件自定义属性标签。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function unsetFileCustomTagPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.unsetFileCustomTag(path, tagList).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
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
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

/**
 * 设置文件属性标签。使用callback异步回调。
 */
function setFileTagCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  let tag: string = 'test1';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件属性标签。使用Promise异步回调。
 */
function setFileTagPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  let tag: string = 'test2';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting file tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 4

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件自定义属性标签。使用callback异步回调。
 * @param accountId: 用户ID
 */
function setFileCustomTagCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
    }
  });
}
```

### Code block 5

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置文件自定义属性标签。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function setFileCustomTagPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.setFileCustomTag(path, tagList).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting file custom tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 6

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消文件自定义属性标签。使用callback异步回调。
 * @param accountId: 用户ID
 */
function unsetFileCustomTagCallback(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test1.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
    } else {
      hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
    }
  });
}
```

### Code block 7

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消文件自定义属性标签。使用Promise异步回调。
 * @param accountId: 用户ID
 */
function unsetFileCustomTagPromise(accountId: number) {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = `/data/service/el2/${accountId}/hmdfs/account/files/Docs/Documents/test2.txt`;
  let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
  guard.unsetFileCustomTag(path, tagList).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in unsetting file custom tag.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
