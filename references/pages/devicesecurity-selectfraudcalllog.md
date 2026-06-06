# 获取诈骗通话记录

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-selectfraudcalllog_

selectFraudCallLog(context: common.Context, options?: AntifraudCallLogOptions): Promise<AntifraudCallLogResult>	获取诈骗通话记录信息。
开发步骤
说明

在开发准备过程中，需要申请权限：ohos.permission.USE_FRAUD_CALL_LOG_PICKER。

只允许清单内的应用申请该权限，申请方式请参考：申请使用受限权限

开发者需向用户说明数据使用的目的、方式和范围。

导入Device Security Kit模块及相关公共模块。

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

调用selectFraudCallLog接口获取诈骗通话记录信息。

const TAG = "AntifraudPickerJsTest";


// 请求获取诈骗通话记录信息，并进行业务处理
let options: antifraudPicker.AntifraudCallLogOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudCallLog begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudCallLogResult = await antifraudPicker.selectFraudCallLog(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudCallLog failed: %{public}d %{public}s', e.code, e.message);
}
获取诈骗消息
获取诈骗应用
