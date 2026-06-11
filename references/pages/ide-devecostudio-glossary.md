# DevEco Profiler术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-devecostudio-glossary_

异步栈缝合

在异步回栈时，该功能支持多回一层异步栈帧。如下图中的start_malloc_xxx_work异步调用malloc_xxx_work，当开关未开启时，仅能回malloc_xxx_work栈帧；当开关开启后，支持回malloc_xxx_work栈帧和start_malloc_xxx_work栈帧。
