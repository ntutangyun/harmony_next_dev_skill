# 游戏截图回调没有返回的文件描述符如何处理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-faq-2_

可能原因及处理方式：

游戏处于后台：游戏截图功能在游戏处于后台时onGameSnapshot不会触发回调。请确保游戏在前台时再获取截图。

服务未就绪：游戏伴随服务可能尚未完成初始化，请等待1秒后再尝试获取截图。
