# 事件交互

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-listening_

本章节包含地图的点击和长按、相机移动（华为地图的移动是通过模拟相机移动的方式实现的）、以及“我的位置”按钮点击等事件监听。

接口说明

以下是地图监听事件相关接口，以下功能主要由MapEventManager提供，可通过getEventManager方法获得MapEventManager，更多接口及使用方法请参见接口文档。

接口名	描述
on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void	设置地图点击事件监听器。
on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void	设置地图长按事件监听器。
on(type: 'cameraMoveStart', callback: Callback<number>): void	设置相机开始移动事件监听器。
on(type: 'cameraMove', callback: Callback<void>): void	设置相机移动事件监听器。
on(type: 'cameraIdle', callback: Callback<void>): void	设置相机移动结束事件监听器。
on(type: 'markerClick' , callback: Callback<Marker>): void	设置标记点击事件监听器。
on(type: 'myLocationButtonClick', callback: Callback<void>): void	设置我的位置按钮点击事件监听器。
on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void	设置点注释点击事件监听器。

开发步骤

[h2]初始化地图组件的事件管理接口

this.mapEventManager = this.mapController.getEventManager();

[h2]地图点击事件监听

let callback = (position: mapCommon.LatLng) => {
  console.info("mapClick", `on-mapClick position = ${position.longitude}`);
};
this.mapEventManager.on("mapClick", callback);

[h2]地图长按事件监听

let callback = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `on-mapLongClick position = ${position.longitude}`);
};
this.mapEventManager.on("mapLongClick", callback);

[h2]相机移动监听

相机移动时（华为地图的移动是通过模拟相机移动的方式实现的），通过设置监听器，能够对相机移动状态进行监听。

当相机开始移动时，会回调cameraMoveStart。

let callback = (reason: number) => {
  console.info("cameraMoveStart", `on-cameraMoveStart reason = ${reason}`);
};
this.mapEventManager.on("cameraMoveStart", callback);

当相机移动或用户与触摸屏交互时，会多次调用cameraMove。

let callback = () => {
  console.info("cameraMove", `on-cameraMove`);
};
this.mapEventManager.on("cameraMove", callback);

当相机停止移动时，会回调cameraIdle。

let callback = () => {
  console.info("cameraIdle", `on-cameraIdle`);
};
this.mapEventManager.on("cameraIdle", callback);

[h2]标记点击事件监听

标记是指在地图的指定位置添加标记以标识位置、商家、建筑等。详情请参见标记。

let callback = (marker: map.Marker) => {
  console.info("markerClick", `markerClick: ${marker.getId()}`);
};
this.mapEventManager.on("markerClick", callback);

[h2]我的位置监听

详情请参见显示我的位置。

let callback = () => {
  console.info("myLocationButtonClick", `myLocationButtonClick`);
};
this.mapEventManager.on("myLocationButtonClick", callback);

[h2]点注释事件监听

点注释是指在地图的指定位置添加点注释以标识位置、商家、建筑等，并可以通过信息窗口展示详细信息。详情请参见点注释。

let callback = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `pointAnnotationClick: ${pointAnnotation.getId()}`);
};
this.mapEventManager.on("pointAnnotationClick", callback);

## Code blocks

### Code block 1

```
this.mapEventManager = this.mapController.getEventManager();
```

### Code block 2

```
let callback = (position: mapCommon.LatLng) => {
  console.info("mapClick", `on-mapClick position = ${position.longitude}`);
};
this.mapEventManager.on("mapClick", callback);
```

### Code block 3

```
let callback = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", `on-mapLongClick position = ${position.longitude}`);
};
this.mapEventManager.on("mapLongClick", callback);
```

### Code block 4

```
let callback = (reason: number) => {
  console.info("cameraMoveStart", `on-cameraMoveStart reason = ${reason}`);
};
this.mapEventManager.on("cameraMoveStart", callback);
```

### Code block 5

```
let callback = () => {
  console.info("cameraMove", `on-cameraMove`);
};
this.mapEventManager.on("cameraMove", callback);
```

### Code block 6

```
let callback = () => {
  console.info("cameraIdle", `on-cameraIdle`);
};
this.mapEventManager.on("cameraIdle", callback);
```

### Code block 7

```
let callback = (marker: map.Marker) => {
  console.info("markerClick", `markerClick: ${marker.getId()}`);
};
this.mapEventManager.on("markerClick", callback);
```

### Code block 8

```
let callback = () => {
  console.info("myLocationButtonClick", `myLocationButtonClick`);
};
this.mapEventManager.on("myLocationButtonClick", callback);
```

### Code block 9

```
let callback = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", `pointAnnotationClick: ${pointAnnotation.getId()}`);
};
this.mapEventManager.on("pointAnnotationClick", callback);
```
