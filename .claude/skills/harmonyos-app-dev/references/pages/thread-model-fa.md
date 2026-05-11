# 线程模型

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/thread-model-fa_

基于当前的线程模型，不同的业务功能运行在不同的线程上，业务功能的交互就需要线程间通信。线程间通信目前主要有Emitter和Worker两种方式，其中Emitter主要适用于线程间的事件同步， Worker主要用于新开一个线程执行耗时任务。

说明

FA模型每个Ability都有一个独立的线程，Emitter可用于Ability线程内、Ability线程间、Ability线程与Worker线程的事件同步。

进程模型概述
FA模型应用配置文件
