# 长时任务开发指导（TaskPool）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-guide_

import { BusinessError, emitter } from '@kit.BasicServicesKit';

定义长时任务，内部监听sensor数据，并通过emitter注册销毁通知。

// Index.ets
@Concurrent
async function SensorListener() : Promise<void> {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
    emitter.emit({ eventId: 0 }, { data: data });
  }, { interval: 1000000000 });


  emitter.on({ eventId: 1 }, () => {
    sensor.off(sensor.SensorId.ACCELEROMETER)
    emitter.off(1)
  })
}

给sensor添加ohos.permission.ACCELEROMETER权限。

// module.json5
"requestPermissions": [
  {
    "name": "ohos.permission.ACCELEROMETER"
  }
]

宿主线程定义注册及销毁的行为。

注册：发起长时任务，并通过emitter接收监听数据。
销毁：发送取消传感器监听的事件，并结束长时任务。
import { sensor } from '@kit.SensorServiceKit';
import { taskpool } from '@kit.ArkTS';
import { BusinessError, emitter } from '@kit.BasicServicesKit';


@Concurrent
async function sensorListener(): Promise<void> {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
    emitter.emit({ eventId: 0 }, { data: data });
  }, { interval: 1000000000 });


  emitter.on({ eventId: 1 }, () => {
    sensor.off(sensor.SensorId.ACCELEROMETER)
    emitter.off(1)
  })
}


@Entry
@Component
struct Index {
  sensorTask?: taskpool.LongTask
  @State addListener: string = 'Add listener';
  @State deleteListener: string = 'Delete listener';


  build() {
    Column() {
      Text(this.addListener)
        .id('Add listener')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.sensorTask = new taskpool.LongTask(sensorListener);
          emitter.on({ eventId: 0 }, (data) => {
            // Do something here
            console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}`);
          });
          taskpool.execute(this.sensorTask).then(() => {
            console.info('Add listener of ACCELEROMETER success');
          }).catch((e: BusinessError) => {
            // Process error
          })
          this.addListener = 'success';
        })
      Text(this.deleteListener)
        .id('Delete listener')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          emitter.emit({ eventId: 1 });
          emitter.off(0);
          if (this.sensorTask != undefined) {
            taskpool.terminateTask(this.sensorTask);
          } else {
            console.error('sensorTask is undefined.');
          }
          this.deleteListener = 'success';
        })
    }
    .height('100%')
    .width('100%')
  }
}
LongTimeTaskGuide.ets
长时任务并发场景简介
常驻任务并发场景
