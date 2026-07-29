# 获取文件属性标签

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-query-tags_

场景介绍

Enterprise Data Guard Kit为应用提供获取文件属性标签的能力，HarmonyOS系统根据管控策略和文件属性标签对文件实行管控。

接口说明

详细接口说明可参考接口文档。

接口名	描述
queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void	使用Callback方式获取文件属性标签。
queryFileTag(path: string): Promise<FileTagInfo>	使用Promise方式获取文件属性标签。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口queryFileTag，获取文件属性标签。

通过回调函数方式，获取文件属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件属性标签。使用callback异步回调。
 */
function queryFileTagCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG,
      `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
  });
}

通过Promise方式，获取文件属性标签。

const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件属性标签。使用Promise异步回调。
 */
function queryFileTagPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
    hilog.info(DOMAIN, TAG,
      `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
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

// ...
/**
 * 获取文件属性标签。使用callback异步回调。
 */
function queryFileTagCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test1.txt';
  guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
    if (err) {
      hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    hilog.info(DOMAIN, TAG,
      `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_FileTag';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取文件属性标签。使用Promise异步回调。
 */
function queryFileTagPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test2.txt';
  guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
    hilog.info(DOMAIN, TAG,
      `Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
