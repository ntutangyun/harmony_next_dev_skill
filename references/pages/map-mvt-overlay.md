# 矢量图层

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-mvt-overlay_

场景介绍

新增矢量图层，用于在基础地图之上叠加矢量数据。

通过矢量图层可在基础地图之上添加额外特性，例如实时展示全球或区域的天气状况户、商户自定义图标标记、 车辆位置信息等。

6.0.0(20)开始，支持矢量图层功能。

接口说明

矢量图层功能主要由MvtOverlayParams、addMvtOverlay和MvtOverlay提供，更多接口及使用方法请参见接口文档。

接口名	描述
MvtOverlayParams	矢量图层的参数。
addMvtOverlay(params: mapCommon.MvtOverlayParams): MvtOverlay	添加矢量图层。
MvtOverlay	矢量图层管理对象，支持添加和删除图层。

开发步骤

矢量图层的绘制方式提供两种方式：在线下载和本地加载。

[h2]在线下载

在开发过程中，开发者需要在应用的module.json5文件中配置网络访问权限以支持在线下载矢量图层。具体操作如下：打开module.json5文件，在requestPermissions数组中添加如下配置项：允许应用使用Internet网络。

{
  "module" : {
    // ...
    "requestPermissions":[
      {
        // 允许应用使用Internet网络。
        "name": "ohos.permission.INTERNET",
        "usedScene": {
          "when": "always"
        }
      }
    ]
  }
}

导入相关模块。

import { mapCommon, map, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

绘制矢量图层。

矢量图层支持的数据源类型为通用矢量瓦片格式（PBF/MVT）。MvtOverlayParams类中的layers参数，其中sourceLayer、fillColor/fillOpacity默认值从矢量数据里获取，也可自己设置。

@Entry
@Component
struct MvtOverlayDemo {
  private TAG = 'OHMapSDK_MvtOverlayDemo';
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          latitude: 35.899780,
          longitude: 107.766172
        },
        zoom: 6
      },
      scaleControlsEnabled: true
    }
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let params: mapCommon.MvtOverlayParams = {
          source: {
            // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
            tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
            minZoom: 2,
            maxZoom: 15
          },
          layers: [{
            id: 'layer-map',
            type: mapCommon.MvtLayerType.FILL,
            // 对应矢量图层数据中图层的name字段
            sourceLayer: 'XX',
            paint: {
              fillColor: {
                operator: mapCommon.Operator.GET,
                args: 'fill'
              },
              fillOpacity: {
                operator: mapCommon.Operator.GET,
                args: 'fill-opacity'
              }
            }
          }]
        }
        try {
          this.mapController?.addMvtOverlay(params);
        } catch (e) {
          console.error(this.TAG, `code:${e.code}, message:${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }
  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }
}

[h2]本地加载

导入相关模块。

import { mapCommon, map, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

增加本地矢量图层。

@Entry
@Component
struct MvtOverlayDemo {
  private TAG = 'OHMapSDK_MvtOverlayDemo';
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          latitude: 35.899780,
          longitude: 107.766172
        },
        zoom: 6
      },
      scaleControlsEnabled: true
    }
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let params: mapCommon.MvtOverlayParams = {
          source: {
            // 根据矢量坐标获取矢量图层，本地获取矢量图层方式需开发者自行实现tileProvider方法
            tileProvider: this.tileProviderMethod,
            minZoom: 2,
            maxZoom: 15
          },
          layers: [{
            id: 'layer-map',
            type: mapCommon.MvtLayerType.FILL,
            // 对应矢量图层数据中图层的name字段
            sourceLayer: 'XX',
            paint: {
              fillColor: {
                operator: mapCommon.Operator.GET,
                args: 'fill'
              },
              fillOpacity: {
                operator: mapCommon.Operator.GET,
                args: 'fill-opacity'
              }
            }
          }]
        }
        try {
          this.mapController?.addMvtOverlay(params);
        } catch (e) {
          console.error(this.TAG, `code:${e.code}, message:${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }

  // 需要开发者自行实现tileProviderMethod方法，负责加载本地项目中的矢量图层资源
  private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {});
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }
}

## Code blocks

### Code block 1

```
{
  "module" : {
    // ...
    "requestPermissions":[
      {
        // 允许应用使用Internet网络。
        "name": "ohos.permission.INTERNET",
        "usedScene": {
          "when": "always"
        }
      }
    ]
  }
}
```

### Code block 2

```
import { mapCommon, map, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
```

### Code block 3

```
@Entry
@Component
struct MvtOverlayDemo {
  private TAG = 'OHMapSDK_MvtOverlayDemo';
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          latitude: 35.899780,
          longitude: 107.766172
        },
        zoom: 6
      },
      scaleControlsEnabled: true
    }
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let params: mapCommon.MvtOverlayParams = {
          source: {
            // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
            tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
            minZoom: 2,
            maxZoom: 15
          },
          layers: [{
            id: 'layer-map',
            type: mapCommon.MvtLayerType.FILL,
            // 对应矢量图层数据中图层的name字段
            sourceLayer: 'XX',
            paint: {
              fillColor: {
                operator: mapCommon.Operator.GET,
                args: 'fill'
              },
              fillOpacity: {
                operator: mapCommon.Operator.GET,
                args: 'fill-opacity'
              }
            }
          }]
        }
        try {
          this.mapController?.addMvtOverlay(params);
        } catch (e) {
          console.error(this.TAG, `code:${e.code}, message:${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }
  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }
}
```

### Code block 4

```
import { mapCommon, map, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
```

### Code block 5

```
@Entry
@Component
struct MvtOverlayDemo {
  private TAG = 'OHMapSDK_MvtOverlayDemo';
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          latitude: 35.899780,
          longitude: 107.766172
        },
        zoom: 6
      },
      scaleControlsEnabled: true
    }
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let params: mapCommon.MvtOverlayParams = {
          source: {
            // 根据矢量坐标获取矢量图层，本地获取矢量图层方式需开发者自行实现tileProvider方法
            tileProvider: this.tileProviderMethod,
            minZoom: 2,
            maxZoom: 15
          },
          layers: [{
            id: 'layer-map',
            type: mapCommon.MvtLayerType.FILL,
            // 对应矢量图层数据中图层的name字段
            sourceLayer: 'XX',
            paint: {
              fillColor: {
                operator: mapCommon.Operator.GET,
                args: 'fill'
              },
              fillOpacity: {
                operator: mapCommon.Operator.GET,
                args: 'fill-opacity'
              }
            }
          }]
        }
        try {
          this.mapController?.addMvtOverlay(params);
        } catch (e) {
          console.error(this.TAG, `code:${e.code}, message:${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }

  // 需要开发者自行实现tileProviderMethod方法，负责加载本地项目中的矢量图层资源
  private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
    return new Promise((resolve, reject) => {});
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%')
      }.width('100%')
    }.height('100%')
  }
}
```
