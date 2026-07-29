# 工作空间配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-workspace-configuration_

从6.0.0(20)开始，支持自定义工作空间显示属性的能力。

场景介绍

Enterprise Space Kit为应用提供自定义工作空间显示属性的能力。企业可以设置工作空间的域信息、资料照片、本地名称和状态栏图标，以满足企业个性化定制需求。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setWorkspaceInfo(workspaceId: number, domainInfo: WorkspaceDomainInfo): Promise<void>	设置工作空间信息。
setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<void>	设置工作空间资料照片。
setWorkspaceLocalName(localName: string, workspaceId?: number): Promise<void>	设置工作空间本地名称。
setWorkspaceStatusBarIcon(icon: StatusBarIcon, workspaceId?: number): Promise<void>	设置工作空间状态栏图标。
setWorkspacePolicy(key: string, value: number, workspaceId?: number): Promise<void>	设置工作空间策略。
getWorkspacePolicy(key: string, workspaceId?: number): number	查询工作空间策略并返回结果。

开发步骤

1.导入工作空间配置API模块相关依赖。

import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ErrCode } from '../../common/ErrCode';

2.工作空间配置API接口封装。

const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class WorkspaceConfigurationApi {
  static async setWorkspacePolicy(workspaceId: number, key: string,
    value: spaceManager.LockdownModePolicy): Promise<number> {
    try {
      await spaceManager.setWorkspacePolicy(key, value, workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace policy.');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async getWorkspacePolicy(workspaceId: number, key: string): Promise<number | undefined> {
    try {
      const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in getting workspace policy. value: ${value}`);
      return value;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }

  static async setWorkspaceInfo(workspaceId: number, domainInfo: spaceManager.WorkspaceDomainInfo): Promise<number> {
    try {
      await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace info');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<number> {
    try {
      await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace profile photo');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceStatusBarIcon(workspaceId: number, icons: spaceManager.StatusBarIcon): Promise<number> {
    try {
      await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in setting workspace status bar icon`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceLocalName(workspaceId: number, localName: string): Promise<number> {
    try {
      await spaceManager.setWorkspaceLocalName(localName, workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace local name');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }
}

3.导入工作空间配置业务实现相关依赖。

import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { image } from '@kit.ImageKit';
import { util } from '@kit.ArkTS';
import { resourceManager } from '@kit.LocalizationKit';
import { ErrCode } from '../../common/ErrCode';
import { WorkspaceConfigurationApi } from '../api/WorkspaceConfigurationApi'
import { hilog } from '@kit.PerformanceAnalysisKit';

4.工作空间配置业务相关实现。

const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct WorkspaceConfigurationPage {
  async setWorkspacePolicy() {
    const key: string = 'lockdown';
    const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
    const workspaceId: number = 100;

    if (await WorkspaceConfigurationApi.setWorkspacePolicy(workspaceId, key, value) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace policy!');
      return;
    }
    // 处理后置逻辑
  }

  async getWorkspacePolicy() {
    const key: string = 'lockdown';
    const workspaceId: number = 100;
    const value: number | undefined = await WorkspaceConfigurationApi.getWorkspacePolicy(workspaceId, key);
    if (value === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to get workspace policy!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceLocalName() {
    const localName: string = 'localName';
    const workspaceId: number = 100;
    if (await WorkspaceConfigurationApi.setWorkspaceLocalName(workspaceId, localName) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace local name!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceStatusBarIcon() {
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      hilog.error(DOMAIN, TAG, 'get host context fail!');
      return;
    }
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

    // 创建white pixelMap，使用资源rawfile文件夹中预置HuaweiWhite.jpg图片
    let whiteFileData = await resourceMgr.getRawFd('HuaweiWhite.jpg');
    const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
    const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();

    // 创建black pixelMap，使用资源rawfile文件夹中预置HuaweiBlack.jpg图片
    let blackFileData = await resourceMgr.getRawFd('HuaweiBlack.jpg');
    const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
    const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();

    // 构建图标信息
    const icons: spaceManager.StatusBarIcon = {
      white: whitePixelMap,
      black: blackPixelMap
    };
    const workspaceId: number = 100;
    if (await WorkspaceConfigurationApi.setWorkspaceStatusBarIcon(workspaceId, icons) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace status bar icon!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceInfo() {
    const workspaceId: number = 100;
    const domainInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'test1',
      workspaceName: 'test2',
      accountId: 'test3',
      isAuthenticated: false,
      serverConfigId: 'test4',
      enterpriseWorkspaceName: 'default'
    };
    if (await WorkspaceConfigurationApi.setWorkspaceInfo(workspaceId, domainInfo) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace info!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceProfilePhoto() {
    const workspaceId: number = 100;
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      hilog.error(DOMAIN, TAG, 'get context fail!');
      return;
    }
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    const photoData = await resourceMgr.getRawFileContent('HuaweiWhite.jpg');
    const base64Helper = new util.Base64Helper();
    const base64Img: string = base64Helper.encodeToStringSync(photoData);
    const photo: string = JSON.stringify({ type: 0, defaultImg: `data:image/jpeg;base64,${base64Img}` });
    if (await WorkspaceConfigurationApi.setWorkspaceProfilePhoto(workspaceId, photo) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace profile photo!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setWorkspacePolicy'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspacePolicy();
          })
      }

      Row() {
        Button($r('app.string.getWorkspacePolicy'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getWorkspacePolicy();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceLocalName'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceLocalName();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceStatusBarIcon'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceStatusBarIcon();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceInfo'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceInfo();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceProfilePhoto'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceProfilePhoto();
          })
      }

      Row() {
        Button($r('app.string.back'))
          .buttonCommonStyle()
          .onClick(() => {
            router.back();
          })
      }
    }
  }
}

@Extend(Button)
function buttonCommonStyle() {
  .width(200)
  .height(50)
  .backgroundColor('#6366F1')
  .fontColor('#FFFFFF')
  .fontSize(14)
  .margin({ left: 20, bottom: 5 })
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { ErrCode } from '../../common/ErrCode';
```

### Code block 2

```
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class WorkspaceConfigurationApi {
  static async setWorkspacePolicy(workspaceId: number, key: string,
    value: spaceManager.LockdownModePolicy): Promise<number> {
    try {
      await spaceManager.setWorkspacePolicy(key, value, workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace policy.');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async getWorkspacePolicy(workspaceId: number, key: string): Promise<number | undefined> {
    try {
      const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in getting workspace policy. value: ${value}`);
      return value;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }

  static async setWorkspaceInfo(workspaceId: number, domainInfo: spaceManager.WorkspaceDomainInfo): Promise<number> {
    try {
      await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace info');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceProfilePhoto(workspaceId: number, photo: string): Promise<number> {
    try {
      await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace profile photo');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceStatusBarIcon(workspaceId: number, icons: spaceManager.StatusBarIcon): Promise<number> {
    try {
      await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in setting workspace status bar icon`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async setWorkspaceLocalName(workspaceId: number, localName: string): Promise<number> {
    try {
      await spaceManager.setWorkspaceLocalName(localName, workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in setting workspace local name');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }
}
```

### Code block 3

```
import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { image } from '@kit.ImageKit';
import { util } from '@kit.ArkTS';
import { resourceManager } from '@kit.LocalizationKit';
import { ErrCode } from '../../common/ErrCode';
import { WorkspaceConfigurationApi } from '../api/WorkspaceConfigurationApi'
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 4

```
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct WorkspaceConfigurationPage {
  async setWorkspacePolicy() {
    const key: string = 'lockdown';
    const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
    const workspaceId: number = 100;

    if (await WorkspaceConfigurationApi.setWorkspacePolicy(workspaceId, key, value) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace policy!');
      return;
    }
    // 处理后置逻辑
  }

  async getWorkspacePolicy() {
    const key: string = 'lockdown';
    const workspaceId: number = 100;
    const value: number | undefined = await WorkspaceConfigurationApi.getWorkspacePolicy(workspaceId, key);
    if (value === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to get workspace policy!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceLocalName() {
    const localName: string = 'localName';
    const workspaceId: number = 100;
    if (await WorkspaceConfigurationApi.setWorkspaceLocalName(workspaceId, localName) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace local name!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceStatusBarIcon() {
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      hilog.error(DOMAIN, TAG, 'get host context fail!');
      return;
    }
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

    // 创建white pixelMap，使用资源rawfile文件夹中预置HuaweiWhite.jpg图片
    let whiteFileData = await resourceMgr.getRawFd('HuaweiWhite.jpg');
    const whiteImageSource: image.ImageSource = image.createImageSource(whiteFileData);
    const whitePixelMap: image.PixelMap = await whiteImageSource.createPixelMap();

    // 创建black pixelMap，使用资源rawfile文件夹中预置HuaweiBlack.jpg图片
    let blackFileData = await resourceMgr.getRawFd('HuaweiBlack.jpg');
    const blackImageSource: image.ImageSource = image.createImageSource(blackFileData);
    const blackPixelMap: image.PixelMap = await blackImageSource.createPixelMap();

    // 构建图标信息
    const icons: spaceManager.StatusBarIcon = {
      white: whitePixelMap,
      black: blackPixelMap
    };
    const workspaceId: number = 100;
    if (await WorkspaceConfigurationApi.setWorkspaceStatusBarIcon(workspaceId, icons) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace status bar icon!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceInfo() {
    const workspaceId: number = 100;
    const domainInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'test1',
      workspaceName: 'test2',
      accountId: 'test3',
      isAuthenticated: false,
      serverConfigId: 'test4',
      enterpriseWorkspaceName: 'default'
    };
    if (await WorkspaceConfigurationApi.setWorkspaceInfo(workspaceId, domainInfo) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace info!');
      return;
    }
    // 处理后置逻辑
  }

  async setWorkspaceProfilePhoto() {
    const workspaceId: number = 100;
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      hilog.error(DOMAIN, TAG, 'get context fail!');
      return;
    }
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    const photoData = await resourceMgr.getRawFileContent('HuaweiWhite.jpg');
    const base64Helper = new util.Base64Helper();
    const base64Img: string = base64Helper.encodeToStringSync(photoData);
    const photo: string = JSON.stringify({ type: 0, defaultImg: `data:image/jpeg;base64,${base64Img}` });
    if (await WorkspaceConfigurationApi.setWorkspaceProfilePhoto(workspaceId, photo) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to set workspace profile photo!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setWorkspacePolicy'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspacePolicy();
          })
      }

      Row() {
        Button($r('app.string.getWorkspacePolicy'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getWorkspacePolicy();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceLocalName'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceLocalName();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceStatusBarIcon'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceStatusBarIcon();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceInfo'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceInfo();
          })
      }

      Row() {
        Button($r('app.string.setWorkspaceProfilePhoto'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setWorkspaceProfilePhoto();
          })
      }

      Row() {
        Button($r('app.string.back'))
          .buttonCommonStyle()
          .onClick(() => {
            router.back();
          })
      }
    }
  }
}

@Extend(Button)
function buttonCommonStyle() {
  .width(200)
  .height(50)
  .backgroundColor('#6366F1')
  .fontColor('#FFFFFF')
  .fontSize(14)
  .margin({ left: 20, bottom: 5 })
}
```
