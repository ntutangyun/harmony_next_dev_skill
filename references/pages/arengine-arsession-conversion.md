# 管理AR会话介绍

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession-conversion_

在开发AR应用之前，需调用AR会话接口创建一个独立的AR会话，用于管理AR Engine的整个运行状态。AR会话是AR Engine运行的基础，启动会话前需设置相关配置，通过AR会话可以实现：控制AR Engine的启动、暂停、结束等行为。更新并获取AR Engine内部数据，如：锚点、平面、可跟踪对象等。

在进行后续功能开发前，请确保已创建一个可用的AR会话。
