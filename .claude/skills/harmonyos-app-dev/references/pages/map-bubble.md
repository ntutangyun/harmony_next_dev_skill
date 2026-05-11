# 气泡

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-bubble_

addBubble(params: mapCommon.BubbleParams): Promise<Bubble>	在地图上添加气泡。
Bubble	气泡，支持更新和查询相关属性。
开发步骤
添加气泡

导入相关模块。

import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

添加气泡，在callback方法中创建初始化参数并新建气泡。

@Entry
@Component
struct BubbleDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private bubble?: map.Bubble;


  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.918,
          longitude: 116.397
        },
        zoom: 14
      }
    };


    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let bubbleOptions: mapCommon.BubbleParams = {
          // 气泡位置
          positions: [[{
            latitude: 39.918,
            longitude: 116.397
          }]],
          // 设置图标，必须提供4个方向的图标，图标存放在resources/rawfile
          icons: [
            'speed_limit_10.png',
            'speed_limit_20.png',
            'speed_limit_30.png',
            'speed_limit_40.png'
          ],
          // 定义气泡的显示属性，为true时，在被碰撞后仍能显示
          forceVisible: true,
          // 定义气泡碰撞优先级，数值越大，优先级越低
          priority: 3,
          // 定义气泡展示的最小层级
          minZoom: 2,
          // 定义气泡展示的最大层级
          maxZoom: 20,
          // 定义气泡是否可见
          visible: true,
          // 定义气泡叠加层级属性
          zIndex: 1
        }


        // 添加气泡
        try {
          this.bubble = await this.mapController.addBubble(bubbleOptions);
        } catch (e) {
          console.error(`Failed to create the bubble, code is：${e.code}, message is ${e.message}`);
        }
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    };
  }


  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
      }.width('100%')
    }.height('100%')
  }
}

设置监听气泡点击事件
let callback = (bubble: map.Bubble) => {
  console.info("bubbleClick", `callback bubble = ${bubble.getId()}`);
};
this.mapController?.on("bubbleClick", callback);
气泡动画

Bubble调用setAnimation设置动画。

Bubble调用startAnimation启动动画。

let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
// 设置动画单次的时长
animation.setDuration(3000);
// 设置动画开始监听
let callbackStart = () => {
  console.info("animationStart", `callback`);
};
animation.on("animationStart", callbackStart);
// 设置动画结束监听
let callbackEnd = () => {
  console.info("animationEnd", `callback`);
};
animation.on("animationEnd", callbackEnd);
// 设置动画执行完成的状态
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
// 设置动画重复的方式
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
// 设置动画插值器
animation.setInterpolator(Curve.Linear);
// 设置动画的重复次数
animation.setRepeatCount(100);
this.bubble.setAnimation(animation);
this.bubble.startAnimation();
点注释
点聚合
