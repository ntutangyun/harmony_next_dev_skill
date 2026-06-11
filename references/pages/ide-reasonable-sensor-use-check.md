# @performance/reasonable-sensor-use-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-sensor-use-check_

应用退到后台时，禁止使用传感器资源。

规则配置

// code-linter.json5
{
  "rules": {
    "@performance/reasonable-sensor-use-check": "suggestion",
  }
}

选项

该规则无需配置额外选项。

正例

import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
export default class EntryAbility extends UIAbility {
  onForeground(): void {
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

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@performance/reasonable-sensor-use-check": "suggestion",
  }
}
```

### Code block 2

```
import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
export default class EntryAbility extends UIAbility {
  onForeground(): void {
    // In the foreground, listen to the required type of sensor based on the service requirements
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    });
  }
  onBackground(): void {
    // The background cancels the listening
    sensor.off(sensor.SensorId.ACCELEROMETER);
  }
}
```

### Code block 3

```
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
```

### Code block 4

```
plugin:@performance/all
```
