# 深度冻结策略

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-lockdown-exemptionapps_

从6.0.2(22)开始，支持设置和查询深度冻结豁免名单的能力。

场景介绍

Enterprise Space Kit为企业应用提供设备在深度冻结模式下的应用豁免管理能力，支持设置豁免应用，使其在后台正常运行。同时，支持查询深度冻结豁免的应用名单。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setLockdownExemptionApps(appIds: string[], workspaceId?: number): Promise<void>	设置深度冻结豁免名单。
getLockdownExemptionApps(workspaceId?: number): Promise<string[]>	查询深度冻结豁免名单。

开发步骤

1.导入深度冻结策略API模块相关依赖。

import { spaceManager } from '@kit.EnterpriseSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.深度冻结策略API接口封装。

const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class LockDownExemptionApi {
  static async setLockdownExemptionApps(workspaceId: number, appIds: string[]): Promise<void> {
    try {
      await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in setting lockdown exemption apps.`);
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set lockdown exemption apps. Code: ${err?.code}, message: ${err?.message}`);
    }
  }

  static async getLockdownExemptionApps(workspaceId: number): Promise<string[]> {
    try {
      const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
      return apps;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
      return [];
    }
  }
}

3.导入深度冻结策略业务实现相关依赖。

import { router } from '@kit.ArkUI';
import { LockDownExemptionApi } from '../api/LockDownExemptionApi'

4.深度冻结策略业务相关实现。

@Entry
@Component
struct LockDownExemptionPage {
  async setLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = [
      'com.example.test'
    ]
    LockDownExemptionApi.setLockdownExemptionApps(workspaceId, appIds);
  }

  async getLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = await LockDownExemptionApi.getLockdownExemptionApps(workspaceId);
    // 获取冻结豁免应用后， 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setLockdownExemptionApps'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setLockdownExemptionApps();
          })
      }

      Row() {
        Button($r('app.string.getLockdownExemptionApps'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getLockdownExemptionApps();
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
```

### Code block 2

```
const TAG = '[Sample_SpaceManagerSample]';
const DOMAIN = 0xF811;

export class LockDownExemptionApi {
  static async setLockdownExemptionApps(workspaceId: number, appIds: string[]): Promise<void> {
    try {
      await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in setting lockdown exemption apps.`);
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to set lockdown exemption apps. Code: ${err?.code}, message: ${err?.message}`);
    }
  }

  static async getLockdownExemptionApps(workspaceId: number): Promise<string[]> {
    try {
      const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
      hilog.info(DOMAIN, TAG, `Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
      return apps;
    } catch (err) {
      hilog.error(DOMAIN, TAG, `Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
      return [];
    }
  }
}
```

### Code block 3

```
import { router } from '@kit.ArkUI';
import { LockDownExemptionApi } from '../api/LockDownExemptionApi'
```

### Code block 4

```
@Entry
@Component
struct LockDownExemptionPage {
  async setLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = [
      'com.example.test'
    ]
    LockDownExemptionApi.setLockdownExemptionApps(workspaceId, appIds);
  }

  async getLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = await LockDownExemptionApi.getLockdownExemptionApps(workspaceId);
    // 获取冻结豁免应用后， 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button($r('app.string.setLockdownExemptionApps'))
          .buttonCommonStyle()
          .onClick(() => {
            this.setLockdownExemptionApps();
          })
      }

      Row() {
        Button($r('app.string.getLockdownExemptionApps'))
          .buttonCommonStyle()
          .onClick(() => {
            this.getLockdownExemptionApps();
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
