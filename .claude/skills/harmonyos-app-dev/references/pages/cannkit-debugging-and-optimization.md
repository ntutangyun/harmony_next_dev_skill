# 维测调优

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-debugging-and-optimization_

维测调优是CANN Kit提供的对AI模型进行性能统计，并获取性能数据的能力。当前HiAI_OmType接口支持通过AI模型和随机构造的输入文件快速获取Profiling/Dump数据，开发人员可分析模型和单算子的性能数据，并通过模型的层级输出对比精度来完成问题定位。

能力简介

Profiling模式：

支持单算子及整网模型的Profiling性能数据获取，从而分析单算子及整网的执行耗时。
支持Profiling性能数据可视化。

Dump模式：

获取模型的层级输出。
使用说明

开发者可参考CANN Kit Codelab示例完成性能数据获取。当前仅支持HarmonyOS 6.0.0(20)及以上版本的华为手机使用，可在版本说明获取匹配的开发者套件，包含DevEco Studio和SDK。

异构
内存零拷贝
