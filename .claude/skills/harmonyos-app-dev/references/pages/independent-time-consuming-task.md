# 使用TaskPool执行独立的耗时任务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/independent-time-consuming-task_

constructor(image: string | Resource = '', text: string | Resource = '') {
    this.image = image;
    this.text = text;
  }
}
IconItemSource.ets
import { IconItemSource } from './IconItemSource';


// 在Task中执行的方法，需要添加@Concurrent注解，否则无法正常调用。
@Concurrent
export function loadPicture(count: number): IconItemSource[] {
  let iconItemSourceList: IconItemSource[] = [];
  // 遍历添加6*count个IconItem的数据
  for (let index = 0; index < count; index++) {
    const numStart: number = index * 6;
    // 此处循环使用6张图片资源
    iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 1}`));
    iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 2}`));
    iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 3}`));
    iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 4}`));
    iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 5}`));
    iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 6}`));
  }
  return iconItemSourceList;
}
IndependentTask.ets

使用TaskPool的execute方法执行任务，加载图片。

import { taskpool } from '@kit.ArkTS';
import { IconItemSource } from './IconItemSource';
import { loadPicture } from './IndependentTask';


@Entry
@Component
struct Index {
  @State message: string = 'Hello World';


  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let iconItemSourceList: IconItemSource[] = [];
            // 创建Task
            let loadPictureTask: taskpool.Task = new taskpool.Task(loadPicture, 30);
            // 执行Task，并返回结果
            taskpool.execute(loadPictureTask).then((res: object) => {
              // loadPicture方法的执行结果
              iconItemSourceList = res as IconItemSource[];
            })
            this.message = 'success';
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
IndependentTimeConsumingTask.ets
线程间通信场景
使用TaskPool执行多个耗时任务
