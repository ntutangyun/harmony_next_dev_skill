# 游戏截图回调没有返回的文件描述符如何处理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-faq-2_

可能原因及处理方式：

游戏处于后台：游戏截图功能仅在游戏处于前台时可调用，此时onGameSnapshot不会触发。确保游戏在前台时再获取截图。

截图频率过高：游戏截图接口有频率限制，每秒最多调用一次。如果调用过于频繁，会返回错误。请在回调中检查返回的文件描述符是否为有效值。

服务未就绪：游戏伴随服务可能尚未完成初始化。建议在收到FOREGROUND状态通知后，等待一段时间后再尝试获取截图。
