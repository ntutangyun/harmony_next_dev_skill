# 发送星闪广播

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-send-advertising_

场景介绍

发送星闪广播，广播数据可以被支持星闪能力的中心设备扫描到。

接口说明

接口名	描述
startAdvertising(advertisingParams: AdvertisingParams): Promise<number>	启动星闪广播。使用Promise异步回调。
stopAdvertising(advertisingId: number): Promise<void>	停止星闪广播。使用Promise异步回调。
on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void	订阅星闪广播状态变化事件。使用callback异步回调。
off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void	取消订阅星闪广播状态变化事件。使用callback异步回调。

开发步骤

导入相关模块。

import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

订阅星闪广播状态变化事件。

let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void =
   (data:advertising.AdvertisingStateChangeInfo) => {
   console.info('advertisingId:' + data.advertisingId);
   console.info('advertisingState:' + data.state);
};
try {
   advertising.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
   console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

构造用户需要的广播参数及数据。

let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;
let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = ' + JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = ' + JSON.stringify(serviceValueBuffer));
let setting: advertising.AdvertisingSettings = {
  interval:5000,
  power:advertising.TxPowerMode.ADV_TX_POWER_LOW
};
let manufactureDataUnit: advertising.ManufacturerData = {
  manufacturerId:4567,
  manufacturerData:manufactureValueBuffer.buffer
};
let serviceDataUnit: advertising.ServiceData = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000001234',
  serviceData:serviceValueBuffer.buffer
};
let advData: advertising.AdvertisingData = {
  serviceUuids:['37bea880-fc70-11ea-b720-000000001234'],
  manufacturerData:[manufactureDataUnit],
  serviceData:[serviceDataUnit]
};
let advertisingParams: advertising.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData
};

开启星闪广播，返回advertisingId表示当前广播索引。

let advId = -1;
try {
  advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
    advId = advertisingId;
    console.info('advertising id:' + JSON.stringify(advId));
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

停止星闪广播，其中advId是步骤4开启广播后返回的advertisingId。

try {
  advertising.stopAdvertising(advId).then(() => {
      console.info('stop advertising success');
    }).catch ((err: BusinessError) => {
      console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
    });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

取消订阅星闪广播状态变化事件。

try {
  advertising.off('advertisingStateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

示例代码

星闪广播场景可参考星闪示例代码，entry/src/main/ets/pages/MainPage.ets中的实现方法。

## Code blocks

### Code block 1

```
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void =
   (data:advertising.AdvertisingStateChangeInfo) => {
   console.info('advertisingId:' + data.advertisingId);
   console.info('advertisingState:' + data.state);
};
try {
   advertising.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
   console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 3

```
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;
let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = ' + JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = ' + JSON.stringify(serviceValueBuffer));
let setting: advertising.AdvertisingSettings = {
  interval:5000,
  power:advertising.TxPowerMode.ADV_TX_POWER_LOW
};
let manufactureDataUnit: advertising.ManufacturerData = {
  manufacturerId:4567,
  manufacturerData:manufactureValueBuffer.buffer
};
let serviceDataUnit: advertising.ServiceData = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000001234',
  serviceData:serviceValueBuffer.buffer
};
let advData: advertising.AdvertisingData = {
  serviceUuids:['37bea880-fc70-11ea-b720-000000001234'],
  manufacturerData:[manufactureDataUnit],
  serviceData:[serviceDataUnit]
};
let advertisingParams: advertising.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData
};
```

### Code block 4

```
let advId = -1;
try {
  advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
    advId = advertisingId;
    console.info('advertising id:' + JSON.stringify(advId));
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 5

```
try {
  advertising.stopAdvertising(advId).then(() => {
      console.info('stop advertising success');
    }).catch ((err: BusinessError) => {
      console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
    });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 6

```
try {
  advertising.off('advertisingStateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
