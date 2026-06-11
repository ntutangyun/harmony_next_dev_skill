# 游戏调用UnityEngine.Application.Quit侧滑退出时出现黑屏现象，应该如何避免

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-4_

需根据“退出后是否希望继续使用秒级启动能力”选择不同的退出策略：

希望下次启动仍支持秒级启动

在侧滑退出场景下，应调用terminateSelf实现退出，确保进程状态可被系统正确保留，避免出现黑屏问题。

不希望下次启动使用秒级启动

在侧滑退出场景下，应调用killAllProcesses实现强制退出，彻底清理进程，避免残留状态引发异常。
