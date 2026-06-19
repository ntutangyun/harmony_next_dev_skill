# 通过Push Kit更新实况窗

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-update-by-push_

场景介绍

本地实况窗的更新依赖于应用进程的存活，为了让实况窗在生命周期内正常完成更新和结束，我们更推荐开发者使用Push Kit实时更新实况窗状态。

通过Push Kit更新实况窗的流程如下图：

使用Push Kit，获取Push Token。

使用Live View Kit创建实况窗成功后，开发者需要将实况窗id、pushToken、实况窗场景event以及业务服务的相关的状态属性保存到业务服务端。

当业务服务的用户订单状态发生变化时，通过Push Kit通道推送更新消息，更新/结束实况窗。

详细开发流程请参见Push Kit推送实况窗消息。

具体的Live View Kit ArkTS API和Push Kit REST API的字段关联关系请参见Live View Kit ArkTS API与Push Kit REST API的字段关联关系表。

支持网络图片下载

从26.0.0开始，实况窗支持通过Push Kit下载网络图片，存在以下限制条件：

支持下载的网络图片大小不大于512KB。

支持下载的网络图片文件格式包括jpg、jpeg、png、bmp、webp。

仅支持HTTPS协议的网络图片下载，即只支持以"https://"开头的图片网址。

仅如下1到7位置支持网络图片下载，具体请参考请求体参数说明。

模板类型	示意图
基础模板	
进度可视化模板	
强调文本模板	
左右文本模板	
赛事比分模板	
胶囊模板	
