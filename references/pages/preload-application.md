# 应用预加载

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preload-application_

概述

从API version 20开始，提供应用预加载机制。该机制会根据用户的使用习惯，在系统资源充足时提前加载应用至特定阶段。当用户启动应用时，由于此前已完成了应用的部分加载，所需的启动时间会缩短，有助于提升用户体验和应用竞争力。

该机制尤其适用于因加载大量资源而启动耗时较长的应用，例如大型游戏应用和大型办公应用。

约束限制

仅支持entry模块的AbilityStage和UIAbility预加载。无论预加载到哪种阶段，entry模块必须配置入口UIAbility，详见开发步骤中步骤2。

应用配置预加载后，实际是否进行预加载以及具体的预加载时机，均由系统根据用户习惯等信息来综合决定。开发者无法对此进行干预。

运行机制

当系统资源充足时，系统将应用加载到特定阶段，提升启动速度。当前支持预加载到三种阶段。开发者可以根据应用冷启动各阶段耗时情况，选择其中的一种。

说明

在应用预加载过程中不会显示任何界面，因此在预加载的任何阶段不应包含与界面显示、界面交互或依赖用户可见的相关操作，同时应确保用户正式启动应用后，所有功能正常运行且体验不受影响。

processCreated：进程创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，但是不会触发任何生命周期回调。

abilityStageCreated：AbilityStage创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，随后触发entry模块AbilityStage的onCreate回调。

windowStageCreated：WindowStage创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，随后触发entry模块AbilityStage的onCreate回调。接着会拉起entry模块的入口UIAbility，并触发其onCreate回调和onWindowStageCreate回调。开发者可以在UIAbility的onCreate回调中，通过launchParam.launchReason的枚举值获取启动原因。枚举值为PRELOAD表示当前UIAbility是由预加载机制启动的。

应用预加载状态识别与判断

从API version 22开始，应用可以在启动过程中识别并判断当前进程的预加载状态。

当应用被预加载后，开发者可以在AbilityStage的onCreate生命周期回调中，通过调用application.getAppPreloadType()获取当前进程的预加载类型（返回值为AppPreloadType）。从而判断本次启动是否由预加载触发，并明确应用当前正处于哪一个预加载阶段。

说明

只有在进程首次执行AbilityStage的onCreate完成之前调用application.getAppPreloadType()接口，才可以返回真实的预加载类型。

AbilityStage创建完成后，应用的预加载数据将被清除，此时调用application.getAppPreloadType()将返回UNSPECIFIED，无法获取到真实的预加载类型。

import { AbilityStage, application } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    // 根据appPreloadType的值判断当前进程的预加载类型
    let appPreloadType = application.getAppPreloadType();
  }
}

除了在AbilityStage中判断进程级别的预加载类型外，若应用配置的预加载阶段为windowStageCreated，开发者还可以在UIAbility的onCreate生命周期回调中进行判断。通过校验launchParam.launchReason是否等于PRELOAD，即可识别当前UIAbility实例是否由预加载机制启动。具体实现请参考开发步骤中的步骤3。

应用声明支持预加载到abilityStageCreated阶段

从HarmonyOS 6.0.0开始，在Phone、Tablet和PC/2in1设备上，应用应尽量声明支持预加载到abilityStageCreated阶段。

应用需确保在预加载启动阶段（AbilityStage.onCreate）以及后续用户点击后的完整启动阶段（UIAbility.onCreate、UIAbility.onForeground）中，业务初始化逻辑均能正确执行。

不同设备类型预加载到windowStage阶段的生命周期差异

从HarmonyOS 6.0.0开始，PC/2in1设备上的应用支持预加载到windowStage阶段；从HarmonyOS 7.0.0开始，该能力进一步扩展至Phone和Tablet设备。

不同设备类型的应用在执行预加载启动时，生命周期触发状态存在差异，具体如下表所示。

表1 不同设备类型预加载到windowStage阶段的生命周期差异说明

应用选项	预加载生命周期
"deviceTypes": ["phone","tablet","2in1"]	加载至后台
"deviceTypes": ["phone","tablet"]	加载至后台
"deviceTypes": ["phone","2in1"]	加载至后台
"deviceTypes": ["phone"]	加载至后台
"deviceTypes": ["tablet"]	加载至后台
"deviceTypes": ["tablet","2in1"]	加载至前台初始
"deviceTypes": ["2in1"]	加载至前台初始

支持Phone或仅支持Tablet的应用：加载至后台

执行预加载启动时，系统会启动一个UIAbility至后台状态，依次触发UIAbility.onCreate()、UIAbility.onWindowStageCreate()、UIAbility.onBackground()生命周期回调（不会触发onForeground()），一小段时间后应用进程会被挂起。

用户点击应用启动到前台时，系统会依次触发UIAbility.onNewWant()、UIAbility.onForeground()生命周期回调，走完前台启动流程。

支持PC/2in1且不支持Phone的应用：加载至隐藏窗口前台初始状态

此类应用在UIAbility生命周期中无后台状态，详见不同设备UIAbility生命周期的差异化行为。

执行预加载启动时，系统会启动一个UIAbility至隐藏窗口前台初始状态，依次触发UIAbility.onCreate()、UIAbility.onWindowStageCreate()生命周期回调，并初始化一个隐藏窗口，一小段时间后应用进程会被挂起。

用户点击应用启动到前台时，系统会依次触发UIAbility.onNewWant()、UIAbility.onForeground()生命周期回调，走完前台启动流程。

开发步骤

声明应用支持预加载到的阶段。

以windowStageCreated阶段为例，在app.json5配置文件中配置appPreloadPhase标签。

{
  "app": {
    "bundleName": "com.demo.preloadtest",
    "vendor": "example",
    "versionCode": 1000000,
    "versionName": "1.0.0",
    "icon": "$media:layered_image",
    "label": "$string:app_name",
    "appPreloadPhase": "windowStageCreated"
  }
}

配置入口UIAbility（新建工程默认已自动配置）。

以EntryAbility为例，在entry模块的module.json5配置文件中，设置mainElement为EntryAbility，且EntryAbility的skills标签下面的entities中添加"entity.system.home"、actions中添加"ohos.want.action.home"。

当app.json5配置文件中的appPreloadPhase配置为windowStageCreated时，需要在entry模块的module.json5配置文件中配置EntryAbility的launchType标签为singleton或specified。

{
  "module": {
    "name": "entry",
    "type": "entry",
    "mainElement": "EntryAbility",
    // ...
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "launchType": "singleton",
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          }
        ]
        // ...
      }
    ]
  }
}

（可选）获取UIAbility启动原因。

仅当appPreloadPhase配置为windowStageCreated时，开发者可在UIAbility的onCreate生命周期回调中通过launchParam.launchReason的枚举值获取启动原因。枚举值为PRELOAD表示当前UIAbility是由预加载机制启动的。

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info(`EntryAbility onCreate, LaunchReason:${launchParam.launchReason}`);
    // 判断是否是预加载启动
    let isPreloadStart = launchParam.launchReason === AbilityConstant.LaunchReason.PRELOAD;
    // ...
  }
}

使用调试命令主动触发应用预加载。

$ hidumper -s 1901 -a 'preloadAbilityStage com.ohos.preloadapplication.testapp'
-------------------------------[ability]-------------------------------
----------------------------------ResourceSched----------------------------------

$ hidumper -s 1901 -a 'preloadWindowStage com.ohos.preloadapplication.testapp TestAppMainUIAbility'
-------------------------------[ability]-------------------------------
----------------------------------ResourceSched----------------------------------

常见问题

[h2]启动时延计算错误

问题现象

应用在AbilityStage.onCreate中记录启动起始时间戳，在应用绘制或onForeground时记录启动截止时间戳，以两者差值计算启动时延。由于预加载启动阶段与用户点击启动阶段可能间隔较久，会导致计算出的启动时延异常偏大。

解决措施

参考预加载状态识别与判断，若本次启动为预加载启动，则不在AbilityStage.onCreate中记录起始时间，应在UIAbility.onCreate中根据launchReason判断后再确定起始时间。

[h2]服务器路由地址选路错误

问题现象

应用在AbilityStage.onCreate中执行了连接服务器网络初始化，随后被系统冻结断网，导致应用误判为服务器网络不可用，选择了备用服务器路由地址。

解决措施

参考预加载状态识别与判断，若本次启动为预加载启动，则不执行服务器网络初始化；或重新启动到前台后，优先尝试优选服务器路由地址。

[h2]应用内部模块初始化异常

问题现象

应用内部模块初始化分散在AbilityStage.onCreate、UIAbility.onCreate、UIAbility.onForeground中，由于业务执行时间跨度太长，导致业务逻辑执行失败，未完成模块初始化，进而引发部分业务（如Push、VoIP呼叫等）逻辑执行异常。

解决措施

将业务模块初始化操作统一移动到UIAbility.onForeground中。

## Code blocks

### Code block 1

```
import { AbilityStage, application } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    // 根据appPreloadType的值判断当前进程的预加载类型
    let appPreloadType = application.getAppPreloadType();
  }
}
```

### Code block 2

```
{
  "app": {
    "bundleName": "com.demo.preloadtest",
    "vendor": "example",
    "versionCode": 1000000,
    "versionName": "1.0.0",
    "icon": "$media:layered_image",
    "label": "$string:app_name",
    "appPreloadPhase": "windowStageCreated"
  }
}
```

### Code block 3

```
{
  "module": {
    "name": "entry",
    "type": "entry",
    "mainElement": "EntryAbility",
    // ...
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "launchType": "singleton",
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          }
        ]
        // ...
      }
    ]
  }
}
```

### Code block 4

```
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info(`EntryAbility onCreate, LaunchReason:${launchParam.launchReason}`);
    // 判断是否是预加载启动
    let isPreloadStart = launchParam.launchReason === AbilityConstant.LaunchReason.PRELOAD;
    // ...
  }
}
```

### Code block 5

```
$ hidumper -s 1901 -a 'preloadAbilityStage com.ohos.preloadapplication.testapp'
-------------------------------[ability]-------------------------------
----------------------------------ResourceSched----------------------------------

$ hidumper -s 1901 -a 'preloadWindowStage com.ohos.preloadapplication.testapp TestAppMainUIAbility'
-------------------------------[ability]-------------------------------
----------------------------------ResourceSched----------------------------------
```
