# 更新活动/景点门票

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-update_

当门票信息发生变更时，如座位变更、入场提醒等，更新钱包中的凭证数据。

交互流程

服务端开发

用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发检测更新。

开发者服务器检测到变化，通知钱包服务器进行活动/景点门票数据更新，钱包服务端给钱包推送更新通知。
