# 删除文件到回收站

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-deletetotrash_

deleteToTrash(uri: string): Promise<string>	删除指定文件到回收站，并返回文件删除到回收站后的uri。使用Promise异步回调。
示例代码

1.导入文件管理服务模块及相关模块

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

2.删除指定文件到回收站

async function deleteFile() {
  // 以内置存储目录为例
  // 示例代码targetUri表示Download目录下文件
  // 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info("trashUri: " + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
File Manager Service Kit简介
获取文件图标
