# 打开文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-openfile_

普通应用无法直接访问公共路径下的文件，Enterprise Data Guard Kit为应用提供相关接口以获取文件描述符（fd）。

接口说明

详细接口说明可参考接口文档。

接口名	描述
openFile(path: string, callback: AsyncCallback<number>): void	通过Callback方式获取指定路径下文件的文件描述符（fd）。
openFile(path: string): Promise<number>	使用Promise方式获取指定路径下文件的文件描述符（fd）。
openFileWrite(path: string, callback: AsyncCallback<number>): void	在只写模式下，通过Callback方式获取指定路径下文件的文件描述符（fd）。
openFileWrite(path: string): Promise<number>	在只写模式下，使用Promise方式获取指定路径下文件的文件描述符（fd）。
开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

初始化FileGuard对象guard，调用接口openFile或者openFileWrite，并且可选择以下一种方式获取指定目录文件fd。

通过回调函数方式，获取文件fd。

function openFileCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test.txt';
  guard.openFile(path, (err: BusinessError, fd: number) => {
    if (err) {
      console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
  });
}

通过Promise方式，获取文件fd。

function openFilePromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test.txt';
  guard.openFile(path).then((fd: number) => {
    console.info(`Succeeded in opening file. path: ${path} , fd: ${fd}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
  });
}
启动文件扫描任务
设置文件属性标签
