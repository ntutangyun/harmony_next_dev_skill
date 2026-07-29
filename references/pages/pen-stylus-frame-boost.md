# 接入手写笔跟手性加速

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-frame-boost_

从API版本26.0.0开始，新增手写笔跟手性加速接口，支持笔记类应用提升手写笔书写时延。

场景介绍

在应用使用书写绘制功能时，获取到界面的触摸事件的类型，通过调用手写笔跟手性加速的接口，可以提升手写笔书写时延。

限制与约束

调用手写笔跟手性加速的能力需要申请手写笔跟手性权限ohos.permission.STYLUS_FRAME_BOOST。

设备未连接手写笔，无法使用手写笔跟手性加速能力。

应用的屏幕刷新率需要大于60HZ。

接口说明

以下是手写笔跟手性加速接口说明，更多接口及使用方法请参见API参考。

接口名	描述
forceRefreshOneFrame(action: number): number	提高手写应用在高帧率状态下的手写笔书写时延。

开发步骤

在module.json5配置文件中声明ohos.permission.STYLUS_FRAME_BOOST权限。

"requestPermissions": [
  {
    "name": "ohos.permission.STYLUS_FRAME_BOOST"
  }
]

导入相关模块，并调用手写笔跟手性加速的接口，提升手写笔书写时延。

import { inputDevice } from '@kit.InputKit';
import { StylusFrameBoost } from '@kit.Penkit';

@Entry
@Component
struct StylusFrameBoostDemo {
  private device: PencilHelper = new PencilHelper()
  private stylusFrameBoost: StylusFrameBoost = new StylusFrameBoost();

  build() {
    Column() {
      Canvas()
        .onTouch((event: TouchEvent) => {
          // 判断是否连接手写笔。该接口依赖手写笔服务。
          if (this.device.hasPencil) {
            if (event.sourceTool === SourceTool.Pen || event.sourceTool === SourceTool.MOUSE ||
              event.sourceTool === SourceTool.Finger) {
              this.handleWriteEvent(event)
            }
          }
        })
    }
  }

  aboutToAppear(): void {
    this.device.init();
  }

  handleWriteEvent(event: TouchEvent) {
    if (event.touches.length <= 0) {
      return
    }
    switch (event.type) {
      case TouchType.Down:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
      case TouchType.Move:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
      case TouchType.Up:
      case TouchType.Cancel:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
    }
  }
}

class PencilHelper {
  private _hasPencil: boolean = false
  private pencilId: number = 0

  public get hasPencil(): boolean {
    return this._hasPencil
  }

  async init() {
    const deviceIds = await inputDevice.getDeviceList()
    inputDevice.on('change', async (device: inputDevice.DeviceListener) => {
      if (device.type === 'add') {
        const isPencil = await this.isPencil(device.deviceId)
        if (isPencil) {
          this._hasPencil = true
          this.pencilId = device.deviceId
        }
      } else if (this.pencilId === device.deviceId) {
        // 删除无法查询信息，只能通过之前的 id 判断。
        this._hasPencil = false
        this.pencilId = 0
      }
    })
    for (const id of deviceIds) {
      const isPencil = await this.isPencil(id)
      if (isPencil) {
        this._hasPencil = true
        this.pencilId = id
        break
      }
    }
  }

  async isPencil(deviceId: number) {
    const info = await inputDevice.getDeviceInfo(deviceId)
    return info.name.toLowerCase().indexOf('pencil') >= 0
  }
}

## Code blocks

### Code block 1

```
"requestPermissions": [
  {
    "name": "ohos.permission.STYLUS_FRAME_BOOST"
  }
]
```

### Code block 2

```
import { inputDevice } from '@kit.InputKit';
import { StylusFrameBoost } from '@kit.Penkit';

@Entry
@Component
struct StylusFrameBoostDemo {
  private device: PencilHelper = new PencilHelper()
  private stylusFrameBoost: StylusFrameBoost = new StylusFrameBoost();

  build() {
    Column() {
      Canvas()
        .onTouch((event: TouchEvent) => {
          // 判断是否连接手写笔。该接口依赖手写笔服务。
          if (this.device.hasPencil) {
            if (event.sourceTool === SourceTool.Pen || event.sourceTool === SourceTool.MOUSE ||
              event.sourceTool === SourceTool.Finger) {
              this.handleWriteEvent(event)
            }
          }
        })
    }
  }

  aboutToAppear(): void {
    this.device.init();
  }

  handleWriteEvent(event: TouchEvent) {
    if (event.touches.length <= 0) {
      return
    }
    switch (event.type) {
      case TouchType.Down:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
      case TouchType.Move:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
      case TouchType.Up:
      case TouchType.Cancel:
        try {
          this.stylusFrameBoost.forceRefreshOneFrame(event.type);
        } catch (error) {
          console.error(`Failed to stylusFrameBoost. Code: ${error.code}, message: ${error.message}`);
        }
        break
    }
  }
}

class PencilHelper {
  private _hasPencil: boolean = false
  private pencilId: number = 0

  public get hasPencil(): boolean {
    return this._hasPencil
  }

  async init() {
    const deviceIds = await inputDevice.getDeviceList()
    inputDevice.on('change', async (device: inputDevice.DeviceListener) => {
      if (device.type === 'add') {
        const isPencil = await this.isPencil(device.deviceId)
        if (isPencil) {
          this._hasPencil = true
          this.pencilId = device.deviceId
        }
      } else if (this.pencilId === device.deviceId) {
        // 删除无法查询信息，只能通过之前的 id 判断。
        this._hasPencil = false
        this.pencilId = 0
      }
    })
    for (const id of deviceIds) {
      const isPencil = await this.isPencil(id)
      if (isPencil) {
        this._hasPencil = true
        this.pencilId = id
        break
      }
    }
  }

  async isPencil(deviceId: number) {
    const info = await inputDevice.getDeviceInfo(deviceId)
    return info.name.toLowerCase().indexOf('pencil') >= 0
  }
}
```
