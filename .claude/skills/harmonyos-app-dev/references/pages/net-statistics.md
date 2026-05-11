# 统计网络流量消耗

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-statistics_

为了保证应用的运行效率，大部分 API 调用都是异步的，对于异步调用的 API 均提供了 callback 和 Promise 两种方式，以下示例均采用 Promise 函数，更多方式可以查阅@ohos.net.statistics (流量管理)。

以下分别介绍具体开发方式。

开发步骤

导入statistics、socket以及错误码模块。

import { socket, statistics } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
Index.ets

获取指定网卡实时流量数据

调用getIfaceRxBytes接口传入网卡名获取实时下行流量数据。

  // wlan0为主WiFi网卡名，获取主WiFi实时下行流量数据。
  statistics.getIfaceRxBytes('wlan0').then((stats: number) => {
    hilog.info(0x0000, 'testTag', JSON.stringify(stats));
    // ...
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', JSON.stringify(err));
    // ...
  });
  // ...
  // wlan0为主WiFi网卡名，获取主WiFi实时上行流量数据。
  statistics.getIfaceTxBytes('wlan0').then((stats: number) => {
    hilog.info(0x0000, 'testTag', JSON.stringify(stats));
    // ...
  })
  .catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', JSON.stringify(err));
    // ...
  });
// ...
Index.ets

获取蜂窝实时流量数据

调用getCellularRxBytes接口获取蜂窝实时上下行流量数据。

// 获取蜂窝实时下行流量数据。
statistics.getCellularRxBytes().then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
// 获取蜂窝实时上行流量数据。
statistics.getCellularTxBytes().then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
Index.ets

获取所有网卡实时流量数据

调用getAllRxBytes接口获取所有网卡实时上下行流量数据。

// 获取所有网卡实时下行流量数据。
statistics.getAllRxBytes().then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
// 获取所有网卡实时上行流量数据。
statistics.getAllTxBytes().then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
Index.ets

获取指定应用实时流量数据

调用getUidRxBytes接口，传入UID获取指定应用实时上下行流量数据。

 let UID = 20010038;
// 获取指定应用实时下行流量数据。
// ...
statistics.getUidRxBytes(UID).then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
// 获取指定应用实时上行流量数据。
// ...
statistics.getUidTxBytes(UID).then((stats: number) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(stats));
  // ...
})
// ...
Index.ets

获取指定socket实时流量数据

调用getSockfdRxBytes接口，传入指定的sockFd获取指定socket实时上下行流量数据。

// 获取指定socket实时下行流量数据。
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
// ...
tcp.getSocketFd().then((sockfd: number) => {
  statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
    hilog.info(0x0000, 'testTag', JSON.stringify(stats));
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', JSON.stringify(err));
    // ...
  });
})
// ...
// 获取指定socket实时上行流量数据。
tcp.getSocketFd().then((sockfd: number) => {
  statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
    hilog.info(0x0000, 'testTag', JSON.stringify(stats));
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', JSON.stringify(err));
    // ...
  });
})
// ...
Index.ets
管理网络
使用网络防火墙
