# 滑动过程流畅

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413_

规则详情

应用的滑动过程卡顿率≤ 5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。

检测逻辑

开始时间：以APP_LIST_FLING滑动泳道为例，泳道的起点（如图标记1）。

其他滑动泳道标记如下：

H:APP_SWIPER_SCROLL

H:WEB_LIST_FLING

查找滑动泳道：H:APP_LIST_FLING，如果是web页面，找H:WEB_LIST_FLING。

总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 * 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
