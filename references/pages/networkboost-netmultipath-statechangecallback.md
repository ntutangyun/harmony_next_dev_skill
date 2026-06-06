# 多网状态监听

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-statechangecallback_

on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void	订阅多网状态信息变化。
off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void	取消订阅多网状态信息变化。
开发步骤

导入Network Boost Kit模块。

import { netHandover } from '@kit.NetworkBoostKit';
import { BusinessError } from '@kit.BasicServicesKit';

通过订阅的方式监听多网状态变化信息。

try {
  netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
    // 回调信息处理
    console.info("on multiPathStateChange: " + JSON.stringify(data));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

当应用业务流程结束和应用退出时，取消订阅多网状态变化信息。

try {
  netHandover.off('multiPathStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
业务场景设置
多网建议监听
