# 进程管控时长管理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-managed-process-management_

从API版本26.0.0开始，新增支持进程管控策略查询与设置、进程管控信息的查询、添加以及删除。

场景介绍

为应用提供进程管控能力。包括：

查询与设置当前设备的进程管控策略，可用于统一设置所有策略的管控时长。

在时长管控场景中，查询、添加和删除进程管控信息。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getManagedProcessPolicy(): Promise<ManagedProcessPolicy | null>	使用Promise方式获取当前设备处于管控状态下的进程管控策略。
setManagedProcessPolicy(policy: ManagedProcessPolicy): Promise<void>	使用Promise方式设置当前设备进程管控的策略。
getManagedProcessList(): Promise<ManagedProcessInfo[]>	使用Promise方式获取当前设备处于管控状态下的进程管控信息列表。
addManagedProcess(processInfo: ManagedProcessInfo): Promise<void>	使用Promise方式添加管控进程。
removeManagedProcess(processInfo: ManagedProcessInfo): Promise<void>	使用Promise方式删除管控进程。

开发步骤

导入模块。

import { process } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口setManagedProcessPolicy，设置当前设备进程管控的策略。

const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置当前设备进程管控的策略。使用Promise异步回调。
 */
function testSetManagedProcessPolicy() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: fileGuard.ManagedProcessPolicy = {
    status: fileGuard.ManagedProcessStatus.TIME_BASED,
    time: 3000
  };
  guard.setManagedProcessPolicy(policy).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting the managed process policy.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set the managed process policy. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口getManagedProcessPolicy，可以查询当前设备处于管控状态下的进程管控策略。

const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

/**
 * 获取当前设备处于管控状态下的进程管控策略。使用Promise异步回调。
 */
function testGetManagedProcessPolicy() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getManagedProcessPolicy().then((policy: fileGuard.ManagedProcessPolicy | null) => {
    if (policy === null) {
      hilog.info(DOMAIN, TAG, `The managed process policy is null.`);
      return;
    }
    hilog.info(DOMAIN, TAG,
      `Succeeded in getting the managed process policy. status: ${policy.status}, time: ${policy.time}`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the managed process policy. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口addManagedProcess，可以添加管控进程。

const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 添加管控进程。使用Promise异步回调。
 */
function testAddManagedProcess() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let processInfo: fileGuard.ManagedProcessInfo = {
    pid: process.pid
  };
  guard.addManagedProcess(processInfo).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in adding the managed process.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to add the managed process. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口getManagedProcessList，可以查询当前设备处于管控状态下的进程管控信息列表。

const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取当前设备处于管控状态下的进程管控信息列表。使用Promise异步回调。
 */
function testGetManagedProcessList() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getManagedProcessList().then((infos: fileGuard.ManagedProcessInfo[]) => {
    hilog.info(DOMAIN, TAG, `Succeeded in getting the managed process list.`);
    infos.forEach((info: fileGuard.ManagedProcessInfo) => {
      hilog.info(DOMAIN, TAG, `ManagedProcessInfo pid: ${info.pid}, policy: ${info.policy}`);
    });
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the managed process list. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口removeManagedProcess，可以删除管控进程。

const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除管控进程。使用Promise异步回调。
 */
function testRemoveManagedProcess() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let processInfo: fileGuard.ManagedProcessInfo = {
    pid: process.pid,
    policy: 'Tag1'
  };
  guard.removeManagedProcess(processInfo).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in removing the managed process.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to remove the managed process. Code: ${err.code}, message: ${err.message}.`);
  });
}

## Code blocks

### Code block 1

```
import { process } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 设置当前设备进程管控的策略。使用Promise异步回调。
 */
function testSetManagedProcessPolicy() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: fileGuard.ManagedProcessPolicy = {
    status: fileGuard.ManagedProcessStatus.TIME_BASED,
    time: 3000
  };
  guard.setManagedProcessPolicy(policy).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in setting the managed process policy.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to set the managed process policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 3

```
const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

/**
 * 获取当前设备处于管控状态下的进程管控策略。使用Promise异步回调。
 */
function testGetManagedProcessPolicy() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getManagedProcessPolicy().then((policy: fileGuard.ManagedProcessPolicy | null) => {
    if (policy === null) {
      hilog.info(DOMAIN, TAG, `The managed process policy is null.`);
      return;
    }
    hilog.info(DOMAIN, TAG,
      `Succeeded in getting the managed process policy. status: ${policy.status}, time: ${policy.time}`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the managed process policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 4

```
const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 添加管控进程。使用Promise异步回调。
 */
function testAddManagedProcess() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let processInfo: fileGuard.ManagedProcessInfo = {
    pid: process.pid
  };
  guard.addManagedProcess(processInfo).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in adding the managed process.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to add the managed process. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 5

```
const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 获取当前设备处于管控状态下的进程管控信息列表。使用Promise异步回调。
 */
function testGetManagedProcessList() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getManagedProcessList().then((infos: fileGuard.ManagedProcessInfo[]) => {
    hilog.info(DOMAIN, TAG, `Succeeded in getting the managed process list.`);
    infos.forEach((info: fileGuard.ManagedProcessInfo) => {
      hilog.info(DOMAIN, TAG, `ManagedProcessInfo pid: ${info.pid}, policy: ${info.policy}`);
    });
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to get the managed process list. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 6

```
const TAG: string = 'FileGuard_ManagedProcess';
const DOMAIN: number = 0x0000;

// ...
/**
 * 删除管控进程。使用Promise异步回调。
 */
function testRemoveManagedProcess() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let processInfo: fileGuard.ManagedProcessInfo = {
    pid: process.pid,
    policy: 'Tag1'
  };
  guard.removeManagedProcess(processInfo).then(() => {
    hilog.info(DOMAIN, TAG, `Succeeded in removing the managed process.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, TAG, `Failed to remove the managed process. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
