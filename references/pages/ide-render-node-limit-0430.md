# 节点数超过500过多

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-render-node-limit-0430_

如果使用DevEco Studio 6.0.1 Beta1以下版本，规则名称为：图形渲染服务处理节点数小于500。

规则详情

后端Render Server在每帧数据里处理的节点数不应该超过500，否则会造成CPU使用过高，引发帧时延过高，从而导致丢帧。

检测逻辑

H:APP_LIST_FLING

H:APP_SWIPER_SCROLL

H:WEB_LIST_FLING

H:ABILITY_OR_PAGE_SWITCH

H:APP_TRANSITION_FROM_OTHER_APP

H:APP_TRANSITION_TO_OTHER_APP

H:APP_SWIPER_NO_ANIMATION_SWITCH

H:APP_TABS_NO_ANIMATION_SWITCH

H:APP_TABS_FLING

在泳道时序范围内，每一个RenderFrame为一帧，找到这一帧所有的ProcessedNodes字段，提取节点数累加求和（每一帧可能对应多个ProcessedNodes，所以需要累加求和），即每帧渲染的节点数 = Σ ProcessedNodes。

计算逻辑

每帧渲染的节点数小于等于500。
