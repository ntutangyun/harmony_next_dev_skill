# 启动文件扫描任务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-start-task_

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
文件分级管控
打开文件
