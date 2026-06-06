# 弧线

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-arc_

private callback?: AsyncCallback<map.MapComponentController>;
  private mapArc?: map.MapArc;


  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 34.757975,
          longitude: 113.665412
        },
        zoom: 6
      }
    }


    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        if (!this.mapController) {
          console.error(this.TAG, "mapController is null");
          return;
        }
        // 设置弧线参数
        let mapArcParams: mapCommon.MapArcParams = {
          // 弧线起点坐标
          startPoint: {
            latitude: 39.913138,
            longitude: 116.415112
          },
          // 弧线终点坐标
          endPoint: {
            latitude: 28.239473,
            longitude: 112.954094
          },
          // 弧线中心点坐标
          centerPoint: {
            latitude: 33.86970399048567,
            longitude: 112.08633528544145
          },
          width: 10,
          color: 0xffff0000,
          visible: true,
          zIndex: 100
        };
        // 添加弧线
        try {
          this.mapArc = await this.mapController.addArc(mapArcParams);
        } catch (e) {
          console.error(`Failed to create the mapArc, code is：${e.code}, message is ${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    }
  }


  build() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback
        })
          .width('100%')
          .height('100%');
      }.width('100%')
    }.height('100%')
  }
}

折线
多边形
