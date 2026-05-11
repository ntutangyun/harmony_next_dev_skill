# 云侧围栏开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fenceextensionability_

定位服务在满足围栏触发条件后，通过FenceExtensionAbility把围栏事件通知给APP，APP接收到围栏事件后完成相关的业务处理。

接口介绍

接口详情参见FenceExtensionAbility。

接口	描述
onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void	接收系统通知的地理围栏事件，根据围栏事件类型和数据进行相应处理。
onDestroy(): void	接收FenceExtensionAbility的销毁事件并处理，会在FenceExtensionAbility销毁前回调。
开发步骤

要实现一个地理围栏扩展服务，开发者需要实现FenceExtensionAbility的能力，具体步骤如下：

在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为fenceextensionability;

在fenceextensionability目录，右键选择“New > File”，新建一个.ets文件并命名为MyFenceExtensionAbility.ets;

打开MyFenceExtensionAbility.ets，导入FenceExtensionAbility的依赖包，自定义类继承FenceExtensionAbility并实现onFenceStatusChange和onDestroy接口;

示例代码如下：

import { FenceExtensionAbility, geoLocationManager } from '@kit.LocationKit';
import { wantAgent } from '@kit.AbilityKit';
import { notificationManager } from '@kit.NotificationKit';


export default class MyFenceExtensionAbility extends FenceExtensionAbility {
  async onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): Promise<void> {
    super.onFenceStatusChange(transition, additions);


    // 接收围栏触发信息
    console.info('MyFenceExtensionAbility onFenceStatusChange');


    let poiId: string = additions['poiId'];// 围栏id，唯一标识，示例：'999287512272780934'
    let policyType: string = additions['policyType'];// 策略类型：'0'-普通策略;'1'-标签策略
    let policyResult: string = additions['policyResult'];// 策略结果：标签等策略的额外信息


    console.info(`poiId:${poiId},policyType:${policyType},policyResult:${policyResult}`);


    // 可以发送围栏业务通知
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: 'com.huawei.hmos.locationtest.smartfence',
          abilityName: 'EntryAbility'
        } as Want
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 100
    };
    let wantAgentMy = await wantAgent.getWantAgent(wantAgentInfo);
    let notificationRequest: notificationManager.NotificationRequest = {
      id: 1,
      content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
          title: `围栏通知`,
          text: `poiId:${poiId},policyType:${policyType},policyResult:${policyResult}`,
        }
      },
      notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
      wantAgent: wantAgentMy
    };
    notificationManager.publish(notificationRequest);
  }


  onDestroy(): void {
    super.onDestroy();
    console.info('MyFenceExtensionAbility onDestroy');
  }
}

在工程Module对应的module.json5配置文件中注册FenceExtensionAbility，type标签需要设置为fence，srcEntry标签表示当前FenceExtensionAbility组件所对应的代码路径。

{
  "module": {
    "extensionAbilities": [
      {
        "name": "MyFenceExtensionAbility",
        "srcEntry": "./ets/fenceextensionability/MyFenceExtensionAbility.ets",
        "description": "MyFenceExtensionAbility",
        "type": "fence",
        "exported": false
      },
    ]
  }
}
端侧GNSS围栏开发指导
个人数据处理说明
