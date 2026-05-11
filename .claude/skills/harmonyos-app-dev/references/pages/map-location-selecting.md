# 地点选取

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-selecting_

本章节将向您介绍如何集成地点选取控件，您无需自己开发地图页面，可快速实现地点选取的能力。该控件不支持在智能表设备中调用。

图1 地点选取页

图2 地点选取

约束与限制

使用该功能需满足以下条件：

仅支持手机、平板和2in1设备。
接口说明

地点选取控件功能主要由sceneMap命名空间下的chooseLocation方法提供，更多接口及使用方法请参见接口文档。

接口名	描述
LocationChoosingOptions	地点选取的参数。
chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>	地点选取。
LocationChoosingResult	地点选取的返回结果。
开发步骤

导入相关模块。

import { sceneMap } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

创建地点选取参数，调用chooseLocation方法拉起地点选取页。

let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
  // 地图中心点坐标
  location: {
    latitude: 39.91804051376904,
    longitude: 116.3970536796932
  },
  // 展示搜索控件
  searchEnabled: true,
  // 展示附近POI
  showNearbyPoi: true
};
// 拉起地点选取页
sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext,
  locationChoosingOptions).then((data) => {
  console.info("ChooseLocation", "Succeeded in choosing location.");
}).catch((err: BusinessError) => {
  console.error("ChooseLocation", `Failed to choose location, code: ${err.code}, message: ${err.message}`);
});
地点详情展示
区划选择
