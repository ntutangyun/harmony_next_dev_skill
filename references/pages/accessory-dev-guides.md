# 配件接入开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessory-dev-guides_

本文档旨在帮助开发者为华为分享生态合作设备及其生态应用提供关联唤醒、系统服务关联、按需调度和安全授信管理等能力。

场景介绍

Accessory Kit助力华为分享生态合作设备实现更高级的体验。例如：结合Accessory Kit与Share Kit，可实现无感回传功能。

约束与限制

通信能力依赖

本功能需调用以下通信能力与配件进行交互：

蓝牙低功耗（BLE）广播

蓝牙低功耗（BLE）连接

Wi-Fi连接

权限申请说明

需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放，仅支持部分生态合作企业应用接入。权限申请方式请参考申请使用受限权限。

接口说明

具体API说明详见接口文档。

接口名	功能描述
showAccessPicker(items: Array<PickerItemInfo>, callback: Callback<AccessEventInfo>): number	接入配件设备信息及其关联的服务信息。
modifyDisplayName(accessoryId: string, displayName: string): number	重命名配件，用于修改配件设备的展示名称。
queryAttachedService(): Array<AttachServiceInfo>	查询已经关联的配件和服务信息。
detachService(attachId: number, callback: Callback<DetachServiceEvent>): number	移除某个已关联的配件或配件关联的服务信息。
registerConnectListener(attachId: number, stateCallback: Callback<ChannelEventInfo>): number	注册一个连接事件监听器。
unregisterConnectListener(attachId: number): number	取消注册连接事件监听器。
connect(connectRequestInfo: ConnectRequestInfo): number	建立与配件的连接。
disconnect(attachId: number): number	断开与配件的连接。

接入配件

[h2]导入模块

import { accessoryAccessManager } from '@kit.AccessoryKit';
import { image } from '@kit.ImageKit';

[h2]配件接入

配置briefDesc对象以指定被唤醒应用的简要描述信息。

let briefDesc: accessoryAccessManager.StringResourceInfo = {
  'bundleName': 'com.huawei.accessoryDemo',
  'moduleName': 'EntryAbility',
  'stringResourceId': $r('app.string.EntryAbility_desc').id // 被唤醒应用的简要描述字串的资源Id
}

定义唤醒方式的类型和被唤醒应用的信息。

let wakeupInfo: accessoryAccessManager.WakeupInfo = {
  'wakeupType': accessoryAccessManager.WakeupType.START_ABILITY_BY_CALL, // 唤醒应用的方式
  'bundleName': 'com.huawei.accessoryDemo', // 被唤醒的包名
  'abilityName': 'EntryAbility', // 被唤醒的能力名称
  'briefDesc': briefDesc // 被唤醒应用的简要描述
}

定义关联的服务类型和对应的服务参数。

let serviceInfo: Array<accessoryAccessManager.ServiceInfo> = [
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_APP_ACCESSORY_COLLABORATION, // 关联的服务类型
    parameters: {
      serviceName: wakeupInfo
    }
  }
];

定义配件的信息及配件关联的服务。

// 此处创建了一张空图，开发时可自行换成所需图片
const color: ArrayBuffer = new ArrayBuffer(96);
let bufferArr: Uint8Array = new Uint8Array(color);
for (let i = 0; i < bufferArr.length; i++) {
  bufferArr[i] = 0x80;
}
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.BGRA_8888,
  size: { height: 4, width: 6 },
  alphaType: image.AlphaType.UNPREMUL
}
let pixelMap: image.PixelMap | undefined = undefined;
image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
  pixelMap = srcPixelMap;
}).catch((err: BusinessError) => {
  // 异常处理
});

let items: Array<accessoryAccessManager.PickerItemInfo> = [
  {
    discoveryType: accessoryAccessManager.DiscoveryType.PARTNER_BLE_CONNECT, // 发现方式
    hasScreen: true, // 设备是否有屏幕
    bleAddress: 'XXX.XXX.XXX.XXX', // 设备的ble地址
    bleMtuSize: 1,// 最大传输单元（MTU）大小
    productId: 'productId1',// 产品编号
    subProductId: 'subProductId',// 子产品编号
    displayName: '有屏设备',// 设备展示名称
    displayImage: pixelMap, // 设备展示图片
    requestAttachServiceInfo: serviceInfo // 关联的服务信息
  }
];

通过前4步构建好的PickerItemInfo对象，明确拉起的目标配件设备以及关联的服务信息，通过调用showAccessPicker接口来接入配件设备和关联服务。当配件接入状态发生改变时，会通过callback回调函数通知应用。

let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.showAccessPicker(items, (event: accessoryAccessManager.AccessEventInfo) => {
  if (!event) {
    return;
  }
});

[h2]重命名配件

重命名配件，通过modifyDisplayName接口修改配件设备的展示名称。

let accessoryId = 'accessoryIdTest';
let deviceName = 'deviceNameTest';
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.modifyDisplayName(accessoryId, deviceName);

[h2]查询已经关联的配件和服务信息

使用queryAttachedService接口查询已经关联的配件和服务信息。

let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let resultArr: Array<accessoryAccessManager.AttachServiceInfo> = accessoryManager.queryAttachedService();

[h2]移除已关联的配件或配件关联的服务信息

使用detachService接口移除某个已关联的配件或配件关联的服务信息。

let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let attachId = 1;
let result: number = accessoryManager.detachService(attachId, (event: accessoryAccessManager.DetachServiceEvent) => {
  if (!event) {
    return;
  }
});

连接配件

[h2]导入模块

import { accessoryAccessManager } from '@kit.AccessoryKit';

[h2]注册配件连接状态监听器

使用registerConnectListener接口注册连接状态监听器，当配件设备连接状态发生变化时会通过回调函数通知应用。

let attachId = 0;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number =
  connectManager.registerConnectListener(attachId, (event: accessoryAccessManager.ChannelEventInfo) => {
    if (!event) {
      return;
    }
  });

[h2]取消配件连接状态监听器

使用unregisterConnectListener接口取消连接状态监听器。

let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.unregisterConnectListener(attachId);

[h2]主动连接配件

使用connect接口主动建立与配件的连接，通过registerConnectListener接口注册的回调来通知配件的连接状态。

let connectAttachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let shareDesc: accessoryAccessManager.StringResourceInfo = {
  bundleName: "com.huawei.accessoryDemo",
  moduleName: "EntryAbility",
  stringResourceId: $r('app.string.EntryAbility_desc').id // 服务简要描述信息字串的资源Id
};
let info: accessoryAccessManager.ConnectRequestInfo = {
    attachId: connectAttachId,
    channelType: accessoryAccessManager.ChannelType.PARTNER_WIFI_CHANNEL,// 连接通道类型
    serviceDesc: shareDesc // 服务简要描述信息
  };
let result: number = connectManager.connect(info);

[h2]断开与配件的连接

使用disconnect接口断开与配件的连接，通过registerConnectListener接口注册的回调来通知配件的断连状态。

let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.disconnect(attachId);

## Code blocks

### Code block 1

```
import { accessoryAccessManager } from '@kit.AccessoryKit';
import { image } from '@kit.ImageKit';
```

### Code block 2

```
let briefDesc: accessoryAccessManager.StringResourceInfo = {
  'bundleName': 'com.huawei.accessoryDemo',
  'moduleName': 'EntryAbility',
  'stringResourceId': $r('app.string.EntryAbility_desc').id // 被唤醒应用的简要描述字串的资源Id
}
```

### Code block 3

```
let wakeupInfo: accessoryAccessManager.WakeupInfo = {
  'wakeupType': accessoryAccessManager.WakeupType.START_ABILITY_BY_CALL, // 唤醒应用的方式
  'bundleName': 'com.huawei.accessoryDemo', // 被唤醒的包名
  'abilityName': 'EntryAbility', // 被唤醒的能力名称
  'briefDesc': briefDesc // 被唤醒应用的简要描述
}
```

### Code block 4

```
let serviceInfo: Array<accessoryAccessManager.ServiceInfo> = [
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_APP_ACCESSORY_COLLABORATION, // 关联的服务类型
    parameters: {
      serviceName: wakeupInfo
    }
  }
];
```

### Code block 5

```
// 此处创建了一张空图，开发时可自行换成所需图片
const color: ArrayBuffer = new ArrayBuffer(96);
let bufferArr: Uint8Array = new Uint8Array(color);
for (let i = 0; i < bufferArr.length; i++) {
  bufferArr[i] = 0x80;
}
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: image.PixelMapFormat.BGRA_8888,
  size: { height: 4, width: 6 },
  alphaType: image.AlphaType.UNPREMUL
}
let pixelMap: image.PixelMap | undefined = undefined;
image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
  pixelMap = srcPixelMap;
}).catch((err: BusinessError) => {
  // 异常处理
});

let items: Array<accessoryAccessManager.PickerItemInfo> = [
  {
    discoveryType: accessoryAccessManager.DiscoveryType.PARTNER_BLE_CONNECT, // 发现方式
    hasScreen: true, // 设备是否有屏幕
    bleAddress: 'XXX.XXX.XXX.XXX', // 设备的ble地址
    bleMtuSize: 1,// 最大传输单元（MTU）大小
    productId: 'productId1',// 产品编号
    subProductId: 'subProductId',// 子产品编号
    displayName: '有屏设备',// 设备展示名称
    displayImage: pixelMap, // 设备展示图片
    requestAttachServiceInfo: serviceInfo // 关联的服务信息
  }
];
```

### Code block 6

```
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.showAccessPicker(items, (event: accessoryAccessManager.AccessEventInfo) => {
  if (!event) {
    return;
  }
});
```

### Code block 7

```
let accessoryId = 'accessoryIdTest';
let deviceName = 'deviceNameTest';
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let result: number = accessoryManager.modifyDisplayName(accessoryId, deviceName);
```

### Code block 8

```
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let resultArr: Array<accessoryAccessManager.AttachServiceInfo> = accessoryManager.queryAttachedService();
```

### Code block 9

```
let accessoryManager: accessoryAccessManager.AccessManager = new accessoryAccessManager.AccessManager();
let attachId = 1;
let result: number = accessoryManager.detachService(attachId, (event: accessoryAccessManager.DetachServiceEvent) => {
  if (!event) {
    return;
  }
});
```

### Code block 10

```
import { accessoryAccessManager } from '@kit.AccessoryKit';
```

### Code block 11

```
let attachId = 0;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number =
  connectManager.registerConnectListener(attachId, (event: accessoryAccessManager.ChannelEventInfo) => {
    if (!event) {
      return;
    }
  });
```

### Code block 12

```
let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.unregisterConnectListener(attachId);
```

### Code block 13

```
let connectAttachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let shareDesc: accessoryAccessManager.StringResourceInfo = {
  bundleName: "com.huawei.accessoryDemo",
  moduleName: "EntryAbility",
  stringResourceId: $r('app.string.EntryAbility_desc').id // 服务简要描述信息字串的资源Id
};
let info: accessoryAccessManager.ConnectRequestInfo = {
    attachId: connectAttachId,
    channelType: accessoryAccessManager.ChannelType.PARTNER_WIFI_CHANNEL,// 连接通道类型
    serviceDesc: shareDesc // 服务简要描述信息
  };
let result: number = connectManager.connect(info);
```

### Code block 14

```
let attachId = 1;
let connectManager: accessoryAccessManager.ConnectManager = new accessoryAccessManager.ConnectManager();
let result: number = connectManager.disconnect(attachId);
```
