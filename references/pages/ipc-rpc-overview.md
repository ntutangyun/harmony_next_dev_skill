# IPC Kit简介

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-rpc-overview_

使用IPC和RPC进行跨进程通信时，需要先调用元能力的连接服务接口获取Proxy对象。IPC和RPC的典型使用场景包括：

IPC典型使用场景是后台服务，后台服务通过IPC机制提供单设备跨进程接口调用与数据传递能力。

RPC典型使用场景是多端协同，多端协同通过RPC机制提供跨设备远端接口调用与数据传递能力。

实现原理

IPC和RPC用于实现跨进程通信。IPC使用Binder驱动，适用于设备内的跨进程通信；RPC使用软总线驱动，适用于跨设备的跨进程通信。每个进程拥有独立的资源和内存空间，其他进程无法直接访问，因此需要使用IPC和RPC实现跨进程通信。

IPC和RPC采用客户端-服务端（Client-Server）模型。在使用时，Client进程可以获取Server进程的代理（Proxy），通过Proxy读写数据和发起请求，Stub处理请求并应答结果，实现进程间通信。Proxy和Stub提供了一组由服务/业务自定义的接口，Proxy实现每一个具体的请求方法，Stub实现对应的每一个具体请求的处理方法以及应答数据的内容。

约束与限制

单个设备上跨进程通信时，传输的数据量最大为200KB。超过200KB的数据量传输可以使用匿名共享内存。

不支持在RPC中订阅匿名Stub对象（没有向SAMgr注册的Stub对象）的死亡通知。

不支持把跨设备的Proxy对象回传到该Proxy对象指向的Stub对象所在的设备。

指向远端设备Stub的Proxy对象不能在本设备内二次跨进程传递。

模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“模拟器与真机的差异”。

IPC Kit（进程间通信服务）
IPC与RPC通信开发指导(ArkTS)
