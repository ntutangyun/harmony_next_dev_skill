# 更新通用凭证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-update_

当通用凭证信息发生变更时，如预约时间变更、状态更新等，更新钱包中的凭证数据。

交互流程

服务端开发

用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发检测更新。

开发者服务器检测到变化，通知钱包服务器进行通用凭证数据更新，钱包服务端给钱包推送更新通知。
