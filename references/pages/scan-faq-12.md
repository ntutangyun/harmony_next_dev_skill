# 默认界面扫码取消后，如何感知

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-12_

开启扫码，却没有进行任何扫码操作而直接取消扫码，可以从回调中获取返回错误码：1000500002，用户取消扫码，据此自行修改逻辑操作。

通过字节数组生成码图无法识别
H5场景如何接入扫码
