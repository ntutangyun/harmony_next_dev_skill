# 气泡提示概述

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-overview_

不依赖UI组件的全局气泡提示 (openPopup)	用于需要在无法直接访问UI组件的场景中给提示时，例如在事件回调中弹出一段帮助提示等。
规格约束
Popup的弹出需要等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致popup弹窗显示位置及形状错误。
openPopup的弹出需要传入有效的TargetInfo，否则无法弹出气泡。
其他规格约束，具体可参考Popup控制、openPopup 说明。
气泡提示
气泡提示（Popup）
