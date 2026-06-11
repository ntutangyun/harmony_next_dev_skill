# 管理用户授权

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-litewearable-add-permissions_

场景介绍

应用拉起华为账号同步和授权界面，由用户授权相应的数据访问权限。用户可以自主选择授权的数据类型，可以只授权部分数据权限。

应用所能操作的用户数据，是用户授权和运动健康服务审批通过的数据权限的交集。

约束与限制

从6.1.1(24) 版本开始，Lite Wearable设备新增支持health Service Kit特性。

接口说明

接口名	描述
requestAuthorizations(request: AuthorizationRequest): AuthorizationResponse	用户授权，入参为授权参数AuthorizationRequest，添加需要读写的数据类型，拉起账号授权页面，引导用户完成授权，返回结果中的数据类型列表，其对应权限在应用申请权限和用户授权权限的交集中。
getAuthorizations(request: AuthorizationRequest): AuthorizationResponse	查询用户权限，入参为AuthorizationRequest，添加需要查询的数据类型，查询传入类型是否有权限，返回结果中的数据类型列表，其对应权限在应用申请权限和用户授权权限的交集中。

开发前检查

完成申请运动健康服务。

常见问题请参考Health Service Kit常见问题。

开发步骤

导入运动健康服务功能模块及相关公共模块。

import healthStore from '@hms.health.store';

查询权限。

function getAuthorizations() {
  let queryAuthorizationRequest = {
    readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    scopes: ['https://www.huawei.com/healthkit/workout']
  }

  try {
    let queryAuthorizationResponse = healthStore.getAuthorizations(queryAuthorizationRequest);
  } catch (err) {
    // 异常场景处理
  }
}

发起用户授权请求。

function requestAuthorizations() {
  let authorizationParameter = {
    readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    scopes: ['https://www.huawei.com/healthkit/workout']
  }
  try {
    let authorizationResponse = healthStore.requestAuthorizations(authorizationParameter);
  } catch (err) {
    // 异常场景处理
  }
}

## Code blocks

### Code block 1

```
import healthStore from '@hms.health.store';
```

### Code block 2

```
function getAuthorizations() {
  let queryAuthorizationRequest = {
    readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    scopes: ['https://www.huawei.com/healthkit/workout']
  }

  try {
    let queryAuthorizationResponse = healthStore.getAuthorizations(queryAuthorizationRequest);
  } catch (err) {
    // 异常场景处理
  }
}
```

### Code block 3

```
function requestAuthorizations() {
  let authorizationParameter = {
    readDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    writeDataTypes: [healthStore.healthDataTypes.WORKOUT_SUMMARY],
    scopes: ['https://www.huawei.com/healthkit/workout']
  }
  try {
    let authorizationResponse = healthStore.requestAuthorizations(authorizationParameter);
  } catch (err) {
    // 异常场景处理
  }
}
```
