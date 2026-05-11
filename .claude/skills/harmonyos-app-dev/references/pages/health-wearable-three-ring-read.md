# 实时三环数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-three-ring-read_

const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
  });
} catch(err) {
  hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
}
读取健康记录
数据类型
