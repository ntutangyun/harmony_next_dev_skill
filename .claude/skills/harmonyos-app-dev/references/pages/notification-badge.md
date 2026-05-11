# 管理通知角标

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-badge_

发布通知时，在NotificationRequest的badgeNumber字段里携带，桌面收到通知后，在原角标数上累加、呈现。

调用接口setBadgeNumber()设置，桌面按设置的角标数呈现。

减少角标数，目前仅支持通过setBadgeNumber()设置。

接口名	描述
setBadgeNumber(badgeNumber: number): Promise<void>	设置角标个数。
开发步骤

导入NotificationManager模块。

import { notificationManager } from '@kit.NotificationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';


const TAG: string = '[PublishOperation]';
const DOMAIN_NUMBER: number = 0xFF00;
ManageNotificationBadges.ets

增加角标个数。

发布通知时，可在NotificationRequest的badgeNumber字段里携带相关信息，具体可参考通知发布章节。

示例为调用setBadgeNumber接口增加角标，在发布完新的通知后，调用该接口。

let badgeNumber: number = 9;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN_NUMBER, TAG,
    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
ManageNotificationBadges.ets

减少角标个数。

一条通知被查看后，应用需要调用接口设置剩下未读通知个数，桌面刷新角标。

let badgeNumber: number = 8;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  hilog.info(DOMAIN_NUMBER, TAG, `Succeeded in setting badge number.`);
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN_NUMBER, TAG,
    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
ManageNotificationBadges.ets
常见问题

由于setBadgeNumber为异步接口，使用setBadgeNumber连续设置角标时，为了确保执行顺序符合预期，需要确保上一次设置完成后才能进行下一次设置。

反例

每次接口调用是相互独立的、没有依赖关系的，实际执行时无法保证调用顺序。

示例如下：

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN_NUMBER, TAG,
    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
badgeNumber = 11;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN_NUMBER, TAG,
    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
ManageNotificationBadges.ets

正例

多次接口调用存在依赖关系，确保上一次设置完成后才能进行下一次设置。

示例如下：

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 10 success.`);
  badgeNumber = 11;
  notificationManager.setBadgeNumber(badgeNumber).then(() => {
    hilog.info(DOMAIN_NUMBER, TAG, `setBadgeNumber 11 success.`);
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN_NUMBER, TAG,
      `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN_NUMBER, TAG,
    `Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
ManageNotificationBadges.ets
请求通知授权
管理通知渠道
