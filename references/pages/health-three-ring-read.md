# 实时三环数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-three-ring-read_

场景介绍

实时三环数据，包括实时步数，活动热量，锻炼时长，活动小时数以及目标类数据。

说明

此接口使用日常活动数据类型读权限，参考权限说明。

OAuth权限

联盟卡片申请的权限名称：日常活动 > 日常活动数据（读）

接口说明

接口名	描述
readActivityReport(): Promise<ActivityReport>	读取实时三环数据。

开发前检查

完成申请运动健康服务与配置Client ID。

接口首次调用前，需先使用init方法进行初始化。

需先通过用户授权接口引导用户授权，用户授权日常活动数据类型读权限（参考权限说明）后，才有权限读取实时三环数据。

错误码请参考ArkTS API错误码，常见问题请参考Health Service Kit常见问题。

开发步骤

导入运动健康服务功能模块及相关公共模块。

import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

调用readActivityReport方法读取实时三环数据，并处理返回结果。

try {
  const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();

  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
}

## Code blocks

### Code block 1

```
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
try {
  const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();

  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
}
```
