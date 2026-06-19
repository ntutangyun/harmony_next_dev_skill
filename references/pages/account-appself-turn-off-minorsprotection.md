# 关闭应用的未成年人模式（推荐）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-appself-turn-off-minorsprotection_

场景介绍

系统的未成年人模式已开启，用户打开应用，希望单独关闭应用的未成年人模式，系统的未成年人模式仍保持开启。

当用户需要关闭应用的未成年人模式时，应用可调用系统家长身份验证接口verifyMinorsProtectionCredential，验证通过后可关闭应用的未成年人模式。

说明

当前场景为关闭未成年人模式的推荐方案，相较于关闭系统的未成年人模式，单独关闭应用的未成年人模式更为灵活，且较符合用户体验预期。当前场景需要开发者在应用侧记录单独关闭状态（示例：userTurnOffFlag，记录用户是否主动关闭了应用的未成年人模式），便于后续与系统重新联动。如应用重新启动时：

当应用查询到userTurnOffFlag为True，应用需保持应用的未成年人模式为关闭状态。

当应用查询到userTurnOffFlag为False，应用需与系统进行联动。

建议开发者在选择这种接入方式的时候，在界面上告知用户，当前仅关闭应用的未成年人模式，但系统的未成年人模式仍保持开启，避免用户误解。

业务流程

流程说明：

用户打开应用时，应用通过订阅系统未成年人模式公共事件感知未成年人模式的状态变化。可以调用getMinorsProtectionInfoSync或getMinorsProtectionInfo获取系统未成年人模式信息。当查询到未成年人模式未开启，需要记录单独关闭的标记为false。

当系统未成年人模式已开启，且用户需要在应用内关闭未成年人模式时，应用可调用verifyMinorsProtectionCredential验证未成年人模式密码，当校验通过后，才可关闭当前应用的未成年人模式，同时记录单独关闭的标记为true。

接口说明

以下是关闭应用的未成年人模式相关接口说明，更多接口及使用方法请参见API参考。

接口名	描述
getMinorsProtectionInfoSync(): MinorsProtectionInfo	同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。
getMinorsProtectionInfo(): Promise<MinorsProtectionInfo>	异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。
verifyMinorsProtectionCredential(context: common.Context): Promise<boolean>	调用该方法拉起验证未成年人模式密码页面。

注意

verifyMinorsProtectionCredential接口需在页面或自定义组件生命周期内调用。接口调用前提是未成年人模式已开启，如果在未开启未成年人模式下调用此接口会返回错误码1009900002。

当未成年人模式开启时，当前设备的开发者调试模式会被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。

如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见hilog。

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

订阅系统未成年人模式开启或关闭事件、获取未成年人模式的开启状态，以及年龄段信息请参考应用与系统联动切换未成年人模式章节的开发步骤。当查询到未成年人模式已关闭或订阅系统未成年人模式关闭事件，需要记录单独关闭的标记为false。

当未成年人模式已开启，用户需要关闭应用的未成年人模式时调用verifyMinorsProtectionCredential方法拉起验证未成年人模式密码页面。验证成功后才可关闭，同时记录单独关闭的标记为true。

if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
  try {
    // 查询是否支持系统未成年人模式
    if (minorsProtection.supportMinorsMode()) {
      // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
      await minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
        .then((result: boolean) => {
          hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
          // 使用结果判断验密是否通过，执行后续流程，验证成功后，关闭应用的未成年人模式，同时记录单独关闭的标记为true，需要缓存该标记
          // ...
        })
        .catch((error: BusinessError<Object>) => {
          dealVerifyAllError(error);
          // ...
        });
      // ...
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
      // ...
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
    // ...
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
  // ...
}

function dealVerifyAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
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
      await minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
        .then((result: boolean) => {
          hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
          // 使用结果判断验密是否通过，执行后续流程，验证成功后，关闭应用的未成年人模式，同时记录单独关闭的标记为true，需要缓存该标记
          // ...
        })
        .catch((error: BusinessError<Object>) => {
          dealVerifyAllError(error);
          // ...
        });
      // ...
    } else {
      hilog.info(0x0000, 'testTag',
        'The current device environment does not support the youth mode, please check the current device environment.');
      // ...
    }
  } catch (error) {
    hilog.error(0x0000, 'testTag',
      `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
    // ...
  }
} else {
  hilog.info(0x0000, 'testTag',
    'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
  // ...
}
```

### Code block 3

```
function dealVerifyAllError(error: BusinessError<Object>): void {
  hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
}
```
