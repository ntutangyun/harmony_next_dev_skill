# 读取健康记录

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-healthsequence-manage_

readData<T extends HealthSequence>(request: HealthSequenceReadRequest): Promise<T[]>	查询最新一条健康记录。
说明

当前HealthSequenceReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据。

开发前检查

完成申请运动健康服务与配置Client ID。

接口首次调用前，需先使用init方法进行初始化。

需先通过用户授权接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。

错误码请参考ArkTS API错误码，常见问题请参考Health Service Kit常见问题。

开发步骤

导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

创建查询健康记录请求。

let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
  healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
  startTime: 1695740400000,
  endTime: 1695769200000,
  readOptions: {
    withDetails: true
  }
}

调用readData方法执行查询请求，并处理返回结果。

try {
  const healthSequences = await healthStore.readData(healthSequenceReadRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  healthSequences.forEach((healthSequence) => {
    hilog.info(0x0000, 'testTag', `the start time is ${healthSequence.startTime}.`);
    hilog.info(0x0000, 'testTag', `the end time is ${healthSequence.endTime}.`);
    Object.keys(healthSequence.summaries).forEach((key) => {
      hilog.info(0x0000, 'testTag', `the summaries of ${key} is ${healthSequence.summaries[key]}.`);
    });
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
读取锻炼记录
实时三环数据
