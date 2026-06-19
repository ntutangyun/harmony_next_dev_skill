# 查询星闪开关状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-getstate_

场景介绍

使用星闪前需要在设置应用里手动打开星闪。可以通过主动查询或订阅通知方式获取星闪状态，星闪状态变化为STATE_ON时可以进行相应的业务流程。

接口说明

提供2种获取星闪开关状态的方式，主动查询和订阅状态变化。

接口名	描述
getState(): NearlinkState	主动查询星闪开关状态。
on(type: 'stateChange', callback: Callback<NearlinkState>): void	订阅星闪开关状态变化事件。使用callback异步回调。
off(type: 'stateChange', callback?: Callback<NearlinkState>): void	取消订阅星闪开关状态变化事件。使用callback异步回调。

开发步骤

说明

可以在设备“设置 > 多设备协同 > 星闪”（不同产品或系统版本可能为“设置 > 星闪和蓝牙 > 星闪”）路径下，打开或关闭星闪，触发开关状态的变化。

导入相关模块。

import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

发起星闪状态查询。

try {
  let state : manager.NearlinkState = manager.getState();
  console.info('state = ' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

或者通过注册的方式订阅星闪开关状态变化。

let onReceiveEvent:(data: manager.NearlinkState) => void = (data: manager.NearlinkState) => {
  console.info('nearlink state = ' + JSON.stringify(data));
};
try {
  manager.on('stateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

取消订阅星闪开关状态变化，其中onReceiveEvent是步骤3中定义的回调函数。

try {
  manager.off('stateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

## Code blocks

### Code block 1

```
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
try {
  let state : manager.NearlinkState = manager.getState();
  console.info('state = ' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 3

```
let onReceiveEvent:(data: manager.NearlinkState) => void = (data: manager.NearlinkState) => {
  console.info('nearlink state = ' + JSON.stringify(data));
};
try {
  manager.on('stateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 4

```
try {
  manager.off('stateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
