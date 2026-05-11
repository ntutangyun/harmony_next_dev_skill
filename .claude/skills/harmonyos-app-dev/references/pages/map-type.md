# 切换地图类型

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-type_

在地图初始化的时候，在mapOptions参数中新增mapType属性：mapCommon.MapType.STANDARD（标准地图）。

this.mapOptions = {
  position: {
    target: {
      latitude: 31.984410259206815,
      longitude: 118.76625379397866
    },
    zoom: 15
  },
  mapType: mapCommon.MapType.STANDARD
};

显示效果如下：

方式二：地图创建后，调用setMapType方法设置地图类型为地形图。设置为地形图时，为了获得最佳显示效果，推荐将地图缩放层级保持在5至14之间。

this.mapController.setMapType(mapCommon.MapType.TERRAIN);

显示效果如下：

显示地图
显示我的位置
