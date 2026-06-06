# @performance/reasonable

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-sensor-use-check_

// In the foreground, listen to the required type of sensor based on the service requirements
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    });
  }
  onBackground(): void {
    // The background cancels the listening
    sensor.off(sensor.SensorId.ACCELEROMETER);
  }
}
反例
import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
export default class EntryAbility extends UIAbility {
  onForeground(): void {
    // In the foreground, listen to the required type of sensor based on the service requirements
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    });
  }
  onBackground(): void {
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/reuse-date-instances-check
@performance/sparse-array-check
