# 配件接入开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/accessory-dev-guides_

本文档旨在帮助开发者为华为生态合作设备及其生态应用提供关联唤醒、系统服务关联、按需调度和安全授信管理等能力。

场景介绍

Accessory Kit助力华为生态合作设备实现更高级的体验。例如：结合Accessory Kit与Share Kit，可实现无感回传功能。

约束与限制

通信能力依赖

本功能需调用以下通信能力与配件进行交互：

蓝牙低功耗（BLE）广播

蓝牙低功耗（BLE）连接

Wi-Fi连接

权限申请说明

需申请权限ohos.permission.ALLOW_ACCESSORY_ACCESS，该能力受限开放，仅对华为生态合作的配件设备厂商App开放。配件设备厂商需和华为完成生态合作协商，并通过测试验证准入后，才允许应用申请此权限。权限申请方式请参考申请受限权限。

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
      'serviceName': wakeupInfo,
      // base64编码的配件设备的引导操作图，无屏配件设备需要配置，用于跟配件设备配对时，引导用户在配件设备上做挂载的确认。
      'pressKeyGuideImage': '',
      // 无屏配件设备挂载时，需要配件设备确认操作时，手机侧的提示语。
      'pressKeyGuideBriefDesc': '请靠近设备，在设备上按键确认',
      // base64编码的配件设备的小尺寸图片，用于发现多个设备时，做列表展示。
      'displayLittleImage': '',
      // 0代表半托管模式，系统只弹窗确认是否与配件设备互联协同，已经接入的配件设备关联关系在有效期内（365天）重新连接时不会再需要弹窗确认。
      // 1代表全托管模式，系统会通过半模态弹窗接入配件设备，配件设备每次接入时都需要走全流程进行关联。
      'showPickerDialogStyle': 0
    }
  },
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_SHARE_SERVICE, // 关联的服务类型
    parameters: {
      'bundleName': 'com.huawei.accessoryDemo'
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
    bleMtuSize: 1,// BLE最大传输单元（MTU）大小
    productId: 'productId1',// 产品编号
    subProductId: 'subProductId',// 子产品编号
    displayName: '有屏设备',// 设备展示名称
    displayImage: pixelMap, // 设备展示图片
    requestAttachServiceInfo: serviceInfo // 关联的服务信息
  }
];

通过前4步构建好的PickerItemInfo对象，明确拉起的目标配件设备以及关联的服务信息，通过调用showAccessPicker接口来接入配件设备和关联服务。当配件接入状态发生改变时，会通过callback回调函数通知应用。

请注意：调用showAccessPicker接口前，配件设备需要处于BLE可连接状态（配件的BLE广播处于广播态或者配件BLE已连接）。

调用showAccessPicker接口后，会弹出关联弹窗，根据使用者的选择，会通过接口回调当前状态，开发时可根据业务具体情况处理所关注的事件，具体可能出现的情况请详见：showAccessPicker接口事件回调数据结构说明。

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

配件设备主动唤醒应用页面代码示例

当配件首次接入成功后，后续配件再次主动连接主机设备时，需要拉起配件所关联的应用页面。具体开发步骤如下：

配置应用页面的启动模式：在module.json5中，配置拉起页面的相关信息。注意：请将launchType配置为单实例"singleton"。配置标签示例如下：

  "abilities":[
    {
      "name": "CalleeAbility",  // 这里用户可以自定义名称
      "srcEntry": "./ets/xxx/CalleeAbility.ets", // 这里需要填写实际路径
      "launchType": "singleton", // Ability的启动模式，设置为"singleton"类型。
      // 以下内容需要填写项目实际信息
      "description": "$string:EntryAbility_desc",
      "icon": "$media:layered_image",
      "label": "$string:EntryAbility_label",
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start_window_background",
      "exported": true,
    }
  ]

导入UIAbility模块。

import { UIAbility } from '@kit.AbilityKit';

实现唤醒的监听及解除监听。如下示例：

onCreate中调用Callee.on注册唤醒的监听，其中method参数固定为"AccessoryKitWakeup"，并在收到序列化数据后作相应处理；

onDestroy中调用Callee.off取消监听，其中method参数同样固定为"AccessoryKitWakeup"。开发者需根据实际业务做相应处理。

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

const DOMAIN = 0x0000;

const BACKGROUND_TASK_TAG = 'access_service_background_app';

class MyMessageAble implements rpc.Parcelable {
  attachId: number = 0; // attachId值
  custData: string = ''; // custData值

  constructor(attachId: number, custData: string) {
    this.attachId = attachId;
    this.custData = custData;
  }

  // 数据的序列化方法
  marshalling(messageSequence: rpc.MessageSequence) {
    let name: string = '';
    messageSequence.writeString(name);
    messageSequence.writeInt(this.attachId);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble marshalling name[${name}]`);
    messageSequence.writeString(name);
    messageSequence.writeString(this.custData);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble marshalling name[${name}]`);
    return true;
  }

  // 数据的反序列化方法
  unmarshalling(messageSequence: rpc.MessageSequence) {
    let name: string = messageSequence.readString();
    this.attachId = messageSequence.readInt(); // attachId值
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble unmarshalling name[${name}]`);
    name = messageSequence.readString();
    this.custData = messageSequence.readString(); // custData值
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble unmarshalling name[${name}]`);
    return true;
  }
}

// 指定数据接收的回调函数
function funcCallBack(pdata: rpc.MessageSequence): MyMessageAble {
  hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `Callee funcCallBack is called ${pdata}`);
  let msg = new MyMessageAble(0, '');
  pdata.readParcelable(msg);
  hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `Callee funcCallBack custData[${msg.custData}]`);
  return new MyMessageAble(msg.attachId, 'Callee Response');
}

let method = 'AccessoryKitWakeup';

export default class BackgroundAbility extends UIAbility {
  id: number = 0;
  // 保存通知id
  attachId: number = 0;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG,
      `onCreate, custData: ${want.parameters?.custData}, callerId: ${want.parameters?.callerId}`);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG,
      `onCreate, custData: ${JSON.stringify(want)}, launchParam: ${JSON.stringify(launchParam)}`);
    let parameters = want.parameters;
    if (!parameters) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG, `${JSON.stringify(parameters)}`);
      return;
    }
    let attachIdObj = parameters['attachId'];
    if (!attachIdObj) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'attachId undefined');
      return;
    }
    let attachId = attachIdObj as number;
    this.attachId = attachId;
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'end');
    try {
      // 通过on接口注册监听系统唤醒信息。
      this.callee.on(method, funcCallBack);
    } catch (error) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG,
        `Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onDestroy');
    // 通过off接口取消注册监听系统唤醒信息。
    this.callee.off(method);
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'onDestroy stopBackgroundRunning succeeded');
      // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知。
    });
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/BackgroundIndex', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, BACKGROUND_TASK_TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onWindowStageDestroy');
    this.callee.off(method);
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'onWindowStageDestroy stopBackgroundRunning succeeded');
      // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知。
    });
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onBackground');
  }
}

showAccessPicker接口事件回调数据结构说明

下图梳理了正常流程和异常流程的情况，其中绿色实线为正常流程，红色虚线为异常流程；accessEvent参考accessoryAccessManager (配件接入管理)中相关说明。

showAccessPicker回调的accessEvent为0时，代表弹窗弹出，数据结构如下：

{
  "accessEvent": 0,
  "errorCode": 0,
  "errorDesc": "dialog succ"
}

showAccessPicker回调的accessEvent为1时，代表弹窗关闭，数据结构如下：

{
  "accessEvent": 1,
  "errorCode": 0,
  "errorDesc": "dialog close"
}

showAccessPicker回调的accessEvent为2时，代表接入完成，数据结构如下：

{
  "accessEvent": 2,
  "errorCode": 0,
  "errorDesc": "succ end"
}

showAccessPicker回调的accessEvent为3时，errorCode为10000代表用户主动取消接入，数据结构如下：

{
  "accessEvent": 3,
  "errorCode": 10000,
  "errorDesc": "user confirm cancel"
}

showAccessPicker回调的accessEvent为3时，errorCode为10002代表鉴权失败，需检查productId是否正确。数据结构如下：

{
  "accessEvent": 3,
  "errorCode": 10002,
  "errorDesc": "check hilink error"
}

showAccessPicker回调的accessEvent为3时，errorCode为10004代表创建session失败，数据结构如下：

{
  "accessEvent": 3,
  "errorCode": 10004,
  "errorDesc": "open session failed"
}

showAccessPicker回调的accessEvent为3时，errorCode为10006代表关联失败，数据结构如下：

{
  "accessEvent": 3,
  "errorCode": 10006,
  "errorDesc": "attach failed"
}

showAccessPicker回调的accessEvent为300时，代表开始关联服务，数据结构如下：

{
  "accessEvent": 300,
  "errorCode": 0,
  "errorDesc": "start attaching"
}

showAccessPicker回调的accessEvent为301时，代表关联服务完成，当前实例为关联P_ShareService服务的回调数据，数据结构如下：

{
  "accessEvent": 301,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_ShareService",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach succ"
}

showAccessPicker回调的accessEvent为301时，代表关联服务完成，当前实例为关联三方服务完成，数据结构如下：

{
  "accessEvent": 301,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_AppAccessoryCollaboration",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach succ"
}

showAccessPicker回调的accessEvent为302时，serviceName为P_ShareService，代表关联P_ShareService服务异常。数据结构如下：

{
  "accessEvent": 302,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "xxxx"
    },
    "serviceInfo": {
      "serviceName": "P_ShareService",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach failed"
}

showAccessPicker回调的accessEvent为302时，serviceName为P_AppAccessoryCollaboration，代表关联P_AppAccessoryCollaboration服务异常。数据结构如下：

{
  "accessEvent": 302,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_AppAccessoryCollaboration",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach failed"
}

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
      'serviceName': wakeupInfo,
      // base64编码的配件设备的引导操作图，无屏配件设备需要配置，用于跟配件设备配对时，引导用户在配件设备上做挂载的确认。
      'pressKeyGuideImage': '',
      // 无屏配件设备挂载时，需要配件设备确认操作时，手机侧的提示语。
      'pressKeyGuideBriefDesc': '请靠近设备，在设备上按键确认',
      // base64编码的配件设备的小尺寸图片，用于发现多个设备时，做列表展示。
      'displayLittleImage': '',
      // 0代表半托管模式，系统只弹窗确认是否与配件设备互联协同，已经接入的配件设备关联关系在有效期内（365天）重新连接时不会再需要弹窗确认。
      // 1代表全托管模式，系统会通过半模态弹窗接入配件设备，配件设备每次接入时都需要走全流程进行关联。
      'showPickerDialogStyle': 0
    }
  },
  {
    serviceName: accessoryAccessManager.ServiceName.PARTNER_SHARE_SERVICE, // 关联的服务类型
    parameters: {
      'bundleName': 'com.huawei.accessoryDemo'
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
    bleMtuSize: 1,// BLE最大传输单元（MTU）大小
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

### Code block 15

```
  "abilities":[
    {
      "name": "CalleeAbility",  // 这里用户可以自定义名称
      "srcEntry": "./ets/xxx/CalleeAbility.ets", // 这里需要填写实际路径
      "launchType": "singleton", // Ability的启动模式，设置为"singleton"类型。
      // 以下内容需要填写项目实际信息
      "description": "$string:EntryAbility_desc",
      "icon": "$media:layered_image",
      "label": "$string:EntryAbility_label",
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start_window_background",
      "exported": true,
    }
  ]
```

### Code block 16

```
import { UIAbility } from '@kit.AbilityKit';
```

### Code block 17

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { rpc } from '@kit.IPCKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

const DOMAIN = 0x0000;

const BACKGROUND_TASK_TAG = 'access_service_background_app';

class MyMessageAble implements rpc.Parcelable {
  attachId: number = 0; // attachId值
  custData: string = ''; // custData值

  constructor(attachId: number, custData: string) {
    this.attachId = attachId;
    this.custData = custData;
  }

  // 数据的序列化方法
  marshalling(messageSequence: rpc.MessageSequence) {
    let name: string = '';
    messageSequence.writeString(name);
    messageSequence.writeInt(this.attachId);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble marshalling name[${name}]`);
    messageSequence.writeString(name);
    messageSequence.writeString(this.custData);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble marshalling name[${name}]`);
    return true;
  }

  // 数据的反序列化方法
  unmarshalling(messageSequence: rpc.MessageSequence) {
    let name: string = messageSequence.readString();
    this.attachId = messageSequence.readInt(); // attachId值
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble unmarshalling name[${name}]`);
    name = messageSequence.readString();
    this.custData = messageSequence.readString(); // custData值
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `MyMessageAble unmarshalling name[${name}]`);
    return true;
  }
}

// 指定数据接收的回调函数
function funcCallBack(pdata: rpc.MessageSequence): MyMessageAble {
  hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `Callee funcCallBack is called ${pdata}`);
  let msg = new MyMessageAble(0, '');
  pdata.readParcelable(msg);
  hilog.info(DOMAIN, BACKGROUND_TASK_TAG, `Callee funcCallBack custData[${msg.custData}]`);
  return new MyMessageAble(msg.attachId, 'Callee Response');
}

let method = 'AccessoryKitWakeup';

export default class BackgroundAbility extends UIAbility {
  id: number = 0;
  // 保存通知id
  attachId: number = 0;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG,
      `onCreate, custData: ${want.parameters?.custData}, callerId: ${want.parameters?.callerId}`);
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG,
      `onCreate, custData: ${JSON.stringify(want)}, launchParam: ${JSON.stringify(launchParam)}`);
    let parameters = want.parameters;
    if (!parameters) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG, `${JSON.stringify(parameters)}`);
      return;
    }
    let attachIdObj = parameters['attachId'];
    if (!attachIdObj) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'attachId undefined');
      return;
    }
    let attachId = attachIdObj as number;
    this.attachId = attachId;
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'end');
    try {
      // 通过on接口注册监听系统唤醒信息。
      this.callee.on(method, funcCallBack);
    } catch (error) {
      hilog.error(DOMAIN, BACKGROUND_TASK_TAG,
        `Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onDestroy');
    // 通过off接口取消注册监听系统唤醒信息。
    this.callee.off(method);
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'onDestroy stopBackgroundRunning succeeded');
      // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知。
    });
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/BackgroundIndex', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, BACKGROUND_TASK_TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onWindowStageDestroy');
    this.callee.off(method);
    backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
      hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'onWindowStageDestroy stopBackgroundRunning succeeded');
      // 对于上传下载类的长时任务，应用可以使用res中返回的notificationId来更新通知，比如发送带进度条的模板通知。
    });
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, BACKGROUND_TASK_TAG, '%{public}s', 'Ability onBackground');
  }
}
```

### Code block 18

```
{
  "accessEvent": 0,
  "errorCode": 0,
  "errorDesc": "dialog succ"
}
```

### Code block 19

```
{
  "accessEvent": 1,
  "errorCode": 0,
  "errorDesc": "dialog close"
}
```

### Code block 20

```
{
  "accessEvent": 2,
  "errorCode": 0,
  "errorDesc": "succ end"
}
```

### Code block 21

```
{
  "accessEvent": 3,
  "errorCode": 10000,
  "errorDesc": "user confirm cancel"
}
```

### Code block 22

```
{
  "accessEvent": 3,
  "errorCode": 10002,
  "errorDesc": "check hilink error"
}
```

### Code block 23

```
{
  "accessEvent": 3,
  "errorCode": 10004,
  "errorDesc": "open session failed"
}
```

### Code block 24

```
{
  "accessEvent": 3,
  "errorCode": 10006,
  "errorDesc": "attach failed"
}
```

### Code block 25

```
{
  "accessEvent": 300,
  "errorCode": 0,
  "errorDesc": "start attaching"
}
```

### Code block 26

```
{
  "accessEvent": 301,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_ShareService",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach succ"
}
```

### Code block 27

```
{
  "accessEvent": 301,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_AppAccessoryCollaboration",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach succ"
}
```

### Code block 28

```
{
  "accessEvent": 302,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "xxxx"
    },
    "serviceInfo": {
      "serviceName": "P_ShareService",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach failed"
}
```

### Code block 29

```
{
  "accessEvent": 302,
  "attachServiceInfo": {
    "attachId": 76,
    "accessoryInfo": {
      "accessoryId": "xxxxxxxxxxxxxxxx",
      "bleAddress": "XX:XX:XX:XX:XX:XX",
      "displayName": "XXXXX",
      "productId": "XXXXX"
    },
    "serviceInfo": {
      "serviceName": "P_AppAccessoryCollaboration",
      "parameters": {
        "wakeupInfo": {
          "abilityName": "BackgroundAbility",
          "briefDesc": {
            "bundleName": "com.xxx.xxx",
            "moduleName": "entry",
            "stringResourceId": 16777226
          },
          "bundleName": "com.xxx.xxx",
          "wakeupType": 0
        }
      }
    }
  },
  "errorCode": 0,
  "errorDesc": "attach failed"
}
```
