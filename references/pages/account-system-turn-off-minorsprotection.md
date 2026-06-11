# 关闭系统的未成年人模式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-system-turn-off-minorsprotection_

场景介绍

系统的未成年人模式已开启。用户打开应用，在应用内关闭系统未成年人模式。

应用可调用系统的未成年人模式关闭接口leadToTurnOffMinorsMode，验证家长密码后关闭系统的未成年人模式。

说明

用户在应用内操作时，预期可能是关闭应用的未成年人模式，而非关闭整个系统的未成年人模式（其他应用/元服务的未成年人模式也会随之关闭）。如果开发者选择这种接入方式，建议在界面上告知用户即将关闭系统的未成年人模式。

业务流程

流程说明：

用户打开应用时，应用通过订阅系统未成年人模式公共事件感知未成年人模式的状态变化。可以调用getMinorsProtectionInfoSync或getMinorsProtectionInfo获取系统未成年人模式信息。

当系统未成年人模式已开启，且用户需要在应用内关闭未成年人模式时，应用可调用leadToTurnOffMinorsMode引导关闭系统未成年人模式流程，关闭整个系统的未成年人模式。

接口说明

以下是关闭系统的未成年人模式相关接口说明，更多接口及使用方法请参见API参考。

接口名	描述
getMinorsProtectionInfoSync(): MinorsProtectionInfo	同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。
getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>	异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。
leadToTurnOffMinorsMode(context: common.Context): Promise<void>	调用该方法进行关闭系统未成年人模式流程。

注意

leadToTurnOffMinorsMode接口需在页面或自定义组件生命周期内调用。

当未成年人模式开启时，当前设备的开发者调试模式会被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。

如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见hilog。

在应用内调用开启或关闭系统未成年人模式接口，如应用需弹出toast或弹框告知用户“未成年人模式已开启或关闭”，须在接口执行完成之后，在接口的then方法里面弹出toast或弹框，否则可能出现因系统页面未完全关闭，导致toast无法正常展示的情况。

如开发者需要频繁使用未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅系统未成年人模式公共事件来刷新未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。

当设备处于开机未解锁状态下，开发者调用getMinorsProtectionInfoSync接口时，其返回的minorsProtectionMode字段为false。

事件说明

以下是系统未成年人模式开启或关闭发送的广播事件。

事件名称	值	描述
COMMON_EVENT_MINORSMODE_ON	usual.event.MINORSMODE_ON	表示系统未成年人模式开启事件。
COMMON_EVENT_MINORSMODE_OFF	usual.event.MINORSMODE_OFF	表示系统未成年人模式关闭事件。

说明

未成年人模式开启事件触发时机：

主动开启系统未成年人模式（PC/2in1设备暂不支持从控制中心开启未成年人模式），当前设备会发送未成年人模式开启事件。

开发前提

请先参考“开发准备”的配置签名和指纹章节，通过自动签名方式完成签名信息的配置。请注意，该接口无需配置公钥指纹、Client ID，也无需申请账号权限。

开发步骤

导入minorsProtection模块及相关公共模块。

import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

订阅系统未成年人模式开启或关闭事件、获取未成年人模式的开启状态，以及年龄段信息请参考应用与系统联动切换未成年人模式章节的开发步骤。

当系统未成年人模式已开启，且用户主动关闭应用内未成年人模式时，应用需要调用leadToTurnOffMinorsMode引导用户关闭系统的未成年人模式。

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    // 查询是否支持系统未成年人模式
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
      minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // 接口调用完成，如需显示弹窗，请在此处处理
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOffAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
}

function dealTurnOffAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
}

## Code blocks

### Code block 1

```
import { minorsProtection } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    // 查询是否支持系统未成年人模式
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
      minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
        .then(() => {
          // 接口调用完成，如需显示弹窗，请在此处处理
        })
        .catch((error: BusinessError<Object>) => {
          dealTurnOffAllError(error);
        });
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
}
```

### Code block 3

```
function dealTurnOffAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
}
```
