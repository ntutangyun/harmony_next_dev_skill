# 更新出行凭证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-update_

当出行凭证信息发生变更时，如登机口变更、延误信息等，更新钱包中的凭证数据。

交互流程

服务端开发

用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发检测更新。

开发者服务器检测到变化，通知钱包服务器进行出行凭证数据更新，钱包服务端给钱包推送更新通知。
