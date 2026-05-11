# 点聚合

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-aggregate_

聚合功能主要由ClusterOverlayParams、addClusterOverlay、ClusterOverlay提供，更多接口及使用方法请参见接口文档。

接口名	描述
ClusterOverlayParams	点聚合参数。
addClusterOverlay(params: mapCommon.ClusterOverlayParams): Promise<ClusterOverlay>	聚合接口，支持节点聚合能力。
ClusterOverlay	点聚合，支持更新和查询相关属性。
开发步骤

导入相关模块。

import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

新增聚合图层。

@Entry
@Component
struct ClusterOverlayDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;


  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.98,
          longitude: 118.7
        },
        zoom: 7
      }
    }


    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 生成待聚合点
        let clusterItem1: mapCommon.ClusterItem = {
          position: {
            latitude: 31.98,
            longitude: 118.7
          }
        };
        let clusterItem2: mapCommon.ClusterItem = {
          position: {
            latitude: 32.99,
            longitude: 118.9
          }
        };
        let clusterItem3: mapCommon.ClusterItem = {
          position: {
            latitude: 31.5,
            longitude: 118.7
          }
        };
        let clusterItem4: mapCommon.ClusterItem = {
          position: {
            latitude: 30,
            longitude: 118.7
          }
        };
        let clusterItem5: mapCommon.ClusterItem = {
          position: {
            latitude: 29.98,
            longitude: 117.7
          }
        };
        let clusterItem6: mapCommon.ClusterItem = {
          position: {
            latitude: 31.98,
            longitude: 120.7
          }
        };
        let clusterItem7: mapCommon.ClusterItem = {
          position: {
            latitude: 25.98,
            longitude: 119.7
          }
        };
        let clusterItem8: mapCommon.ClusterItem = {
          position: {
            latitude: 30.98,
            longitude: 110.7
          }
        };
        let clusterItem9: mapCommon.ClusterItem = {
          position: {
            latitude: 30.98,
            longitude: 115.7
          }
        };
        let clusterItem10: mapCommon.ClusterItem = {
          position: {
            latitude: 28.98,
            longitude: 122.7
          }
        };
        let array: Array<mapCommon.ClusterItem> = [
          clusterItem1,
          clusterItem2,
          clusterItem3,
          clusterItem4,
          clusterItem5,
          clusterItem6,
          clusterItem7,
          clusterItem8,
          clusterItem9,
          clusterItem10
        ]
        for(let index = 0; index < 100; index++){
          array.push(clusterItem1)
        }
        for(let index = 0; index < 10; index++){
          array.push(clusterItem2)
        }
        // 生成聚合图层的入参 聚合distance设置为100vp
        let clusterOverlayParams: mapCommon.ClusterOverlayParams = {
          distance: 100,
          clusterItems: array
        };
        try {
          // 调用addClusterOverlay生成聚合图层
          await this.mapController.addClusterOverlay(clusterOverlayParams);
        } catch (e) {
          console.error(`code:${e.code}, message:${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }


  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .width('100%')
          .height('100%');
      }.width('100%')
    }.height('100%')
  }
}

聚合标记点击事件监听。

let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", `callback1 markerClusterInfo`);
};
// 添加监听
clusterOverlay.on("markerClusterClick", callback1);
// 取消监听
clusterOverlay.off("markerClusterClick", callback1);
气泡
覆盖物
