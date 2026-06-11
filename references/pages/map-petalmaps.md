# 通过地图应用实现导航等能力

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-petalmaps_

场景介绍

从5.0.3(15)开始，支持地图应用首页、搜索地点、查看地点详情、规划路线和进行导航功能；从6.0.1(21)开始，支持地图应用发起打车功能；从6.1.1(24)开始，打开地图应用查看地点详情支持终点描述，支持拉起地图应用离线地图管理页面。

本章节将向您介绍如何打开地图应用实现如下能力：

打开地图应用首页

打开地图应用搜索地点

打开地图应用查看地点详情

打开地图应用规划路线

打开地图应用进行导航

打开地图应用发起打车

打开地图应用离线地图管理页面

接口说明

调用地图应用的功能主要通过petalMaps命名空间下的openMapHomePage、openMapTextSearch、openMapPoiDetail、openMapRoutePlan、openMapNavi、openMapTaxi、openMapOfflineDataManagement等接口实现，更多接口及使用方法请参见接口文档。

接口说明	描述
TextSearchParams	文本搜索的参数。
PoiDetailParams	POI详情的参数。
RoutePlanParams	路线规划的参数。
NaviParams	导航的参数。
TaxiParams	打车的参数。
OfflineDataParams	离线地图管理参数。
openMapHomePage(context: common.Context): Promise<void>	打开地图应用首页。
openMapTextSearch(context: common.Context, textSearchParams: TextSearchParams): Promise<void>	打开地图应用搜索地点。
openMapPoiDetail(context: common.Context, poiDetailParams: PoiDetailParams): Promise<void>	打开地图应用查看地点详情。
openMapRoutePlan(context: common.Context, routePlanParams: RoutePlanParams): Promise<void>	打开地图应用规划路线。
openMapNavi(context: common.Context, naviParams: NaviParams): Promise<void>	打开地图应用进行导航。
openMapTaxi(context: common.Context, taxiParams: TaxiParams): Promise<void>	打开地图应用打车页面。
openMapOfflineDataManagement(context: common.Context, offlineDataParams: OfflineDataParams): Promise<void>	打开地图应用的离线地图管理页面。

地图应用使用的坐标类型

在国内站点，中国大陆使用GCJ02坐标系，中国台湾使用WGS84坐标系。

在海外站点，统一使用WGS84坐标系。坐标系转换参考：坐标纠偏。

开发步骤

导入相关模块

import { petalMaps } from '@kit.MapKit'

[h2]打开地图应用首页

通过openMapHomePage，打开地图应用首页。

try {
  await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图1 打开地图应用首页

[h2]打开地图应用进行地点搜索

通过openMapTextSearch，传入搜索目标名称，打开地图应用进行地点搜索。

try {
  let params: petalMaps.TextSearchParams = {
    destinationName: '云谷'
  };
  await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图2 打开地图应用进行地点搜索

[h2]打开地图应用查看地点详情

通过openMapPoiDetail，传入地点的经纬度，打开地图应用查看地点详情。

try {
  let params: petalMaps.PoiDetailParams = {
    destinationPosition: {
      latitude: 31.968789,
      longitude: 118.798537
    },
    destinationName: '标记点',
    zoom: 17,
    coordinateType: mapCommon.CoordinateType.GCJ02,
    destinationAddress: '这是我选择的演示名称'
  };
  await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图3 打开地图应用查看地点详情

[h2]打开地图应用规划路线

通过openMapRoutePlan，传入终点经纬度，打开地图应用规划路线。

try {
  let params: petalMaps.RoutePlanParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图4 打开地图应用规划路线

[h2]打开地图应用进行导航

通过openMapNavi，传入终点经纬度，打开地图应用发起导航。

try {
  let params: petalMaps.NaviParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图5 打开地图应用进行导航

[h2]打开地图应用打车页面

通过openMapTaxi，传入终点经纬度，打开地图应用发起打车。

try {
  let params: petalMaps.TaxiParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图6 打开地图应用进行打车

[h2]打开地图应用离线地图管理页面

通过openMapOfflineDataManagement，传入离线地图管理参数，打开地图应用离线地图管理页面。

try {
  // 打开地图应用手表离线地图管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'WATCH',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用地图资源（手机离线地图）管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'PHONE',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用导航语音管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'VOICE'
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

图7 打开地图应用手表离线地图管理页面

图8 打开地图应用地图资源（手机离线地图）管理页面

图9 打开地图应用导航语音管理页面

## Code blocks

### Code block 1

```
import { petalMaps } from '@kit.MapKit'
```

### Code block 2

```
try {
  await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 3

```
try {
  let params: petalMaps.TextSearchParams = {
    destinationName: '云谷'
  };
  await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 4

```
try {
  let params: petalMaps.PoiDetailParams = {
    destinationPosition: {
      latitude: 31.968789,
      longitude: 118.798537
    },
    destinationName: '标记点',
    zoom: 17,
    coordinateType: mapCommon.CoordinateType.GCJ02,
    destinationAddress: '这是我选择的演示名称'
  };
  await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 5

```
try {
  let params: petalMaps.RoutePlanParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 6

```
try {
  let params: petalMaps.NaviParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 7

```
try {
  let params: petalMaps.TaxiParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```

### Code block 8

```
try {
  // 打开地图应用手表离线地图管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'WATCH',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用地图资源（手机离线地图）管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'PHONE',
    // 推荐下载离线地图的地区集合
    recommendedRegionIds: ['1026355368865976081']
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}

try {
  // 打开地图应用导航语音管理页面
  let params: petalMaps.OfflineDataParams = {
    scenarios: 'VOICE'
  };
  await petalMaps.openMapOfflineDataManagement(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(`code:${e.code}, message:${e.message}`);
}
```
