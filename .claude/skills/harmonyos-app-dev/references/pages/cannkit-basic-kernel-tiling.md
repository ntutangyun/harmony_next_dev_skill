# Kernel Tiling

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-kernel-tiling_

KirinX90/Kirin9030 AI处理器为耦合架构(AI Core: 1 * AIC + 1 * AIV)，下发Task执行时，会将整个AI Core启动。当算子配置MIX_AIC_1_2时，需要关注AIV核个数的差异对算子功能的影响。

系统变量
SuperKernel
