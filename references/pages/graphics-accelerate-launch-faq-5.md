# 日志中频繁打印BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage错误信息，应该如何排查

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-5_

TuanjieMainWorker Error TypeError: undefined is not callable entry|entry|1.0.0|src/main/ets/workers/TuanjieMainWorkerHandler.ts

根据worker.onerror日志排查，确认是否同时存在以下情况：

在onDestroy生命周期中销毁三方SDK。

三方SDK被销毁后，仍继续向Worker线程发送消息。

Worker线程在处理消息过程中仍继续调用已销毁的三方SDK，且未进行异常处理。

在秒级启动场景下，如果用户重新启动游戏后又上滑移除游戏App，游戏进程不会主动销毁Worker线程和团结引擎。当上述三种情况同时发生时，可能导致Worker线程崩溃，并在日志中频繁打印如下错误信息：

BusinessError: The Worker instance is not running, maybe worker is terminated when PostMessage
游戏调用UnityEngine.Application.Quit侧滑退出时出现黑屏现象，应该如何避免
游戏出现卡死后，应该如何避免下一次秒启后还是卡死场景
