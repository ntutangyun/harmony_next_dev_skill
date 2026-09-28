# 常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-faq_

Native Leaks泳道录制捕获的泄露数据减少或丢失

问题现象

应用生命周期中，使用Allocation模板在当前会话录制ArkTS Snapshot泳道后，未重启应用在后续会话直接录制Native Leaks泳道，可能会导致捕获的泄露数据减少或丢失问题。

解决措施

录制ArkTS Snapshot泳道后，需重启应用，再录制Native Leaks泳道。
