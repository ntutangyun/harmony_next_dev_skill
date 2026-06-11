# 自定义界面扫码黑屏现象

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-9_

问题现象

自定义启动相机却显示黑屏现象。

解决措施

权限校验错误码：201，没有申请相机权限，向用户申请授权。

参考ArkTS API错误码1000500001：如首次未调用customScan.init初始化，直接调用customScan.start启动扫码相机流，请参考自定义界面扫码的业务流程。
