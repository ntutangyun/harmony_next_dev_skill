# 身高

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-height_

此数据记录用户在某时刻的身高数据。

Harmony SDK类型常量：samplePointHelper.height.DATA_TYPE

说明

Wearable设备暂不支持该数据类型。

OAuth权限

联盟卡片申请的权限名称：健康数据 > 体脂数据

采样明细数据

[h2]明细字段说明

字段定义：samplePointHelper.height.Fields

字段列表	描述	类型	可选/必选	单位	取值范围
height	身高	number	M	厘米	-

[h2]数据开放说明

开放API	查询及时性	数据源
healthStore.readData	小时级	运动健康App个人信息
