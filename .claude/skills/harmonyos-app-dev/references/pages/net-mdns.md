# 使用MDNS访问局域网服务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mdns_

为了保证应用的运行效率，大部分API调用都是异步的，对于异步调用的API均提供了callback和Promise两种方式，以下示例均采用promise函数，更多方式可以查阅@ohos.net.mdns (MDNS管理)。

以下分别介绍具体开发方式。

说明

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见获取UIAbility的上下文信息。

管理本地服务

设备连接WiFi。

从@kit.NetworkKit里导入mdns、错误码、以及common命名空间。

// 从@kit.NetworkKit中导入mdns命名空间。
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
Index.ets

调用addLocalService方法，添加本地服务。

// 建立LocalService对象。
private localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: '_print._tcp',
  serviceName: 'servicename',
  port: 5555,
  host: {
    address: '127.0.0.1'
  },
  serviceAttribute: [{ key: '111', value: [1] }]
};
// ...
  let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // addLocalService添加本地服务。
  mdns.addLocalService(context, this.localServiceInfo).then((data) => {
    // ...
    hilog.info(0x0000, 'testTag', `Local Service Added: ${JSON.stringify(data)}`);
  })
  // ...
Index.ets

通过resolveLocalService方法，解析本地网络的IP地址（非必要，根据需求使用）。

// resolveLocalService解析本地服务对象（非必要，根据需求使用）。
mdns.resolveLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  // ...
  hilog.info(0x0000, 'testTag', `Resolved Local Service: ${JSON.stringify(data)}`);
})
Index.ets

通过removeLocalService方法，移除本地服务。

// removeLocalService移除本地服务。
mdns.removeLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  // ...
  hilog.info(0x0000, 'testTag', `Local Service Removed: ${JSON.stringify(data)}`);
})
Index.ets
发现本地服务

设备连接WiFi。

从@kit.NetworkKit里导入mdns的命名空间。

// 从@kit.NetworkKit中导入mdns命名空间。
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
Index.ets

创建DiscoveryService对象，用于发现指定服务类型的MDNS服务。

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
// ...
// 创建DiscoveryService对象，用于发现指定服务类型的MDNS服务。
let serviceType = '_print._tcp';
let discoveryService = mdns.createDiscoveryService(context, serviceType);
Index.ets

订阅MDNS服务发现相关状态变化。

// 订阅MDNS服务发现相关状态变化。
discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ...
});
discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ...
});
Index.ets

启动搜索局域网内的MDNS服务。

// 启动搜索局域网内的MDNS服务。
discoveryService.startSearchingMDNS();
Index.ets

停止搜索局域网内的MDNS服务。

// 停止搜索局域网内的MDNS服务。
discoveryService.stopSearchingMDNS();
Index.ets

取消订阅的MDNS服务。

// 取消订阅的MDNS服务。
discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ...
});
discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ...
});
Index.ets
使用Socket访问网络
使用DNS解析域名
