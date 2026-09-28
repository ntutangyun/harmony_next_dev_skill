# Linx Kit术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linx-kit-glossary_

B

[h2]Branch Jump；分支跳转

程序运行过程中的条件分支跳转行为，是热点加速模块记录和重放的关键信息之一，用于在下一帧中预判执行路径以提升效率。

C

[h2]Context Index；上下文索引

热点加速API中用于标识一次加速会话的uint32_t类型索引。需在HMS_LINX_HotspotAccelerateBegin和HMS_LINX_HotspotAccelerateEnd调用中保持一致，以确保加速与释放操作对应同一会话。

I

[h2]Inter-frame Information Reuse；帧间信息复用

利用相邻帧之间执行行为的相似性，将上一帧记录的关键信息（如分支跳转）在下一帧进行重放，减少重复计算开销，是热点加速的核心优化原理。
