# 概述

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-overview_

手机应用发起碰一碰分享时，双端设备需要在亮屏、且解锁的状态下并且都已开启华为分享服务（系统默认开启），设备顶部轻碰即可触发。如果用户已手动关闭华为分享服务开关，轻碰事件触发时，用户会接收到系统通知提示开启。

Share Kit的处理机制：

任意一端设备不支持碰一碰能力时，轻碰无任何响应。

宿主应用无法获得分享结果，Share Kit会通过系统通知消息告知用户对端接收或拒绝。

环境要求

支持的手机系统：HarmonyOS NEXT Release及以上版本，可使用canIUse判断系统能力是否支持。

if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
  // 支持一碰分享的能力.
}

集成开发环境：DevEco Studio NEXT Beta1及以上版本。

手机与手机碰一碰分享
内容分享
