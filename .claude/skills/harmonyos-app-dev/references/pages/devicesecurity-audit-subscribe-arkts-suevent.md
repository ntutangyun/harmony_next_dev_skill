# 单客户端订阅场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-subscribe-arkts-suevent_

on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void	订阅安全审计数据
off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void	取消订阅安全审计数据
开发步骤
说明

在开发准备过程中，需要申请权限：ohos.permission.QUERY_AUDIT_EVENT。

只允许清单内的企业类应用申请该权限，申请方式请参考：申请使用企业类应用可用权限。

导入Device Security Kit模块及相关公共模块。

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

订阅安全审计事件。

const TAG = "SecurityAuditJsTest";
const callback = (event: securityAudit.AuditEvent) => {
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func eventId= ' + event.eventId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func version= ' + event.version);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func content= ' + event.content);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func timestamp= ' + event.timestamp);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func userId= ' + event.userId);
  hilog.info(0x0000, TAG, '%{public}s', 'Security_SecurityAudit_JsApi_Func deviceId= ' + event.deviceId);
};
let auditEventInfo: securityAudit.AuditEventInfo = {
   eventId: 0x810800800
};
 
try {
  hilog.info(0x0000, TAG, 'on begin.');
  securityAudit.on('auditEventOccur', auditEventInfo, callback);
  hilog.info(0x0000, TAG, 'Succeeded in on.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message);
}

取消订阅安全审计事件。

try {
  hilog.info(0x0000, TAG, 'off begin.');
  securityAudit.off('auditEventOccur', auditEventInfo, callback);
  hilog.info(0x0000, TAG, 'Succeeded in off.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message);
}
安全审计
多客户端订阅场景
