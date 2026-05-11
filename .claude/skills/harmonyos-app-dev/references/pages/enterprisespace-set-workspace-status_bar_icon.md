# 设置工作空间状态栏图标

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-workspace-status_bar_icon_

setWorkspaceStatusBarIcon(statusBarIcon: StatusBarIcon, workspaceId?: number): Promise<void>	设置工作空间状态栏图标。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用setWorkspaceStatusBarIcon接口，设置工作空间状态栏图标，并且查看打印信息。

const context: Context = getContext();
if (!context) {
  console.error('getHostContext failed');
  return;
}
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;


// 创建white pixelMap，需在资源rawfile文件夹中预置HuaweiWhite.jpg图片
let whiteFileData = await resourceMgr.getRawFd('HuaweiWhite.jpg');
const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();


// 创建black pixelMap，需在资源rawfile文件夹中预置HuaweiBlack.jpg图片
let blackFileData = await resourceMgr.getRawFd('HuaweiBlack.jpg');
const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();


// 构建图标信息
const icons: spaceManager.StatusBarIcon = { // 设置的工作空间的状态栏图标。
    white: whitePixelMap,
    black: blackPixelMap
};
const workspaceId: number = 100; // 工作空间ID。
try {
  await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
  console.info(TAG, `Succeeded in setting workspace status bar icon`);
} catch (err) {
  console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
}
获取企业应用访问令牌
设置空间本地名称
