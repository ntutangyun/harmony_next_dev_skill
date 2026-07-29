# 使用perfHint系统性能优化(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-scheduling-optimization_arkts_

从API版本26.0.0版本开始，新增支持perfHint系统性能优化特性。

perfHint(Performance Hint)是系统性能优化的简称，用于向系统提供性能场景信息。

场景介绍

允许应用程序向系统提供性能场景信息，系统据此在API生效范围内尽可能优化应用性能，以提升用户体验。

支持多种场景上报，包括应用启动、页面切换、页面加载、网络文件处理、本地文件处理、页面绘制、动效、音视频播放与媒体编解码。

场景状态控制：场景开始和场景结束。

持续时间提示：短持续时间、中等持续时间和长持续时间。支持不同的间隔要求，以提高策略差异化。各类型界定标准如下：

短持续时间（SHORT）：单次最大持续时间1秒，间隔大于3秒。

中等持续时间（MEDIUM）：单次最大持续时间10秒，间隔大于30秒。

长持续时间（LONG）：单次最大持续时间60秒，间隔大于180秒。

支持同时上报多个线程。可以携带线程ID数组。

约束与限制

perfHint只是应用向系统发送的性能优化提示，系统收到提示后会综合考量整机CPU负载、系统温度等因素进行决策，不保证一定进行性能提升。

性能提示仅当应用在前台运行时才会生效，应用切换到后台后提示将失效。

通过线程ID提升QoS优先级时，请避免与QoS API混用。

接口说明

perfHint系统性能优化场景提供以下ArkTS接口，具体API说明详见接口文档。

接口名	描述
perfHint(config: PerfHintConfig): Promise<void>	系统性能优化接口。使用Promise异步回调。

开发步骤

导入schedulingOptimization模块及相关公共模块。

import { schedulingOptimization } from '@kit.FASTKit';

构造参数。入参为PerfHintConfig配置参数，包含场景类型、场景状态、持续时间类型和线程ID数组。

let config: schedulingOptimization.PerfHintConfig = {
    sceneType: schedulingOptimization.SceneType.APP_LAUNCH,
    sceneState: schedulingOptimization.SceneState.BEGIN,
    durationType: schedulingOptimization.DurationType.SHORT,
    tids: [] // 按需填入线程ID
};

调用perfHint方法，将步骤2中构造的参数传入模块中的perfHint方法。

try {
    await schedulingOptimization.perfHint(config);
    console.info('perfHint success');
} catch (err) {
    console.error(`perfHint error.code is ${error.code}, message is ${error.message}`);
    // 根据错误码进行相应处理
}

## Code blocks

### Code block 1

```
import { schedulingOptimization } from '@kit.FASTKit';
```

### Code block 2

```
let config: schedulingOptimization.PerfHintConfig = {
    sceneType: schedulingOptimization.SceneType.APP_LAUNCH,
    sceneState: schedulingOptimization.SceneState.BEGIN,
    durationType: schedulingOptimization.DurationType.SHORT,
    tids: [] // 按需填入线程ID
};
```

### Code block 3

```
try {
    await schedulingOptimization.perfHint(config);
    console.info('perfHint success');
} catch (err) {
    console.error(`perfHint error.code is ${error.code}, message is ${error.message}`);
    // 根据错误码进行相应处理
}
```
