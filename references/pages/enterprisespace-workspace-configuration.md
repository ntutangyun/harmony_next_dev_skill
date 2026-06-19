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

1.导入Enterprise Space Kit模块和相关依赖模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

2.设置用户工作空间信息。

@Entry
@Component
struct Index {
  // 设置工作空间信息
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
    try {
      await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
      console.info(`Succeeded in setting workspace info.`);
    } catch (err) {
      console.error(`Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
        Row() {
        Button('设置工作空间信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceInfo();
          })
      }
    }
  }
}

3.设置工作空间资料照片。

@Entry
@Component
struct Index {
  // 设置工作空间资料照片
  async setWorkspaceProfilePhoto() {
    const workspaceId: number = 100;
    const photo: string =
      '{"type":0,"defaultImg":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAAAALSURBVAhbY2AAAgAABQABHh/sFAAAAABJRU5ErkJggg=="}';
    try {
      await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
      console.info(`Succeeded in setting workspace profile photo.`);
    } catch (err) {
      console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间资料照片')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceProfilePhoto();
          })
      }
    }
  }
}

4.设置工作空间本地名称。

@Entry
@Component
struct Index {
  // 设置工作空间本地名称
  async setWorkspaceLocalName() {
    const localName: string = 'localName';
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspaceLocalName(localName, workspaceId);
      console.info(`Succeeded in setting workspace local name.`);
    } catch (err) {
      console.error(`Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间本地名称')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceLocalName();
          })
      }
    }
  }
}

5.设置工作空间状态栏图标。

@Entry
@Component
struct Index {
  // 设置工作空间状态栏图标
  async setWorkspaceStatusBarIcon() {
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error(`getHostContext failed.`);
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
    try {
      await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
      console.info(`Succeeded in setting workspace status bar icon.`);
    } catch (err) {
      console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间状态栏图标')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceStatusBarIcon();
          })
      }
    }
  }
}

6.设置和查询工作空间策略。

@Entry
@Component
struct Index {
  // 设置工作空间策略。
  async setWorkspacePolicy() {
    const key: string = 'lockdown';
    const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspacePolicy(key, value, workspaceId);
      console.info(`Succeeded in setting workspace policy.`);
    } catch (err) {
      console.error(`Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询工作空间策略
  async getWorkspacePolicy() {
    const key: string = 'lockdown';
    const workspaceId: number = 100;
    try {
      const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
      console.info(`Succeeded in getting workspace policy. value: ${value}`);
    } catch (err) {
      console.error(`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

    build() {
    Column() {
      Row() {
        Button('设置工作空间策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspacePolicy();
          })
      }

      Row() {
        Button('查询工作空间策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getWorkspacePolicy();
          })
      }
    }
  }
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
```

### Code block 2

```
@Entry
@Component
struct Index {
  // 设置工作空间信息
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
    try {
      await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
      console.info(`Succeeded in setting workspace info.`);
    } catch (err) {
      console.error(`Failed to set workspace info. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
        Row() {
        Button('设置工作空间信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceInfo();
          })
      }
    }
  }
}
```

### Code block 3

```
@Entry
@Component
struct Index {
  // 设置工作空间资料照片
  async setWorkspaceProfilePhoto() {
    const workspaceId: number = 100;
    const photo: string =
      '{"type":0,"defaultImg":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAAAALSURBVAhbY2AAAgAABQABHh/sFAAAAABJRU5ErkJggg=="}';
    try {
      await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
      console.info(`Succeeded in setting workspace profile photo.`);
    } catch (err) {
      console.error(`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间资料照片')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceProfilePhoto();
          })
      }
    }
  }
}
```

### Code block 4

```
@Entry
@Component
struct Index {
  // 设置工作空间本地名称
  async setWorkspaceLocalName() {
    const localName: string = 'localName';
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspaceLocalName(localName, workspaceId);
      console.info(`Succeeded in setting workspace local name.`);
    } catch (err) {
      console.error(`Failed to set workspace local name. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间本地名称')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceLocalName();
          })
      }
    }
  }
}
```

### Code block 5

```
@Entry
@Component
struct Index {
  // 设置工作空间状态栏图标
  async setWorkspaceStatusBarIcon() {
    const context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error(`getHostContext failed.`);
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
    try {
      await spaceManager.setWorkspaceStatusBarIcon(icons, workspaceId);
      console.info(`Succeeded in setting workspace status bar icon.`);
    } catch (err) {
      console.error(`Failed to set workspace status bar icon. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
          Button('设置工作空间状态栏图标')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspaceStatusBarIcon();
          })
      }
    }
  }
}
```

### Code block 6

```
@Entry
@Component
struct Index {
  // 设置工作空间策略。
  async setWorkspacePolicy() {
    const key: string = 'lockdown';
    const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspacePolicy(key, value, workspaceId);
      console.info(`Succeeded in setting workspace policy.`);
    } catch (err) {
      console.error(`Failed to set workspace policy. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询工作空间策略
  async getWorkspacePolicy() {
    const key: string = 'lockdown';
    const workspaceId: number = 100;
    try {
      const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
      console.info(`Succeeded in getting workspace policy. value: ${value}`);
    } catch (err) {
      console.error(`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

    build() {
    Column() {
      Row() {
        Button('设置工作空间策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setWorkspacePolicy();
          })
      }

      Row() {
        Button('查询工作空间策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getWorkspacePolicy();
          })
      }
    }
  }
}
```
