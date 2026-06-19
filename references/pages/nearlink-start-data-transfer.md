# 使用星闪传输数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-start-data-transfer_

提供星闪数传相关的端口通道建立和数据传输等功能，同一设备可以同时承担数据发送端和接收端的角色。

场景介绍

从5.1.0(18)开始支持星闪数据传输，包括端口注册、建立连接、读写数据等能力。

星闪设备间已建立起逻辑链路基础上，支持应用基于Nearlink技术进行设备间的数据传输。

说明

数据传输通道不保证链路加密。如需加密数传，需先进行配对流程，通过startPairing接口发起。

链路是否加密可通过getAcbState接口查询，ENCRYPTED状态表示链路已加密。

接口说明

接口名	描述
createPort(uuid: string): void	注册端口服务。
connect(params: ConnectionParams): Promise<void>	连接远端设备，建立端口通道。使用Promise异步回调。
writeData(params: DataParams): Promise<void>	通过设备地址和UUID向远端设备发数据。使用Promise异步回调。
on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void	订阅端口通道连接状态变更事件。使用callback异步回调。
on(type: 'readData', callback: Callback<DataParams>): void	订阅端口通道数据接收事件。使用callback异步回调。

开发步骤

导入相关模块。

import { dataTransfer, remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

与远端设备配对加密（可选，如需加密数传，则需执行此步骤）。该步骤执行后，将依据本端与远端设备的输入输出能力标识弹出不同类型的弹窗，需使用者进一步确认。目前支持免输入配对弹窗、数字比较弹窗与通行码鉴权弹窗。

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  device.startPairing().then(()=>{
    console.info('start pairing success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

注册端口通道，发送端和接收端均需注册，并需保证发送端和接收端UUID相同。

let serviceUuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID，此处举例为自定义服务UUID
try {
  dataTransfer.createPort(serviceUuid);
  console.info('create port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

订阅端口通道连接状态变更事件。

let onReceiveConnectionStateEvent:(data: dataTransfer.ConnectionResult) => void =
  (data: dataTransfer.ConnectionResult) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('connectionStateChanged', onReceiveConnectionStateEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

订阅端口通道数据接收事件。

let onReceiveReadDataEvent:(data: dataTransfer.DataParams) => void = (data: dataTransfer.DataParams) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('readData', onReceiveReadDataEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

连接远端设备，建立端口通道。其中UUID要与步骤3中注册的UUID相同。

// 构造端口通道建立的参数
let connectionParams:dataTransfer.ConnectionParams = {
  address: addr, // 扫描获取到的远端设备地址
  uuid: serviceUuid, // 星闪服务UUID
  mtu: 1024 // 期望发送数据包的字节大小，可选参数
};
try {
  dataTransfer.connect(connectionParams).then(()=>{
    console.info('connect success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

通过设备地址和UUID向远端设备发数据。其中UUID要与步骤3中注册的UUID相同。

// 构造发送数据参数
let transferValueBuffer: Uint8Array = new Uint8Array(4);
transferValueBuffer[0] = 1;
transferValueBuffer[1] = 2;
transferValueBuffer[2] = 3;
transferValueBuffer[3] = 4;
let dataParams: dataTransfer.DataParams = {
  address: addr, // 星闪远端设备地址
  uuid: serviceUuid, // 星闪服务UUID
  data: transferValueBuffer.buffer // 星闪设备间传输的数据
};
try {
  dataTransfer.writeData(dataParams).then(() => {
    console.info('writeData success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

示例代码

数据传输功能可参考星闪示例代码，entry/src/main/ets/pages/SsapClientPage.ets中的实现方法。

## Code blocks

### Code block 1

```
import { dataTransfer, remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  device.startPairing().then(()=>{
    console.info('start pairing success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 3

```
let serviceUuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID，此处举例为自定义服务UUID
try {
  dataTransfer.createPort(serviceUuid);
  console.info('create port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 4

```
let onReceiveConnectionStateEvent:(data: dataTransfer.ConnectionResult) => void =
  (data: dataTransfer.ConnectionResult) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('connectionStateChanged', onReceiveConnectionStateEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 5

```
let onReceiveReadDataEvent:(data: dataTransfer.DataParams) => void = (data: dataTransfer.DataParams) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('readData', onReceiveReadDataEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 6

```
// 构造端口通道建立的参数
let connectionParams:dataTransfer.ConnectionParams = {
  address: addr, // 扫描获取到的远端设备地址
  uuid: serviceUuid, // 星闪服务UUID
  mtu: 1024 // 期望发送数据包的字节大小，可选参数
};
try {
  dataTransfer.connect(connectionParams).then(()=>{
    console.info('connect success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 7

```
// 构造发送数据参数
let transferValueBuffer: Uint8Array = new Uint8Array(4);
transferValueBuffer[0] = 1;
transferValueBuffer[1] = 2;
transferValueBuffer[2] = 3;
transferValueBuffer[3] = 4;
let dataParams: dataTransfer.DataParams = {
  address: addr, // 星闪远端设备地址
  uuid: serviceUuid, // 星闪服务UUID
  data: transferValueBuffer.buffer // 星闪设备间传输的数据
};
try {
  dataTransfer.writeData(dataParams).then(() => {
    console.info('writeData success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
