# 离线地图

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-offlinemapdata_

场景介绍

从26.0.0开始，支持根据经纬度数组查询未下载的区域地图功能。

离线地图允许用户提前下载指定区域的地图数据，以便在无网络或网络不佳时正常使用地图功能。

接口说明

接口名	描述
getRecommendedCityIdsByLatLngs(context: common.Context, latlngs: mapCommon.LatLng[]): Promise<string[]>	根据经纬度数组查询设备上离线地图未下载的区域。

开发步骤

[h2]根据经纬度数组查询未下载的区域

1.导入相关模块。

import { offlineMapData } from '@kit.MapKit';

2.通过getRecommendedCityIdsByLatLngs，查询离线地图未下载的区域。

try {
  // 经纬度数组
  let latLngArr: mapCommon.LatLng[] = [{
    latitude: 49.5,
    longitude: 3.5
  }, {
    latitude: 49.5,
    longitude: 4.5
  }, {
    latitude: 50.5,
    longitude: 4.5
  }, {
    latitude: 51.5,
    longitude: 4.5
  }];
  // 根据经纬度数组查询设备上未下载的区域
  let resArray: string[] = await offlineMapData.getRecommendedCityIdsByLatLngs(
    this.getUIContext().getHostContext(), latLngArr);
  console.info(`resArray: ${JSON.stringify(resArray)}`);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

## Code blocks

### Code block 1

```
import { offlineMapData } from '@kit.MapKit';
```

### Code block 2

```
try {
  // 经纬度数组
  let latLngArr: mapCommon.LatLng[] = [{
    latitude: 49.5,
    longitude: 3.5
  }, {
    latitude: 49.5,
    longitude: 4.5
  }, {
    latitude: 50.5,
    longitude: 4.5
  }, {
    latitude: 51.5,
    longitude: 4.5
  }];
  // 根据经纬度数组查询设备上未下载的区域
  let resArray: string[] = await offlineMapData.getRecommendedCityIdsByLatLngs(
    this.getUIContext().getHostContext(), latLngArr);
  console.info(`resArray: ${JSON.stringify(resArray)}`);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```
