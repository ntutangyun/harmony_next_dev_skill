# 权限说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-permission-description_

运动健康数据读写以及运动联动接口调用需要相应的权限，权限申请参考申请运动健康服务，数据类型对应权限如下：

Wearable

数据类型	Harmony SDK类型常量	读权限	写权限
日常活动	samplePointHelper.dailyActivities.DATA_TYPE	日常活动数据（读）	日常活动数据（写）
动态心率	samplePointHelper.heartRate.DATA_TYPE	心率数据（读）	心率数据（写）
静息心率	samplePointHelper.restingHeartRate.DATA_TYPE	心率数据（读）	心率数据（写）
血氧	samplePointHelper.bloodOxygenSaturation.DATA_TYPE	血氧数据（读）	血氧数据（写）
压力	samplePointHelper.stress.DATA_TYPE	压力数据（读）	压力数据（写）
体温	samplePointHelper.bodyTemperature.DATA_TYPE	体温数据（读）	体温数据（写）
皮肤体温	samplePointHelper.skinTemperature.DATA_TYPE	体温数据（读）	体温数据（写）
血压	samplePointHelper.bloodPressure.DATA_TYPE	血压数据（读）	血压数据（写）
身高	samplePointHelper.height.DATA_TYPE	体脂数据（读）	体脂数据（写）
体重	samplePointHelper.weight.DATA_TYPE	体脂数据（读）	体脂数据（写）
情绪	samplePointHelper.emotion.DATA_TYPE	情绪数据（读）	情绪数据（写）
心率变异性	samplePointHelper.heartRateVariability.DATA_TYPE	心率数据（读）	心率数据（写）
睡眠	healthSequenceHelper.sleepRecord.DATA_TYPE healthSequenceHelper.sleepNapRecord.DATA_TYPE	睡眠数据（读）	睡眠数据（写）
锻炼记录	exerciseSequenceHelper.DATA_TYPE	锻炼记录概要（读） 锻炼记录详情数据（读） 锻炼记录位置详情数据（读）	锻炼记录概要（写） 锻炼记录详情数据（写） 锻炼记录位置详情数据（写）

Lite Wearable

权限名称	权限对应字段和取值	说明
运动联动	scopes: ['https://www.huawei.com/healthkit/workout']	管理运动联动的开关，打开后可调用运动联动相关的开关。
锻炼记录概要读权限	readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY]	开启后可读取锻炼数据。
锻炼记录概要写权限	writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY]	开启后可写入锻炼数据。

说明

如需读/写锻炼记录，请申请锻炼记录概要的读/写权限。

如需读/写锻炼记录且关联对应的详情数据，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据的读/写权限。

如需读/写锻炼记录且关联的详情数据包含位置详情，则需同时申请锻炼记录概要读/写权限、锻炼记录详情数据读/写、锻炼记录位置详情数据的读/写权限。
