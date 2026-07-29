# SSAP服务端

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-ssap-server-connect_

提供SSAP（SparkLink Service Access Protocol）服务端相关的连接、数据传输和服务管理功能。

注意

建立SSAP连接后，SSAP服务端广播会自动停止。后续如果服务端期望被客户端发现，可参见发送星闪广播，重新发起广播。

场景介绍

支持应用基于Nearlink技术进行数据传输，设备作为服务端，客户端可连接该服务端进行数据传输。

接口说明

接口名	描述
createServer(): Server	创建ssap服务端实例。
addService(service: Service): void	服务端添加服务。
on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void	订阅连接状态变化事件。使用callback异步回调。
on(type: 'propertyRead', callback: Callback<PropertyReadRequest>): void	订阅客户端的读属性请求事件。使用callback异步回调。
sendResponse(response: ServerResponse): void	回复客户端读/写请求。
notifyPropertyChanged(address: string, property: Property): Promise<void>	通知客户端属性值更新。使用Promise异步回调。

开发步骤

导入相关模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { ssap, advertising, dataTransfer, constant, manager } from '@kit.NearLinkKit';

创建ssap服务端实例。

let server: ssap.Server;
try {
  server = ssap.createServer();
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

添加服务端支持的服务，其中server对象在步骤2创建，后续步骤中使用的server对象也是一样，不再赘述。

let property1: ssap.Property;
let property2: ssap.Property;
const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID_1: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID_2: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
let READABLE: number = ssap.Operation.READABLE;
let WRITE_NO_RESPONSE: number = ssap.Operation.WRITE_NO_RESPONSE;
let WRITE_WITH_RESPONSE: number = ssap.Operation.WRITE_WITH_RESPONSE;
let NOTIFY: number = ssap.Operation.NOTIFY;
// ...
try {
  let descriptorsArray1: ssap.PropertyDescriptor[] = [];
  let descriptorsArray2: ssap.PropertyDescriptor[] = [];
  let arrayBuffer = new ArrayBuffer(2);
  let descValue = new Uint8Array(arrayBuffer);
  descValue[0] = 1;
  descValue[1] = 0;
  let descriptor1: ssap.PropertyDescriptor = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_1,
    value: arrayBuffer,
    descriptorType:ssap.PropertyDescriptorType.CLIENT_PROPERTY_CONFIG,
    isWriteable:true
  };
  let descriptor2: ssap.PropertyDescriptor = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_2,
    value: arrayBuffer,
    descriptorType:ssap.PropertyDescriptorType.PROPERTY,
    isWriteable:false
  };
  descriptorsArray1[0] = descriptor1;
  descriptorsArray2[0] = descriptor2;
  let propertiesArray: ssap.Property[] = [];
  let arrayBufferProperty = new ArrayBuffer(1);
  let properValue = new Uint8Array(arrayBufferProperty);
  properValue[0] = 11;
  property1 = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_1,
    value: arrayBufferProperty,
    descriptors: descriptorsArray1,
    operation: READABLE | WRITE_NO_RESPONSE | NOTIFY
  };
  property2 = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_2,
    value: arrayBufferProperty,
    descriptors: descriptorsArray2,
    operation: READABLE | WRITE_WITH_RESPONSE
  };
  propertiesArray[0] = property1;
  propertiesArray[1] = property2;
  let service: ssap.Service = {
    serviceUuid: SERVICE_UUID,
    properties:propertiesArray
  };
  server.addService(service);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

订阅连接状态变化事件。

let connectionStateChangeCallback = (data: ssap.ConnectionChangeState) => {
  hilog.info(this.domainId, this.logTag, `Connection state change: ${JSON.stringify(data)}`);
  // ...
};
try {
  server.on('connectionStateChange', connectionStateChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

订阅客户端读属性请求事件。

let onReceivePropertyReadEvent:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  hilog.info(this.domainId, this.logTag, `Property data received: ${JSON.stringify(data)}`);
  // ...
};
try {
  server.on('propertyRead', onReceivePropertyReadEvent);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

通知客户端属性值更新。其中参数address是步骤4中获取的已连接客户端设备地址。

let onReceivePropertyWriteEvent:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  hilog.info(this.domainId, this.logTag, `PropertyWriteRequest: ${JSON.stringify(data)}`);
  let property: ssap.Property = {
    serviceUuid: data.serviceUuid,
    propertyUuid: data.propertyUuid,
    value: data.value
  };
  server.notifyPropertyChanged(data.address, property).then(() => {
    hilog.info(this.domainId, this.logTag, `notifyPropertyChanged success`);
    // ...
  }).catch((err:BusinessError) => {
    hilog.error(this.domainId, this.logTag,
      `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
    // ...
  });
};
try {
  server.on('propertyWrite', onReceivePropertyWriteEvent);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

示例代码

SSAP服务端功能可参考星闪示例代码，entry/src/main/ets/pages/SsapServerPage.ets中的实现方法。

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { ssap, advertising, dataTransfer, constant, manager } from '@kit.NearLinkKit';
```

### Code block 2

```
let server: ssap.Server;
try {
  server = ssap.createServer();
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 3

```
let property1: ssap.Property;
let property2: ssap.Property;
const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID_1: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID_2: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
let READABLE: number = ssap.Operation.READABLE;
let WRITE_NO_RESPONSE: number = ssap.Operation.WRITE_NO_RESPONSE;
let WRITE_WITH_RESPONSE: number = ssap.Operation.WRITE_WITH_RESPONSE;
let NOTIFY: number = ssap.Operation.NOTIFY;
// ...
try {
  let descriptorsArray1: ssap.PropertyDescriptor[] = [];
  let descriptorsArray2: ssap.PropertyDescriptor[] = [];
  let arrayBuffer = new ArrayBuffer(2);
  let descValue = new Uint8Array(arrayBuffer);
  descValue[0] = 1;
  descValue[1] = 0;
  let descriptor1: ssap.PropertyDescriptor = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_1,
    value: arrayBuffer,
    descriptorType:ssap.PropertyDescriptorType.CLIENT_PROPERTY_CONFIG,
    isWriteable:true
  };
  let descriptor2: ssap.PropertyDescriptor = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_2,
    value: arrayBuffer,
    descriptorType:ssap.PropertyDescriptorType.PROPERTY,
    isWriteable:false
  };
  descriptorsArray1[0] = descriptor1;
  descriptorsArray2[0] = descriptor2;
  let propertiesArray: ssap.Property[] = [];
  let arrayBufferProperty = new ArrayBuffer(1);
  let properValue = new Uint8Array(arrayBufferProperty);
  properValue[0] = 11;
  property1 = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_1,
    value: arrayBufferProperty,
    descriptors: descriptorsArray1,
    operation: READABLE | WRITE_NO_RESPONSE | NOTIFY
  };
  property2 = {
    serviceUuid: SERVICE_UUID,
    propertyUuid: PROPERTY_UUID_2,
    value: arrayBufferProperty,
    descriptors: descriptorsArray2,
    operation: READABLE | WRITE_WITH_RESPONSE
  };
  propertiesArray[0] = property1;
  propertiesArray[1] = property2;
  let service: ssap.Service = {
    serviceUuid: SERVICE_UUID,
    properties:propertiesArray
  };
  server.addService(service);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 4

```
let connectionStateChangeCallback = (data: ssap.ConnectionChangeState) => {
  hilog.info(this.domainId, this.logTag, `Connection state change: ${JSON.stringify(data)}`);
  // ...
};
try {
  server.on('connectionStateChange', connectionStateChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 5

```
let onReceivePropertyReadEvent:(data: ssap.PropertyReadRequest) => void = (data: ssap.PropertyReadRequest) => {
  hilog.info(this.domainId, this.logTag, `Property data received: ${JSON.stringify(data)}`);
  // ...
};
try {
  server.on('propertyRead', onReceivePropertyReadEvent);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 6

```
let onReceivePropertyWriteEvent:(data: ssap.PropertyWriteRequest) => void = (data: ssap.PropertyWriteRequest) => {
  hilog.info(this.domainId, this.logTag, `PropertyWriteRequest: ${JSON.stringify(data)}`);
  let property: ssap.Property = {
    serviceUuid: data.serviceUuid,
    propertyUuid: data.propertyUuid,
    value: data.value
  };
  server.notifyPropertyChanged(data.address, property).then(() => {
    hilog.info(this.domainId, this.logTag, `notifyPropertyChanged success`);
    // ...
  }).catch((err:BusinessError) => {
    hilog.error(this.domainId, this.logTag,
      `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
    // ...
  });
};
try {
  server.on('propertyWrite', onReceivePropertyWriteEvent);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```
