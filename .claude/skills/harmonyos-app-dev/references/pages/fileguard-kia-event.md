# 订阅或取消订阅KIA文件拷贝、重命名和压缩事件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-event_

为应用提供监听或取消监听KIA文件拷贝、重命名和压缩事件的能力，当KIA文件发生变种时，通过回调函数，返回KIA变种信息。

接口说明

详细接口说明可参考接口文档。

接口名	描述
on(type: 'kiaCopy', callback: Callback<string>): void	订阅KIA拷贝事件，需在业务初始化时注册。当用户拷贝KIA文件时会触发回调。
off(type: 'kiaCopy', callback?: Callback<string>): void	取消订阅KIA拷贝事件。
on(type: 'kiaRename', callback: Callback<string>): void	订阅KIA重命名事件，需在业务初始化时注册。当用户重命名KIA文件时会触发回调。
off(type: 'kiaRename', callback?: Callback<string>): void	取消订阅KIA重命名事件。
on(type: 'kiaCompress', callback: Callback<string>): void	订阅KIA压缩事件，需在业务初始化时注册。当用户压缩KIA文件时会触发回调。
off(type: 'kiaCompress', callback?: Callback<string>): void	取消订阅KIA压缩事件。
开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';

初始化FileGuard对象guard，调用接口on或off，订阅或取消订阅KIA文件拷贝、重命名和压缩事件。

function onKiaCopyCallback(eventData: string) {
  console.info(`Succeeded in receiving kia copy eventData: ${eventData}.`);
}
function onKiaRenameCallback(eventData: string) {
  console.info(`Succeeded in receiving kia rename eventData: ${eventData}.`);
}
function onKiaCompressCallback(eventData: string) {
  console.info(`Succeeded in receiving kia compress eventData: ${eventData}.`);
}


function listenKIAEvent() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  try {
    guard.on('kiaCopy', onKiaCopyCallback);
    guard.on('kiaRename', onKiaRenameCallback);
    guard.on('kiaCompress', onKiaCompressCallback);
  } catch (e) {
    console.error(`Failed to monitor the kia event. Code: ${e.code}, message: ${e.message}.`);
  }
  try {
    guard.off('kiaCopy');
    guard.off('kiaRename');
    guard.off('kiaCompress');
  } catch (e) {
    console.error(`Failed to cancel monitoring the kia event. Code: ${e.code}, message: ${e.message}.`);
  }
}
设置KIA文件列表
设置KIA文件水印图片
