# 用户状态感知开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/userstatus-guidelines_

on(type:'userAgeGroupDetected',callback:Callback<UserClassification>):void;	订阅年龄群组检测功能，检测结果通过callback返回。
off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void;	取消年龄群组检测功能。
约束与限制

此功能如果设备不支持，将返回801错误码。

此功能涉及安全隐私，如需使用，请 联系技术人员。

开发步骤

导入模块。

import { userStatus } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';
Index.ets

定义回调函数，监听年龄群组检测结果变化。

let callback : Callback<userStatus.UserClassification> = (data : userStatus.UserClassification) => {
  console.info('callback succeeded, ageGroup:' + data.ageGroup + ", confidence:" + data.confidence);
};
Index.ets

订阅年龄群组检测功能。

try {
   userStatus.on('userAgeGroupDetected', callback);
   console.info("on succeeded");
} catch (err) {
   let error = err as BusinessError;
   console.error("Failed on and err code is " + error.code);
}
Index.ets

取消订阅年龄群组检测功能。

try {
   userStatus.off('userAgeGroupDetected');
   console.info("off succeeded");
} catch (err) {
   let error = err as BusinessError;
   console.error("Failed off and err code is " + error.code);
}
Index.ets
设备状态感知开发指导
记忆链接开发指导
