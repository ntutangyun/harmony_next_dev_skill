# 线程模型

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/thread-model-stage_

同一线程中存在多个组件，例如UIAbility组件和UI组件都存在于主线程中。在Stage模型中目前主要使用EventHub进行数据通信。
执行hdc shell命令，进入设备的shell命令行。在shell命令行中，执行ps -p <pid> -T命令，可以查看指定应用进程的线程信息。其中，<pid>为需要指定的应用进程的进程ID。
使用EventHub进行线程内通信

EventHub提供了线程内发送和处理事件的能力，包括对事件订阅、取消订阅、触发事件等。以UIAbility组件与UI之间的数据同步为例，具体使用方法可以参考UIAbility组件与UI的数据同步。

进程模型
Stage模型应用配置文件
