# 更新酒店房卡

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-update_

当用户更换房间时，更新钱包中的房卡数据，自动同步为新房间号，无需重新开卡。

交互流程

服务端开发

用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发酒店房卡检测更新（每日最多一次）。

开发者服务器检测到变化，通知钱包服务器进行酒店房卡数据更新。
