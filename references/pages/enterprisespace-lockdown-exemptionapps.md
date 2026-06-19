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

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

2.设置和查询深度冻结豁免名单。

@Entry
@Component
struct Index {
  // 设置深度冻结豁免名单
  async setLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = [
      'com.example.test'
    ]
    try {
      await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
      console.info(`Succeeded in setting lockdown exemption apps.`);
    } catch (err) {
      console.error(`Failed to set lockdown exemption apps. Code: ${err?.code}, message: ${err?.message}`);
    }
  }

  // 查询深度冻结豁免名单
  async getLockdownExemptionApps() {
    let workspaceId: number = 100;
    try {
      const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
      console.info(`Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
    } catch (err) {
      console.error(`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
    }
    // 获取冻结豁免应用后，处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('设置冻结豁免应用')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setLockdownExemptionApps();
          })
      }

      Row() {
        Button('获取冻结豁免应用')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getLockdownExemptionApps();
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
  // 设置深度冻结豁免名单
  async setLockdownExemptionApps() {
    let workspaceId: number = 100;
    let appIds: string[] = [
      'com.example.test'
    ]
    try {
      await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
      console.info(`Succeeded in setting lockdown exemption apps.`);
    } catch (err) {
      console.error(`Failed to set lockdown exemption apps. Code: ${err?.code}, message: ${err?.message}`);
    }
  }

  // 查询深度冻结豁免名单
  async getLockdownExemptionApps() {
    let workspaceId: number = 100;
    try {
      const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
      console.info(`Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
    } catch (err) {
      console.error(`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
    }
    // 获取冻结豁免应用后，处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('设置冻结豁免应用')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setLockdownExemptionApps();
          })
      }

      Row() {
        Button('获取冻结豁免应用')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getLockdownExemptionApps();
          })
      }
    }
  }
}
```
