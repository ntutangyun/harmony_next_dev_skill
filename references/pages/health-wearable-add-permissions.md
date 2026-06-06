# 管理用户授权

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-add-permissions_

requestAuthorizations(context: common.UIAbilityContext, request: AuthorizationRequest): Promise<AuthorizationResponse>	用户授权，入参为UIAbility上下文和授权参数AuthorizationRequest，添加需要读写的数据类型，拉起账号授权页面，引导用户完成授权，返回结果中的数据类型列表，其对应权限在应用申请权限和用户授权权限的交集中。
getAuthorizations(request: AuthorizationRequest): Promise<AuthorizationResponse>	查询用户权限，入参为AuthorizationRequest，添加需要查询的数据类型，查询传入类型是否有权限，返回结果中的数据类型列表，其对应权限在应用申请权限和用户授权权限的交集中。
cancelAuthorizations(): Promise<void>	取消用户所有授权。
开发前检查

完成申请运动健康服务与配置Client ID。

接口需在页面或自定义组件生命周期内调用。接口首次调用前，需先使用init方法进行初始化。

错误码请参考ArkTS API错误码，常见问题请参考Health Service Kit常见问题。

开发步骤
用户授权

1.导入运动健康功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.创建授权请求，确保授权参数中的权限已在申请运动健康服务时勾选，权限说明请参考权限说明。

let authorizationParameter: healthStore.AuthorizationRequest = {
  readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
  writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
}

3.调用requestAuthorizations方法执行登录授权请求，并处理返回结果。

try {
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
  let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);
  hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
  authorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
  });
  authorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to request authorization. Code: ${err.code}, message: ${err.message}`);
}
查询权限

1.导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.创建查询权限请求。

let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
  readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
  writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
}

3.调用getAuthorizations方法执行查询权限请求，并处理返回结果。

try {
  let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
  queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
  });
  queryAuthorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to get authorization. Code: ${err.code}, message: ${err.message}`);
}
取消授权

导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

调用cancelAuthorizations方法执行取消授权，并处理返回结果。

try {
  await healthStore.cancelAuthorizations();
  hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`);
}
Wearable应用开发
管理运动健康数据
