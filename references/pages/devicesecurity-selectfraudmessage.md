# 获取诈骗消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-selectfraudmessage_

selectFraudMessage(context: common.Context, options?: AntifraudMessageOptions): Promise<AntifraudMessageResult>	获取诈骗消息信息。
开发步骤
说明

在开发准备过程中，需要申请权限：ohos.permission.USE_FRAUD_MESSAGES_PICKER。

只允许清单内的应用申请该权限，申请方式请参考：申请使用受限权限

开发者需向用户说明数据使用的目的、方式和范围。

导入Device Security Kit模块及相关公共模块。

import { antifraudPicker} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common} from '@kit.AbilityKit';

调用selectFraudMessage接口获取诈骗消息信息。

const TAG = "AntifraudPickerJsTest";


// 请求获取诈骗消息信息，并进行业务处理
let options: antifraudPicker.AntifraudMessageOptions = {
  maxSelectNumber: 5
};
try {
  hilog.info(0x0000, TAG, 'SelectFraudMessage begin.');
  let context = this.getUIContext().getHostContext();
  const result: antifraudPicker.AntifraudMessageResult = await antifraudPicker.selectFraudMessage(context, options);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'SelectFraudMessage failed: %{public}d %{public}s', e.code, e.message);
}
反诈选择器
获取诈骗通话记录
