# 添加、删除、获取放通应用列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-unrestricted-app-list_

从6.1.1(24)版本开始，新增添加、删除和获取放通应用列表的接口，支持用户维护放通应用列表。

场景介绍

为应用提供添加、删除和获取放通应用列表的能力，添加到列表中的应用将不受updatePolicy接口下发的网络、U盘、蓝牙、星闪、Samba客户端和服务端策略管控，但打印管控策略仍会受到限制。

接口说明

详细接口说明可参考接口文档。

接口名	描述
addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>	使用Promise方式添加放通应用列表。
removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>	使用Promise方式删除放通应用列表。
getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>	使用Promise方式获取放通应用列表。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口addUnrestrictedApplicationList，添加放通应用列表。

const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

/**
 * 添加放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testAddUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];

    guard.addUnrestrictedApplicationList(appIds, userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in adding the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to add the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test addUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}

初始化FileGuard对象guard，调用接口getUnrestrictedApplicationList，可以查看放通应用列表。

const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testGetUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;

    guard.getUnrestrictedApplicationList(userId).then((appIds: string[]) => {
      hilog.info(DOMAIN, TAG,
        `Succeeded in getting the application from the unrestricted list. appIds: ${appIds.toString()}`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to get the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test getUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}

初始化FileGuard对象guard，调用接口removeUnrestrictedApplicationList，可以删除放通应用列表。

const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testRemoveUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;

    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];

    guard.removeUnrestrictedApplicationList(appIds, userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in removing the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to remove the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test removeUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

/**
 * 添加放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testAddUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];

    guard.addUnrestrictedApplicationList(appIds, userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in adding the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to add the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test addUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

### Code block 3

```
const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testGetUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;

    guard.getUnrestrictedApplicationList(userId).then((appIds: string[]) => {
      hilog.info(DOMAIN, TAG,
        `Succeeded in getting the application from the unrestricted list. appIds: ${appIds.toString()}`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to get the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test getUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

### Code block 4

```
const TAG: string = 'FileGuard_UnrestrictedApplicationList';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除放通应用列表。使用Promise异步回调。
 * @param accountId: 用户ID
 */
async function testRemoveUnrestrictedApplicationList(accountId: number) {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let userId: number = accountId;

    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];

    guard.removeUnrestrictedApplicationList(appIds, userId).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in removing the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to remove the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    hilog.error(DOMAIN, TAG,
      `Failed to test removeUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```
