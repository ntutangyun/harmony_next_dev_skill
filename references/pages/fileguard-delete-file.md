# 删除指定路径下的文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-delete-file_

deleteFile(path: string, callback: AsyncCallback<void>): void	使用Callback方式删除指定路径下的文件。
deleteFile(path: string): Promise<void>	使用Promise方式删除指定路径下的文件。
开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

初始化FileGuard对象guard，调用接口deleteFile，删除扫描范围内的文件。

通过回调函数方式，删除扫描范围内的文件。

function deleteFileCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
  guard.deleteFile(path, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in deleting file.`);
    }
  });
}

通过Promise方式，删除扫描范围内的文件。

function deleteFilePromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
  guard.deleteFile(path).then(() => {
    console.info(`Succeeded in deleting file.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
  });
}
获取文件URI
更新安全管控策略
