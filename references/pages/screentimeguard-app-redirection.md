# 拦截页跳转至管控应用

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-app-redirection_

场景介绍

Screen Time Guard Kit支持用户通过被管控应用拦截页跳转至当前管控应用，管理当前的管控策略。从26.0.0版本开始，Screen Time Guard Kit新增支持跳转时want参数携带当前管控策略相关信息。

用户体验设计

业务流程

流程说明：

应用的某一管控规则生效，导致被管控应用不可用时，用户点击被管控应用，健康使用设备会拉起该应用的拦截页面。

用户点击拦截页面下方跳转按钮，健康使用设备查询被管控应用的token和对被管控应用生效的规则，将规则相关信息写入want自定义参数中。

健康使用设备调用startAbility接口拉起管控应用，传递的want参数携带当前管控规则相关信息。

应用可以在入口Ability的onCreate和onNewWant回调中接收并解析want参数，获取被管控应用的token、正在生效的管控规则名称等信息。

参数说明

want自定义参数如下表所示：

参数名	类型	描述
token	string	被管控应用的token。
strategyNames	string[]	当前对被管控应用生效的策略名称。 若有多个时间守护策略对该应用进行管控，则返回对应的策略名称数组。
isSetAppsRestriction	boolean	正在生效的规则是否包含应用访问限制。 true: 正在生效的规则包含应用访问限制，应用访问限制规则名称不会体现在strategyNames参数中。 false: 正在生效的规则不包含应用访问限制。

开发前提

拦截页跳转至管控应用并携带管控规则相关信息需要申请用户授权，请先参考请求用户授权章节完成用户授权。

拦截页跳转至管控应用并携带管控规则相关信息

导入相关模块。

import { UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import Utils from '../utils/Utils';

在onCreate和onNewWant回调中接收并解析want参数，获取当前管控规则相关信息。

export default class EntryAbility extends UIAbility {

  onCreate(want: Want): void {
    hilog.info(0x0000, 'GuardService', 'onCreate');
    if (want.parameters && want.parameters['ohos.aafwk.param.callerBundleName']) {
      Utils.setCallerBundleName(want.parameters['ohos.aafwk.param.callerBundleName'] as string);
    }
    let token: string = want.parameters?.['token'] as string;
    let strategyNames: string[] =  want.parameters?.['strategyNames'] as string[];
    let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
    Utils.setControlDetails(token, strategyNames, isSetAppsRestriction);
  }

  // ...

  onNewWant(want: Want): void {
    hilog.info(0x0000, 'GuardService', 'onNewWant');
    if (want.parameters && want.parameters['ohos.aafwk.param.callerBundleName']) {
      Utils.setCallerBundleName(want.parameters['ohos.aafwk.param.callerBundleName'] as string);
    }
    let token: string = want.parameters?.['token'] as string;
    let strategyNames: string[] =  want.parameters?.['strategyNames'] as string[];
    let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
    Utils.setControlDetails(token, strategyNames, isSetAppsRestriction);
  }

  // ...
}

## Code blocks

### Code block 1

```
import { UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import Utils from '../utils/Utils';
```

### Code block 2

```
export default class EntryAbility extends UIAbility {

  onCreate(want: Want): void {
    hilog.info(0x0000, 'GuardService', 'onCreate');
    if (want.parameters && want.parameters['ohos.aafwk.param.callerBundleName']) {
      Utils.setCallerBundleName(want.parameters['ohos.aafwk.param.callerBundleName'] as string);
    }
    let token: string = want.parameters?.['token'] as string;
    let strategyNames: string[] =  want.parameters?.['strategyNames'] as string[];
    let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
    Utils.setControlDetails(token, strategyNames, isSetAppsRestriction);
  }

  // ...

  onNewWant(want: Want): void {
    hilog.info(0x0000, 'GuardService', 'onNewWant');
    if (want.parameters && want.parameters['ohos.aafwk.param.callerBundleName']) {
      Utils.setCallerBundleName(want.parameters['ohos.aafwk.param.callerBundleName'] as string);
    }
    let token: string = want.parameters?.['token'] as string;
    let strategyNames: string[] =  want.parameters?.['strategyNames'] as string[];
    let isSetAppsRestriction: boolean = want.parameters?.['isSetAppsRestriction'] as boolean;
    Utils.setControlDetails(token, strategyNames, isSetAppsRestriction);
  }

  // ...
}
```
