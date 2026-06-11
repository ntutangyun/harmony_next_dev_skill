# 自定义界面扫码同时调用本地图片识码时，应用概率性自动退出

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-18_

问题现象

自定义界面扫码，点击图库，选中图片进行本地图片识码时，应用概率性的自动退出。

解决措施

自定义界面扫码接口和识别本地图片接口不支持并发执行。

点击图库按钮的时候，需要先暂停并释放相机流（customScan.stop、customScan.release），再进行本地图片识码。
