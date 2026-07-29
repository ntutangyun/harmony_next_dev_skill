# 订阅或取消订阅KIA文件拷贝、重命名和压缩事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-event_

场景介绍

为应用提供监听或取消监听KIA文件拷贝、重命名和压缩事件的能力，当KIA文件发生拷贝、重命名或压缩时，通过回调函数，返回KIA事件信息。

接口说明

详细接口说明可参考接口文档。

接口名	描述
on(type: 'kiaCopy', callback: Callback<string>): void	订阅KIA文件拷贝事件，需在业务初始化时注册。当用户拷贝KIA文件时会触发回调。
off(type: 'kiaCopy', callback?: Callback<string>): void	取消订阅KIA文件拷贝事件。
on(type: 'kiaRename', callback: Callback<string>): void	订阅KIA文件重命名事件，需在业务初始化时注册。当用户重命名KIA文件时会触发回调。
off(type: 'kiaRename', callback?: Callback<string>): void	取消订阅KIA文件重命名事件。
on(type: 'kiaCompress', callback: Callback<string>): void	订阅KIA文件压缩事件，需在业务初始化时注册。当用户压缩KIA文件时会触发回调。
off(type: 'kiaCompress', callback?: Callback<string>): void	取消订阅KIA文件压缩事件。

开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口on，订阅KIA文件拷贝、重命名和压缩事件。

const TAG: string = 'FileGuard_KIAVariantEvent';
const DOMAIN: number = 0x0000;

/**
 * KIA文件拷贝回调事件
 */
function onKiaCopyCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia copy eventData: ${eventData}.`);
}

/**
 * KIA文件重命名回调事件
 */
function onKiaRenameCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia rename eventData: ${eventData}.`);
}

/**
 * KIA文件压缩回调事件
 */
function onKiaCompressCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia compress eventData: ${eventData}.`);
}

/**
 * 订阅KIA文件拷贝、重命名和压缩事件
 */
function listenKIAEvent() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  try {
    guard.on('kiaCopy', onKiaCopyCallback);
    guard.on('kiaRename', onKiaRenameCallback);
    guard.on('kiaCompress', onKiaCompressCallback);
    hilog.info(DOMAIN, TAG, `Succeeded in monitoring the KIA event.`);
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to monitor the KIA event. Code: ${e.code}, message: ${e.message}.`);
  }
}

初始化FileGuard对象guard，调用接口off，取消订阅KIA文件拷贝、重命名和压缩事件。

const TAG: string = 'FileGuard_KIAVariantEvent';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消订阅KIA文件拷贝、重命名和压缩事件
 */
function unListenKIAEvent() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  try {
    guard.off('kiaCopy');
    guard.off('kiaRename');
    guard.off('kiaCompress');
    hilog.info(DOMAIN, TAG, `Succeeded in cancelling monitoring the KIA event.`);
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to cancel monitoring the KIA event. Code: ${e.code}, message: ${e.message}.`);
  }
}

## Code blocks

### Code block 1

```
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'FileGuard_KIAVariantEvent';
const DOMAIN: number = 0x0000;

/**
 * KIA文件拷贝回调事件
 */
function onKiaCopyCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia copy eventData: ${eventData}.`);
}

/**
 * KIA文件重命名回调事件
 */
function onKiaRenameCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia rename eventData: ${eventData}.`);
}

/**
 * KIA文件压缩回调事件
 */
function onKiaCompressCallback(eventData: string) {
  hilog.info(DOMAIN, TAG, `Succeeded in receiving kia compress eventData: ${eventData}.`);
}

/**
 * 订阅KIA文件拷贝、重命名和压缩事件
 */
function listenKIAEvent() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  try {
    guard.on('kiaCopy', onKiaCopyCallback);
    guard.on('kiaRename', onKiaRenameCallback);
    guard.on('kiaCompress', onKiaCompressCallback);
    hilog.info(DOMAIN, TAG, `Succeeded in monitoring the KIA event.`);
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to monitor the KIA event. Code: ${e.code}, message: ${e.message}.`);
  }
}
```

### Code block 3

```
const TAG: string = 'FileGuard_KIAVariantEvent';
const DOMAIN: number = 0x0000;

// ...
/**
 * 取消订阅KIA文件拷贝、重命名和压缩事件
 */
function unListenKIAEvent() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  try {
    guard.off('kiaCopy');
    guard.off('kiaRename');
    guard.off('kiaCompress');
    hilog.info(DOMAIN, TAG, `Succeeded in cancelling monitoring the KIA event.`);
  } catch (e) {
    hilog.error(DOMAIN, TAG, `Failed to cancel monitoring the KIA event. Code: ${e.code}, message: ${e.message}.`);
  }
}
```
