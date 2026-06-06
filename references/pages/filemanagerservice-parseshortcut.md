# 解析文件快捷方式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-parseshortcut_

parseShortcut(linkUri: string): Promise<string>	根据快捷方式文件的URI解析出对应原文件的URI，并返回。使用Promise异步回调。
示例代码

1.导入文件管理服务模块及相关模块。

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

2.根据指定快捷方式文件的URI解析出对应原文件的URI。

public static async getTargetUriByLinkUri() {
  // 示例代码linkUri表示快捷方式文件的URI，快捷方式文件的后缀为“.hlink”
  // 开发者应根据自己实际的URI进行开发，并确保对该文件有读写权限
  let linkUri: string = "file://docs/storage/Users/currentUser/Documents/1.jpg.hlink";
  try {
    let targetUri: string = await fileManagerService.parseShortcut(linkUri);
    console.info("targetUri is: " + targetUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("parse shortcut failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
获取文件图标
Game Controller Kit（游戏控制器服务）
