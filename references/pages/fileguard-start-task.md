# 启动文件扫描任务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-start-task_

场景介绍

Enterprise Data Guard Kit为应用提供公共路径和指定目录的扫描能力，获取对应目录下的文件列表。

接口说明

详细接口说明可参考接口文档。

接口名	描述
startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void	通过Callback的方式，扫描公共目录并返回结果。
startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void	通过Callback的方式，扫描指定目录并返回结果。

开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';

初始化FileGuard对象guard，并且声明扫描结果回调函数。

按照文件类型扫描公共空间文件，查看打印结果。

function startFileScanTaskUnderCommonDir() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
    files.forEach((value: string, index: number) => {
      console.info(`Succeeded in getting file: ${value}.`);
    })
  };
  let onCompleteScanTask: (count: number) => void = (count: number) => {
    console.info(`Succeeded in getting count: ${count}.`);
  };
  let scanFileCallback: fileGuard.ScanFileCallback = {
    onReceiveFileList: onReceiveFileList,
    onTaskCompleted: onCompleteScanTask
  };
  guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
}

扫描公共空间指定路径下的文件，查看打印结果。

function startFileScanTaskUnderSpecifiedDir() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test';
  let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
    files.forEach((value: string, index: number) => {
      console.info(`Succeeded in getting file: ${value}.`);
    })
  };
  let onCompleteScanTask: (count: number) => void = (count: number) => {
    console.info(`Succeeded in getting count: ${count}.`);
  };
  let scanFileCallback: fileGuard.ScanFileCallback = {
    onReceiveFileList: onReceiveFileList,
    onTaskCompleted: onCompleteScanTask
  };
  guard.startFileScanTask(path, scanFileCallback);
}

## Code blocks

### Code block 1

```
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
```

### Code block 2

```
function startFileScanTaskUnderCommonDir() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
    files.forEach((value: string, index: number) => {
      console.info(`Succeeded in getting file: ${value}.`);
    })
  };
  let onCompleteScanTask: (count: number) => void = (count: number) => {
    console.info(`Succeeded in getting count: ${count}.`);
  };
  let scanFileCallback: fileGuard.ScanFileCallback = {
    onReceiveFileList: onReceiveFileList,
    onTaskCompleted: onCompleteScanTask
  };
  guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
}
```

### Code block 3

```
function startFileScanTaskUnderSpecifiedDir() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test';
  let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
    files.forEach((value: string, index: number) => {
      console.info(`Succeeded in getting file: ${value}.`);
    })
  };
  let onCompleteScanTask: (count: number) => void = (count: number) => {
    console.info(`Succeeded in getting count: ${count}.`);
  };
  let scanFileCallback: fileGuard.ScanFileCallback = {
    onReceiveFileList: onReceiveFileList,
    onTaskCompleted: onCompleteScanTask
  };
  guard.startFileScanTask(path, scanFileCallback);
}
```
