# 应用内处理分享内容

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-interface-description_

目标应用可以通过UIAbility构建接收分享内容的界面，并将应用显示到分享面板应用推荐区内，以实现将分享内容传递到目标应用内进行处理。开发时需要接入方实现UIAbility并于module.json5中注册支持分享内容的能力。

接口说明

getSharedData接口用于从want中获取分享数据；getContactInfo接口用于从want中获取联系人信息（仅当用户选择联系人分享时有返回值）。具体API说明详见接口文档。

表1 目标应用解析分享数据接口功能介绍

接口名	描述
getSharedData(want: Want): Promise<SharedData>	从want中获取分享数据
getContactInfo(want: Want): Promise<ContactInfo>	从want中获取联系人信息
开发步骤

导入相关模块。

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { systemShare } from '@kit.ShareKit';
import { BusinessError } from '@kit.BasicServicesKit';

目标应用可实现UIAbility。在Ability被启动后，可以在其onCreate或onNewWant回调中获取传入的want参数。将want参数通过getSharedData解析后得到分享数据。

export default class TestUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    systemShare.getSharedData(want)
      .then((data: systemShare.SharedData) => {
        data.getRecords().forEach((record: systemShare.SharedRecord) => {
          // 处理分享数据
        });
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
        this.context.terminateSelf();
      });
  }
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    windowStage.loadContent('pages/Index', (error) => {
      if (error.code) {
        console.error(`Failed to load the content. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info('Succeeded in loading the content.');
    });
  }
}

构建完UIAbility，需要在应用配置文件（src/main/module.json5）的skills配置中注册。配置actions为ohos.want.action.sendData；uris需穷举所有支持的数据类型。

"abilities": [
  {
    "name": "TestUIAbility",
    "srcEntry": "./ets/entryability/TestUIAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:layered_image",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "skills": [
      {
        "actions": [
          "ohos.want.action.sendData"
        ],
        // scheme为预留字段，在此处不生效，配置file仅为示例
        // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD，比如：支持全部图片类型，可声明：general.image
        // maxFileSupported 对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享。
        // 文件类型归属关系参考：@ohos.data.uniformTypeDescriptor (标准化数据定义与描述)
        "uris": [
          {
            "scheme": "file",
            "utd": "general.text",
            "maxFileSupported": 1
          },
          {
            "scheme": "file",
            "utd": "general.png",
            "maxFileSupported": 1
          },
          {
            "scheme": "file",
            "utd": "general.jpeg",
            "maxFileSupported": 1
          }
        ]
      }
    ]
  }
]
目标应用处理分享内容
分享详情页处理分享内容
