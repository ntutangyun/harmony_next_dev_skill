# 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-18_

点击图库按钮的时候，需要先暂停并释放相机流（customScan.stop、customScan.release），再进行本地图片识码。

自定义界面扫码如何增加重试机制
如何将码图背景颜色设置成透明色
