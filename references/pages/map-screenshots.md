# 地图截图

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-screenshots_

private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  @State image?: image.PixelMap = undefined;


  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      }
    };


    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    };
  }


  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .width('100%')
          .height('50%');


        Scroll(new Scroller()) {
          Column() {
            Image(this.image)
              .objectFit(ImageFit.Auto)
              .border({ width: 1, color: Color.Red }).width("100%")
            Button("获取截图")
              .margin({ left: 10 })
              .fontSize(12)
              .onClick(async () => {
                if (this.mapController) {
                  let pixelMap = await this.mapController.snapshot();
                  this.image = pixelMap;
                }
              });
          }
        }.width('70%').height("50%")
      }.width('100%')
    }.height('100%')
  }
}
更改地图位置
在地图上绘制
