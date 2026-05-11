# 关闭指定生物类型认证能力

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-del-bio_

本功能在API 24之前版本仅支持Phone；API24及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口checkConfirmUITextFormat查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。
本功能需应用服务器端完成接口接入，以配合端云协同认证流程。
业务流程

接口说明

接口及使用方法请参见API参考。

接口名	描述
disableTrustedBioAuthentication(authID: bigint, authType: AuthType): Promise<void>	解绑指定生物类型认证能力
开发步骤

导入trustedAuthentication 和相关依赖模块。

import { trustedAuthentication} from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起解绑指定生物类型认证能力请求。

发起关闭指定生物类型认证能力请求前，需从服务器获取当前账号在设置数字盾密码时获取的authID。

调用数字盾解绑指定生物类型认证能力接口发起关闭对应生物类型认证能力申请。

const TAG = "TrustedAuthenticationJsTest";
try {
 const authID: bigint = 1687413472599354502n;//实际填充为从服务器获取到的账号对应的authID值
 const authType = trustedAuthentication.AuthType.AUTH_TYPE_FACE; //实际填充为计划解绑的生物特征类型
 const remainTimes = await trustedAuthentication.disableTrustedBioAuthentication(authID, authType);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'disableTrustedBioAuthentication: %{public}d %{public}s', e.code, e.message);
}

在接收到端侧解绑成功结果后，开发者需要同步将服务器绑定的生物特征信息解绑。

生物特征认证交易
数字盾签名密钥备份与恢复
