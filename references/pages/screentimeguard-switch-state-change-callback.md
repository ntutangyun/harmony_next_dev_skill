# 健康使用设备授权列表页中应用授权开关打开/关闭时触发回调

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-switch-state-change-callback_

场景介绍

当用户通过健康使用设备的授权列表页开启或关闭应用的授权开关时，系统会执行TimeGuardExtensionAbility中的回调方法，以此支持管控应用感知用户授权状态的变化。

说明

健康使用设备授权列表页（访问入口为：设置-健康使用设备-右上角四点设置-可访问健康使用设备的应用），用于统一管理所有管控应用的用户授权。

若用户已设置健康使用设备的密码，则在此页面取消应用授权时需要输入相应的密码。

管控应用调用Screen Time Guard Kit接口获取授权或者取消授权时，不会触发onUserAuthSwitchOn/onUserAuthSwitchOff回调方法。只有在健康使用设备授权列表页操作授权开关时才会触发。

业务流程

流程说明（以关闭授权开关为例）：

应用继承TimeGuardExtensionAbility，实现onUserAuthSwitchOn、onUserAuthSwitchOff方法，以监听用户授权状态。

用户在健康使用设备的授权列表页中关闭授权开关后会拉起extension进程，执行TimeGuardExtensionAbility的onUserAuthSwitchOff回调。

onUserAuthSwitchOff回调执行，应用可以在该回调中可以执行特定逻辑。

接口说明

授权开关打开/关闭时的回调关键接口如下表所示：

接口名	描述
onUserAuthSwitchOn(): Promise<void>	当用户授予授权时执行特定逻辑。
onUserAuthSwitchOff(): Promise<void>	当用户撤销授权时执行特定逻辑。

说明

TimeGuardExtensionAbility与应用运行在不同进程，但共用沙箱。

TimeGuardExtensionAbility与应用直接无法直接传递数据，如需传递数据可以通过用户首选项/数据库等数据持久化手段进行传递，或者通过公共事件模块传递。

开发步骤

导入相关模块。

import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

继承TimeGuardExtensionAbility，重写onUserAuthSwitchOn和onUserAuthSwitchOff回调。

export default class TimeGuardExtAbility extends TimeGuardExtensionAbility {
  // ...

  async onUserAuthSwitchOn(): Promise<void> {
    hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOn');
  }

  async onUserAuthSwitchOff(): Promise<void> {
    hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOff');
  }
}

在工程中entry模块的module.json5文件中的"extensionAbilities"节点添加如下代码。

"extensionAbilities": [
  {
    "name": "TimeGuardExtAbility",
    "type": "screenTimeGuard",
    "srcEntry": "./ets/timeguardextability/TimeGuardExtAbility.ets",
    "exported": false,
    "skills": [
      {
        "actions": [
          "action.ohos.timeGuard.listener"
        ]
      }
    ],
  }
],

## Code blocks

### Code block 1

```
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
export default class TimeGuardExtAbility extends TimeGuardExtensionAbility {
  // ...

  async onUserAuthSwitchOn(): Promise<void> {
    hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOn');
  }

  async onUserAuthSwitchOff(): Promise<void> {
    hilog.info(0x0000, 'TimeGuardExtensionAbility', 'onUserAuthSwitchOff');
  }
}
```

### Code block 3

```
"extensionAbilities": [
  {
    "name": "TimeGuardExtAbility",
    "type": "screenTimeGuard",
    "srcEntry": "./ets/timeguardextability/TimeGuardExtAbility.ets",
    "exported": false,
    "skills": [
      {
        "actions": [
          "action.ohos.timeGuard.listener"
        ]
      }
    ],
  }
],
```
