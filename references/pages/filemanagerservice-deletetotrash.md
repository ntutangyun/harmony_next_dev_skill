# 删除文件到回收站

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-deletetotrash_

场景介绍

删除公共目录的文件到回收站。

接口说明

接口名	描述
deleteToTrash(uri: string): Promise<string>	删除指定文件到回收站，并返回文件删除到回收站后的uri。使用Promise异步回调。

示例代码

1.导入文件管理服务模块及相关模块。

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

2.删除指定文件到回收站。

private async deleteFile(targetUri: string) {
// 以内置存储目录的Download目录下的文件为例，targetUri可以输入为："file://docs/storage/Users/currentUser/Download/1.txt"
// 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info('trashUri: ' + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error('delete failed, errCode:' + error.code + ', errMessage:' + error.message);
  }
}

## Code blocks

### Code block 1

```
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
private async deleteFile(targetUri: string) {
// 以内置存储目录的Download目录下的文件为例，targetUri可以输入为："file://docs/storage/Users/currentUser/Download/1.txt"
// 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info('trashUri: ' + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error('delete failed, errCode:' + error.code + ', errMessage:' + error.message);
  }
}
```
