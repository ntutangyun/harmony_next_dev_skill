# 模拟点击检测

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-simulatedclickdetection_

场景介绍

从6.0.0(20) 版本开始，新增支持模拟点击检测。

应用通过调用Device Security Kit的detectSimulatedClickRisk接口，获取模拟点击检测结果，用于检测自动化点击、设备农场等作弊行为。

应用可以根据检测结果评估如何进行业务操作。

约束与限制

每30秒最多可以调用10次，每个应用在每个设备上每天最多可以调用20次。

业务流程

流程说明：

开发者应用调用detectSimulatedClickRisk接口，发起模拟点击检测请求。

Device Security Kit收到请求后，首先采集当前设备模拟点击线索数据，然后将线索数据发送到Device Security服务器做检测，最后通过detectSimulatedClickRisk接口的返回值将检测结果传递给开发者应用。

获取检测结果，并根据结果做出相应处理。

接口说明

以下是模拟点击检测相关接口，更多接口及使用方法请参见API参考。

接口名	描述
detectSimulatedClickRisk(params: SimulatedClickDetectionRequest): Promise<string>	模拟点击检测。

开发步骤

导入Device Security Kit模块及相关公共模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用detectSimulatedClickRisk接口获取模拟点击检测结果。

const TAG: string = '[SimulatedClickRiskDetectModel]';

function  simulatedClickRiskDetectPromise(): Promise<String> {
  return new Promise(async (resolve: Function, reject: Function) => {
    let params = {
      version: 1
    } as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
    try {
      hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
      businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
        // Indicates communication with the service was successful.
        // Use result to get the result data.
        // It is recommended that the result be parsed and verified on the server.
        hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
        resolve(result);
      }).catch((error: Error) => {
        // An error occurred while communicating with the service.
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
        reject(error);
      });
    } catch (error) {
      // An error occurred while using api.
      let e: BusinessError = error as BusinessError;
      hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
      reject(error);
    }
  });
}

开发者应用可以根据模拟点击检测结果进行业务处理。

模拟点击检测结果是一个格式为JSON格式的字符串，内容示例如下

{
  "timestampMs": 9860437986543,
  "version": 1,
  "riskDecision": "fake",
  "tags": ["AbnormalTap"]
}

说明

timestampMs：发起请求时生成的时间戳。

riskDecision：风险检测结果。

version：检测结果消息格式的版本。默认值为1，当前只支持1。

tags：模拟点击关键特征。如果tags列表为空，表示未发现关键特征。如果tags列表不为空，表示发现关键特征。

tags值	含义
AbnormalDeviceIntegrity	设备完整性遭到破坏。
AbnormalDeviceBehavior	设备行为异常，例如，设备连接状态、传感器状态等行为异常。
AbnormalTap	存在异常点击行为，例如，点击事件注入，自动化点击等。

riskDecision值	含义
fake	当前设备存在作弊风险行为。详情见上方tags表格。
likelyReal	当前操作设备的是真人用户的可能性较高。
unknown	未知。未检测到明显特征，无法识别。

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
const TAG: string = '[SimulatedClickRiskDetectModel]';

function  simulatedClickRiskDetectPromise(): Promise<String> {
  return new Promise(async (resolve: Function, reject: Function) => {
    let params = {
      version: 1
    } as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
    try {
      hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
      businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
        // Indicates communication with the service was successful.
        // Use result to get the result data.
        // It is recommended that the result be parsed and verified on the server.
        hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
        resolve(result);
      }).catch((error: Error) => {
        // An error occurred while communicating with the service.
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
        reject(error);
      });
    } catch (error) {
      // An error occurred while using api.
      let e: BusinessError = error as BusinessError;
      hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
      reject(error);
    }
  });
}
```

### Code block 3

```
{
  "timestampMs": 9860437986543,
  "version": 1,
  "riskDecision": "fake",
  "tags": ["AbnormalTap"]
}
```
