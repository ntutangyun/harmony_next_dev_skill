# 设置KIA文件列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-kia-file-list_

Enterprise Data Guard Kit为应用提供设置KIA文件列表的能力，HarmonyOS系统根据管控策略对KIA文件列表中的文件实行管控。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void	使用Callback方式设置KIA文件列表。
setKiaFilelist(filelist: string): Promise<void>	使用Promise方式设置KIA文件列表。
开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

初始化FileGuard对象guard，将KIA文件列表对象转为字符串，调用接口setKiaFilelist，设置KIA文件列表。

通过回调函数方式，设置KIA文件列表。

function setKiaFilelistCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let fileListStr: string =
    '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
      '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
      '"kia_keyword":["key1","key2","key3"],' +
      '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
      '"compress_suffix":[".rar", ".zip"],' +
      '"kia_update_type":0}';
  guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in setting the list of KIA file.`);
    }
  });
}

通过Promise方式，设置KIA文件列表。

function setKiaFilelistPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let fileListStr: string =
    '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
      '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
      '"kia_keyword":["key1","key2","key3"],' +
      '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
      '"compress_suffix":[".rar", ".zip"],' +
      '"kia_update_type":0}';
  guard.setKiaFilelist(fileListStr).then(() => {
    console.info(`Succeeded in setting the list of KIA file.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
  });
}
更新安全管控策略
订阅或取消订阅KIA文件拷贝、重命名和压缩事件
