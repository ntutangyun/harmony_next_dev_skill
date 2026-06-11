# 情绪

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-emotion_

此数据记录用户在某时刻的情绪数据。

Harmony SDK类型常量：samplePointHelper.emotion.DATA_TYPE

OAuth权限

联盟卡片申请的权限名称：健康数据 > 情绪数据

采样明细数据

[h2]明细字段说明

字段定义：samplePointHelper.emotion.Fields

字段列表	描述	类型	可选/必选	单位	取值范围
emotionStatus	情绪状态	number	M	-	[0, 100) 当前运动健康App仅展示以下值： 1：不愉悦 2：平静 3：愉悦

[h2]数据开放说明

开放API	查询及时性	数据源
healthStore.readData	小时级	手表、手环等
