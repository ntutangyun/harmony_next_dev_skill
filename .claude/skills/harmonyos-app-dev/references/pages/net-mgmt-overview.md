# Network Kit简介

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mgmt-overview_

网络连接管理：网络连接管理提供管理网络一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、DNS解析等功能。
MDNS管理：MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、删除、发现、解析等能力。
模拟器支持情况

Network Kit支持模拟器，但与真机存在差异，具体差异如下。

通用差异：详情请参见“模拟器与真机的差异”。
模拟器不支持VPN功能。
约束与限制

使用网络管理模块的相关功能时，需要请求相应的权限。

在申请权限前，请保证符合权限使用的基本原则。然后参考访问控制-声明权限声明对应权限。

权限名	说明
ohos.permission.GET_NETWORK_INFO	获取网络连接信息。
ohos.permission.INTERNET	允许程序打开网络套接字，进行网络连接。
Network Kit（网络服务）
Network Kit术语
