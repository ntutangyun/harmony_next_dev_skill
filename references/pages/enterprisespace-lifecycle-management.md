# 工作空间管理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-lifecycle-management_

从6.0.0(20)开始，支持应用开启双空间功能并创建、查询、删除工作空间的能力。

从26.0.0开始，支持查询设备双空间状态、判断工作空间是否为企业空间，以及切换工作空间。

场景介绍

Enterprise Space Kit为应用提供启用双空间功能及管理工作空间的能力。应用需要先使能工作空间，然后才能创建个人空间。同时，提供查询、移除工作空间的功能。

双空间分别为企业空间和个人空间，企业空间为完全受企业管控的通用办公空间，个人空间为因工作需要对外交流、作业、开源开发等用途的空间。

接口说明

详细接口说明可参考接口文档。

接口名	描述
enableWorkspace(enable: boolean): Promise<void>	启用或禁用工作空间功能。MDM应用调用该接口后，还需调用MDM Kit的restrictions.setDisallowedPolicy接口，启用INACTIVE_USER_FREEZE设备特性，以开启非活跃用户运行能力。
createWorkspace(localName: string, workspaceType: WorkspaceType, params?: CreateWorkspaceParams): Promise<WorkspaceInfo>	创建工作空间并返回工作空间信息。
queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>	查询工作空间信息并返回结果。
removeWorkspace(localId: number): Promise<void>	移除工作空间。
isEnterpriseWorkspaceEnabled(): Promise<boolean>	查询设备是否开启双空间并返回结果。
isEnterpriseWorkspace(workspaceId?: number): Promise<boolean>	查询工作空间是否为企业空间并返回结果。
switchWorkspace(workspaceId?: number): Promise<void>	切换工作空间。

开发步骤

1.导入工作空间管理API模块相关依赖。

import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.工作空间管理API接口封装。

const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class SpaceLifeCircleManagerApi {
  static async createWorkspace(localName: string, workspaceType: spaceManager.WorkspaceType,
    params: spaceManager.CreateWorkspaceParams): Promise<spaceManager.WorkspaceInfo | undefined> {
    try {
      const workspaceInfo: spaceManager.WorkspaceInfo =
        await spaceManager.createWorkspace(localName, workspaceType, params);
      hilog.info(DOMAIN, TAG,
        `Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
      return workspaceInfo;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }

  static async enableWorkspace(enable: boolean): Promise<number> {
    try {
      await spaceManager.enableWorkspace(enable);
      hilog.info(DOMAIN, TAG, 'Succeeded in enabling workspace');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async queryWorkspace(queryType: spaceManager.QueryType): Promise<spaceManager.WorkspaceInfo[]> {
    try {
      const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryType);
      hilog.info(DOMAIN, TAG, `Succeeded in querying workspace`);
      return spaces;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
      return [];
    }
  }

  static async removeWorkspace(workspaceId: number): Promise<number> {
    try {
      await spaceManager.removeWorkspace(workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in removing workspace');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async isEnterpriseWorkspaceEnabled(): Promise<boolean> {
    try {
      const status = await spaceManager.isEnterpriseWorkspaceEnabled();
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise workspace enabled. enabled: ${status}`);
      return status;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to get enterprise workspace enabled. Code: ${err.code}, message: ${err.message}`);
      return false;
    }
  }

  static async isEnterpriseWorkspace(): Promise<boolean> {
    try {
      const isEnterpriseWorkspace = await spaceManager.isEnterpriseWorkspace();
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise workspace. isEnterprise: ${isEnterpriseWorkspace}`);
      return isEnterpriseWorkspace;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get enterprise workspace. Code: ${err.code}, message: ${err.message}`);
      return false;
    }
  }

  static async switchWorkspace(workspaceId: number): Promise<number> {
    try {
      await spaceManager.switchWorkspace(workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in switching enterprise workspace. workspaceId: ${workspaceId}`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to switch enterprise workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }
}

3.导入工作空间管理业务实现相关依赖。

import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { SpaceLifeCircleManagerApi } from '../api/SpaceLifeCircleManagerApi';
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';

4.工作空间管理业务相关实现。

const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct SpaceLifeCircleManagerPage {
  async enableWorkspace() {
    // 预置参数
    const enable: boolean = true;

    if (await SpaceLifeCircleManagerApi.enableWorkspace(enable) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to enable workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async createWorkspace() {
    // 预置参数
    const localName: string = 'localName'; // 空间名称
    const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
    const params: spaceManager.CreateWorkspaceParams = {
      shortName: 'test'
    };

    const workspaceInfo: spaceManager.WorkspaceInfo | undefined = await
    SpaceLifeCircleManagerApi.createWorkspace(localName, workspaceType, params);
    if (workspaceInfo === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to create workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async queryWorkspace() {
    const queryType: spaceManager.QueryType = spaceManager.QueryType.ALL;
    let spaceInfo = await SpaceLifeCircleManagerApi.queryWorkspace(queryType)
    // 处理后置逻辑
  }

  async removeWorkspace() {
    const workspaceId: number = 101;
    if (await SpaceLifeCircleManagerApi.removeWorkspace(workspaceId) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to remove workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async isEnterpriseWorkspaceEnabled() {
    const status = await SpaceLifeCircleManagerApi.isEnterpriseWorkspaceEnabled();
    // 处理后置逻辑
  }

  async isEnterpriseWorkspace() {
    const isEnterpriseWorkspace = await SpaceLifeCircleManagerApi.isEnterpriseWorkspace();
    // 处理后置逻辑
  }

  async switchWorkspace() {
    const workspaceId: number = 101; // 已经创建的工作空间ID
    if (await SpaceLifeCircleManagerApi.switchWorkspace(workspaceId) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to switch workspace!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.enableWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.enableWorkspace();
          })
      }

      Row() {
        Button($r('app.string.createWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.createWorkspace();
          })
      }

      Row() {
        Button($r('app.string.queryWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.queryWorkspace();
          })
      }

      Row() {
        Button($r('app.string.removeWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.removeWorkspace();
          })
      }

      Row() {
        Button($r('app.string.isEnterpriseWorkspaceEnabled'))
          .buttonCommonStyle()
          .onClick(() => {
            this.isEnterpriseWorkspaceEnabled();
          })
      }

      Row() {
        Button($r('app.string.isEnterpriseWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.isEnterpriseWorkspace();
          })
      }

      Row() {
        Button($r('app.string.switchWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.switchWorkspace();
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
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class SpaceLifeCircleManagerApi {
  static async createWorkspace(localName: string, workspaceType: spaceManager.WorkspaceType,
    params: spaceManager.CreateWorkspaceParams): Promise<spaceManager.WorkspaceInfo | undefined> {
    try {
      const workspaceInfo: spaceManager.WorkspaceInfo =
        await spaceManager.createWorkspace(localName, workspaceType, params);
      hilog.info(DOMAIN, TAG,
        `Succeeded in creating workspace, workspaceInfo:` + JSON.stringify(workspaceInfo));
      return workspaceInfo;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to create workspace. Code: ${err.code}, message: ${err.message}`);
      return undefined;
    }
  }

  static async enableWorkspace(enable: boolean): Promise<number> {
    try {
      await spaceManager.enableWorkspace(enable);
      hilog.info(DOMAIN, TAG, 'Succeeded in enabling workspace');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to enable workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async queryWorkspace(queryType: spaceManager.QueryType): Promise<spaceManager.WorkspaceInfo[]> {
    try {
      const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryType);
      hilog.info(DOMAIN, TAG, `Succeeded in querying workspace`);
      return spaces;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
      return [];
    }
  }

  static async removeWorkspace(workspaceId: number): Promise<number> {
    try {
      await spaceManager.removeWorkspace(workspaceId);
      hilog.info(DOMAIN, TAG, 'Succeeded in removing workspace');
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to remove workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }

  static async isEnterpriseWorkspaceEnabled(): Promise<boolean> {
    try {
      const status = await spaceManager.isEnterpriseWorkspaceEnabled();
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise workspace enabled. enabled: ${status}`);
      return status;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `Failed to get enterprise workspace enabled. Code: ${err.code}, message: ${err.message}`);
      return false;
    }
  }

  static async isEnterpriseWorkspace(): Promise<boolean> {
    try {
      const isEnterpriseWorkspace = await spaceManager.isEnterpriseWorkspace();
      hilog.info(DOMAIN, TAG, `Succeeded in getting enterprise workspace. isEnterprise: ${isEnterpriseWorkspace}`);
      return isEnterpriseWorkspace;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get enterprise workspace. Code: ${err.code}, message: ${err.message}`);
      return false;
    }
  }

  static async switchWorkspace(workspaceId: number): Promise<number> {
    try {
      await spaceManager.switchWorkspace(workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in switching enterprise workspace. workspaceId: ${workspaceId}`);
      return ErrCode.OK;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to switch enterprise workspace. Code: ${err.code}, message: ${err.message}`);
      return ErrCode.ERR;
    }
  }
}
```

### Code block 3

```
import { router } from '@kit.ArkUI';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { SpaceLifeCircleManagerApi } from '../api/SpaceLifeCircleManagerApi';
import { ErrCode } from '../../common/ErrCode';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 4

```
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

@Entry
@Component
struct SpaceLifeCircleManagerPage {
  async enableWorkspace() {
    // 预置参数
    const enable: boolean = true;

    if (await SpaceLifeCircleManagerApi.enableWorkspace(enable) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to enable workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async createWorkspace() {
    // 预置参数
    const localName: string = 'localName'; // 空间名称
    const workspaceType: spaceManager.WorkspaceType = spaceManager.WorkspaceType.ADMIN;
    const params: spaceManager.CreateWorkspaceParams = {
      shortName: 'test'
    };

    const workspaceInfo: spaceManager.WorkspaceInfo | undefined = await
    SpaceLifeCircleManagerApi.createWorkspace(localName, workspaceType, params);
    if (workspaceInfo === undefined) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to create workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async queryWorkspace() {
    const queryType: spaceManager.QueryType = spaceManager.QueryType.ALL;
    let spaceInfo = await SpaceLifeCircleManagerApi.queryWorkspace(queryType)
    // 处理后置逻辑
  }

  async removeWorkspace() {
    const workspaceId: number = 101;
    if (await SpaceLifeCircleManagerApi.removeWorkspace(workspaceId) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to remove workspace!');
      return;
    }
    // 处理后置逻辑
  }

  async isEnterpriseWorkspaceEnabled() {
    const status = await SpaceLifeCircleManagerApi.isEnterpriseWorkspaceEnabled();
    // 处理后置逻辑
  }

  async isEnterpriseWorkspace() {
    const isEnterpriseWorkspace = await SpaceLifeCircleManagerApi.isEnterpriseWorkspace();
    // 处理后置逻辑
  }

  async switchWorkspace() {
    const workspaceId: number = 101; // 已经创建的工作空间ID
    if (await SpaceLifeCircleManagerApi.switchWorkspace(workspaceId) !== ErrCode.OK) {
      // 异常处理
      hilog.error(DOMAIN, TAG, 'Failed to switch workspace!');
      return;
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.enableWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.enableWorkspace();
          })
      }

      Row() {
        Button($r('app.string.createWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.createWorkspace();
          })
      }

      Row() {
        Button($r('app.string.queryWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.queryWorkspace();
          })
      }

      Row() {
        Button($r('app.string.removeWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.removeWorkspace();
          })
      }

      Row() {
        Button($r('app.string.isEnterpriseWorkspaceEnabled'))
          .buttonCommonStyle()
          .onClick(() => {
            this.isEnterpriseWorkspaceEnabled();
          })
      }

      Row() {
        Button($r('app.string.isEnterpriseWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.isEnterpriseWorkspace();
          })
      }

      Row() {
        Button($r('app.string.switchWorkspace'))
          .buttonCommonStyle()
          .onClick(() => {
            this.switchWorkspace();
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
