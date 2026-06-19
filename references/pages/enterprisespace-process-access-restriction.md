# 进程访问限制

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-process-access-restriction_

从6.0.1(21)开始，支持应用配置系统服务进程对后台用户数据的访问控制。

场景介绍

Enterprise Space Kit支持应用设置系统服务进程不可访问后台用户数据的能力，同时支持获取系统服务进程管控不可访问后台用户数据的状态。另外，支持应用提供获取、新增和删除不可访问后台用户数据的系统服务进程列表的能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>	设置系统服务进程不可访问后台用户数据。
getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>	获取系统服务进程管控不可访问后台用户数据的状态。
getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>	获取不可访问后台用户数据的系统服务进程列表。
addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>	新增系统服务进程不可访问后台用户数据路径列表。
deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string): Promise<void>	删除系统服务进程不可访问后台用户数据路径列表。

开发步骤

1.导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

2.设置和查询系统服务进程不可访问后台用户数据的功能。

@Entry
@Component
struct Index {
  // 设置系统服务进程不可访问后台用户数据。
  async setRestrictedAccessBackgroundUserdata() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const enable: boolean = false;
    try {
      await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
      console.info(
        `Succeeded in setting restricted access background user data. userData:${userData},enable:${enable}`);
    } catch (err) {
      console.error(`Failed to set restricted access background user data. Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取系统服务进程管控不可访问后台用户数据的状态。
  async getRestrictedAccessBackgroundUserdataStatus() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    try {
      const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
      console.info(`Succeeded in getting restricted access background user data status. status:${status}`);
    } catch (err) {
      console.error(
        `Failed to get restricted access background user data status. Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('使能系统服务进程不可访问后台用户数据')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setRestrictedAccessBackgroundUserdata();
          })
      }

      Row() {
        Button('获取不可访问后台用户数据的系统服务状态')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataStatus();
          })
      }
    }
  }
}

3.获取、新增和删除不可访问后台用户数据的系统服务进程列表。

@Entry
@Component
struct Index {
  // 新增系统服务进程不可访问后台用户数据路径列表。
  async addRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 系统实际服务进程的名称。
    const disallowPaths: string[] = ['path'];
    try {
      await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
      console.info(`Succeeded in adding restricted access background user data process list`);
    } catch (err) {
      console.error(
        `Failed to add restricted access background user data process list.Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取不可访问后台用户数据的系统服务进程列表。
  async getRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    try {
      let processConfigInfo: spaceManager.ProcessConfigInfo[] =
        await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
      console.info(`Succeeded in getting restricted access background user data process list.`);
      return processConfigInfo;
    } catch (err) {
      console.error(`Failed to get restricted access background user data process list.`);
      return [];
    }
    // 处理后置逻辑
  }

  // 删除系统服务进程不可访问后台用户数据路径列表。
  async deleteRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 系统实际服务进程的名称。
    try {
      await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
      console.info(`Succeeded in deleting restricted access background user data process list`);
    } catch (err) {
      console.error(
        `Failed to delete restricted access background user data process list.Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('获取不可访问后台用户数据的系统服务进程列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button('新增系统服务进程不可访问后台用户数据路径列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.addRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button('删除系统服务进程不可访问后台用户数据路径列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.deleteRestrictedAccessBackgroundUserdataProcessList();
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
  // 设置系统服务进程不可访问后台用户数据。
  async setRestrictedAccessBackgroundUserdata() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const enable: boolean = false;
    try {
      await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
      console.info(
        `Succeeded in setting restricted access background user data. userData:${userData},enable:${enable}`);
    } catch (err) {
      console.error(`Failed to set restricted access background user data. Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取系统服务进程管控不可访问后台用户数据的状态。
  async getRestrictedAccessBackgroundUserdataStatus() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    try {
      const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
      console.info(`Succeeded in getting restricted access background user data status. status:${status}`);
    } catch (err) {
      console.error(
        `Failed to get restricted access background user data status. Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('使能系统服务进程不可访问后台用户数据')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setRestrictedAccessBackgroundUserdata();
          })
      }

      Row() {
        Button('获取不可访问后台用户数据的系统服务状态')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataStatus();
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
  // 新增系统服务进程不可访问后台用户数据路径列表。
  async addRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 系统实际服务进程的名称。
    const disallowPaths: string[] = ['path'];
    try {
      await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
      console.info(`Succeeded in adding restricted access background user data process list`);
    } catch (err) {
      console.error(
        `Failed to add restricted access background user data process list.Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取不可访问后台用户数据的系统服务进程列表。
  async getRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    try {
      let processConfigInfo: spaceManager.ProcessConfigInfo[] =
        await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
      console.info(`Succeeded in getting restricted access background user data process list.`);
      return processConfigInfo;
    } catch (err) {
      console.error(`Failed to get restricted access background user data process list.`);
      return [];
    }
    // 处理后置逻辑
  }

  // 删除系统服务进程不可访问后台用户数据路径列表。
  async deleteRestrictedAccessBackgroundUserdataProcessList() {
    const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
    const processName: string = 'testSa'; // 系统实际服务进程的名称。
    try {
      await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
      console.info(`Succeeded in deleting restricted access background user data process list`);
    } catch (err) {
      console.error(
        `Failed to delete restricted access background user data process list.Code:${err.code},message:${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('获取不可访问后台用户数据的系统服务进程列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button('新增系统服务进程不可访问后台用户数据路径列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.addRestrictedAccessBackgroundUserdataProcessList();
          })
      }

      Row() {
        Button('删除系统服务进程不可访问后台用户数据路径列表')
          .width(400)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.deleteRestrictedAccessBackgroundUserdataProcessList();
          })
      }
    }
  }
}
```
