# 取消通知

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-cancel_

通知取消接口如下。接口详情参见@ohos.notificationManager (NotificationManager模块)。

接口名	描述
cancel(id: number, callback: AsyncCallback<void>): void	取消指定的通知。
cancelAll(callback: AsyncCallback<void>): void	取消所有该应用发布的通知。
开发步骤

本文以取消文本类型通知为例进行说明，其他类型通知取消操作与此类似。

导入模块。

import { notificationManager } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;
CancelNotification.ets

发布通知。

参考发布文本类型通知。

取消通知。

// 当拉起应用到前台，查看消息后，调用该接口取消通知。
notificationManager.cancel(1, (err: BusinessError) => {
  if (err) {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in canceling notification.');
});
CancelNotification.ets
更新通知
跨设备协同通知
