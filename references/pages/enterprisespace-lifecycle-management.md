# 工作空间管理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-lifecycle-management_

从6.0.0(20)开始，支持应用开启双空间功能并创建、查询、删除工作空间的能力。

从26.0.0开始，支持查询设备是否开启双空间，以及工作空间是否为企业空间的能力。

场景介绍

Enterprise Space Kit为应用提供启用双空间功能及管理工作空间的能力。应用需要先使能工作空间，然后才能创建个人空间。同时，提供查询、移除工作空间的功能。

双空间分别为企业空间和个人空间，企业空间为完全受企业管控的通用办公空间，个人空间为因工作需要对外交流、作业、开源开发等用途的空间。

接口说明

详细接口说明可参考接口文档。

接口名	描述
enableWorkspace(enable: boolean): Promise<void>	使能或禁用工作空间功能。
createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>	创建工作空间并返回工作空间信息。
queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>	查询工作空间信息并返回结果。
removeWorkspace(localId: number): Promise<void>	移除工作空间。
isEnterpriseWorkspaceEnabled(): Promise<boolean>	查询设备是否开启双空间并返回结果。
isEnterpriseWorkspace(workspaceId?: number): Promise<boolean>	查询工作空间是否为企业空间并返回结果。

开发步骤

1.导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

2.使能工作空间，即打开双空间功能。

@Entry
@Component
struct Index {
  // 使能工作空间
  async enableWorkspace() {
    // 预置参数
    const enable: boolean = true;

    try {
      await spaceManager.enableWorkspace(enable);
      console.info(`Succeeded in enabling workspace.`);
    } catch (err) {
      console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('使能工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.removeWorkspace();
          })
      }
    }
  }
}

3.打开工作空间后，支持创建、查询和删除操作，也可查看设备双空间状态、识别企业空间属性。

@Entry
@Component
struct Index {
  // 创建工作空间
  async createWorkspace() {
    const localName: string = 'locaName'; // 空间名称
    const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
    const params: spaceManager.CreateWorkspaceParams = {
      shortName: 'test'
    };

    try {
      const workspaceInfo: spaceManager.WorkspaceInfo =
        await spaceManager.createWorkspace(localName, workspaceType, params);
      console.info(`Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
    } catch (err) {
      console.error(`Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询工作空间
  async queryWorkspace() {
    const queryType: spaceManager.QueryType = spaceManager.QueryType.ALL;
    try {
      const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryType);
      console.info(`Succeeded in querying workspace` + JSON.stringify(spaces));
    } catch (err) {
      console.error(`Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 移除工作空间
  async removeWorkspace() {
    const workspaceId: number = 101; // 已经创建的工作空间ID。
    try {
      await spaceManager.removeWorkspace(workspaceId);
      console.info(`Succeeded in removing workspace.`);
    } catch (err) {
      console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询设备是否开启双空间
  async isEnterpriseWorkspaceEnabled() {
    try {
      const status = await spaceManager.isEnterpriseWorkspaceEnabled();
      console.info(`Succeeded in getting enterprise workspace enabled. enabled: ${status}`);
      // 处理后置逻辑
    } catch (err) {
      console.error(`Failed to get enterprise workspace enabled. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 查询工作空间是否为企业空间
  async isEnterpriseWorkspace() {
    try {
      const isEnterprise = await spaceManager.isEnterpriseWorkspace();
      console.info(`Succeeded in getting enterprise workspace. isEnterprise: ${isEnterprise}`);
      // 处理后置逻辑
    } catch (err) {
      console.error(`Failed to get enterprise workspace. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('创建工作空间')
          .id('createWorkspace')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.createWorkspace();
          })
      }

      Row() {
        Button('查询工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.queryWorkspace();
          })
      }

      Row() {
        Button('移除工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.removeWorkspace();
          })
      }

      Row() {
        Button('查询设备是否开启双空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.isEnterpriseWorkspaceEnabled();
          })
      }

      Row() {
        Button('查询工作空间是否为企业空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.isEnterpriseWorkspace();
          })
      }
    }
  }
}

## Code blocks

### Code block 1

```
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
@Entry
@Component
struct Index {
  // 使能工作空间
  async enableWorkspace() {
    // 预置参数
    const enable: boolean = true;

    try {
      await spaceManager.enableWorkspace(enable);
      console.info(`Succeeded in enabling workspace.`);
    } catch (err) {
      console.error(`Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('使能工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.removeWorkspace();
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
  // 创建工作空间
  async createWorkspace() {
    const localName: string = 'locaName'; // 空间名称
    const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
    const params: spaceManager.CreateWorkspaceParams = {
      shortName: 'test'
    };

    try {
      const workspaceInfo: spaceManager.WorkspaceInfo =
        await spaceManager.createWorkspace(localName, workspaceType, params);
      console.info(`Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
    } catch (err) {
      console.error(`Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询工作空间
  async queryWorkspace() {
    const queryType: spaceManager.QueryType = spaceManager.QueryType.ALL;
    try {
      const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryType);
      console.info(`Succeeded in querying workspace` + JSON.stringify(spaces));
    } catch (err) {
      console.error(`Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 移除工作空间
  async removeWorkspace() {
    const workspaceId: number = 101; // 已经创建的工作空间ID。
    try {
      await spaceManager.removeWorkspace(workspaceId);
      console.info(`Succeeded in removing workspace.`);
    } catch (err) {
      console.error(`Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 查询设备是否开启双空间
  async isEnterpriseWorkspaceEnabled() {
    try {
      const status = await spaceManager.isEnterpriseWorkspaceEnabled();
      console.info(`Succeeded in getting enterprise workspace enabled. enabled: ${status}`);
      // 处理后置逻辑
    } catch (err) {
      console.error(`Failed to get enterprise workspace enabled. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 查询工作空间是否为企业空间
  async isEnterpriseWorkspace() {
    try {
      const isEnterprise = await spaceManager.isEnterpriseWorkspace();
      console.info(`Succeeded in getting enterprise workspace. isEnterprise: ${isEnterprise}`);
      // 处理后置逻辑
    } catch (err) {
      console.error(`Failed to get enterprise workspace. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('创建工作空间')
          .id('createWorkspace')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.createWorkspace();
          })
      }

      Row() {
        Button('查询工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.queryWorkspace();
          })
      }

      Row() {
        Button('移除工作空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.removeWorkspace();
          })
      }

      Row() {
        Button('查询设备是否开启双空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.isEnterpriseWorkspaceEnabled();
          })
      }

      Row() {
        Button('查询工作空间是否为企业空间')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.isEnterpriseWorkspace();
          })
      }
    }
  }
}
```
