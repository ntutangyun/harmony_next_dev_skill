# 实现应用图标动态切换

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-appinfo-use_

图标管理服务支持Phone、Tablet、PC/2in1设备。并且从5.1.1(18)版本开始，新增支持Wearable设备，从5.1.1(19)版本开始，新增支持TV设备。

接口说明

图标管理服务提供以下接口，具体API说明详见接口文档。

接口名	描述
queryDynamicIcons(): Promise<DynamicIconInfo[]>	查询动态图标信息接口，用于查询动态图标信息。
selectDynamicIcon(iconId: string): Promise<void>	切换动态图标接口，用于切换动态图标。
disableDynamicIcon(): Promise<void>	禁用动态图标接口，用于停止动态图标，恢复默认图标。
说明

从版本6.0.0(20)开始，切换动态图标接口支持返回1006800013错误码。

开发步骤
查询动态图标信息

导入appInfoManager模块及相关公共模块。

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用queryDynamicIcons方法查询动态图标信息。

try {
  appInfoManager.queryDynamicIcons()
    .then((queryResult: appInfoManager.DynamicIconInfo[]) => {
      hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo size = " + queryResult.length);
      for (let i = 0; i < queryResult.length; i++) {
        hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo iconUrl = " + queryResult[i]["iconUrl"] + ", iconId = " + queryResult[i]["iconId"] + ", enabled = "+queryResult[i]["enabled"]);
      }
    }).catch((error: BusinessError) => {
      hilog.error(0, 'TAG', "queryDynamicIcons failed, code: " + error.code + ", exception message: " + error.message);
    });
} catch (error) {
  hilog.error(0, 'TAG', "queryDynamicIcons exception code: " + error.code + ", exception message: " + error.message);
}
切换动态图标

导入appInfoManager模块及相关公共模块。

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用selectDynamicIcon方法切换动态图标。

try {
  let iconId: string = 'iconId';
  appInfoManager.selectDynamicIcon(iconId).then(() => {
      hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
恢复默认图标

导入appInfoManager模块及相关公共模块。

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用disableDynamicIcon方法恢复默认图标。

try {
  appInfoManager.disableDynamicIcon().then(() => {
      hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
通过AppGallery Connect动态管理应用图标
应用评论服务
