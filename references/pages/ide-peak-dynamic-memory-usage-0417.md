# 动态内存峰值占用

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-dynamic-memory-usage-0417_

应用/元服务完成操作后，各类应用在后台的内存占用峰值应≤ 1300MB；应用完成操作后切换到后台，静置3min以后采集内存占用。

检测逻辑
执行hdc shell。
执行hidumper --mem <进程pid>命令，获取如图Pss字段。

计算逻辑

执行多轮测试，取最大Pss值为占用峰值，内存占用须小于1300M。

转场操作流畅
前台场景内存峰值占用
