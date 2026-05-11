# 代码签名信息查询场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-arkts_

签名信息包括：应用ID、签发组织证书链、签名摘要、签名时间戳、签名使用的Hash算法。通过acquireCodeSign接口，应用可以获取代码签名信息，辅助应用判断运行代码的完整性和安全性，从而有效防止恶意软件的运行，提升设备安全防护能力。

约束和限制
当前能力仅支持2in1设备。
调用acquireCodeSign接口的应用程序需要具备读取目标代码签名文件的权限。
业务流程

流程说明：

用户在hap应用上调用文件代码签名信息查询接口acquireCodeSign。

acquireCodeSign接口同步返回应用所传入的文件对应的代码签名信息。

接口说明

接口如下表，更多接口及使用方法请参见API参考。

接口名	描述
acquireCodeSign(path: string): string	获取输入的文件路径的代码签名信息。
开发步骤
说明

在开发准备过程中，需要申请权限：ohos.permission.QUERY_AUDIT_EVENT，只允许清单内的企业类应用申请该权限，申请方式请参考：申请使用企业类应用可用权限。

导入Device Security Kit模块及相关公共模块。

import { securityAudit } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

开发者调用acquireCodeSign接口，获取所传入的文件对应的代码签名信息。

const TAG = "SecurityAuditJsTest";
let path = 'test';
try {
  hilog.info(0x0000, TAG, 'acquireCodeSign begin.');
  const result = securityAudit.acquireCodeSign(path);
  hilog.info(0x0000, TAG, 'Succeeded in queryCodeSign.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'acquireCodeSign failed: %{public}d %{public}s', e.code, e.message);
}
进程信息查询场景
多客户端订阅场景（C/C++）
