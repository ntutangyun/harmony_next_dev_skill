# 心率

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-heart-rate_

Harmony SDK类型常量：samplePointHelper.restingHeartRate.DATA_TYPE

OAuth权限

联盟卡片申请的权限名称：健康数据 > 心率数据

采样明细数据

明细字段说明

字段定义：samplePointHelper.restingHeartRate.Fields

字段列表	描述	类型	可选/必选	单位	取值范围
restBpm	静息心率	number	M	次/分钟	[0, ∞)

数据开放说明

开放API	查询及时性	数据源
healthStore.readData	小时级	手表、手环等
采样统计数据

聚合统计策略说明

字段定义：samplePointHelper.restingHeartRate.AggregateFields

字段列表	描述	聚合策略	类型	单位
restBpm	静息心率	last	number	次/分钟

数据开放说明

开放API	查询及时性	数据源
healthStore.aggregateData	小时级	手表、手环等
日常活动
血氧
