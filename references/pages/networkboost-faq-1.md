# 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-1_

请求多网成功后可以获取到多个可用的netHandle，通过connection.getNetCapabilities()方法查询网络信息，通过NetBearType字段判断网络类型，其中BEARER_CELLULAR是蜂窝网络，BEARER_WIFI是Wi-Fi网络。在设计多网并发策略时可以通过网络类型和网络能力调整对应网络通路的网络任务。
