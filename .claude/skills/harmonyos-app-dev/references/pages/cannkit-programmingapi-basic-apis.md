# 基础API

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-programmingapi-basic-apis_

AscendC编程范式，把算子核内的处理程序，分成多个流水任务，通过队列(Queue)完成任务间通信和同步，并通过统一的资源管理模块(Pipe)来统一管理内存、事件等资源。

AscendC提供一组内存管理与同步控制API，开发者使用这一组API即可完成任务间同步和内存管理。

核心的API包括：

AllocTensor：从Queue中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。

FreeTensor：释放Queue中的指定Tensor，供Queue后续使用。

EnQue：将Tensor push到队列Queue。

DeQue：将Tensor从队列Queue中取出，用于后续处理。

接口概述
高阶API
