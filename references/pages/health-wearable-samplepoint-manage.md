# 读取运动健康采样数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-samplepoint-manage_

readData<T extends SamplePoint>(request: SamplePointReadRequest): Promise<T[]>	查询最新一条运动健康采样数据。
说明

当前SamplePointReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据，读取实时日常活动数据使用读取实时三环数据接口。

开发前检查

完成申请运动健康服务与配置Client ID。

接口首次调用前，需先使用init方法进行初始化。

需先通过用户授权接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。

错误码请参考ArkTS API错误码，常见问题请参考Health Service Kit常见问题。

开发步骤

导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

创建查询请求。

let samplePointReadRequest: healthStore.SamplePointReadRequest = {
  samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000,
  fields: {
    bodyTemperature: 39
  }
}

调用readData方法执行查询请求，并处理返回结果。

try {
  let samplePoints = await healthStore.readData(samplePointReadRequest);
  samplePoints.forEach((samplePoint) => {
    hilog.info(0x0000, 'testTag', `Succeeded in reading data, the bodyTemperature is ${samplePoint.fields.bodyTemperature}.`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
管理运动健康数据
读取锻炼记录
