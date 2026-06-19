# 查询策略运行数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-query-guard-strategy-data_

场景介绍

从26.0.0版本开始，Screen Time Guard Kit新增支持查询管控策略运行数据，运行数据包括策略的已使用时长。

业务流程

流程说明：

应用调用查询策略运行数据的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。

若没有权限，则抛出相应错误码；若有权限，则解析参数中传入的策略名称，判断策略是否存在。

若策略不存在，则抛出相应错误码；若存在，则查询该策略类型是否为INCLUSIVE_DURATION_TYPE。

若策略类型不是INCLUSIVE_DURATION_TYPE，则抛出相应错误码；若策略类型是INCLUSIVE_DURATION_TYPE，则查询该策略是否正在执行。

若策略未在执行中，则抛出相应错误码；若策略正在执行，查询并返回该策略下应用的使用时长。

接口说明

查询策略运行数据的关键接口如下表所示：

接口名	描述
queryGuardStrategyData(strategyName: string): Promise<GuardStrategyData>	查询该管控策略的运行数据。

说明

目前仅支持查询INCLUSIVE_DURATION_TYPE类型的策略运行数据。

开发前提

查询策略运行数据需要申请用户授权，请先参考请求用户授权章节完成用户授权。

开发步骤

导入相关模块。

import { guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用queryGuardStrategyData，查询对应管控策略的运行数据。

private async getStrategyData(strategyName: string): Promise<guardService.GuardStrategyData> {
  let usageData: guardService.GuardStrategyData = { usageDuration: 0 };
  try {
    // 查询策略类型为INCLUSIVE_DURATION_TYPE策略的已使用时长.
    usageData = await guardService.queryGuardStrategyData(strategyName);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'GuardService',
      `queryGuardStrategyData failed, errCode is ${err.code}, errMessage is ${err.message}`);
  }
  return usageData;
}

## Code blocks

### Code block 1

```
import { guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
private async getStrategyData(strategyName: string): Promise<guardService.GuardStrategyData> {
  let usageData: guardService.GuardStrategyData = { usageDuration: 0 };
  try {
    // 查询策略类型为INCLUSIVE_DURATION_TYPE策略的已使用时长.
    usageData = await guardService.queryGuardStrategyData(strategyName);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'GuardService',
      `queryGuardStrategyData failed, errCode is ${err.code}, errMessage is ${err.message}`);
  }
  return usageData;
}
```
