# 应用声明接入系统关怀模式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/eldercare-appconfig_

从API版本26.0.0开始，已实现独立关怀模式功能（或称长辈模式、长辈版、关爱版、关怀版、大字版、敬老版等）的应用，可以通过在应用工程module.json5对应module声明如下metadata，让用户可以在设备“设置>关怀和无障碍>关怀模式>应用管理”里查看本应用，并自由切换关怀模式开关状态。需要注意的是，如果用户在设置里关闭了系统关怀模式开关，应用内关怀模式也会随之关闭，重新开启系统关怀模式，原先被关闭的应用会同步开启。

为实现应用内关怀模式状态与系统设置页面的开关状态保持实时同步，建议参照应用内关怀模式与系统设置同步完成配置。

建议声明在有关怀模式功能的module下：

{
  "module": {
    // 其他声明此处省略
    "metadata": [{
      "name": "senior_mode",
      "value": "independent_control"
    }]
  }
}

如应用内没有独立关怀模式开关，可参照获取系统关怀模式状态以实现跟随系统关怀模式变化。

## Code blocks

### Code block 1

```
{
  "module": {
    // 其他声明此处省略
    "metadata": [{
      "name": "senior_mode",
      "value": "independent_control"
    }]
  }
}
```
