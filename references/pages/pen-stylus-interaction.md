# 接入手写交互

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-interaction_

为实现手写笔的双击、轻捏及传感器数据交互，开发者应用可集成对应接口以订阅相关事件，并通过回调机制触发应用内部指定操作。

接口说明

类名	接口名	说明
stylusInteraction	on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void	订阅手写笔轻捏事件。
stylusInteraction	off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void	取消订阅手写笔轻捏事件。
stylusInteraction	on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void	订阅手写笔双击事件。
stylusInteraction	off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void	取消订阅手写笔双击事件。
stylusInteraction	isSensorSupported(): boolean	查询设备是否支持手写笔传感器数据功能。
stylusInteraction	onAccelerometer(receiver: Callback<AccelerometerEvent>): void	订阅手写笔加速度传感器数据。
stylusInteraction	offAccelerometer(receiver?: Callback<AccelerometerEvent>): void	取消订阅手写笔加速度传感器数据。
stylusInteraction	onGyroscope(receiver: Callback<GyroscopeEvent>): void	订阅手写笔陀螺仪传感器数据。
stylusInteraction	offGyroscope(receiver?: Callback<GyroscopeEvent>): void	取消订阅手写笔陀螺仪传感器数据。
stylusInteraction	onSensor(receiver: Callback<SensorEvent>): void	订阅手写笔加速度和陀螺仪传感器数据。
stylusInteraction	offSensor(receiver?: Callback<SensorEvent>): void	取消订阅手写笔加速度和陀螺仪传感器数据。

开发步骤

[h2]手写笔轻捏事件

导入相关模块。

import { stylusInteraction } from '@kit.Penkit';

订阅手写笔轻捏事件。

try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

取消订阅手写笔轻捏事件。

try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

[h2]手写笔双击事件

导入相关模块。

import { stylusInteraction } from '@kit.Penkit';

订阅手写笔双击事件。

try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

取消订阅手写笔双击事件。

try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

[h2]手写笔传感器功能

导入相关模块。

import { stylusInteraction } from '@kit.Penkit';

查询设备是否支持手写笔传感器数据功能。

 try {
   let supported: boolean = stylusInteraction.isSensorSupported();
   console.info(`stylus sensor is supported: ${supported}`);
 } catch (error) {
   console.error(`${error.code}: ${error.message}`);
 }

订阅手写笔加速度传感器数据。

try {
  stylusInteraction.onAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`got accelerometer event, time: ${event.timestamp}`);
    for (let i = 0; i < event.accelerometerData.length; i++) {
      console.info(`accelerometer data: x=${event.accelerometerData[i].x}, y=${event.accelerometerData[i].y}
      , z=${event.accelerometerData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

取消订阅手写笔加速度传感器数据。

try {
  stylusInteraction.offAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`off accelerometer event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

订阅手写笔陀螺仪传感器数据。

try {
  stylusInteraction.onGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`got gyroscope event, time: ${event.timestamp}`);
    for (let i = 0; i < event.gyroscopeData.length; i++) {
      console.info(`gyroscope data: x=${event.gyroscopeData[i].x}, y=${event.gyroscopeData[i].y}
  , z=${event.gyroscopeData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

取消订阅手写笔陀螺仪传感器数据。

try {
  stylusInteraction.offGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`off gyroscope event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

订阅手写笔加速度和陀螺仪传感器数据。

try {
  stylusInteraction.onSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`got sensor event, time: ${event.timestamp}`);
    for (let i = 0; i < event.sensorData.length; i++) {
      let accel = event.sensorData[i].accelerometerData;
      let gyro = event.sensorData[i].gyroscopeData;
      console.info(`sensor data: accel.x=${accel.x}, accel.y=${accel.y}, accel.z=${accel.z}, gyro.x=${gyro.x},
      gyro.y=${gyro.y}, gyro.z=${gyro.z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

取消订阅手写笔加速度和陀螺仪传感器数据。

try {
  stylusInteraction.offSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`off sensor event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}

## Code blocks

### Code block 1

```
import { stylusInteraction } from '@kit.Penkit';
```

### Code block 2

```
try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 3

```
try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 4

```
import { stylusInteraction } from '@kit.Penkit';
```

### Code block 5

```
try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 6

```
try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 7

```
import { stylusInteraction } from '@kit.Penkit';
```

### Code block 8

```
 try {
   let supported: boolean = stylusInteraction.isSensorSupported();
   console.info(`stylus sensor is supported: ${supported}`);
 } catch (error) {
   console.error(`${error.code}: ${error.message}`);
 }
```

### Code block 9

```
try {
  stylusInteraction.onAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`got accelerometer event, time: ${event.timestamp}`);
    for (let i = 0; i < event.accelerometerData.length; i++) {
      console.info(`accelerometer data: x=${event.accelerometerData[i].x}, y=${event.accelerometerData[i].y}
      , z=${event.accelerometerData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 10

```
try {
  stylusInteraction.offAccelerometer((event: stylusInteraction.AccelerometerEvent) => {
    console.info(`off accelerometer event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 11

```
try {
  stylusInteraction.onGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`got gyroscope event, time: ${event.timestamp}`);
    for (let i = 0; i < event.gyroscopeData.length; i++) {
      console.info(`gyroscope data: x=${event.gyroscopeData[i].x}, y=${event.gyroscopeData[i].y}
  , z=${event.gyroscopeData[i].z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 12

```
try {
  stylusInteraction.offGyroscope((event: stylusInteraction.GyroscopeEvent) => {
    console.info(`off gyroscope event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 13

```
try {
  stylusInteraction.onSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`got sensor event, time: ${event.timestamp}`);
    for (let i = 0; i < event.sensorData.length; i++) {
      let accel = event.sensorData[i].accelerometerData;
      let gyro = event.sensorData[i].gyroscopeData;
      console.info(`sensor data: accel.x=${accel.x}, accel.y=${accel.y}, accel.z=${accel.z}, gyro.x=${gyro.x},
      gyro.y=${gyro.y}, gyro.z=${gyro.z}`);
    }
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```

### Code block 14

```
try {
  stylusInteraction.offSensor((event: stylusInteraction.SensorEvent) => {
    console.info(`off sensor event, time: ${event.timestamp}`);
  });
} catch (error) {
  console.error(`${error.code}: ${error.message}`);
}
```
