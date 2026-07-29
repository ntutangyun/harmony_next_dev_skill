# SSAP客户端

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-ssap-client-connect_

说明

提供SSAP（SparkLink Service Access Protocol）客户端相关的连接、数据传输和服务操作功能。

场景介绍

提供设备作为客户端的能力，客户端可连接服务端进行数据传输。

接口说明

接口名	描述
createClient(address: string): Client	创建ssap客户端实例。
connect(): Promise<void>	向服务端发起连接。
getServices(): Promise<Array<Service>>	获取服务端支持的服务列表。使用Promise异步回调。
readProperty(property: Property): Promise<Property>	读取服务端属性。使用Promise异步回调。
writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>	写入服务端属性。使用Promise异步回调。
setPropertyNotification(property: Property, enable: boolean): Promise<void>	启用/禁用某个属性变化的通知。
on(type: 'propertyChange', callback: Callback<Property>): void	订阅属性变化事件。使用callback异步回调。
on(type: 'connectionStateChange', callback: Callback<ConnectionChangeState>): void	订阅连接状态变化事件。使用callback异步回调。

开发步骤

导入相关模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scan, ssap, dataTransfer, constant, remoteDevice } from '@kit.NearLinkKit';

创建ssap客户端实例。其中参数addr是通过扫描流程获取的远端设备地址。

let client: ssap.Client;
@State chosenDeviceAddr: string = '00:11:22:33:AA:FF';
try {
  client = ssap.createClient(chosenDeviceAddr);
  hilog.info(this.domainId, this.logTag, `client: ${JSON.stringify(client)}`);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

订阅连接状态变化事件。其中client对象在步骤2创建，后续步骤中使用的client对象也是一样，不再赘述。

let connectionStateChangeCallback:(data: ssap.ConnectionChangeState) => void =
  (data: ssap.ConnectionChangeState) => {
  hilog.info(this.domainId, this.logTag, `Connection state: ${JSON.stringify(data)}`);
};
try {
  client.on('connectionStateChange', connectionStateChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

订阅属性变化事件。

let propertyChangeCallback:(data: ssap.Property) => void = (data: ssap.Property) => {
  hilog.info(this.domainId, this.logTag, `Property changed: ${JSON.stringify(data)}`);
  // ...
};
try {
  client.on('propertyChange', propertyChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

向服务端发起连接。连接成功后会收到步骤3中订阅的连接状态变化的回调，之后可以进行数据交互。

try {
  client.connect().then(() => {
    hilog.info(this.domainId, this.logTag, `Connect success`);
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

获取服务端支持的服务列表。

try {
  client.getServices().then((result: Array<ssap.Service>) => {
    // ...
    hilog.info(this.domainId, this.logTag, `Get services successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

读取指定服务的属性值，参数property中的serviceUuid以及propertyUuid通过步骤6获取。

const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';

let arrayBufferProperty = new ArrayBuffer(1);
let properV = new Uint8Array(arrayBufferProperty);
properV[0] = 1;
let property: ssap.Property = {
  serviceUuid: SERVICE_UUID,
  propertyUuid: PROPERTY_UUID,
  value: arrayBufferProperty
};
// ...
try {
  client.readProperty(property).then((result: ssap.Property) => {
    hilog.info(this.domainId, this.logTag, `Read property successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

写入指定服务的属性值，参数property中的serviceUuid以及propertyUuid通过步骤6获取。

try {
  let properValue = new Uint8Array(arrayBufferProperty);
  properValue[0] = 1;
  client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
    hilog.info(this.domainId, this.logTag, `Write property success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

设置支持属性变化通知，参数property中的serviceUuid以及propertyUuid通过步骤6获取。

之后如果服务端属性值发生变化，则客户端通过步骤4订阅的事件接收新数据。

try {
  client.setPropertyNotification(property, true).then(() => {
    hilog.info(this.domainId, this.logTag, `setPropertyNotification success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}

示例代码

SSAP客户端功能可参考星闪示例代码，entry/src/main/ets/pages/SsapClientPage.ets中的实现方法。

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scan, ssap, dataTransfer, constant, remoteDevice } from '@kit.NearLinkKit';
```

### Code block 2

```
let client: ssap.Client;
@State chosenDeviceAddr: string = '00:11:22:33:AA:FF';
try {
  client = ssap.createClient(chosenDeviceAddr);
  hilog.info(this.domainId, this.logTag, `client: ${JSON.stringify(client)}`);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 3

```
let connectionStateChangeCallback:(data: ssap.ConnectionChangeState) => void =
  (data: ssap.ConnectionChangeState) => {
  hilog.info(this.domainId, this.logTag, `Connection state: ${JSON.stringify(data)}`);
};
try {
  client.on('connectionStateChange', connectionStateChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 4

```
let propertyChangeCallback:(data: ssap.Property) => void = (data: ssap.Property) => {
  hilog.info(this.domainId, this.logTag, `Property changed: ${JSON.stringify(data)}`);
  // ...
};
try {
  client.on('propertyChange', propertyChangeCallback);
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 5

```
try {
  client.connect().then(() => {
    hilog.info(this.domainId, this.logTag, `Connect success`);
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 6

```
try {
  client.getServices().then((result: Array<ssap.Service>) => {
    // ...
    hilog.info(this.domainId, this.logTag, `Get services successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 7

```
const SERVICE_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';
const PROPERTY_UUID: string = 'FFFFFFFF-1234-5678-ABCD-000000001234';

let arrayBufferProperty = new ArrayBuffer(1);
let properV = new Uint8Array(arrayBufferProperty);
properV[0] = 1;
let property: ssap.Property = {
  serviceUuid: SERVICE_UUID,
  propertyUuid: PROPERTY_UUID,
  value: arrayBufferProperty
};
// ...
try {
  client.readProperty(property).then((result: ssap.Property) => {
    hilog.info(this.domainId, this.logTag, `Read property successfully: ${JSON.stringify(result)}`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 8

```
try {
  let properValue = new Uint8Array(arrayBufferProperty);
  properValue[0] = 1;
  client.writeProperty(property, ssap.PropertyWriteType.WRITE_NO_RESPONSE).then(() => {
    hilog.info(this.domainId, this.logTag, `Write property success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```

### Code block 9

```
try {
  client.setPropertyNotification(property, true).then(() => {
    hilog.info(this.domainId, this.logTag, `setPropertyNotification success`);
    // ...
  }).catch((err: BusinessError) => {
    hilog.error(this.domainId, this.logTag, `errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  hilog.error(this.domainId, this.logTag,
    `errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
}
```
