# 后台CPU占用峰值

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-peak-background-cpu-usage-0420_

规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

检测逻辑

执行hdc shell。

执行hidumper --cpuusage <进程pid>命令，获取总的cpu使用率。

计算逻辑

执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。
