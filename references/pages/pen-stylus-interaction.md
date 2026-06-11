# 接入手写交互

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pen-stylus-interaction_

接入手写交互功能，对于需要接入支持双击/轻捏功能的手写笔的第三方应用，可以通过调用下面相应接口来监听手写笔双击/轻捏事件，从而触发自身应用内部回调，来执行指定操作。

接口说明

类名	接口名	说明
stylusInteraction	on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void	监听手写笔轻捏事件。
stylusInteraction	off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void	取消监听手写笔轻捏事件。
stylusInteraction	on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void	监听手写笔双击事件。
stylusInteraction	off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void	取消监听手写笔双击事件。

手写笔轻捏事件

导入相关模块。

import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';

监听手写笔轻捏事件。

try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

取消监听手写笔轻捏事件。

try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

手写笔双击事件

1.导入相关模块。

import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';

2.监听手写笔双击事件。

try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

3.取消监听手写笔双击事件。

try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

## Code blocks

### Code block 1

```
import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`got squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 3

```
try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(`off squeeze event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 4

```
import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 5

```
try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`got doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### Code block 6

```
try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(`off doubleTap event, time: ${event.timestamp}`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
